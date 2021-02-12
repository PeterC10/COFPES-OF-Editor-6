from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeEyesLength(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Eyes Length"

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
        and return seventh value (eyes length is set seventh)
        """
        full_label = self.parent.get_label()
        return full_label[6]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        cheek_type_label = self.parent.cheek_type.get_label()
        cheek_shape_label = self.parent.cheek_shape.get_label()
        brows_height_label = self.parent.brows_height.get_label()
        eyebrow_spacing_label = self.parent.eyebrow_spacing.get_label()
        brows_angle_label = self.parent.brows_angle.get_label()
        eyes_angle_label = self.parent.eyes_angle.get_label()
        eyes_width_label = self.parent.eyes_width.get_label()

        full_label = (
            cheek_type_label,
            cheek_shape_label,
            brows_height_label,
            eyebrow_spacing_label,
            brows_angle_label,
            eyes_angle_label,
            label,
            eyes_width_label,
        )
        return self.parent.set_value_from_label(full_label)
