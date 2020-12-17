from bidict import bidict

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.utils.common_functions import get_base_byte_value


class PlayerAttributeHeadHeight(PlayerAttribute):
    opt_m7 = "-7"
    opt_m6 = "-6"
    opt_m5 = "-5"
    opt_m4 = "-4"
    opt_m3 = "-3"
    opt_m2 = "-2"
    opt_m1 = "-1"
    opt_0 = "0"
    opt_1 = "1"
    opt_2 = "2"
    opt_3 = "3"
    opt_4 = "4"
    opt_5 = "5"
    opt_6 = "6"
    opt_7 = "7"

    @classmethod
    def att_class_name(cls):
        return "Head Height"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 90

    @classmethod
    def att_class_array_opts(cls):
        """
        Head Height opts
        """
        options_by_value = bidict(
            {
                0: cls.opt_m7,
                16: cls.opt_m6,
                32: cls.opt_m5,
                48: cls.opt_m4,
                64: cls.opt_m3,
                80: cls.opt_m2,
                96: cls.opt_m1,
                112: cls.opt_0,
                128: cls.opt_1,
                144: cls.opt_2,
                160: cls.opt_3,
                176: cls.opt_4,
                192: cls.opt_5,
                208: cls.opt_6,
                224: cls.opt_7,
            }
        )
        return options_by_value

    def get_raw_value(self):
        """
        Get byte value currently set in player's byte array
        """
        of_data = self.player.option_file.data
        value = of_data[self.player.address + self.array_pos]
        return value

    def get_value(self):
        """
        Get byte value via `get_raw_value`.

        Get base byte value (to be used to identify label)
        """
        value = self.get_raw_value()
        byte_factor = 16
        value = get_base_byte_value(value, byte_factor)
        return value

    def get_label(self):
        value = self.get_value()
        label = self.array_opts[value]
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = self.array_opts.inverse[label]
        self.set_value(value)
        return True
