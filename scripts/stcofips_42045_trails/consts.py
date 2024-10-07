from datetime import date

# URLs
PRIMARY_NETWORK_URL = "ESRIJSON:https://gis.delcopa.gov/arcgis/rest/services/Trails/Delaware_County_Primary_Trail_Network_February_2024/FeatureServer/0/query?where=1%3D1&outFields=*&orderByFields=OBJECTID+ASC&f=json"
GENERIC_TRAILS_URL = "ESRIJSON:https://gis.delcopa.gov/arcgis/rest/services/Trails/Delaware_County_Trails/FeatureServer/0/query?where=1%3D1&outFields=*&orderByFields=OBJECTID+ASC&f=json"

# Mapping status field names to the corresponding date they represent.
PRIMARY_NETWORK_FIELD2DATE: dict[str, date] = {
    "delcogis_PLANNING_trails_Prim_6": date(year=2016, month=6, day=1),
    "delcogis_PLANNING_trails_Prim_9": date(year=2016, month=9, day=1),
    "Sheet1__StatusFeb2017": date(year=2017, month=2, day=1),
    "Status_Feb2018": date(year=2018, month=2, day=1),
    "Status_Feb2020": date(year=2020, month=2, day=1),
    "StatusFeb2022": date(year=2022, month=2, day=1),
    "StatusFeb2024": date(year=2024, month=2, day=1),
}

# Since status choices changed at 2024 vintage, this establishes a consistent set of values regardless of vintage.
PRIMARY_NETWORK_STATUS_VAL_NORMALIZER: dict[str, str] = {
    # Conceptual
    "Potential": "Conceptual",
    "Planned (Conceptual)": "Conceptual",
    # Proposed
    "Proposed": "Proposed",
    "Pipeline (Feasibility Stage)": "Proposed",
    # Design
    "Design": "Design",
    "In Progress - Design": "Design",
    # Under Construction
    "Construction": "Under Construction",
    "In Progress - Under Construction": "Under Construction",
    # Existing
    "Existing": "Existing",
}

# Files
TGT_GDB = "data/STCOFIPS_42045_Trails.gdb"
TGT_LYR_PRIMARY_NETWORK = "Trails_Primary_Network"
TGT_LYR_GENERIC = "Trails"
QGIS_PROJECT = "projects/STCOFIPS_42045_Trails.qgz"
