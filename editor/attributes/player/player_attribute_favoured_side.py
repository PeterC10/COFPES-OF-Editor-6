from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeFavouredSide(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Favoured Side"

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
        and return first value (favoured side is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        weak_foot_acc_label = self.parent.weak_foot_accuracy.get_label()
        condition_label = self.parent.condition.get_label()
        full_label = (label, weak_foot_acc_label, condition_label)

        return self.parent.set_value_from_label(full_label)
