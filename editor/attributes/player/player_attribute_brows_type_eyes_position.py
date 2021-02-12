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

from editor.attributes.player.player_attribute_brows_type import (
    PlayerAttributeBrowsType,
)

from editor.attributes.player.player_attribute_eyes_position import (
    PlayerAttributeEyesPosition,
)


class PlayerAttributeBrowsTypeEyesPosition(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Brows Type/Eyes Position"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 116

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_brows_type(cls):
        """
        Brows Type Opts
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
                8: PlayerAttributeOption.OPT_9,
                9: PlayerAttributeOption.OPT_10,
                10: PlayerAttributeOption.OPT_11,
                11: PlayerAttributeOption.OPT_12,
                12: PlayerAttributeOption.OPT_13,
                13: PlayerAttributeOption.OPT_14,
                14: PlayerAttributeOption.OPT_15,
                15: PlayerAttributeOption.OPT_16,
                16: PlayerAttributeOption.OPT_17,
                17: PlayerAttributeOption.OPT_18,
                18: PlayerAttributeOption.OPT_19,
                19: PlayerAttributeOption.OPT_20,
                20: PlayerAttributeOption.OPT_21,
                21: PlayerAttributeOption.OPT_22,
                22: PlayerAttributeOption.OPT_23,
                23: PlayerAttributeOption.OPT_24,
                24: PlayerAttributeOption.OPT_25,
                25: PlayerAttributeOption.OPT_26,
                26: PlayerAttributeOption.OPT_27,
                27: PlayerAttributeOption.OPT_28,
                28: PlayerAttributeOption.OPT_29,
                29: PlayerAttributeOption.OPT_30,
                30: PlayerAttributeOption.OPT_31,
                31: PlayerAttributeOption.OPT_32,
            }
        )
        return options_by_value

    @property
    def array_opts_brows_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_brows_type()

    @classmethod
    def att_class_array_opts_eyes_position(cls):
        """
        Eyes Position Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                32: PlayerAttributeOption.OPT_2,
                64: PlayerAttributeOption.OPT_1,
                96: PlayerAttributeOption.OPT_0,
                128: PlayerAttributeOption.OPT_M1,
                160: PlayerAttributeOption.OPT_M2,
                192: PlayerAttributeOption.OPT_M3,
                224: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_eyes_position(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eyes_position()

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

    def get_brows_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        return self.array_opts_brows_type[value]

    def get_eyes_position_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 32)
        return self.array_opts_eyes_position[value]

    def get_label(self):
        brows_type_label = self.get_brows_type_label()
        eyes_position_label = self.get_eyes_position_label()
        return (brows_type_label, eyes_position_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_brows_type.inverse[label[0]]
        second_opt_value = self.array_opts_eyes_position.inverse[label[1]]
        return first_opt_value + second_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Brows Type and Eyes Position attributes and link to this attribute
        """
        self.brows_type = PlayerAttributeBrowsType(self.player, parent=self)
        self.eyes_position = PlayerAttributeEyesPosition(
            self.player, parent=self
        )
