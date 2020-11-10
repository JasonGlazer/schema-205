# Data Types
| Data Type |                                                     Description                                                      | JSON Schema Type |          Examples           |
|-----------|----------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------|
| Integer   | A positive or negative whole number (i.e., a number that can be written without a fractional part).                  | integer          | 3, 19, -4                   |
| Numeric   | A number that may include a fractional part with optional leading sign and optional exponent (engineering notation). | number           | 3.43, 0, -4, 1.03e4         |
| Boolean   | True or false.                                                                                                       | boolean          | true, false                 |
| String    | A sequence of characters of any length using any (specified) character set.                                          | string           | Indirect evaporative cooler |
| Null      | Indicator that no value is provided. Only used in combination with other data types, e.g., 'Number/Null'.            | null             | null                        |

# FloorAreaBasis
| Enumerator |       Description       | Notes |
|------------|-------------------------|-------|
| CENTER     | Center line of the wall |       |
| NEAR_SIDE  | Near side of the wall   |       |
| FAR_SIDE   | Far side of the wall    |       |

# ConditioningType
|    Enumerator     |    Description    | Notes |
|-------------------|-------------------|-------|
| HEATED_AND_COOLED | Heated and cooled |       |
| HEATED_ONLY       | Heated only       |       |
| SEMIHEATED        | Semiheated        |       |
| UNCONDITIONED     | Unconditioned     |       |
| PLENUM            | Plenum            |       |

# SurfaceAdjacentTo
| Enumerator |                                  Description                                  | Notes |
|------------|-------------------------------------------------------------------------------|-------|
| AMBIENT    | Exterior wall or roof which is adjacent to the exterior ambient environments. |       |
| GROUND     | Slab-on-grad or below grade surface if adjacent to ground.                    |       |
| INTERIOR   | Interior surface if adjacent to another thermal block.                        |       |

# SurfaceConstructionInputOptions
| Enumerator |               Description                | Notes |
|------------|------------------------------------------|-------|
| LAYERS     | Construction is entered layer-by-layer.  |       |
| SIMPLIFIED | Construction is entered by R-value only. |       |

# TransformerType
|  Enumerator  | Description  | Notes |
|--------------|--------------|-------|
| DRY_TYPE     | Dry Type     |       |
| FLUID_FILLED | Fluid Filled |       |
| OTHER        | Other        |       |

# TransformerPhase
|  Enumerator  | Description  | Notes |
|--------------|--------------|-------|
| SINGLE_PHASE | Single Phase |       |
| THREE_PHASE  | Three Phase  |       |

# DayOfWeek
| Enumerator | Description | Notes |
|------------|-------------|-------|
| SUNDAY     | Sunday      |       |
| MONDAY     | Monday      |       |
| TUESDAY    | Tuesday     |       |
| WEDNESDAY  | Wednesday   |       |
| THURSDAY   | Thursday    |       |
| FRIDAY     | Friday      |       |
| SATURDAY   | Saturday    |       |

# ASHRAE229
| Data Element Name |                                           Description                                           |    Data Type    | Units | Range | Req |                                                                             Notes                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------|-----------------|-------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| transformers      | Electrical transformers at the building site                                                    | [{Transformer}] |       |       |     | Contains a list of transformers that convert electricity from a higher voltage to one used by the building, exterior lighting, and other services at the site. |
| buildings         | Buildings on the site                                                                           | [{Building}]    |       |       |     | Contains a list of buildings on the site (often just one).                                                                                                     |
| calendar          | Information on the calendar used with the simulation.                                           | {Calendar}      |       |       |     |                                                                                                                                                                |
| schedules         | Schedules for internal loads, thermostats, equipment operation and control, and any other need. | [{Schedule}]    |       |       |     | Contains a list of schedules used in model.                                                                                                                    |
| weather           | Information on the local weather conditions used with the simulation.                           | {Weather}       |       |       |     |                                                                                                                                                                |

# Building
| Data Element Name |                         Description                          |      Data Type      | Units | Range | Req |                         Notes                         |
|-------------------|--------------------------------------------------------------|---------------------|-------|-------|-----|-------------------------------------------------------|
| id                | Unique Identification Number                                 | Numeric             |       |       | ✓   |                                                       |
| name              | Name of the Building                                         | String              |       |       | ✓   |                                                       |
| number_of_floors  | Number of floors                                             | Numeric             |       | >=0   | ✓   |                                                       |
| building_segments | Large portions of a building that share a building area type | [{BuildingSegment}] |       |       |     | Contains a list of building segments in the building. |
| is_new            | The schedules assume it is a leap year                       | Boolean             |       |       | ✓   |                                                       |

# BuildingSegment
|              Data Element Name               |                         Description                         |                      Data Type                      | Units | Range | Req |                       Notes                        |
|----------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------|-------|-------|-----|----------------------------------------------------|
| id                                           | Unique Identification Number                                | Numeric                                             |       |       | ✓   |                                                    |
| thermal_blocks                               | thermal blocks in the building                              | [{ThermalBlock}]                                    |       |       |     | Contains a list of thermal blocks in the building. |
| heating_ventilation_air_conditioning_systems | HVAC systems in the building                                | [{HeatingVentilationAirConditioningSystem}]         |       |       |     | Contains a list of HVAC systems in the building.   |
| area_type_vertical_fenestration              | Building area classification used for vertical fenestration | <VerticalFenestrationBuildingAreaType2019ASHRAE901> |       |       | ✓   | The enumeration is based on the standard used.     |

# ThermalBlock
|                   Data Element Name                    |              Description               | Data Type | Units | Range | Req |                                                                        Notes                                                                         |
|--------------------------------------------------------|----------------------------------------|-----------|-------|-------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
| zones                                                  | zones in the building                  | [{Zone}]  |       |       |     | Contains a list of zones in the building.                                                                                                            |
| served_by_heating_ventilation_air_conditioning_systems | HVAC systems serving the thermal block | [String]  |       |       |     | Contains a list of IDs of the HVAC systems serving the thermal block - from Unique Identification Number in HeatingVentilationAirConditioningSystem. |

# Zone
| Data Element Name |      Description       | Data Type | Units | Range | Req |                   Notes                    |
|-------------------|------------------------|-----------|-------|-------|-----|--------------------------------------------|
| spaces            | Spaces in the building | [{Space}] |       |       |     | Contains a list of spaces in the building. |

# Space
|            Data Element Name            |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                           |              Data Type              | Units | Range | Req |                       Notes                        |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------|-------|-----|----------------------------------------------------|
| id                                      | Unique Identification Number                                                                                                                                                                                                                                                                                                                                                                                                                                    | Numeric                             |       |       | ✓   |                                                    |
| name                                    | Name fo the Space                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                              |       |       | ✓   |                                                    |
| surfaces                                | Surfaces surrounding the space                                                                                                                                                                                                                                                                                                                                                                                                                                  | [{Surface}]                         |       |       |     | Contains a list of surfaces that define the space. |
| floor_area                              | The floor area of a space within the building, including basements, mezzanine and intermediate-floored tiers, and penthouses with a headroom height of 7.5 ft or greater. It is measured from the exterior faces of walls or from the center-line of walls separating buildings, but excluding covered walkways, open roofed-over areas, porches and similar spaces, pipe trenches, exterior terraces or steps, chimneys, roof overhangs, and similar features. | Numeric                             |       | >=0   | ✓   |                                                    |
| floor_area_basis_for_exterior           | The basis of the measurement location related to floor area for exterior walls.                                                                                                                                                                                                                                                                                                                                                                                 | <FloorAreaBasis>                    |       |       | ✓   |                                                    |
| floor_area_basis_for_interior           | The basis of the measurement location related to floor area for interior walls.                                                                                                                                                                                                                                                                                                                                                                                 | <FloorAreaBasis>                    |       |       | ✓   |                                                    |
| conditioning_type                       | Space conditioning category                                                                                                                                                                                                                                                                                                                                                                                                                                     | <ConditioningType>                  |       |       |     |                                                    |
| lighting_space_type                     | Lighting space type classification                                                                                                                                                                                                                                                                                                                                                                                                                              | <LightingSpaceType2019ASHRAE901>    |       |       | ✓   | The enumeration is based on the standard used.     |
| ventilations_space_type                 | Ventilation space type classification                                                                                                                                                                                                                                                                                                                                                                                                                           | <VentilationSpaceType2019ASHRAE901> |       |       | ✓   | The enumeration is based on the standard used.     |
| infiltration_modeling_method            | The software methodology chosen for modeling infiltration                                                                                                                                                                                                                                                                                                                                                                                                       | String                              |       |       | ✓   |                                                    |
| infiltration_equivalent_full_load_hours | Annual sum of hourly fractions of infiltration schedule                                                                                                                                                                                                                                                                                                                                                                                                         | Numeric                             |       | >=0   | ✓   |                                                    |

# Surface
|         Data Element Name         |                                                                                               Description                                                                                               |             Data Type             | Units | Range | Req |                       Notes                        |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-------|-------|-----|----------------------------------------------------|
| id                                | Unique Identification Number                                                                                                                                                                            | Numeric                           |       |       | ✓   |                                                    |
| name                              | Name fo the Space                                                                                                                                                                                       | String                            |       |       | ✓   |                                                    |
| fenestration_subsurfaces          | Fenestration suburfaces that are on the surface                                                                                                                                                         | [{Fenestration}]                  |       |       |     | Contains a list of surfaces that define the space. |
| tilt                              | Angle between vertical and the surface outward normal, e.g. 0 = roof, 90 = wall, 180 = downward facing surface (exterior floor)                                                                         | Numeric                           |       |       | ✓   |                                                    |
| azimuth                           | Clockwise angle between North (0 degrees) and the horizontal projection of the wall's outward normal. 0 = north, 90 = East, 180 = South, 270 = West                                                     | Numeric                           |       | >=0   | ✓   |                                                    |
| adjacent_to                       | Determines whether this is an (a) exterior surface if adjacent to ambient, (b) slab-on-grad or below grade surface if adjacent to ground, or (c) interior surface if adjacent to another thermal block. | <SurfaceAdjacentTo>               |       |       | ✓   |                                                    |
| adjacent_space_ID                 | ID of the adjacent space for interior surface                                                                                                                                                           | String                            |       |       | ✓   |                                                    |
| does_cast_shade                   | Determines whether the surface is modeled as casting shade on other exterior surfaces                                                                                                                   | Boolean                           |       |       | ✓   |                                                    |
| surfaces                          | Surfaces surrounding the space                                                                                                                                                                          | [{Surface}]                       |       |       |     | Contains a list of surfaces that define the space. |
| surface_construction_input_option | Identifies whether construction is entered layer-by-layer or simplified (R-value)                                                                                                                       | <SurfaceConstructionInputOptions> |       |       | ✓   |                                                    |
| area                              | area of the surface                                                                                                                                                                                     | Numeric                           |       | >=0   | ✓   |                                                    |
| u_factor                          | suface U-factor                                                                                                                                                                                         | Numeric                           |       | >=0   | ✓   |                                                    |
| c_factor                          | surface C-factor                                                                                                                                                                                        | Numeric                           |       | >=0   | ✓   |                                                    |
| f_factor                          | surface F-factor                                                                                                                                                                                        | Numeric                           |       | >=0   | ✓   |                                                    |
| reflectance                       | Reflectance                                                                                                                                                                                             | Numeric                           |       | >=0   | ✓   |                                                    |
| emittance                         | Emittance                                                                                                                                                                                               | Numeric                           |       | >=0   | ✓   |                                                    |
| reflectivity                      | Reflectivity                                                                                                                                                                                            | Numeric                           |       | >=0   | ✓   |                                                    |

# Fenestration
|      Data Element Name      |                                   Description                                   | Data Type | Units | Range | Req | Notes |
|-----------------------------|---------------------------------------------------------------------------------|-----------|-------|-------|-----|-------|
| id                          | Unique Identification Number                                                    | Numeric   |       |       | ✓   |       |
| name                        | Name of the fenestration subsurface                                             | String    |       |       | ✓   |       |
| area                        | area of fenestration including glass and framing                                | Numeric   |       | >=0   | ✓   |       |
| u_factor                    | fenestration U-factor                                                           | Numeric   |       | >=0   | ✓   |       |
| solar_heat_gain_coefficient | fenestration SHGC                                                               | Numeric   |       | >=0   | ✓   |       |
| has_shading_projections     | identifies whether fenestration has side fins, overhangs or not flush with wall | Boolean   |       |       | ✓   |       |
| has_manual_interior_shades  | are there manually-operated interior shading such as blinds, curtains or shades | Boolean   |       |       | ✓   |       |
| has_automatic_shades        | are there automatic interior shading such as blinds, curtains or shades         | Boolean   |       |       | ✓   |       |

# Transformer
| Data Element Name |                             Description                              |     Data Type      | Units | Range | Req | Notes |
|-------------------|----------------------------------------------------------------------|--------------------|-------|-------|-----|-------|
| name              | Transformer Name                                                     | String             |       |       | ✓   |       |
| type              | The type of transformer                                              | <TransformerType>  |       |       | ✓   |       |
| phase             | The number of electrical phases                                      | <TransformerPhase> |       |       | ✓   |       |
| efficiency        | Transformer efficiency                                               | Numeric            |       | >=0   | ✓   |       |
| capacity          | Rated Capacity of the Transformer                                    | Numeric            | Va    | >=0   | ✓   |       |
| peak_load         | Annual Peak electric load on the transformer                         | Numeric            | W     | >=0   | ✓   |       |
| capacity_ratio    | Annual Peak electric load of the transformer divided by the capacity | Numeric            |       | >=0   | ✓   |       |

# Schedule
| Data Element Name |         Description          |     Data Type      | Units | Range | Req |                                             Notes                                              |
|-------------------|------------------------------|--------------------|-------|-------|-----|------------------------------------------------------------------------------------------------|
| id                | Unique Identification Number | Numeric            |       |       | ✓   |                                                                                                |
| name              | Name of the Schedule         | String             |       |       | ✓   |                                                                                                |
| type              | The type of schedule         | String             |       |       | ✓   | Not an enumerations because we only care that the type assigned by BEM tool matches across RMR |
| values            | Hourly Values of Schedule    | [Numeric][1..8760] |       |       | ✓   |                                                                                                |

# Calendar
|     Data Element Name     |                  Description                   |  Data Type  | Units | Range | Req | Notes |
|---------------------------|------------------------------------------------|-------------|-------|-------|-----|-------|
| id                        | Unique Identification Number                   | Numeric     |       |       | ✓   |       |
| day_of_week_for_january_1 | Day of the Week for January 1                  | <DayOfWeek> |       |       | ✓   |       |
| is_leap_year              | The schedules assume it is a leap year         | Boolean     |       |       | ✓   |       |
| is_daylight_savings_time  | The schedules adjust for daylight Savings Time | Boolean     |       |       | ✓   |       |

# Weather
|     Data Element Name      |                            Description                            |         Data Type          | Units | Range | Req |                     Notes                      |
|----------------------------|-------------------------------------------------------------------|----------------------------|-------|-------|-----|------------------------------------------------|
| monthly_ground_temperature | Modeled monthly ground temperatures                               | [Numeric][1..12]           |       |       | ✓   |                                                |
| climate_zone               | The designation of the climate zone where the building is located | <ClimateZone2019ASHRAE901> |       |       | ✓   | The enumeration is based on the standard used. |

# HeatingVentilationAirConditioningSystem
|       Data Element Name       |                         Description                         | Data Type | Units | Range | Req | Notes |
|-------------------------------|-------------------------------------------------------------|-----------|-------|-------|-----|-------|
| id                            | Unique Identification Number                                | Numeric   |       |       | ✓   |       |
| sensible_cool_output_capacity | Result from the simulation of the sensible cooling capacity | Numeric   |       | >=0   | ✓   |       |
| heat_output_capacity          | Result from the simulation of the heating capacity          | Numeric   |       | >=0   | ✓   |       |

