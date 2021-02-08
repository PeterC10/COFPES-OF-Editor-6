from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeHairColorPattern(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Hair Color Pattern"

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
        and return first value (hair color pattern is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        hair_color_type_label = self.parent.hair_color_type.get_label()
        eye_color_one_label = self.parent.eye_color_one.get_label()
        full_label = (hair_color_type_label, label, eye_color_one_label)

        return self.parent.set_value_from_label(full_label)
