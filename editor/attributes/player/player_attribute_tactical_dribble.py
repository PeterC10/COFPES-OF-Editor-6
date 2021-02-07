from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeTacticalDribble(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Tactical Dribble"

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
        and return first value (tactical dribble is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        shot_power_label = self.parent.shot_power.get_label()
        full_label = (label, shot_power_label)

        return self.parent.set_value_from_label(full_label)
