# Data Types
| Data Type |                                                     Description                                                      | JSON Schema Type |          Examples           |
|-----------|----------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------|
| `Integer` | A positive or negative whole number (i.e., a number that can be written without a fractional part).                  | integer          | 3, 19, -4                   |
| `Numeric` | A number that may include a fractional part with optional leading sign and optional exponent (engineering notation). | number           | 3.43, 0, -4, 1.03e4         |
| `Boolean` | True or false.                                                                                                       | boolean          | true, false                 |
| `String`  | A sequence of characters of any length using any (specified) character set.                                          | string           | Indirect evaporative cooler |
| `Null`    | Indicator that no value is provided. Only used in combination with other data types, e.g., 'Number/Null'.            | null             | null                        |

# FloorAreaBasis
| Enumerator  |       Description       | Notes |
|-------------|-------------------------|-------|
| `CENTER`    | Center line of the wall |       |
| `NEAR_SIDE` | Near side of the wall   |       |
| `FAR_SIDE`  | Far side of the wall    |       |

# ConditioningType
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `HEATED_AND_COOLED` | Heated and cooled |       |
| `HEATED_ONLY`       | Heated only       |       |
| `SEMIHEATED`        | Semiheated        |       |
| `UNCONDITIONED`     | Unconditioned     |       |
| `PLENUM`            | Plenum            |       |

# SpaceFunctionType
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `LABORATORY` | Laboratory  |       |
| `KITCHEN`    | Kitchen     |       |
| `OTHER`      | Other       |       |

# SurfaceClassificationType
| Enumerator |           Description            | Notes |
|------------|----------------------------------|-------|
| `WALL`     | Vertical or nearly vertical wall |       |
| `FLOOR`    | Floor                            |       |
| `CEILING`  | Ceiling                          |       |

# SurfaceAdjacentTo
| Enumerator  |                                  Description                                  | Notes |
|-------------|-------------------------------------------------------------------------------|-------|
| `AMBIENT`   | Exterior wall or roof which is adjacent to the exterior ambient environments. |       |
| `GROUND`    | Slab-on-grad or below grade surface if adjacent to ground.                    |       |
| `INTERIOR`  | Interior surface if adjacent to another thermal block.                        |       |
| `IDENTICAL` | Surface adjacent to a environment identical to the zone.                      |       |
| `UNHEATED`  | Surface adjacent to a environment that is not heated but enclosed.            |       |

# SurfaceConstructionInputOptions
|  Enumerator  |               Description                | Notes |
|--------------|------------------------------------------|-------|
| `LAYERS`     | Construction is entered layer-by-layer.  |       |
| `SIMPLIFIED` | Construction is entered by R-value only. |       |

# FenestrationClassificationType
|   Enumerator    |  Description  | Notes |
|-----------------|---------------|-------|
| `WINDOW`        | Window        |       |
| `SKYLIGHT`      | Skylight      |       |
| `DOOR`          | Door          |       |
| `PLASTIC_PANEL` | Plastic panel |       |
| `CLERESTORIES`  | Clerestories  |       |
| `ROOF_MONITOR`  | Roof monitor  |       |
| `GLASS_BLOCK`   | Glass block   |       |

# TransformerType
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `DRY_TYPE`     | Dry Type     |       |
| `FLUID_FILLED` | Fluid Filled |       |
| `OTHER`        | Other        |       |

# ElectricalPhase
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `SINGLE_PHASE` | Single Phase |       |
| `THREE_PHASE`  | Three Phase  |       |

# DayOfWeek
| Enumerator  | Description | Notes |
|-------------|-------------|-------|
| `SUNDAY`    | Sunday      |       |
| `MONDAY`    | Monday      |       |
| `TUESDAY`   | Tuesday     |       |
| `WEDNESDAY` | Wednesday   |       |
| `THURSDAY`  | Thursday    |       |
| `FRIDAY`    | Friday      |       |
| `SATURDAY`  | Saturday    |       |

# ServiceWaterHeatingEnteringWaterTemperatureInputOptions
|    Enumerator    |                   Description                    | Notes |
|------------------|--------------------------------------------------|-------|
| `ANNUAL_MAIN`    | Annual main entering water temperature option    |       |
| `MONTHLY_MAIN`   | Monthly main entering water temperature option   |       |
| `ANNUAL_GROUND`  | Annual ground entering water temperature option  |       |
| `MONTHLY_GROUND` | Monthly ground entering water temperature option |       |

# FuelTypeOptions
|  Enumerator   | Description | Notes |
|---------------|-------------|-------|
| `ELECTRICITY` | Electricity |       |
| `NATURAL_GAS` | Natural gas |       |

# ASHRAE229
|             Name             |                                           Description                                           |          Data Type           |  Units  | Range | Req |                                                                             Notes                                                                              |
|------------------------------|-------------------------------------------------------------------------------------------------|------------------------------|---------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `transformers`               | Electrical transformers at the building site                                                    | `[{Transformer}]`            |         |       |     | Contains a list of transformers that convert electricity from a higher voltage to one used by the building, exterior lighting, and other services at the site. |
| `buildings`                  | Buildings on the site                                                                           | `[{Building}]`               |         |       |     | Contains a list of buildings on the site (often just one).                                                                                                     |
| `calendar`                   | Information on the calendar used with the simulation.                                           | `{Calendar}`                 |         |       |     |                                                                                                                                                                |
| `schedules`                  | Schedules for internal loads, thermostats, equipment operation and control, and any other need. | `[{Schedule}]`               |         |       |     | Contains a list of schedules used in model.                                                                                                                    |
| `weather`                    | Information on the local weather conditions used with the simulation.                           | `{Weather}`                  |         |       |     |                                                                                                                                                                |
| `overall_simulation_outputs` | Outputs from the simluation summed for all buildings in the simulation.                         | `{OverallSimulationOutputs}` |         |       |     |                                                                                                                                                                |
| `building_rotation_angles`   | A list of angles that building simulations are performed and results are provided.              | `[Numeric]`                  | degrees |       |     | List of angles that the building has been rotated.                                                                                                             |

# Building
|            Name            |                                                                                                                             Description                                                                                                                              |              Data Type              | Units |   Range   | Req |                                         Notes                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------|-----------|-----|----------------------------------------------------------------------------------------|
| `id`                       | Unique Identification Number                                                                                                                                                                                                                                         | `Numeric`                           |       |           | ✓   |                                                                                        |
| `name`                     | Name of the Building                                                                                                                                                                                                                                                 | `String`                            |       |           | ✓   |                                                                                        |
| `number_of_floors`         | Number of floors                                                                                                                                                                                                                                                     | `Numeric`                           |       | `≥0`      |     |                                                                                        |
| `building_segments`        | Large portions of a building that share a building area type                                                                                                                                                                                                         | `[{BuildingSegment}]`               |       |           |     | Contains a list of building segments in the building.                                  |
| `is_new`                   | Indicates whether building is a new construction (true) or existing (false). Projects that include additions will be modeled as two buildings - one new and one existing, as curtain rules such as baseline fenestration area will apply differently to each portion | `Boolean`                           |       |           |     |                                                                                        |
| `compliance_path`          | Indicates the chosen compliance path if the ruleset has multiple compliance paths such as 90.1 Appendix G has code compliance and beyond code                                                                                                                        | `<CompliancePathType2019ASHRAE901>` |       |           |     |                                                                                        |
| `elevators`                | Elevators                                                                                                                                                                                                                                                            | `[{Elevator}]`                      |       |           |     | Contains a list of elevators in the building.                                          |
| `refrigeration_components` | Refrigeration                                                                                                                                                                                                                                                        | `[{Refrigeration}]`                 |       |           |     | Contains a list of refrigeration components in the building.                           |
| `open_time`                | Time that the building opens.                                                                                                                                                                                                                                        | `Numeric`                           |       | `≥1, ≤24` |     | The general time that the building is first opened during normal weekdays from 1 to 24 |
| `close_time`               | Time that the building closes.                                                                                                                                                                                                                                       | `Numeric`                           |       | `≥1, ≤24` |     | The general time that the building is closed during normal weekdays from 1 to 24       |

# BuildingSegment
|                      Name                      |                         Description                         |                       Data Type                       | Units | Range | Req |                               Notes                               |
|------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|-------|-------|-----|-------------------------------------------------------------------|
| `id`                                           | Unique Identification Number                                | `Numeric`                                             |       |       | ✓   |                                                                   |
| `thermal_blocks`                               | Thermal blocks in the building                              | `[{ThermalBlock}]`                                    |       |       |     | Contains a list of thermal blocks in the building.                |
| `heating_ventilation_air_conditioning_systems` | HVAC systems in the building                                | `[{HeatingVentilationAirConditioningSystem}]`         |       |       |     | Contains a list of HVAC systems in the building.                  |
| `service_water_heating_systems`                | Service water heating systems in the building               | `[{ServiceWaterHeatingSystem}]`                       |       |       |     | Contains a list of service water heating systems in the building. |
| `area_type_vertical_fenestration`              | Building area classification used for vertical fenestration | `<VerticalFenestrationBuildingAreaType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used.                    |

# ThermalBlock
|                           Name                           |              Description               | Data Type  | Units | Range | Req |                                                                        Notes                                                                         |
|----------------------------------------------------------|----------------------------------------|------------|-------|-------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `zones`                                                  | Zones in the building                  | `[{Zone}]` |       |       |     | Contains a list of zones in the building.                                                                                                            |
| `served_by_heating_ventilation_air_conditioning_systems` | HVAC systems serving the thermal block | `[String]` |       |       |     | Contains a list of IDs of the HVAC systems serving the thermal block - from Unique Identification Number in HeatingVentilationAirConditioningSystem. |

# Zone
|   Name   |      Description       |  Data Type  | Units | Range | Req |                   Notes                    |
|----------|------------------------|-------------|-------|-------|-----|--------------------------------------------|
| `spaces` | Spaces in the building | `[{Space}]` |       |       |     | Contains a list of spaces in the building. |

# Space
|                   Name                    |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                           |                                   Data Type                                    | Units | Range | Req |                       Notes                        |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------|-------|-----|----------------------------------------------------|
| `id`                                      | Unique Identification Number                                                                                                                                                                                                                                                                                                                                                                                                                                    | `Numeric`                                                                      |       |       | ✓   |                                                    |
| `name`                                    | Name fo the Space                                                                                                                                                                                                                                                                                                                                                                                                                                               | `String`                                                                       |       |       | ✓   |                                                    |
| `surfaces`                                | Surfaces surrounding the space                                                                                                                                                                                                                                                                                                                                                                                                                                  | `[{Surface}]`                                                                  |       |       |     | Contains a list of surfaces that define the space. |
| `floor_area`                              | The floor area of a space within the building, including basements, mezzanine and intermediate-floored tiers, and penthouses with a headroom height of 7.5 ft or greater. It is measured from the exterior faces of walls or from the center-line of walls separating buildings, but excluding covered walkways, open roofed-over areas, porches and similar spaces, pipe trenches, exterior terraces or steps, chimneys, roof overhangs, and similar features. | `Numeric`                                                                      | m2    | `≥0`  |     |                                                    |
| `floor_to_ceiling_height`                 | The height from the floor of the space to the ceiling                                                                                                                                                                                                                                                                                                                                                                                                           | `Numeric`                                                                      | m     | `≥0`  |     |                                                    |
| `floor_area_basis_for_exterior`           | The basis of the measurement location related to floor area for exterior walls.                                                                                                                                                                                                                                                                                                                                                                                 | `<FloorAreaBasis>`                                                             |       |       |     |                                                    |
| `floor_area_basis_for_interior`           | The basis of the measurement location related to floor area for interior walls.                                                                                                                                                                                                                                                                                                                                                                                 | `<FloorAreaBasis>`                                                             |       |       |     |                                                    |
| `conditioning_type`                       | Space conditioning category                                                                                                                                                                                                                                                                                                                                                                                                                                     | `<ConditioningType>`                                                           |       |       |     |                                                    |
| `space_function`                          | Generic function for the space.                                                                                                                                                                                                                                                                                                                                                                                                                                 | `<SpaceFunctionType>`                                                          |       |       |     | The enumeration is based on the standard used.     |
| `lighting_space_type`                     | Lighting space type classification                                                                                                                                                                                                                                                                                                                                                                                                                              | `(<LightingSpaceType2019ASHRAE901T951>, <LightingSpaceType2019ASHRAE901T961>)` |       |       |     | The enumeration is based on the standard used.     |
| `ventilations_space_type`                 | Ventilation space type classification                                                                                                                                                                                                                                                                                                                                                                                                                           | `<VentilationSpaceType2019ASHRAE901>`                                          |       |       |     | The enumeration is based on the standard used.     |
| `service_water_heating_space_type`        | Service water heating space type classification                                                                                                                                                                                                                                                                                                                                                                                                                 | `<ServiceWaterHeatingSpaceType2019ASHRAE901>`                                  |       |       |     | The enumeration is based on the standard used.     |
| `infiltration_modeling_method`            | The software methodology chosen for modeling infiltration                                                                                                                                                                                                                                                                                                                                                                                                       | `String`                                                                       |       |       |     |                                                    |
| `infiltration_equivalent_full_load_hours` | Annual sum of hourly fractions of infiltration schedule                                                                                                                                                                                                                                                                                                                                                                                                         | `Numeric`                                                                      | hr    | `≥0`  |     |                                                    |
| `receptacle_control_credit_taken`         | The receptacle control credit was taken                                                                                                                                                                                                                                                                                                                                                                                                                         | `Boolean`                                                                      |       |       |     |                                                    |
| `receptacle_baseline_exception_taken`     | The excpetion that receptacle power or schedule can be different in the baseline has been taken.                                                                                                                                                                                                                                                                                                                                                                | `Boolean`                                                                      |       |       |     |                                                    |
| `receptacle_power`                        | Peak power consumed by the receptacles.                                                                                                                                                                                                                                                                                                                                                                                                                         | `Numeric`                                                                      | W     |       |     |                                                    |
| `receptacle_schedule_name`                | Receptacle schedule name                                                                                                                                                                                                                                                                                                                                                                                                                                        | `String`                                                                       |       |       |     |                                                    |
| `receptacle_control_credit`               | A multiplier for the fraction of space plug load power applied tothe receptacle controlled credit.                                                                                                                                                                                                                                                                                                                                                              | `Numeric`                                                                      |       | `≥0`  |     |                                                    |

# Surface
|            Name            |                                        Description                                        |           Data Type           |  Units  | Range | Req |                                                                                                  Notes                                                                                                  |
|----------------------------|-------------------------------------------------------------------------------------------|-------------------------------|---------|-------|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                       | Unique Identification Number                                                              | `Numeric`                     |         |       | ✓   |                                                                                                                                                                                                         |
| `name`                     | Name fo the Space                                                                         | `String`                      |         |       | ✓   |                                                                                                                                                                                                         |
| `fenestration_subsurfaces` | Fenestration suburfaces that are on the surface                                           | `[{Fenestration}]`            |         |       |     | Contains a list of surfaces that define the space.                                                                                                                                                      |
| `classification`           | Classification for the surface.                                                           | `<SurfaceClassificationType>` |         |       |     | Options for surface being interior or exterior wall, floor, or ceiling.                                                                                                                                 |
| `tilt`                     | Angle between vertical and the surface outward normal                                     | `Numeric`                     | degrees |       |     | Example value would be 0 = roof, 90 = wall, 180 = downward facing surface (exterior floor)                                                                                                              |
| `azimuth`                  | Clockwise angle between North and the horizontal projection of the wall's outward normal. | `Numeric`                     | degrees | `≥0`  |     | Example values would be 0 = north, 90 = East, 180 = South, 270 = West                                                                                                                                   |
| `adjacent_to`              | Used to classify the conditions on the surface.                                           | `<SurfaceAdjacentTo>`         |         |       |     | Determines whether this is an (a) exterior surface if adjacent to ambient, (b) slab-on-grad or below grade surface if adjacent to ground, or (c) interior surface if adjacent to another thermal block. |
| `adjacent_space_id`        | ID of the adjacent space for interior surface                                             | `String`                      |         |       |     |                                                                                                                                                                                                         |
| `does_cast_shade`          | Determines whether the surface is modeled as casting shade on other exterior surfaces     | `Boolean`                     |         |       |     |                                                                                                                                                                                                         |
| `construction`             | Construction description of surface.                                                      | `{Construction}`              |         |       |     |                                                                                                                                                                                                         |

# Construction
|                Name                 |                                    Description                                    |              Data Type              | Units  | Range | Req |                                                    Notes                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------|--------|-------|-----|--------------------------------------------------------------------------------------------------------------|
| `surface_construction_input_option` | Identifies whether construction is entered layer-by-layer or simplified (R-value) | `<SurfaceConstructionInputOptions>` |        |       |     |                                                                                                              |
| `area`                              | area of the surface                                                               | `Numeric`                           | m2     | `≥0`  |     | Measured from interior face area. It is the gross area of the wall and includes the area of all subsurfaces. |
| `layers`                            | List of names of layer descriptions starting from the outside surface             | `[String]`                          |        |       |     |                                                                                                              |
| `insulation_location`               | The location of the insulation related to the surface                             | `String`                            |        |       |     |                                                                                                              |
| `u_factor`                          | suface U-factor                                                                   | `Numeric`                           | W/m2-K | `≥0`  |     |                                                                                                              |
| `c_factor`                          | surface C-factor                                                                  | `Numeric`                           | W/m2-K | `≥0`  |     |                                                                                                              |
| `f_factor`                          | surface F-factor                                                                  | `Numeric`                           | W/m-K  | `≥0`  |     |                                                                                                              |
| `r_value`                           | r-value of the insulation for the surface                                         | `Numeric`                           | K-m2/W | `≥0`  |     |                                                                                                              |
| `reflectance_thermal_exterior`      | Thermal reflectance of long wavelength radiation on the exterior surface.         | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_thermal_exterior`      | Thermal absorptance of long wavelength radiation on the exterior surface.         | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `reflectance_solar_exterior`        | Thermal reflectance of short wavelength radiation on the exterior surface.        | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_solar_exterior`        | Thermal absorptance of short wavelength radiation on the exterior surface.        | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `reflectance_visible_exterior`      | Thermal reflectance of visible radiation on the exterior surface.                 | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_visible_exterior`      | Thermal absorptance of visible radiation on the exterior surface.                 | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `reflectance_thermal_interior`      | Thermal reflectance of long wavelength radiation on the interior surface.         | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_thermal_interior`      | Thermal absorptance of long wavelength radiation on the interior surface.         | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `reflectance_solar_interior`        | Thermal reflectance of short wavelength radiation on the interior surface.        | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_solar_interior`        | Thermal absorptance of short wavelength radiation on the interior surface.        | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `reflectance_visible_interior`      | Thermal reflectance of visible radiation on the interior surface.                 | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `absorptance_visible_interior`      | Thermal absorptance of visible radiation on the interior surface.                 | `Numeric`                           |        | `≥0`  |     |                                                                                                              |
| `has_radiant_heating`               | Includes embedded radiant heating elements                                        | `Boolean`                           |        |       |     |                                                                                                              |
| `has_radiant_cooling`               | Includes embedded radiant cooling elements                                        | `Boolean`                           |        |       |     |                                                                                                              |

# Fenestration
|                Name                 |                                   Description                                   |             Data Type              | Units  | Range | Req |                          Notes                           |
|-------------------------------------|---------------------------------------------------------------------------------|------------------------------------|--------|-------|-----|----------------------------------------------------------|
| `id`                                | Unique Identification Number                                                    | `Numeric`                          |        |       | ✓   |                                                          |
| `name`                              | Name of the fenestration subsurface                                             | `String`                           |        |       | ✓   |                                                          |
| `classification`                    | Classification for the fenestration being window, skylight, door.               | `<FenestrationClassificationType>` |        |       |     |                                                          |
| `area`                              | Area of fenestration including glass and framing                                | `Numeric`                          | m2     | `≥0`  |     |                                                          |
| `international_glazing_database_id` | International Glazing Database ID Number                                        | `Numeric`                          |        | `≥0`  |     | See https://windows.lbl.gov/software/igdb for ID numbers |
| `u_factor`                          | Fenestration U-factor                                                           | `Numeric`                          | W/m2-K | `≥0`  |     |                                                          |
| `solar_heat_gain_coefficient`       | Fenestration SHGC                                                               | `Numeric`                          |        | `≥0`  |     |                                                          |
| `visible_transmittance`             | Fenestration VT                                                                 | `Numeric`                          |        | `≥0`  |     |                                                          |
| `light_to_solar_gain_ratio`         | Fenestration LSG                                                                | `Numeric`                          |        | `≥0`  |     |                                                          |
| `depth_of_overhang`                 | Distance from the edge of the overhang to the fenestration surface.             | `Numeric`                          | m      | `≥0`  |     |                                                          |
| `has_shading_projections`           | Identifies whether fenestration has side fins, overhangs or not flush with wall | `Boolean`                          |        |       |     |                                                          |
| `has_manual_interior_shades`        | Are there manually-operated interior shading such as blinds, curtains or shades | `Boolean`                          |        |       |     |                                                          |
| `has_automatic_shades`              | Are there automatic interior shading such as blinds, curtains or shades         | `Boolean`                          |        |       |     |                                                          |

# Transformer
|     Name     |                 Description                  |      Data Type      | Units |  Range   | Req |                                                      Notes                                                      |
|--------------|----------------------------------------------|---------------------|-------|----------|-----|-----------------------------------------------------------------------------------------------------------------|
| `name`       | Transformer Name                             | `String`            |       |          | ✓   |                                                                                                                 |
| `type`       | The type of transformer                      | `<TransformerType>` |       |          |     |                                                                                                                 |
| `phase`      | The number of electrical phases              | `<ElectricalPhase>` |       |          |     |                                                                                                                 |
| `efficiency` | Transformer efficiency                       | `Numeric`           |       | `≥0, ≤1` |     | Expresses the efficiency of the transformer as a fraction from 0 to 1, where 1 would represent 100% efficiency. |
| `capacity`   | Rated Capacity of the Transformer            | `Numeric`           | V-A   | `≥0`     |     |                                                                                                                 |
| `peak_load`  | Annual Peak electric load on the transformer | `Numeric`           | W     | `≥0`     |     | Peak electric load on the transfomer based on an annual simulation with typical weather file.                   |

# Schedule
|         Name          |                                    Description                                     |              Data Type               | Units | Range | Req |                                                                                                             Notes                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------|--------------------------------------|-------|-------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                  | Unique Identification Number                                                       | `Numeric`                            |       |       | ✓   |                                                                                                                                                                                                                                |
| `name`                | Name of the Schedule                                                               | `String`                             |       |       | ✓   |                                                                                                                                                                                                                                |
| `purpose`             | The purpose of schedule                                                            | `String`                             |       |       |     | Describe the purpose of the schedule and how it can be used. Not an enumerations. The purpose assigned by BEM tool should match across RMRs. Examples include thermostat, multiplier for lighting, availability for equipment. |
| `values`              | Hourly Values of Schedule                                                          | `[Numeric][8760]`                    |       |       |     | Can also use functions like EFLH(), MAX(), MIN() to determine overall characteristics for the list of schedule values.                                                                                                         |
| `units_of_values`     | The units associated witht the values of the schedule                              | `String`                             |       |       |     | For certain schedule purposes, the values may be represented by units such as C for temperature or W for power.                                                                                                                |
| `prescribed_schedule` | True if any schedule values have changed from what appears in the schedule library | `<PrescribedSchedules2019ASHRAE901>` |       |       |     |                                                                                                                                                                                                                                |

# Calendar
|            Name             |                  Description                   |   Data Type   | Units | Range | Req | Notes |
|-----------------------------|------------------------------------------------|---------------|-------|-------|-----|-------|
| `id`                        | Unique Identification Number                   | `Numeric`     |       |       | ✓   |       |
| `day_of_week_for_january_1` | Day of the week for January 1                  | `<DayOfWeek>` |       |       |     |       |
| `is_leap_year`              | The schedules assume it is a leap year         | `Boolean`     |       |       |     |       |
| `is_daylight_savings_time`  | The schedules adjust for daylight Savings Time | `Boolean`     |       |       |     |       |

# Weather
|             Name             |                            Description                            |          Data Type           | Units | Range | Req |                     Notes                      |
|------------------------------|-------------------------------------------------------------------|------------------------------|-------|-------|-----|------------------------------------------------|
| `monthly_ground_temperature` | Modeled monthly ground temperatures                               | `[Numeric][1..12]`           | C     |       |     |                                                |
| `climate_zone`               | The designation of the climate zone where the building is located | `<ClimateZone2019ASHRAE901>` |       |       | ✓   | The enumeration is based on the standard used. |

# Elevator
|                           Name                            |                          Description                           | Data Type | Units |    Range    | Req | Notes |
|-----------------------------------------------------------|----------------------------------------------------------------|-----------|-------|-------------|-----|-------|
| `id`                                                      | Unique Identification Number                                   | `Numeric` |       |             | ✓   |       |
| `name`                                                    | Name of the elevator                                           | `String`  |       |             | ✓   |       |
| `motor_power`                                             | Elevator peak motor power                                      | `Numeric` | W     |             |     |       |
| `cab_counterweight`                                       | Elevator car counterweight                                     | `Numeric` | kg    |             |     |       |
| `cab_weight`                                              | Weight of elevator car                                         | `Numeric` | kg    |             |     |       |
| `design_elevator_load`                                    | Elevator load at which to operate                              | `Numeric` | kg    |             |     |       |
| `speed`                                                   | Design speed of the elevator                                   | `Numeric` | m/s   |             |     |       |
| `cab_area`                                                | Floor area of elevator cab                                     | `Numeric` | m2    |             |     |       |
| `cab_lighting_power`                                      | Lighitng power of cab                                          | `Numeric` | W     |             |     |       |
| `cab_ventilation_fan_power`                               | Ventilation fan power of cab                                   | `Numeric` | W     |             |     |       |
| `cab_ventilation_fan_flow`                                | Airflow of cab ventfan                                         | `Numeric` | L/s   |             |     |       |
| `cab_motor_schedule`                                      | Elevator motor operation schedule name                         | `String`  |       |             |     |       |
| `cab_ventilation_fan_schedule`                            | Elevator ventilation fan operation schedule name               | `String`  |       |             |     |       |
| `cab_lighting_schedule`                                   | Elevator lighting schedule name                                | `String`  |       |             |     |       |
| `cab_motor_schedule_equivalent_full_load_hours`           | Elevator motor operation schedule equivalent full load hours   | `Numeric` | hr    | `≥0, ≤8760` |     |       |
| `cab_ventilation_fan_schedule_equivalent_full_load_hours` | Elevator ventfan operation schedule equivalent full load hours | `Numeric` | hr    | `≥0, ≤8760` |     |       |
| `cab_lighting_schedule_equivalent_full_load_hours`        | Elevator lighitng schedule equivalent full load hours          | `Numeric` | hr    | `≥0, ≤8760` |     |       |

# HeatingVentilationAirConditioningSystem
|              Name               |                         Description                         |  Data Type  | Units | Range | Req |                                       Notes                                       |
|---------------------------------|-------------------------------------------------------------|-------------|-------|-------|-----|-----------------------------------------------------------------------------------|
| `id`                            | Unique Identification Number                                | `Numeric`   |       |       | ✓   |                                                                                   |
| `sensible_cool_output_capacity` | Result from the simulation of the sensible cooling capacity | `[Numeric]` | W/m2  | `≥0`  |     | If multiple values are provided, they correspond to rotated building orientations |
| `heat_output_capacity`          | Result from the simulation of the heating capacity          | `[Numeric]` | W/m2  | `≥0`  |     | If multiple values are provided, they correspond to rotated building orientations |

# ServiceWaterHeatingSystem
|                 Name                 |                                                           Description                                                            |                          Data Type                          | Units | Range | Req |                                 Notes                                  |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------|-------|-----|------------------------------------------------------------------------|
| `loop_name`                          | Name of service water heating system loop                                                                                        | `String`                                                    |       |       |     |                                                                        |
| `area_type`                          | Service Water Heating Loop Area Type                                                                                             | `<ServiceWaterHeatingSpaceType2019ASHRAE901>`               |       |       |     | The enumeration is based on the standard used.                         |
| `design_flow`                        | Design Flowrate of service water heating loop                                                                                    | `Numeric`                                                   | L/s   |       |     |                                                                        |
| `supply_temperature`                 | Design supply temperature setpoint of service water heating loop                                                                 | `Numeric`                                                   | C     |       |     |                                                                        |
| `flow_schedule`                      | service water heating Loop flow schedule name                                                                                    | `String`                                                    |       |       |     |                                                                        |
| `annual_entering_water_temperature`  | Annual service main or annual ground temperature used for service water heating calculations entering water temperature  degrees | `Numeric`                                                   | C     |       |     |                                                                        |
| `monthly_entering_water_temperature` | Monthly service main or ground temperatures used for service water heating entering water temperature  degrees                   | `[Numeric][1..12]`                                          | C     |       |     | Arrayed variable with 12 values for monthly entering water temperature |
| `entering_water_temperature_type`    | Method of determining service water heating entering water temperature                                                           | `<ServiceWaterHeatingEnteringWaterTemperatureInputOptions>` |       |       |     |                                                                        |
| `heater_name`                        | Service water heating heater name                                                                                                | `String`                                                    |       |       |     |                                                                        |
| `heater_fuel_type`                   | Service water heating heater fuel type                                                                                           | `<FuelTypeOptions>`                                         |       |       |     |                                                                        |
| `heater_efficiency`                  | Service water heating heater efficiency                                                                                          | `Numeric`                                                   |       | `≥0`  |     |                                                                        |

# InteriorLighting
|             Name              |                                   Description                                   |             Data Type              | Units | Range | Req | Notes |
|-------------------------------|---------------------------------------------------------------------------------|------------------------------------|-------|-------|-----|-------|
| `id`                          | Unique ID assigned to each interior lighting fixture(s) reported in an RMR      | `Numeric`                          |       | `>0`  |     |       |
| `name`                        | Interior lighting fixture name                                                  | `String`                           |       |       |     |       |
| `type`                        | The type of interior lighting fixture                                           | `<LightingSpaceType2019ASHRAE901>` |       |       |     |       |
| `norminal_wattage`            | Nominal capacity of interior lighting fixtures                                  | `Numeric`                          | W     |       |     |       |
| `power`                       | Total power of all fixtures in a specific functional area                       | `Numeric`                          | W     |       |     |       |
| `designed_power`              | Total designed power of all fixtures in a specific functional area              | `Numeric`                          | W     |       |     |       |
| `with_occupancy_sensor`       | The flag for occ sensor is modeled with interior lighting                       | `Boolean`                          |       |       |     |       |
| `with_auto_controls`          | The flag for automatic lighting control is modeled with interior lighting  none | `Boolean`                          |       |       |     |       |
| `with_manual_on_sensor`       | The flag for manual-on automatic lighting control for interior lighting         | `Boolean`                          |       |       |     |       |
| `with_partial_auto_on_sensor` | The flag for partial-auto-on automatic lighting control for interior lighting   | `Boolean`                          |       |       |     |       |
| `multiplier`                  | Multiplier for interior lighting specifications                                 | `Numeric`                          |       | `>0`  |     |       |
| `area`                        | Space area for interior lighting                                                | `Numeric`                          | m2    | `>0`  |     |       |
| `with_other_auto_controls`    | Automatic interial lighting controls other than occupancy sensor                | `Boolean`                          |       |       |     |       |

# ExteriorLighting
|               Name                |                                     Description                                      |                   Data Type                    | Units | Range | Req | Notes |
|-----------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------|-------|-------|-----|-------|
| `id`                              | Unique ID assigned to each exterior lighting fixture(s) reported in an RMR           | `Numeric`                                      |       | `>0`  |     |       |
| `name`                            | Exterior lighting fixture name                                                       | `String`                                       |       |       |     |       |
| `type`                            | The type of exterior lighting fixture  none                                          | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |       |       |     |       |
| `area`                            | Area of the exterior functional space.                                               | `Numeric`                                      | m2    | `>0`  |     |       |
| `norminal_wattage`                | Nominal capacity of exterior lighting fixtures                                       | `Numeric`                                      | W     | `>0`  |     |       |
| `fixture_height`                  | Installation height of exterior fixture                                              | `Numeric`                                      | m     | `>0`  |     |       |
| `power`                           | Total exterior lighting power of all fixtures in a specific functional area          | `Numeric`                                      | W     | `>0`  |     |       |
| `designed_power`                  | Total designed exterior lighting power of all fixtures in a specific functional area | `Numeric`                                      | W     | `>0`  |     |       |
| `trade_light_power`               | Exterior Lighting power for tradable surface                                         | `Numeric`                                      | W     | `≥0`  |     |       |
| `non_trade_light_power`           | Exterior Lighting power for non-tradable surface                                     | `Numeric`                                      | W     | `≥0`  |     |       |
| `site_zone_type`                  | Site zone type for Sec 9.4.2                                                         | `<ExteriorLightingZones2019ASHRAE901>`         |       |       |     |       |
| `parking_area`                    | Area of exterior parking space                                                       | `Numeric`                                      | m2    | `≥0`  |     |       |
| `tradable_surface_type`           | Type of tradable surfaces for exterior lighting                                      | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |       |       |     |       |
| `tradable_surface_area`           | Area of tradable surface                                                             | `Numeric`                                      | m2    | `≥0`  |     |       |
| `tradable_surface_linear_footage` | Linear feet of tradable surface                                                      | `Numeric`                                      | m     | `≥0`  |     |       |
| `has_walkway`                     | If the building has an exterior walkway                                              | `Boolean`                                      |       |       |     |       |
| `tradable_walkway_width_footage`  | Width of the exterior walkway                                                        | `Numeric`                                      | m     | `≥0`  |     |       |
| `tradable_opening_width_footage`  | Width of an exterior opening                                                         | `Numeric`                                      | m     | `≥0`  |     |       |
| `multiplier`                      | Multiplier for exterior lighting specifications                                      | `Numeric`                                      |       | `>0`  |     |       |

# Refrigeration
|         Name         |                     Description                      |              Data Type              | Units | Range | Req | Notes |
|----------------------|------------------------------------------------------|-------------------------------------|-------|-------|-----|-------|
| `id`                 | Unique Identification Number                         | `Numeric`                           |       |       | ✓   |       |
| `name`               | Name of the refrigeration component                  | `String`                            |       |       | ✓   |       |
| `type`               | Refrigeration equipment type                         | `<RefrigerationType2019ASHRAE901>`  |       |       |     |       |
| `equipment_class`    | Equipment Class from referenced standard             | `<RefrigerationClass2019ASHRAE901>` |       |       |     |       |
| `energy_per_day`     | Rated electrical energy use per day                  | `Numeric`                           | kWh   |       |     |       |
| `case_volume`        | volume of a refrigerated case in cubic meters        | `Numeric`                           | m3    |       |     |       |
| `total_display_area` | display area of a refrigerated case in square meters | `Numeric`                           | m2    |       |     |       |

# OverallSimulationOutputs
|                       Name                        |                        Description                         | Data Type | Units | Range | Req | Notes |
|---------------------------------------------------|------------------------------------------------------------|-----------|-------|-------|-----|-------|
| `refrigeration_energy_enduse`                     | Annual refrigeration energy end use from simulation output | `Numeric` | kWh   |       |     |       |
| `service_water_heating_annual_enduse_electricity` | Annual electricity energy end_use for SWH loops            | `Numeric` | kWh   | `≥0`  |     |       |
| `service_water_heating_annual_enduse_fossilfuel`  | Annual fossil fuel energy end_use for SWH loops            | `Numeric` | J     | `≥0`  |     |       |

