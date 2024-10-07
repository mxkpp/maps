from qgis.core import QgsProject

from .. import utils
from . import consts as c


def main():
    utils.download_layer_from_arcgis_rest_server(
        c.PRIMARY_NETWORK_URL,
        c.TGT_GDB,
        c.TGT_LYR_PRIMARY_NETWORK,
    )

    utils.download_layer_from_arcgis_rest_server(
        c.URL,
        c.TGT_GDB,
        c.TGT_LYR_GENERIC,
    )

    with utils.QGISHeadless() as qgis:
        print(f"Reading QGIS project: {repr(c.QGIS_PROJECT)}")
        project = QgsProject()
        success = project.read(c.QGIS_PROJECT)
        if not success:
            raise RuntimeError(f"Error reading QGIS project: {repr(c.QGIS_PROJECT)}")
        raise NotImplementedError


if __name__ == "__main__":
    main()
