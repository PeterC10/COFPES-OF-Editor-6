from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeEyeColorOne(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Eye Color 1"

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
        and return first value (eye color one is set second)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        hair_color_type_label = self.parent.hair_color_type.get_label()
        hair_color_pattern_label = self.parent.hair_color_pattern.get_label()
        full_label = (hair_color_type_label, hair_color_pattern_label, label)

        return self.parent.set_value_from_label(full_label)
