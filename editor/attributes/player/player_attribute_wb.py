from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeWb(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "WB"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Position

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (WB is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        acceleration_label = self.parent.acceleration.get_label()
        full_label = (label, acceleration_label)

        return self.parent.set_value_from_label(full_label)
