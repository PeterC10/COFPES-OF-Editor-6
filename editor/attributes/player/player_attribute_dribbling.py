from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeDribbling(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Dribbling"

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
        and return first value (dribbling is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        shot_accuracy_label = self.parent.shot_accuracy.get_label()
        full_label = (label, shot_accuracy_label)

        return self.parent.set_value_from_label(full_label)
