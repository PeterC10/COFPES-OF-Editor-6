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

from editor.attributes.player.player_attribute_head_position import (
    PlayerAttributeHeadPosition,
)

from editor.attributes.player.player_attribute_nose_type import (
    PlayerAttributeNoseType,
)

from editor.attributes.player.player_attribute_nose_height import (
    PlayerAttributeNoseHeight,
)

from editor.attributes.player.player_attribute_nose_width import (
    PlayerAttributeNoseWidth,
)

from editor.attributes.player.player_attribute_mouth_size import (
    PlayerAttributeMouthSize,
)

from editor.attributes.player.player_attribute_jaw_type import (
    PlayerAttributeJawType,
)

from editor.attributes.player.player_attribute_chin_height import (
    PlayerAttributeChinHeight,
)

from editor.attributes.player.player_attribute_chin_width import (
    PlayerAttributeChinWidth,
)


class PlayerAttributeHeadPosNoseTypeHghtWdthMthSJawTChinHghtWdth(
    PlayerAttribute
):
    @classmethod
    def att_class_name(cls):
        return (
            "Head Position/Nose Type/Height/Width/Mouth Size/Jaw Type/"
            "Chin Height/Width"
        )

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return (121, 122, 123)

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_mouth_size(cls):
        """
        Mouth Size Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_1,
                3: PlayerAttributeOption.OPT_0,
                4: PlayerAttributeOption.OPT_M1,
                5: PlayerAttributeOption.OPT_M2,
                6: PlayerAttributeOption.OPT_M3,
                7: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_mouth_size(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_mouth_size()

    @classmethod
    def att_class_array_opts_nose_type(cls):
        """
        Nose Type Opts
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
    def array_opts_nose_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_nose_type()

    @classmethod
    def att_class_array_opts_nose_width(cls):
        """
        Nose Width Opts
        """
        options_by_value = bidict(
            {
                (0, 0): PlayerAttributeOption.OPT_3,
                (64, 0): PlayerAttributeOption.OPT_2,
                (128, 0): PlayerAttributeOption.OPT_1,
                (192, 0): PlayerAttributeOption.OPT_0,
                (0, 1): PlayerAttributeOption.OPT_M1,
                (64, 1): PlayerAttributeOption.OPT_M2,
                (128, 1): PlayerAttributeOption.OPT_M3,
                (192, 1): PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_nose_width(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_nose_width()

    @classmethod
    def att_class_array_opts_nose_height(cls):
        """
        Nose Height Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                2: PlayerAttributeOption.OPT_2,
                4: PlayerAttributeOption.OPT_1,
                6: PlayerAttributeOption.OPT_0,
                8: PlayerAttributeOption.OPT_M1,
                10: PlayerAttributeOption.OPT_M2,
                12: PlayerAttributeOption.OPT_M3,
                14: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_nose_height(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_nose_height()

    @classmethod
    def att_class_array_opts_jaw_type(cls):
        """
        Jaw Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                16: PlayerAttributeOption.OPT_2,
                32: PlayerAttributeOption.OPT_3,
                48: PlayerAttributeOption.OPT_4,
                64: PlayerAttributeOption.OPT_5,
                80: PlayerAttributeOption.OPT_6,
                96: PlayerAttributeOption.OPT_7,
                112: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_jaw_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_jaw_type()

    @classmethod
    def att_class_array_opts_chin_height(cls):
        """
        Chin Height Opts
        """
        options_by_value = bidict(
            {
                (0, 0): PlayerAttributeOption.OPT_3,
                (0, 1): PlayerAttributeOption.OPT_1,
                (0, 2): PlayerAttributeOption.OPT_M1,
                (0, 3): PlayerAttributeOption.OPT_M3,
                (128, 0): PlayerAttributeOption.OPT_2,
                (128, 1): PlayerAttributeOption.OPT_0,
                (128, 2): PlayerAttributeOption.OPT_M2,
                (128, 3): PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_chin_height(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_chin_height()

    @classmethod
    def att_class_array_opts_head_position(cls):
        """
        Head Position Opts
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
    def array_opts_head_position(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_head_position()

    @classmethod
    def att_class_array_opts_chin_width(cls):
        """
        Chin Width Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                4: PlayerAttributeOption.OPT_2,
                8: PlayerAttributeOption.OPT_1,
                12: PlayerAttributeOption.OPT_0,
                16: PlayerAttributeOption.OPT_M1,
                20: PlayerAttributeOption.OPT_M2,
                24: PlayerAttributeOption.OPT_M3,
                28: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_chin_width(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_chin_width()

    @classmethod
    def att_class_hidden(cls):
        return True

    def get_raw_value(self):
        """
        Get byte value currently set in player's byte array
        """
        of_data = self.player.option_file.data
        value1 = of_data[self.player.address + self.array_pos[0]]
        value2 = of_data[self.player.address + self.array_pos[1]]
        value3 = of_data[self.player.address + self.array_pos[2]]
        return (value1, value2, value3)

    def get_value(self):
        value = self.get_raw_value()
        return value

    def get_head_position_label(self):
        value = self.get_value()[2]
        value = get_base_byte_value(value, 32)
        return self.array_opts_head_position[value]

    def get_nose_type_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 64)
        value = get_base_byte_value(value, 8)
        return self.array_opts_nose_type[value]

    def get_nose_height_label(self):
        value = self.get_value()[1]
        value = get_lowest_byte_value(value, 16)
        value = get_base_byte_value(value, 2)
        return self.array_opts_nose_height[value]

    def get_nose_width_label(self):
        value121, value122 = self.get_value()[:2]
        value121 = get_base_byte_value(value121, 64)
        value122 = get_lowest_byte_value(value122, 2)
        return self.array_opts_nose_width[(value121, value122)]

    def get_mouth_size_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_mouth_size[value]

    def get_jaw_type_label(self):
        value = self.get_value()[1]
        value = get_lowest_byte_value(value, 128)
        value = get_base_byte_value(value, 16)
        return self.array_opts_jaw_type[value]

    def get_chin_height_label(self):
        value122, value123 = self.get_value()[-2:]
        value122 = get_base_byte_value(value122, 128)
        value123 = get_lowest_byte_value(value123, 4)
        return self.array_opts_chin_height[(value122, value123)]

    def get_chin_width_label(self):
        value = self.get_value()[2]
        value = get_lowest_byte_value(value, 32)
        value = get_base_byte_value(value, 4)
        return self.array_opts_chin_width[value]

    def get_label(self):
        head_position_label = self.get_head_position_label()
        nose_type_label = self.get_nose_type_label()
        nose_height_label = self.get_nose_height_label()
        nose_width_label = self.get_nose_width_label()
        mouth_size_label = self.get_mouth_size_label()
        jaw_type_label = self.get_jaw_type_label()
        chin_height_label = self.get_chin_height_label()
        chin_width_label = self.get_chin_width_label()

        return (
            head_position_label,
            nose_type_label,
            nose_height_label,
            nose_width_label,
            mouth_size_label,
            jaw_type_label,
            chin_height_label,
            chin_width_label,
        )

    def set_value(self, value):
        val_121, val_122, val_123 = value
        of_data = self.player.option_file.data

        of_data[self.player.address + self.array_pos[0]] = val_121
        of_data[self.player.address + self.array_pos[1]] = val_122
        of_data[self.player.address + self.array_pos[2]] = val_123
        return True

    def get_value_from_label(self, label):
        val_121 = 0
        val_122 = 0
        val_123 = 0

        head_position_value = self.array_opts_head_position.inverse[label[0]]
        nose_type_value = self.array_opts_nose_type.inverse[label[1]]
        nose_height_value = self.array_opts_nose_height.inverse[label[2]]
        nose_width_values = self.array_opts_nose_width.inverse[label[3]]
        mouth_size_value = self.array_opts_mouth_size.inverse[label[4]]
        jaw_type_value = self.array_opts_jaw_type.inverse[label[5]]
        chin_height_values = self.array_opts_chin_height.inverse[label[6]]
        chin_width_value = self.array_opts_chin_width.inverse[label[7]]

        val_121 += nose_type_value
        val_121 += nose_width_values[0]
        val_121 += mouth_size_value

        val_122 += nose_height_value
        val_122 += nose_width_values[1]
        val_122 += jaw_type_value
        val_122 += chin_height_values[0]

        val_123 += head_position_value
        val_123 += chin_height_values[1]
        val_123 += chin_width_value

        return (val_121, val_122, val_123)

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Head Position and Nose Type/Height/Width and Mouth Size and
        Jaw Type and Chin Height/Width and link to this attribute
        """
        self.head_position = PlayerAttributeHeadPosition(
            self.player, parent=self
        )
        self.nose_type = PlayerAttributeNoseType(self.player, parent=self)
        self.nose_height = PlayerAttributeNoseHeight(self.player, parent=self)
        self.nose_width = PlayerAttributeNoseWidth(self.player, parent=self)
        self.mouth_size = PlayerAttributeMouthSize(self.player, parent=self)
        self.jaw_type = PlayerAttributeJawType(self.player, parent=self)
        self.chin_height = PlayerAttributeChinHeight(self.player, parent=self)
        self.chin_width = PlayerAttributeChinWidth(self.player, parent=self)
