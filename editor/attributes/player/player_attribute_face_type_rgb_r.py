from bidict import bidict

from editor.utils.common_functions import (
    get_lowest_byte_value,
    get_base_byte_value,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_face_type import (
    PlayerAttributeFaceType,
)

from editor.attributes.player.player_attribute_rgb_r import (
    PlayerAttributeRgbR,
)


class PlayerAttributeFaceTypeRgbR(PlayerAttribute):
    MIN_RGB_R_VALUE = 0
    MAX_RGB_R_VALUE = 63

    @classmethod
    def att_class_name(cls):
        return "Face Type/Hair Color RGB-R"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 102

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_face_type(cls):
        """
        Face Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_BUILD,
                1: PlayerAttributeOption.OPT_SPECIAL,
                2: PlayerAttributeOption.OPT_PRESET,
            }
        )
        return options_by_value

    @property
    def array_opts_face_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_face_type()

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
        return self.get_raw_value()

    def get_face_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 4)
        return self.array_opts_face_type[value]

    def get_rgb_r_label(self):
        value = self.get_value()
        byte_factor = 4
        rgb_r_offset = get_base_byte_value(value, byte_factor) // byte_factor
        rgb_r = self.MAX_RGB_R_VALUE - rgb_r_offset
        return str(rgb_r)

    def get_label(self):
        face_type_label = self.get_face_type_label()
        rgb_r_label = self.get_rgb_r_label()
        return (face_type_label, rgb_r_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        face_type_value = self.array_opts_face_type.inverse[label[0]]

        rgb_r_value = int(label[1])
        rgb_r_byte_value = 4

        if (
            rgb_r_value < self.MIN_RGB_R_VALUE
            or rgb_r_value > self.MAX_RGB_R_VALUE
        ):
            rgb_r_value = self.MAX_RGB_R_VALUE

        rgb_r_value = (self.MAX_RGB_R_VALUE - rgb_r_value) * rgb_r_byte_value

        return face_type_value + rgb_r_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Face Type and RGB-R attributes
        and link to this attribute
        """
        self.face_type = PlayerAttributeFaceType(self.player, parent=self)
        self.rgb_r = PlayerAttributeRgbR(self.player, parent=self)
