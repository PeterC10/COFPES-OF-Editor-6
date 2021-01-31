from editor.utils.common_functions import get_random_value_from_list

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_growth_type import (
    PlayerAttributeGrowthType,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)


class PlayerAttributeGrowthTypeRandom(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Random Growth Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return None

    @classmethod
    def att_class_array_opts(cls):
        return None

    def get_value(self):
        return None

    def get_label(self):
        return None

    def set_value(self, value):
        return None

    def get_random_growth_type(self):
        growth_types = [
            PlayerAttributeOption.OPT_EARLY,
            PlayerAttributeOption.OPT_EARLY_LASTING,
            PlayerAttributeOption.OPT_STANDARD,
            PlayerAttributeOption.OPT_STANDARD_LASTING,
            PlayerAttributeOption.OPT_LATE,
            PlayerAttributeOption.OPT_LATE_LASTING,
        ]
        return get_random_value_from_list(growth_types)

    def set_value_from_label(self, label):
        if label == PlayerAttributeOption.OPT_R:
            label = self.get_random_growth_type()

        growth_type = PlayerAttributeGrowthType(self.player)
        return growth_type.set_random_value_from_label(label)
