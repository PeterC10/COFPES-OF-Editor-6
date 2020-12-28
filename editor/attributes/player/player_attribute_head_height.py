from bidict import bidict

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.utils.common_functions import get_base_byte_value


class PlayerAttributeHeadHeight(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Head Height"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 90

    @classmethod
    def att_class_array_opts(cls):
        """
        Head Height opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_M7,
                16: PlayerAttributeOption.OPT_M6,
                32: PlayerAttributeOption.OPT_M5,
                48: PlayerAttributeOption.OPT_M4,
                64: PlayerAttributeOption.OPT_M3,
                80: PlayerAttributeOption.OPT_M2,
                96: PlayerAttributeOption.OPT_M1,
                112: PlayerAttributeOption.OPT_0,
                128: PlayerAttributeOption.OPT_1,
                144: PlayerAttributeOption.OPT_2,
                160: PlayerAttributeOption.OPT_3,
                176: PlayerAttributeOption.OPT_4,
                192: PlayerAttributeOption.OPT_5,
                208: PlayerAttributeOption.OPT_6,
                224: PlayerAttributeOption.OPT_7,
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
        """
        Get byte value via `get_raw_value`.

        Get base byte value (to be used to identify label)
        """
        value = self.get_raw_value()
        byte_factor = 16
        value = get_base_byte_value(value, byte_factor)
        return value

    def get_label(self):
        value = self.get_value()
        label = self.array_opts[value]
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = self.array_opts.inverse[label]
        self.set_value(value)
        return True
