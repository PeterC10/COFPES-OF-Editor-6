from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeShoulderHeight(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Shoulder Height"

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
        and return second value (shoulder height is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        leg_length_label = self.parent.leg_length.get_label()
        full_label = (leg_length_label, label)

        return self.parent.set_value_from_label(full_label)
