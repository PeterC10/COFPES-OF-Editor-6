from editor.utils.common_functions import replace_tuple_at_index

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeBandanaType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Bandana Type"

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
        and return first value (bandana type is set sixth)
        """
        full_label = self.parent.get_label()
        return full_label[5]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        hair_key = self.parent.get_hair_key()
        hair_key = replace_tuple_at_index(hair_key, 5, label)

        eye_color_two_label = self.parent.eye_color_two.get_label()
        neck_warmer_label = self.parent.neck_warmer.get_label()

        full_label = hair_key + (eye_color_two_label, neck_warmer_label)
        return self.parent.set_value_from_label(full_label)
