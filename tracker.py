
from typing import Any


MAP_IMAGE_SIDE_LENGTH_PX = 2048

def map_page_index(data: Any) -> int:
    mapping: dict[str, int] = {
        "island": 0,
        "underground": 1,
    }
    return mapping.get(data, 0)

def location_icon_coords(index: int | None, coords: dict[str, Any]) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None
    
    # TODO: change pos x based on underground vs. island
    def pos_x_to_map_y(pos_x: float, index: int) -> int:
        if (index == 0):
            map_y = ((pos_x + 165))/480*MAP_IMAGE_SIDE_LENGTH_PX
        else:
            map_y = ((pos_x + 165 + 5000))/480*MAP_IMAGE_SIDE_LENGTH_PX
        return round(map_y)

    def pos_y_to_map_x(pos_y: float) -> int:
        map_x = (480-(pos_y + 165))/480*MAP_IMAGE_SIDE_LENGTH_PX
        return round(map_x)
    
    return pos_x_to_map_y(coords.get("X", 0), index), pos_y_to_map_x(coords.get("Y", 0)), f"images/icons/lil_gator_icon_outline.png"

tracker_world = {
    "map_page_folder" : "tracker",
    "map_page_maps" : "maps/maps.json",
    "map_page_locations" : "locations/locations.json",
    "map_page_setting_key" : "{player}_{team}_gator_map",
    "map_page_index" : map_page_index,
    "location_setting_key": "{player}_{team}_gator_coords",
    "location_icon_coords": location_icon_coords,
}