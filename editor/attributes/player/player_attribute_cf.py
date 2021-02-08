from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeCf(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "CF"

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
        and return first value (CF is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        short_pass_speed_label = self.parent.short_pass_speed.get_label()
        full_label = (label, short_pass_speed_label)

        return self.parent.set_value_from_label(full_label)
