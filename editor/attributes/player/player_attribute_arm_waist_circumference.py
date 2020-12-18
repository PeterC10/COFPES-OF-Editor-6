from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_arm_circumference import (
    PlayerAttributeArmCircumference,
)

from editor.attributes.player.player_attribute_waist_circumference import (
    PlayerAttributeWaistCircumference,
)

from editor.attributes.player.player_attribute_physical_opts import (
    PlayerAttributePhysicalLinkedOpts,
)


class PlayerAttributeArmWaistCircumference(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Arm/Waist Circumference"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 106

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_hidden(cls):
        return True

    def get_raw_value(self):
        """
        Get byte value currently set in player's byte array
        """
        of_data = self.player.option_file.data
        value = of_data[self.player.address + self.array_pos]
        return value

    def get_value(self):
        value = self.get_raw_value()
        return value

    def get_label(self):
        value = self.get_value()
        label = PlayerAttributePhysicalLinkedOpts.get_full_label(value)
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = PlayerAttributePhysicalLinkedOpts.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Head Width and Neck Width attributes
        and link to this attribute
        """
        self.arm_circumference = PlayerAttributeArmCircumference(
            self.player, parent=self
        )
        self.waist_circumference = PlayerAttributeWaistCircumference(
            self.player, parent=self
        )
