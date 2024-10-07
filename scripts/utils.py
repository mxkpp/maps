import os
import subprocess

# import fiona
# import shapely.geometry

from qgis.core import QgsApplication


class QGISHeadless:
    """A context-managed reference to the QGIS application, without GUI.
    https://docs.qgis.org/3.38/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts"""

    def __init__(self):
        self.qgs = QgsApplication([], False)
        # "lib/qgis" must exist relative to the QGIS prefix path. "/usr" is the default QGIS prefix path on Ubuntu.
        self.qgs.setPrefixPath("/usr", True)
        self.qgs.initQgis()

    def __enter__(self) -> QgsApplication:
        return self.qgs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.qgs.exitQgis()


def download_layer_from_arcgis_rest_server(url: str, file: str, layer: str) -> None:
    print(f"Will download to file: {repr(file)} from URL: {repr(url)}")

    expect_url_startswith = "ESRIJSON:https://"
    expect_url_endswith = "/query?where=1%3D1&outFields=*&orderByFields=OBJECTID+ASC&f=json"
    if not url.startswith(expect_url_startswith):
        raise ValueError(f"URL must start with: {repr(expect_url_startswith)}")
    if not url.endswith(expect_url_endswith):
        raise ValueError(f"URL must end with {repr(expect_url_endswith)} (where 1=1, all fields, ordered, json format)")
    if file.endswith((".shp", ".shp.zip")):
        driver = "ESRI Shapefile"
    elif file.endswith(".gpkg"):
        driver = "GPKG"
    elif file.endswith((".gdb", ".gdb.zip")):
        driver = "OpenFileGDB"
    else:
        raise ValueError(f"Unsupported extension for file: {file}")

    print(f"Writing layer: {repr(layer)} in file: {repr(file)}")

    # # Fiona with FEATURE_SERVER_PAGING="YES" appears to work...
    # with fiona.open(url, FEATURE_SERVER_PAGING="YES") as collection:
    #     with fiona.open(file, "w", crs=collection.crs, driver=driver, schema=collection.schema) as f:
    #         for feat in collection:
    #             geom = shapely.geometry.shape(feat["geometry"])
    #             f.write(
    #                 {
    #                     "geometry": shapely.geometry.mapping(geom),
    #                     "properties": feat["properties"],
    #                 }
    #             )

    # ...But might as well use ogr2ogr.
    cmd_args = ["ogr2ogr", "-progress", "-of", driver, "-overwrite", "-nln", layer, file, url]
    print(f"Running args: {cmd_args}")
    subprocess.check_call(cmd_args)


def zip_directory(d: str) -> str:
    new_zip_file = d + ".zip"
    print(f"Will zip directory: {repr(d)} to new file: {repr(new_zip_file)}")
    if not os.path.isdir(d):
        raise NotADirectoryError(d)
    if os.path.exists(new_zip_file):
        raise FileExistsError(new_zip_file)

    cmd_args = ["zip", "-r", os.path.basename(new_zip_file), os.path.basename(d)]
    d_parent = os.path.dirname(os.path.realpath(d))
    print(f"Running args: {cmd_args} from: {repr(d_parent)}")
    subprocess.check_call(cmd_args, cwd=d_parent)

    return new_zip_file
