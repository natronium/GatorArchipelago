
from typing import Any


MAP_IMAGE_SIDE_LENGTH_PX = 2048

def location_icon_coords(index: int | None, coords: dict[str, Any]) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None
    
    def pos_x_to_map_y(pos_x: float) -> int:
        map_y = ((pos_x + 165))/480*MAP_IMAGE_SIDE_LENGTH_PX
        return round(map_y)

    def pos_y_to_map_x(pos_y: float) -> int:
        map_x = (480-(pos_y + 165))/480*MAP_IMAGE_SIDE_LENGTH_PX
        return round(map_x)
    
    return pos_x_to_map_y(coords.get("X", 0)), pos_y_to_map_x(coords.get("Y", 0)), f"images/icons/lil_gator_icon_outline.png"

tracker_world = {
    "map_page_folder" : "tracker",
    "map_page_maps" : "maps/maps.json",
    "map_page_locations" : "locations/locations.json",
    # "map_page_setting_key" : <optional tag that informs which data storage key will be watched for auto tabbing>
    # "map_page_index" : <optional function with signature Callable[Any,int] that will control the auto tabbing>
    "location_setting_key": "{player}_{team}_gator_coords",
    "location_icon_coords": location_icon_coords,
}