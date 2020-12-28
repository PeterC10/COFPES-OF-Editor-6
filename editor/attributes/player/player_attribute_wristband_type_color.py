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

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_wristband_type import (
    PlayerAttributeWristbandType,
)

from editor.attributes.player.player_attribute_wristband_color import (
    PlayerAttributeWristbandColor,
)


class PlayerAttributeWristbandTypeColor(PlayerAttribute):
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
    def att_class_array_opts_wristband_type(cls):
        """
        Wristband Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                8: PlayerAttributeOption.OPT_L,
                16: PlayerAttributeOption.OPT_R,
                24: PlayerAttributeOption.OPT_B
            }
        )
        return options_by_value

    @property
    def array_opts_wristband_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_wristband_type()

    @classmethod
    def att_class_array_opts_wristband_color(cls):
        """
        Wristband Color Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_WHITE,
                32: PlayerAttributeOption.OPT_BLACK,
                64: PlayerAttributeOption.OPT_RED,
                96: PlayerAttributeOption.OPT_BLUE,
                128: PlayerAttributeOption.OPT_YELLOW,
                160: PlayerAttributeOption.OPT_GREEN,
                192: PlayerAttributeOption.OPT_PURPLE,
                224: PlayerAttributeOption.OPT_CYAN,
            }
        )
        return options_by_value

    @property
    def array_opts_wristband_color(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_wristband_color()

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
        if value in self.array_opts_wristband_color:
            value = 0

        return value

    def get_wristband_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        value = round_down(value, 8)
        return self.array_opts_wristband_type[value]

    def get_wristband_color_label(self):
        label = PlayerAttributeOption.OPT_NONE
        wristband_type = self.get_wristband_type_label()
        value = self.get_value()
        value = get_base_byte_value(value, 32)

        if wristband_type != PlayerAttributeOption.OPT_N:
            label = self.array_opts_wristband_color[value]

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
        first_opt_value = self.array_opts_wristband_type.inverse[label[0]]

        second_opt_value = 0
        # Only check colour if wristband type is not "None"
        if first_opt_value != 0:
            second_opt_value = self.array_opts_wristband_color.inverse[label[1]]

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
