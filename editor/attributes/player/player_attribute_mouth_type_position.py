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

from editor.attributes.player.player_attribute_mouth_type import (
    PlayerAttributeMouthType,
)

from editor.attributes.player.player_attribute_mouth_position import (
    PlayerAttributeMouthPosition,
)


class PlayerAttributeMouthTypePosition(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Mouth Type/Position"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 120

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_mouth_type(cls):
        """
        Mouth Type Opts
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
            }
        )
        return options_by_value

    @property
    def array_opts_mouth_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_mouth_type()

    @classmethod
    def att_class_array_opts_mouth_position(cls):
        """
        Mouth Position Opts
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
    def array_opts_mouth_position(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_mouth_position()

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

    def get_mouth_type_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 32)
        return self.array_opts_mouth_type[value]

    def get_mouth_position_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 32)
        return self.array_opts_mouth_position[value]

    def get_label(self):
        mouth_type_label = self.get_mouth_type_label()
        mouth_position_label = self.get_mouth_position_label()
        return (
            mouth_type_label,
            mouth_position_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_mouth_type.inverse[label[0]]
        second_opt_value = self.array_opts_mouth_position.inverse[label[1]]
        return first_opt_value + second_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Mouth Type and Position attributes and link to this attribute
        """
        self.mouth_type = PlayerAttributeMouthType(self.player, parent=self)
        self.mouth_position = PlayerAttributeMouthPosition(
            self.player, parent=self
        )
