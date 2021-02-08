from bidict import bidict

from editor.utils.common_functions import (
    get_lowest_byte_value,
    get_base_byte_value,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_hair_color_type import (
    PlayerAttributeHairColorType,
)

from editor.attributes.player.player_attribute_hair_color_pattern import (
    PlayerAttributeHairColorPattern,
)

from editor.attributes.player.player_attribute_eye_color_one import (
    PlayerAttributeEyeColorOne,
)


class PlayerAttributeHairColorTypePatternEyeColOne(PlayerAttribute):
    MIN_PATTERN_VALUE = 1
    MAX_PATTERN_VALUE = 62
    MAX_PATTERN_BYTE_VALUE = 61
    RGB_BASE_BYTE_VALUE = 62

    @classmethod
    def att_class_name(cls):
        return "Hair Color Type/Pattern/Eye Color 1"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 94

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_eye_color_one(cls):
        """
        Eye Color One Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                64: PlayerAttributeOption.OPT_2,
                128: PlayerAttributeOption.OPT_3,
                192: PlayerAttributeOption.OPT_4,
            }
        )
        return options_by_value

    @property
    def array_opts_eye_color_one(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eye_color_one()

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
        return self.get_raw_value()

    def get_hair_color_type_label(self):
        value = self.get_value()

        hair_color_type_label = PlayerAttributeOption.OPT_PATTERN
        if value in [62, 126, 190]:
            hair_color_type_label = PlayerAttributeOption.OPT_RGB

        return hair_color_type_label

    def get_hair_color_pattern_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)

        if value == self.RGB_BASE_BYTE_VALUE:
            value = 0

        hair_color_pattern_label = str(value + 1)
        return hair_color_pattern_label

    def get_eye_color_one_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        return self.array_opts_eye_color_one[value]

    def get_label(self):
        hair_color_type_label = self.get_hair_color_type_label()
        hair_color_pattern = self.get_hair_color_pattern_label()
        eye_color_one_label = self.get_eye_color_one_label()
        return (hair_color_type_label, hair_color_pattern, eye_color_one_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        hair_color_type_label = label[0]
        hair_color_pattern_label = label[1]
        hair_color_value = 0

        hair_color_pattern = int(hair_color_pattern_label)

        if hair_color_pattern < self.MIN_PATTERN_VALUE:
            hair_color_pattern = self.MIN_PATTERN_VALUE
        elif hair_color_pattern > self.MAX_PATTERN_VALUE:
            hair_color_pattern = self.MAX_PATTERN_VALUE

        if hair_color_type_label == PlayerAttributeOption.OPT_RGB:
            hair_color_value = 62
        else:
            hair_color_value = hair_color_pattern - 1

        eye_color_one_value = self.array_opts_eye_color_one.inverse[label[2]]
        return hair_color_value + eye_color_one_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Hair Color Type and Hair Color Pattern and Eye Color One
        attributes and link to this attribute
        """
        self.hair_color_type = PlayerAttributeHairColorType(
            self.player, parent=self
        )
        self.hair_color_pattern = PlayerAttributeHairColorPattern(
            self.player, parent=self
        )
        self.eye_color_one = PlayerAttributeEyeColorOne(
            self.player, parent=self
        )
