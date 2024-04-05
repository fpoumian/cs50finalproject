from enum import Enum

class WaterColor(Enum):
    LIGHT_BLUE = 'LIGHT_BLUE'
    TEAL_GREEN = 'TEAL_GREEN'
    DARK_GREEN = 'DARK_GREEN'
    BLACK_GREEN = 'BLACK_GREEN'


def get_water_color_label(water_color: WaterColor) -> str:
    label_dict = {
        WaterColor.LIGHT_BLUE: 'Light Blue (Maintenance)',
        WaterColor.TEAL_GREEN: 'Teal Green',
        WaterColor.DARK_GREEN: 'Dark Green',
        WaterColor.BLACK_GREEN: 'Black Green',
    }
    return label_dict[water_color]
