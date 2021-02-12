from bidict import bidict

from editor.utils.common_functions import (
    get_base_byte_value,
    get_lowest_byte_value,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_cap_type import (
    PlayerAttributeCapType,
)

from editor.attributes.player.player_attribute_glasses_color import (
    PlayerAttributeGlassesColor,
)


class PlayerAttributeCapTypeGlassesColor(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Cap Type/Glasses Color"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 110

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_cap_type(cls):
        """
        Cap Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                8: PlayerAttributeOption.OPT_2,
                16: PlayerAttributeOption.OPT_3,
                24: PlayerAttributeOption.OPT_4,
                32: PlayerAttributeOption.OPT_5,
                40: PlayerAttributeOption.OPT_6,
                48: PlayerAttributeOption.OPT_7,
                56: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_cap_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_cap_type()

    @classmethod
    def att_class_array_opts_glasses_color(cls):
        """
        Glasses Color Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
                3: PlayerAttributeOption.OPT_4,
                4: PlayerAttributeOption.OPT_5,
                5: PlayerAttributeOption.OPT_6,
                6: PlayerAttributeOption.OPT_7,
                7: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_glasses_color(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_glasses_color()

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

    def get_cap_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)
        value = get_base_byte_value(value, 8)
        return self.array_opts_cap_type[value]

    def get_glasses_color_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_glasses_color[value]

    def get_label(self):
        cap_type_label = self.get_cap_type_label()
        glasses_color_label = self.get_glasses_color_label()
        return (cap_type_label, glasses_color_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_cap_type.inverse[label[0]]
        second_opt_value = self.array_opts_glasses_color.inverse[label[1]]
        return first_opt_value + second_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Cap Type and Glasses Color attributes and link to this attribute
        """
        self.cap_type = PlayerAttributeCapType(self.player, parent=self)
        self.glasses_color = PlayerAttributeGlassesColor(
            self.player, parent=self
        )
