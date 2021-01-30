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

from editor.attributes.player.player_attribute_stronger_foot import (
    PlayerAttributeStrongerFoot,
)

from editor.attributes.player.player_attribute_fk_style import (
    PlayerAttributeFkStyle,
)

from editor.attributes.player.player_attribute_pk_style import (
    PlayerAttributePkStyle,
)


class PlayerAttributeStrongerFootFkPkStyle(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Stronger Foot/FK/PK Style"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 52

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_stronger_foot(cls):
        """
        Stronger Foot Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_R,
                1: PlayerAttributeOption.OPT_L,
            }
        )
        return options_by_value

    @property
    def array_opts_stronger_foot(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_stronger_foot()

    @classmethod
    def att_class_array_opts_fk_style(cls):
        """
        Freekick Style Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                2: PlayerAttributeOption.OPT_2,
                4: PlayerAttributeOption.OPT_3,
                6: PlayerAttributeOption.OPT_4,
                8: PlayerAttributeOption.OPT_5,
                10: PlayerAttributeOption.OPT_6,
                12: PlayerAttributeOption.OPT_7,
                14: PlayerAttributeOption.OPT_8,
                16: PlayerAttributeOption.OPT_9,
                18: PlayerAttributeOption.OPT_10,
                20: PlayerAttributeOption.OPT_11,
                22: PlayerAttributeOption.OPT_12,
                24: PlayerAttributeOption.OPT_13,
                26: PlayerAttributeOption.OPT_14,
                28: PlayerAttributeOption.OPT_15,
                30: PlayerAttributeOption.OPT_16,
            }
        )
        return options_by_value

    @property
    def array_opts_fk_style(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_fk_style()

    @classmethod
    def att_class_array_opts_pk_style(cls):
        """
        Penalty kick Style Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                32: PlayerAttributeOption.OPT_2,
                64: PlayerAttributeOption.OPT_3,
                96: PlayerAttributeOption.OPT_4,
                128: PlayerAttributeOption.OPT_5,
                160: PlayerAttributeOption.OPT_6,
                192: PlayerAttributeOption.OPT_7,
                224: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_pk_style(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_pk_style()

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

    def get_stronger_foot_label(self):
        value = self.get_value()
        value = value % 2
        return self.array_opts_stronger_foot[value]

    def get_fk_style_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        # If left footed take away one to get fk style mapping
        if value % 2:
            value -= 1

        return self.array_opts_fk_style[value]

    def get_pk_style_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 32)
        return self.array_opts_pk_style[value]

    def get_label(self):
        stronger_foot_label = self.get_stronger_foot_label()
        fk_style_label = self.get_fk_style_label()
        pk_style_label = self.get_pk_style_label()
        return (
            stronger_foot_label,
            fk_style_label,
            pk_style_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_stronger_foot.inverse[label[0]]
        second_opt_value = self.array_opts_fk_style.inverse[label[1]]
        third_opt_value = self.array_opts_pk_style.inverse[label[2]]

        return first_opt_value + second_opt_value + third_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Stronger Foot and FK and PK Style attributes
        and link to this attribute
        """
        self.stronger_foot = PlayerAttributeStrongerFoot(
            self.player, parent=self
        )
        self.fk_style = PlayerAttributeFkStyle(
            self.player, parent=self
        )
        self.pk_style = PlayerAttributePkStyle(
            self.player, parent=self
        )
