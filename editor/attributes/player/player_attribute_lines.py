from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeLines(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Lines"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.SpecialAbilities

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (lines is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        aggression_label = self.parent.jump.get_label()
        full_label = (label, aggression_label)

        return self.parent.set_value_from_label(full_label)
