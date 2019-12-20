from typing import Union, Sequence


def list_of_extents_to_geojson(extents):
    return {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {},
                'geometry': extent_to_geojson(extent),
            }
            for extent in extents
        ]
    }


def extent_to_geojson(extent: Union[str, Sequence[float]]):
    if isinstance(extent, str):
        extent = [float(c.strip()) for c in extent.split(',')]

    components = extent
    bl = (components[0], components[1])
    br = (components[0], components[3])
    tr = (components[2], components[3])
    tl = (components[2], components[1])

    return {
        'type': 'Polygon',
        'coordinates': ((bl, br, tr, tl, bl),)
    }
