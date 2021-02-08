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

from editor.attributes.player.player_attribute_finger_band_type import (
    PlayerAttributeFingerBandType,
)

from editor.attributes.player.player_attribute_rgb_g import (
    PlayerAttributeRgbG,
)


class PlayerAttributeFingerBandTypeRgbG(PlayerAttribute):
    MIN_RGB_G_VALUE = 0
    MAX_RGB_G_VALUE = 63

    @classmethod
    def att_class_name(cls):
        return "Finger Band Type/Hair Color RGB-G"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 103

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_finger_band_type(cls):
        """
        Finger Band Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                64: PlayerAttributeOption.OPT_1,
                128: PlayerAttributeOption.OPT_2,
            }
        )
        return options_by_value

    @property
    def array_opts_finger_band_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_finger_band_type()

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

    def get_finger_band_type_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        return self.array_opts_finger_band_type[value]

    def get_rgb_g_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)
        value = self.MAX_RGB_G_VALUE - value
        return str(value)

    def get_label(self):
        finger_band_type_label = self.get_finger_band_type_label()
        rgb_g_label = self.get_rgb_g_label()
        return (finger_band_type_label, rgb_g_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        finger_band_type_value = self.array_opts_finger_band_type.inverse[
            label[0]
        ]

        rgb_g_value = int(label[1])

        if (
            rgb_g_value < self.MIN_RGB_G_VALUE
            or rgb_g_value > self.MAX_RGB_G_VALUE
        ):
            rgb_g_value = self.MAX_RGB_G_VALUE

        rgb_g_value = self.MAX_RGB_G_VALUE - rgb_g_value

        return finger_band_type_value + rgb_g_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Finger Band Type and RGB-G attributes
        and link to this attribute
        """
        self.finger_band_type = PlayerAttributeFingerBandType(
            self.player, parent=self
        )
        self.rgb_g = PlayerAttributeRgbG(self.player, parent=self)
