from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_head_width import (
    PlayerAttributeHeadWidth,
)

from editor.attributes.player.player_attribute_neck_width import (
    PlayerAttributeNeckWidth,
)

from editor.attributes.player.player_attribute_physical_opts import (
    PlayerAttributePhysicalLinkedOpts,
)


class PlayerAttributeHeadWidthNeckWidth(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Head/Neck Width"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 91

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
        self.head_width = PlayerAttributeHeadWidth(self.player, parent=self)
        self.neck_width = PlayerAttributeNeckWidth(self.player, parent=self)
