from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeGloves(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Gloves"

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
        and return second value (Gloves is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        ankle_tape_label = self.parent.ankle_tape.get_label()
        rgb_b_label = self.parent.rgb_b.get_label()
        full_label = (label, ankle_tape_label, rgb_b_label)
        return self.parent.set_value_from_label(full_label)
