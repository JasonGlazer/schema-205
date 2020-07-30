import scripts.validate
import scripts.markdown
import scripts.json_translate
import os
from doit.tools import create_folder

BUILD_PATH = "build"
SOURCE_PATH = 'schema-source'
DOCS_PATH = os.path.join(BUILD_PATH,"docs")
SCHEMA_PATH = os.path.join(BUILD_PATH,"schema")

def collect_source_files():
  file_list = []
  for file_name in sorted(os.listdir('schema-source')):
    if '.schema.yaml' in file_name:
      file_list.append(os.path.join(SOURCE_PATH,file_name))
  return file_list

def collect_target_files(target_dir, extension):
  file_list = []
  for file_name in sorted(os.listdir('schema-source')):
    if '.schema.yaml' in file_name:
      file_name_root = os.path.splitext(os.path.splitext(file_name)[0])[0]
      file_list.append(os.path.join(target_dir,f'{file_name_root}.schema.{extension}'))
  return file_list

def task_validate():
  '''Validates common-schema against meta-schema'''
  return {
    'file_dep': collect_source_files(),
    'actions': [(scripts.validate.validate_dir,[SOURCE_PATH])]
  }

def task_doc():
  '''Generates Markdown tables from common-scema'''
  return {
    'file_dep': collect_source_files(),
    'targets': collect_target_files(DOCS_PATH,'md'),
    'task_dep': ['validate'],
    'actions': [
      (create_folder, [DOCS_PATH]),
      (scripts.markdown.write_dir,[SOURCE_PATH, DOCS_PATH])
      ],
    'clean': True
  }

def task_schema():
  '''Generates JSON schema from common-scema'''
  return {
    'file_dep': collect_source_files(),
    'targets': collect_target_files(SCHEMA_PATH,'json'),
    'task_dep': ['validate'],
    'actions': [
      (create_folder, [SCHEMA_PATH]),
      (scripts.json_translate.translate_dir,[SOURCE_PATH, SCHEMA_PATH])
      ],
    'clean': True
  }

def task_test():
  '''Performs unit tests and example file validation tests'''
  return {
    'task_dep': ['schema'],
    'actions': ['pytest -v test']
  }
