from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeInjuryTolerance(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Injury Tolerance"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (injury tolerance is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        weak_foot_freq_label = self.parent.weak_foot_frequency.get_label()
        consistency_label = self.parent.consistency.get_label()
        full_label = (label, weak_foot_freq_label, consistency_label)

        return self.parent.set_value_from_label(full_label)
