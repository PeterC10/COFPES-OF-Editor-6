from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeAnkleTape(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Ankle Tape"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Accessories

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return second value (Ankle Tape is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        gloves_label = self.parent.gloves.get_label()
        rgb_b_label = self.parent.rgb_b.get_label()
        full_label = (gloves_label, label, rgb_b_label)
        return self.parent.set_value_from_label(full_label)
