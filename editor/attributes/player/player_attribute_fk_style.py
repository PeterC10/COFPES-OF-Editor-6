from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeFkStyle(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "FK Style"

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
        and return second value (FK Style is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        stronger_foot_label = self.parent.stronger_foot.get_label()
        pk_style_label = self.parent.pk_style.get_label()
        full_label = (stronger_foot_label, label, pk_style_label)

        return self.parent.set_value_from_label(full_label)
