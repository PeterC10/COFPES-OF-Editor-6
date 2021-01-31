from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeLongThrow(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Long Throw"

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
        and return second value (Long Throw is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        goal_celebration_two_label = (
            self.parent.get_goal_celebration_two.get_label()
        )
        full_label = (label, goal_celebration_two_label)
        return self.parent.set_value_from_label(full_label)
