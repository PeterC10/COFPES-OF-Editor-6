from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeFingerBandType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Finger Band Type"

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
        and return second value (Finger Band Type is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        rgb_g_label = (
            self.parent.rgb_g.get_label()
        )
        full_label = (label, rgb_g_label)
        return self.parent.set_value_from_label(full_label)
