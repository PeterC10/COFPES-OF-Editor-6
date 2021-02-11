from editor.utils.common_functions import replace_tuple_at_index

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeEyeColorTwo(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Eye Color 2"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (eye color 2 is set seventh)
        """
        full_label = self.parent.get_label()
        return full_label[6]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        hair_key = self.parent.get_hair_key()
        neck_warmer_label = self.parent.neck_warmer.get_label()

        full_label = hair_key + (label, neck_warmer_label)
        return self.parent.set_value_from_label(full_label)
