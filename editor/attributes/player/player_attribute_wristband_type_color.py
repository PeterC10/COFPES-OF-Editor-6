from bidict import bidict

from editor.utils.common_functions import (
    get_base_byte_value,
    get_lowest_byte_value,
    round_down,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_wristband_type import (
    PlayerAttributeWristbandType,
)

from editor.attributes.player.player_attribute_wristband_color import (
    PlayerAttributeWristbandColor,
)


class PlayerAttributeWristbandTypeColor(PlayerAttribute):
    opt_n = "N"
    opt_l = "L"
    opt_r = "R"
    opt_b = "B"

    opt_none = "None"
    opt_white = "White"
    opt_black = "Black"
    opt_red = "Red"
    opt_blue = "Blue"
    opt_yellow = "Yellow"
    opt_green = "Green"
    opt_purple = "Purple"
    opt_cyan = "Cyan"

    @classmethod
    def att_class_name(cls):
        return "Wristband Type/Color"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Accessories

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 98

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_arry_opts_wristband_type(cls):
        """
        Wristband Type Opts
        """
        options_by_value = bidict(
            {
                0: cls.opt_n,
                8: cls.opt_l,
                16: cls.opt_r,
                24: cls.opt_b
            }
        )
        return options_by_value

    @property
    def arry_opts_wristband_type(self):
        """
        Return byte array options.
        """
        return self.att_class_arry_opts_wristband_type()

    @classmethod
    def att_class_arry_opts_wristband_color(cls):
        """
        Wristband Color Opts
        """
        options_by_value = bidict(
            {
                0: cls.opt_white,
                32: cls.opt_black,
                64: cls.opt_red,
                96: cls.opt_blue,
                128: cls.opt_yellow,
                160: cls.opt_green,
                192: cls.opt_purple,
                224: cls.opt_cyan,
            }
        )
        return options_by_value

    @property
    def arry_opts_wristband_color(self):
        """
        Return byte array options.
        """
        return self.att_class_arry_opts_wristband_color()

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

        # Set invalid option to no wristband
        if value in self.arry_opts_wristband_color:
            value = 0

        return value

    def get_wristband_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        value = round_down(value, 8)
        return self.arry_opts_wristband_type[value]

    def get_wristband_color_label(self):
        label = self.opt_none
        wristband_type = self.get_wristband_type_label()
        value = self.get_value()
        value = get_base_byte_value(value, 32)

        if wristband_type != self.opt_n:
            label = self.arry_opts_wristband_color[value]

        return label

    def get_label(self):
        wristband_type_label = self.get_wristband_type_label()
        wristband_color_label = self.get_wristband_color_label()
        return (wristband_type_label, wristband_color_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.arry_opts_wristband_type.inverse[label[0]]

        second_opt_value = 0
        # Only check colour if wristband type is not "None"
        if first_opt_value != 0:
            second_opt_value = self.arry_opts_wristband_color.inverse[label[1]]

        return first_opt_value + second_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Wristband Type and Color attributes
        and link to this attribute
        """
        self.wristband_type = PlayerAttributeWristbandType(
            self.player, parent=self
        )
        self.wristband_color = PlayerAttributeWristbandColor(
            self.player, parent=self
        )
