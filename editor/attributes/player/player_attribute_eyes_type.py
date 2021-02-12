from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)


class PlayerAttributeEyesType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Eyes Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 115

    @classmethod
    def att_class_array_opts(cls):
        """
        Eyes Type opts
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
                64: PlayerAttributeOption.OPT_9,
                72: PlayerAttributeOption.OPT_10,
                80: PlayerAttributeOption.OPT_11,
                88: PlayerAttributeOption.OPT_12,
                96: PlayerAttributeOption.OPT_13,
                104: PlayerAttributeOption.OPT_14,
                112: PlayerAttributeOption.OPT_15,
                120: PlayerAttributeOption.OPT_16,
                128: PlayerAttributeOption.OPT_17,
                136: PlayerAttributeOption.OPT_18,
                144: PlayerAttributeOption.OPT_19,
                152: PlayerAttributeOption.OPT_20,
                160: PlayerAttributeOption.OPT_21,
                168: PlayerAttributeOption.OPT_22,
                176: PlayerAttributeOption.OPT_23,
                184: PlayerAttributeOption.OPT_24,
                192: PlayerAttributeOption.OPT_25,
                200: PlayerAttributeOption.OPT_26,
                208: PlayerAttributeOption.OPT_27,
                216: PlayerAttributeOption.OPT_28,
                224: PlayerAttributeOption.OPT_29,
                232: PlayerAttributeOption.OPT_30,
                240: PlayerAttributeOption.OPT_31,
                248: PlayerAttributeOption.OPT_32,
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
        value = self.get_raw_value()
        value = get_base_byte_value(value, 8)
        return value

    def get_label(self):
        value = self.get_value()
        label = self.array_opts[value]
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        return self.array_opts.inverse[label]

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True
