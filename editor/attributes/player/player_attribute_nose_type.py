from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeNoseType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Nose Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return second value (nose type is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        head_position_label = self.parent.head_position.get_label()
        nose_height_label = self.parent.nose_height.get_label()
        nose_width_label = self.parent.nose_width.get_label()
        mouth_size_label = self.parent.mouth_size.get_label()
        jaw_type_label = self.parent.jaw_type.get_label()
        chin_height_label = self.parent.chin_height.get_label()
        chin_width_label = self.parent.chin_width.get_label()

        full_label = (
            head_position_label,
            label,
            nose_height_label,
            nose_width_label,
            mouth_size_label,
            jaw_type_label,
            chin_height_label,
            chin_width_label,
        )
        return self.parent.set_value_from_label(full_label)
