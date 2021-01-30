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

from editor.attributes.player.player_attribute_registered_position import (
    PlayerAttributeRegisteredPosition,
)

from editor.attributes.player.player_attribute_dk_style import (
    PlayerAttributeDkStyle,
)

from editor.attributes.player.player_attribute_dribble_style import (
    PlayerAttributeDribbleStyle,
)


class PlayerAttributeRegisteredPosDkDribbleStyle(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Registered Position/DK/Dribble Style"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 53

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_registered_position(cls):
        """
        Registered Position Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_GK,
                32: PlayerAttributeOption.OPT_SW,
                48: PlayerAttributeOption.OPT_CB,
                64: PlayerAttributeOption.OPT_SB,
                80: PlayerAttributeOption.OPT_DM,
                96: PlayerAttributeOption.OPT_WB,
                112: PlayerAttributeOption.OPT_CM,
                128: PlayerAttributeOption.OPT_SM,
                144: PlayerAttributeOption.OPT_AM,
                160: PlayerAttributeOption.OPT_WF,
                176: PlayerAttributeOption.OPT_SS,
                192: PlayerAttributeOption.OPT_CF,
            }
        )
        return options_by_value

    @property
    def array_opts_registered_position(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_registered_position()

    @classmethod
    def att_class_array_opts_dk_style(cls):
        """
        Dropkick Style Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                4: PlayerAttributeOption.OPT_2,
                8: PlayerAttributeOption.OPT_3,
                12: PlayerAttributeOption.OPT_4,
            }
        )
        return options_by_value

    @property
    def array_opts_dk_style(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_dk_style()

    @classmethod
    def att_class_array_opts_dribble_style(cls):
        """
        Dribble Style Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
                3: PlayerAttributeOption.OPT_4,
            }
        )
        return options_by_value

    @property
    def array_opts_dribble_style(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_dribble_style()

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

    def get_registered_position_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 16)
        return self.array_opts_registered_position[value]

    def get_dk_style_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 16)
        value = get_base_byte_value(value, 4)
        return self.array_opts_dk_style[value]

    def get_dribble_style_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 4)
        return self.array_opts_dribble_style[value]

    def get_label(self):
        registered_position_label = self.get_registered_position_label()
        dk_style_label = self.get_dk_style_label()
        dribble_style_label = self.get_dribble_style_label()
        return (
            registered_position_label,
            dk_style_label,
            dribble_style_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_registered_position.inverse[label[0]]
        second_opt_value = self.array_opts_dk_style.inverse[label[1]]
        third_opt_value = self.array_opts_dribble_style.inverse[label[2]]

        return first_opt_value + second_opt_value + third_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Registered Position and Dropkick and Dribble Style attributes
        and link to this attribute
        """
        self.registered_position = PlayerAttributeRegisteredPosition(
            self.player, parent=self
        )
        self.dk_style = PlayerAttributeDkStyle(self.player, parent=self)
        self.dribble_style = PlayerAttributeDribbleStyle(
            self.player, parent=self
        )
