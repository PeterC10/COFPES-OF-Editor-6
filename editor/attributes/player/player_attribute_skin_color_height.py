from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_skin_color import (
    PlayerAttributeSkinColor,
)

from editor.attributes.player.player_attribute_height import (
    PlayerAttributeHeight,
)


class PlayerAttributeSkinColorHeight(PlayerAttribute):
    height_base = 148

    @classmethod
    def att_class_name(cls):
        return "Skin Color/Height"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 88

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_skin_color(cls):
        """
        Skin Color Opts
        """
        options_by_value = bidict(
            {
                0: 1,
                64: 2,
                128: 3,
                192: 4,
            }
        )
        return options_by_value

    @property
    def array_opts_skin_color(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_skin_color()

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

    def get_skin_color(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        return self.array_opts_skin_color[value]

    def get_height(self):
        value = self.get_value()
        skin_color = self.get_skin_color()
        skin_color_byte_base = self.array_opts_skin_color.inverse[skin_color]
        return (value - skin_color_byte_base) + self.height_base

    def get_skin_color_label(self):
        label = str(self.get_skin_color())
        return label

    def get_height_label(self):
        label = str(self.get_height())
        return label

    def get_label(self):
        skin_color_label = self.get_skin_color_label()
        height_label = self.get_height_label()
        return (skin_color_label, height_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        skin_color = int(label[0])
        height = int(label[1])
        skin_color_byte_base = self.array_opts_skin_color.inverse[skin_color]
        height_byte_offset = height - self.height_base
        return skin_color_byte_base + height_byte_offset

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Skin Color and Height attributes
        and link to this attribute
        """
        self.skin_color = PlayerAttributeSkinColor(
            self.player, parent=self
        )
        self.height = PlayerAttributeHeight(
            self.player, parent=self
        )
