from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)


class PlayerAttributeWristbandType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Wristband Type"

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
        and return second value (wristband type is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        wristband_color_label = self.parent.wristband_color.get_label()

        # Only set wristband type if colour is already set, otherwise use N/None
        wristband_type_label = PlayerAttributeOption.OPT_N
        wristband_color_label = PlayerAttributeOption.OPT_NONE
        necklace_color_label = self.parent.necklace_color.get_label()


        if wristband_color_label != PlayerAttributeOption.OPT_NONE:
            wristband_type_label = label
            wristband_color_label = self.parent.wristband_color.get_label()

        full_label = (
            wristband_type_label,
            wristband_color_label,
            necklace_color_label,
        )

        return self.parent.set_value_from_label(full_label)
