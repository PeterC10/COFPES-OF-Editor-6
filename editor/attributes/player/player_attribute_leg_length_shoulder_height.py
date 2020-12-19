from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_leg_length import (
    PlayerAttributeLegLength,
)

from editor.attributes.player.player_attribute_shoulder_height import (
    PlayerAttributeShoulderHeight,
)

from editor.attributes.player.player_attribute_physical_opts import (
    PlayerAttributePhysicalLinkedOpts,
)


class PlayerAttributeLegLengthShoulderHeight(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Leg Length/Shoulder Height"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 108

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
        Create Leg Length and Shoulder Height attributes
        and link to this attribute
        """
        self.leg_length = PlayerAttributeLegLength(self.player, parent=self)
        self.shoulder_height = PlayerAttributeShoulderHeight(
            self.player, parent=self
        )
