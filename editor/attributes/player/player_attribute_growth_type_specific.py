from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_growth_type import (
    PlayerAttributeGrowthType,
)


class PlayerAttributeGrowthTypeSpecific(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Specific Growth Type"

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

    def set_value_from_label(self, label):
        growth_type = PlayerAttributeGrowthType(self.player)
        value = int(label)
        return growth_type.set_value(value)
