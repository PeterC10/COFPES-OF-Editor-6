from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeUndershortsColor(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Undershorts Color"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Accessories#

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
        and return first value (undershorts color is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        preset_face_label = self.parent.preset_face.get_label()
        socks_type_label = self.parent.undershorts.get_label()
        full_label = (preset_face_label, label, socks_type_label)

        return self.parent.set_value_from_label(full_label)
