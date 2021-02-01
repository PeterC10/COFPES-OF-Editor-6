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

from editor.attributes.player.player_attribute_one_on_one_stopper import (
    PlayerAttributeOneOnOneStopper,
)

from editor.attributes.player.player_attribute_penalty_stopper import (
    PlayerAttributePenaltyStopper,
)

from editor.attributes.player.player_attribute_d_line_control import (
    PlayerAttributeDLineControl,
)

from editor.attributes.player.player_attribute_covering import (
    PlayerAttributeCovering,
)

from editor.attributes.player.player_attribute_sliding import (
    PlayerAttributeSliding,
)

from editor.attributes.player.player_attribute_marking import (
    PlayerAttributeMarking,
)

from editor.attributes.player.player_attribute_outside import (
    PlayerAttributeOutside,
)

from editor.attributes.player.player_attribute_one_touch_pass import (
    PlayerAttributeOneTouchPass,
)


class PlayerAttributeOosPksDlcCovSldTckMarkOutOtp(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return (
            "1-on-1 Stopper/Penalty Stopper/D-Line Control/Covering/Sliding/"
            "Marking/Outside/1-Touch Pass"
        )

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.SpecialAbilities

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 82

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_one_on_one_stopper(cls):
        """
        1-on-1 Stopper Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_one_on_one_stopper(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_one_on_one_stopper()

    @classmethod
    def att_class_array_opts_penalty_stopper(cls):
        """
        Penalty Stopper Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                64: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_penalty_stopper(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_penalty_stopper()

    @classmethod
    def att_class_array_opts_d_line_control(cls):
        """
        D-Line Control Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                32: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_d_line_control(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_d_line_control()

    @classmethod
    def att_class_array_opts_covering(cls):
        """
        Covering Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                16: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_covering(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_covering()

    @classmethod
    def att_class_array_opts_sliding(cls):
        """
        Sliding Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                8: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_sliding(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_sliding()

    @classmethod
    def att_class_array_opts_marking(cls):
        """
        Marking Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                4: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_marking(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_marking()

    @classmethod
    def att_class_array_opts_outside(cls):
        """
        Outside Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                2: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_outside(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_outside()

    @classmethod
    def att_class_array_opts_one_touch_pass(cls):
        """
        1-Touch Pass Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                1: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_one_touch_pass(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_one_touch_pass()

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

    def get_one_on_one_stopper_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 128)
        return self.array_opts_one_on_one_stopper[value]

    def get_penalty_stopper_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        value = get_lowest_byte_value(value, 128)
        return self.array_opts_penalty_stopper[value]

    def get_d_line_control_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 32)
        value = get_lowest_byte_value(value, 64)
        return self.array_opts_d_line_control[value]

    def get_covering_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 16)
        value = get_lowest_byte_value(value, 32)
        return self.array_opts_covering[value]

    def get_sliding_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 8)
        value = get_lowest_byte_value(value, 16)
        return self.array_opts_sliding[value]

    def get_marking_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 4)
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_marking[value]

    def get_outside_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 2)
        value = get_lowest_byte_value(value, 4)
        return self.array_opts_outside[value]

    def get_one_touch_pass_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 2)
        return self.array_opts_one_touch_pass[value]

    def get_label(self):
        one_on_one_stopper_label = self.get_one_on_one_stopper_label()
        penalty_stopper_label = self.get_penalty_stopper_label()
        d_line_control_label = self.get_d_line_control_label()
        covering_label = self.get_covering_label()
        sliding_label = self.get_sliding_label()
        marking_label = self.get_marking_label()
        outside_label = self.get_outside_label()
        one_touch_pass_label = self.get_one_touch_pass_label()

        return (
            one_on_one_stopper_label,
            penalty_stopper_label,
            d_line_control_label,
            covering_label,
            sliding_label,
            marking_label,
            outside_label,
            one_touch_pass_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_one_on_one_stopper.inverse[label[0]]
        second_opt_value = self.array_opts_penalty_stopper.inverse[label[1]]
        third_opt_value = self.array_opts_d_line_control.inverse[label[2]]
        fourth_opt_value = self.array_opts_covering.inverse[label[3]]
        fifth_opt_value = self.array_opts_sliding.inverse[label[4]]
        sixth_opt_value = self.array_opts_marking.inverse[label[5]]
        seventh_opt_value = self.array_opts_outside.inverse[label[6]]
        eigth_opt_value = self.array_opts_one_touch_pass.inverse[label[7]]

        return (
            first_opt_value
            + second_opt_value
            + third_opt_value
            + fourth_opt_value
            + fifth_opt_value
            + sixth_opt_value
            + seventh_opt_value
            + eigth_opt_value
        )

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create 1-on-1 Stopper, Penalty Stopper, D-Line Control, Covering,
        Sliding, Marking, Outside, 1-Touch Pass attributes and link to this
        attribute
        """
        self.one_on_one_stopper = PlayerAttributeOneOnOneStopper(
            self.player, parent=self
        )
        self.penalty_stopper = PlayerAttributePenaltyStopper(
            self.player, parent=self
        )
        self.d_line_control = PlayerAttributeDLineControl(
            self.player, parent=self
        )
        self.covering = PlayerAttributeCovering(self.player, parent=self)
        self.sliding = PlayerAttributeSliding(self.player, parent=self)
        self.marking = PlayerAttributeMarking(self.player, parent=self)
        self.outside = PlayerAttributeOutside(self.player, parent=self)
        self.one_touch_pass = PlayerAttributeOneTouchPass(
            self.player, parent=self
        )
