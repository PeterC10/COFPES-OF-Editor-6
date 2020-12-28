from bidict import bidict

from editor.utils.common_functions import (
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

from editor.attributes.player.player_attribute_bracelet_type import (
    PlayerAttributeBraceletType,
)

from editor.attributes.player.player_attribute_bracelet_color import (
    PlayerAttributeBraceletColor,
)

from editor.attributes.player.player_attribute_undershorts import (
    PlayerAttributeUndershorts,
)


class PlayerAttributeBraceletTypeColorUndershorts(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Bracelet Type + Color/Undershorts"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Accessories

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 99

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_bracelet_type(cls):
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                1: PlayerAttributeOption.OPT_L,
                2: PlayerAttributeOption.OPT_R,
            }
        )
        return options_by_value

    @property
    def array_opts_bracelet_type(self):
        return self.att_class_array_opts_bracelet_type()

    @classmethod
    def att_class_array_opts_bracelet_color(cls):
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_WHITE,
                4: PlayerAttributeOption.OPT_BLACK,
                8: PlayerAttributeOption.OPT_RED,
                12: PlayerAttributeOption.OPT_BLUE,
                16: PlayerAttributeOption.OPT_YELLOW,
                20: PlayerAttributeOption.OPT_GREEN,
                24: PlayerAttributeOption.OPT_PURPLE,
                28: PlayerAttributeOption.OPT_CYAN,
            }
        )
        return options_by_value

    @property
    def array_opts_bracelet_color(self):
        return self.att_class_array_opts_bracelet_color()

    @classmethod
    def att_class_array_opts_undershorts(cls):
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_undershorts(self):
        return self.att_class_array_opts_undershorts()

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

    def get_bracelet_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 4)
        return self.array_opts_bracelet_type[value]

    def get_bracelet_color_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        value = round_down(value, 4)
        return self.array_opts_bracelet_color[value]

    def get_undershorts_label(self):
        value = self.get_value()
        value = round_down(value, 128)
        return self.array_opts_undershorts[value]

    def get_label(self):
        bracelet_type_label = self.get_bracelet_type_label()
        bracelet_color_label = self.get_bracelet_color_label()
        undershorts_label = self.get_undershorts_label()
        return (bracelet_type_label, bracelet_color_label, undershorts_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_bracelet_type.inverse[label[0]]
        second_opt_value = self.array_opts_bracelet_color.inverse[label[1]]
        third_opt_value = self.array_opts_undershorts.inverse[label[2]]

        return first_opt_value + second_opt_value + third_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Bracelet Type, Color and Undershorts attributes
        and link to this attribute
        """
        self.bracelet_type = PlayerAttributeBraceletType(
            self.player, parent=self
        )
        self.barcelet_color = PlayerAttributeBraceletColor(
            self.player, parent=self
        )
        self.undershorts = PlayerAttributeUndershorts(self.player, parent=self)
