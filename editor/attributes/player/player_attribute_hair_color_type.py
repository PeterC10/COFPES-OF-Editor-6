from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeHairColorType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Hair Color Type"

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
        and return first value (hair color type is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        hair_color_pattern_label = self.parent.hair_color_pattern.get_label()
        eye_color_one_label = self.parent.eye_color_one.get_label()
        full_label = (label, hair_color_pattern_label, eye_color_one_label)

        return self.parent.set_value_from_label(full_label)
