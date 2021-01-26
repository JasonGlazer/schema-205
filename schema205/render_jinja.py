"""
Calls all Jinja main_templates to render a result.
"""
import os
import os.path
#import glob
import traceback

from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound
import yaml

import schema205.schema_tables as schema_tables


THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SCHEMA_DIR = os.path.realpath(
        os.path.join(THIS_DIR, '..', 'schema-source'))


#def get_base_stem(path):
#    """
#    For /a/b/c/d.txt.zip, returns 'd.txt'.
#    For /a/b/c/d.txt, returns 'd'
#    - path: string, the path
#    RETURN: string, the base stem
#    """
#    return os.path.splitext(os.path.basename(path))[0]
#
#
#def load_tables(tables_dir=TABLE_DIR, glob_pattern='tables/*.txt'):
#    """
#    """
#    data = {}
#    for path in glob.glob(glob_pattern):
#        tag = get_base_stem(path)
#        with open(path) as f:
#            raw_text = f.read()
#        data[tag] = raw_text
#    return data
#
#
#def make_data_type_table_spec(yaml_src, caption):
#    return {
#        "yaml_source": yaml_src,
#        "caption": caption,
#        "select_by": {
#            "data_path": ["Object Type"],
#            "equals": "Data Type",
#        },
#        "columns": [
#            {
#                "data_path": [],
#                "name_in_table": "Data Type",
#            },
#            {
#                "data_path": ["Description"],
#                "name_in_table": "Description",
#            },
#            {
#                "data_path": ["JSON Schema Type"],
#                "name_in_table": "JSON Schema Type",
#            },
#            {
#                "data_path": ["Examples"],
#                "name_in_table": "Examples",
#                "transforms": [tables.join_with_comma],
#            }
#        ]
#    }
#
#
#def make_string_type_table_spec(yaml_src, caption):
#    return {
#        "yaml_source": yaml_src,
#        "caption": caption,
#        "select_by": {
#            "data_path": ["Object Type"],
#            "equals": "String Type",
#        },
#        "columns": [
#            {
#                "data_path": [],
#                "name_in_table": "Data Type",
#            },
#            {
#                "data_path": ["Description"],
#                "name_in_table": "Description",
#            },
#            {
#                "data_path": ["JSON Schema Pattern"],
#                "name_in_table": "JSON Schema Pattern",
#                "default": "(Not applicable)",
#                "transforms": [
#                    tables.add_space_between("-", "["),
#                    tables.add_space_between("]", "]"),
#                    tables.add_space_between(")", ")"),
#                    tables.add_space_between(")", "("),
#                    tables.add_space_between(")", "\\."),
#                    tables.add_space_between("*", "["),
#                    tables.add_space_between("0", "|"),
#                    tables.add_space_between("*", "|"),
#                    tables.add_space_between("+", "("),
#                    tables.add_space_between("?", "("),
#                    tables.add_space_between("]", "["),
#                    tables.add_space_between("|", "["),
#                    tables.add_space_between("]", "|"),
#                    tables.add_space_between("]", "{"),
#                    tables.add_space_between("}", ":"),
#                    tables.add_space_between("]", ":"),
#                    tables.add_space_between(")", ":"),
#                    tables.add_space_between(":", "["),
#                    tables.add_space_between(":", "("),
#                    tables.add_space_between(":", "{"),
#                ],
#            },
#            {
#                "data_path": ["Examples"],
#                "name_in_table": "Examples",
#                "transforms": [
#                    tables.join_with_comma,
#                ],
#            }
#        ]
#    }
#
#
#def make_enumerator_table_spec(id, yaml_src, caption, columns, key=None):
#    if key is None:
#        key = "Enumerators"
#    def make_rows(_, obj):
#        enumerators = obj[key]
#        return [(k, enumerators[k]) for k in sorted(enumerators.keys())]
#    return {
#        "yaml_source": yaml_src,
#        "caption": caption,
#        "select_by": {
#            "data_path": [],
#            "equals": id,
#        },
#        "derive_rows": make_rows,
#        "columns": columns,
#    }
#
#
#def add_table(source, table_type, caption=None, preferred_column_widths=None, with_header=False):
#    yaml_src = os.path.join(SCHEMA_DIR, f'{source}.schema.yaml')
#    if not os.path.exists(yaml_src):
#        raise Exception(
#            f"Schema source '{yaml_src}' does not exist in '{SCHEMA_DIR}'")
#    if table_type == "Data Type":
#        return tables.generate_table_to_string(
#            make_data_type_table_spec(yaml_src, caption),
#            preferred_size=preferred_column_widths)
#    elif table_type == "String Type":
#        return tables.generate_table_to_string(
#            make_string_type_table_spec(yaml_src, caption),
#            preferred_size=preferred_column_widths)
#    elif table_type == "RS_ID":
#        return tables.generate_table_to_string(
#            make_enumerator_table_spec(
#                "RSID", yaml_src, caption, [
#                    {
#                        "data_path": [],
#                        "name_in_table": "RS_ID",
#                    },
#                    {
#                        "data_path": ["Description"],
#                        "name_in_table": "Title",
#                    },
#                ]
#            ),
#            preferred_size=preferred_column_widths,
#            header=table_type if with_header else None
#        )
#    elif table_type == "ASHRAE205":
#        return tables.generate_table_to_string(
#            make_enumerator_table_spec(
#                table_type, yaml_src, caption, [
#                    {
#                        "data_path": [],
#                        "name_in_table": "Name",
#                    },
#                    {
#                        "data_path": ["Description"],
#                        "name_in_table": "Description",
#                    },
#                    {
#                        "data_path": ["Data Type"],
#                        "name_in_table": "Data Type",
#                    },
#                    {
#                        "data_path": ["Required"],
#                        "name_in_table": "Req",
#                        "transforms": [
#                            tables.bool_to_checkmark
#                        ],
#                        "default": False,
#                        "escape": False,
#                    },
#                    {
#                        "data_path": ["Notes"],
#                        "name_in_table": "Notes",
#                        "default": "",
#                    },
#                ],
#                key="Data Elements",
#            ),
#            preferred_size=preferred_column_widths,
#            header=table_type if with_header else None
#        )
#    else:
#        return tables.generate_table_to_string(
#            make_enumerator_table_spec(
#                table_type, yaml_src, caption, [
#                    {
#                        "data_path": [],
#                        "name_in_table": "Enumerator",
#                    },
#                    {
#                        "data_path": ["Description"],
#                        "name_in_table": "Definition",
#                    },
#                ]
#            ),
#            preferred_size=preferred_column_widths,
#            header=table_type if with_header else None)
#    s = ", ".join([
#        source, table_type, str(caption), str(preferred_column_widths)])
#    return f"Unknown table_type for add_table({s})"
#
#
#def add_data_model(*args):
#    """
#    Add a data model.
#    """
#    s = ", ".join([str(a) for a in args])
#    return "add_data_model(" + s + ")"

def make_args_string(args_dict):
    """
    - args_dict: dict, the dictionary of local variable to value such as returned by locals()
    RETURN: string, all arguments in a string
    """
    return ", ".join(
            [f"{k}={repr(v)}" for k, v in reversed(list(args_dict.items()))])


def make_error_string(msg, args_str):
    """
    - msg: string, an error message
    - args_str: string, original arguments
    RETURN: string, an error message
    """
    return ("\n---\n" +
            "ERROR\n" + msg + f"\nin call to `add_table({args_str})`\n---\n")


def add_table(source, table_type, caption=None, preferred_column_widths=None, with_header=False):
    """
    TODO: document this
    """
    args_str = make_args_string(locals())
    src_path = os.path.join(SCHEMA_DIR, source + '.schema.yaml')
    if not os.path.exists(src_path):
        return make_error_string(
                f"Schema source \"{source}\" (\"{src_path}\") doesn't exist!",
                args_str)
    with open(src_path, 'r') as input_file:
        data = yaml.load(input_file, Loader=yaml.FullLoader)
    table_type_to_fn = {
            'data_types': schema_tables.data_types_table,
            }
    gen_table = table_type_to_fn.get(table_type.lower(), None)
    if gen_table is None:
        return make_error_string(
                f"Unhandled table type \"{table_type}\"!",
                args_str)
    struct = schema_tables.load_structure_from_object(data)
    return gen_table(
            struct[table_type.lower()],
            caption=caption,
            add_training_ws=False)


def main(main_template, output_path, template_dir):
    """
    - main_template: string, path to the main template file. Note: should be a
      path relative to template_dir, not a full path.
    - output_path: string, the output path to write the template to
    - template_dir: string, the directory where the templates (that
      main_template refers to) lives.
    RETURN: None
    SIDE-EFFECTS:
    - load the template main_template from template_dir
    - render that template
    - write the contents to output_path
    """
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True,
        comment_start_string="{##",
        comment_end_string="##}")
    try:
        temp = env.get_template(main_template)
        with open(output_path, 'w') as handle:
            handle.write(temp.render(add_table=add_table))
    except TemplateNotFound as exc:
        print(f"Could not find main template {main_template}")
        print(f"main_template = {main_template}")
        print(f"output_path = {output_path}")
        print(f"template_dir = {template_dir}")
        print("Exception:")
        print(exc)
        traceback.print_exc()
