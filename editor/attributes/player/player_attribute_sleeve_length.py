from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeSleeveLength(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Sleeve Length"

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
        and return second value (sleeve length is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        facial_hair_color_label = self.parent.facial_hair_color.get_label()
        return self.parent.set_value_from_label(label, facial_hair_color_label)
