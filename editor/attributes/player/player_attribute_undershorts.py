from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeUndershorts(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Undershorts"

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
        and return first value (undershorts is set third)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        bracelet_color_label = self.parent.bracelet_color.get_label()
        bracelet_type_label = self.parent.bracelet_type.get_label()
        full_label = (bracelet_type_label, bracelet_color_label, label)

        return self.parent.set_value_from_label(full_label)
