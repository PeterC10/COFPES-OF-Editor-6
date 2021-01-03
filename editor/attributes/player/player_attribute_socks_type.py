from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeSocksType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Socks Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Accessories

    @classmethod
    def att_class_array_pos(cls):
        return 100

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (socks type is set third)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        preset_face_label = self.parent.preset_face.get_label()
        undershorts_color_label = self.parent.undershorts_color.get_label()
        full_label = (preset_face_label, undershorts_color_label, label)

        return self.parent.set_value_from_label(full_label)
