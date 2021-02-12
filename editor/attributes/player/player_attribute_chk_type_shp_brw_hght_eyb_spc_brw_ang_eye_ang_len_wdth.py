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

from editor.attributes.player.player_attribute_cheek_type import (
    PlayerAttributeCheekType,
)

from editor.attributes.player.player_attribute_cheek_shape import (
    PlayerAttributeCheekShape,
)

from editor.attributes.player.player_attribute_brows_height import (
    PlayerAttributeBrowsHeight,
)

from editor.attributes.player.player_attribute_eyebrow_spacing import (
    PlayerAttributeEyebrowSpacing,
)

from editor.attributes.player.player_attribute_brows_angle import (
    PlayerAttributeBrowsAngle,
)

from editor.attributes.player.player_attribute_eyes_angle import (
    PlayerAttributeEyesAngle,
)

from editor.attributes.player.player_attribute_eyes_length import (
    PlayerAttributeEyesLength,
)

from editor.attributes.player.player_attribute_eyes_width import (
    PlayerAttributeEyesWidth,
)


class PlayerAttributeChkTypeShpBrwHghtEybSpcBrwAngEyeAngLenWdth(
    PlayerAttribute
):
    @classmethod
    def att_class_name(cls):
        return (
            "Cheek Type/Shape/Brows Height/Eyebrow Spacing/Brows Angle/"
            "Eyes Angle/Length/Width"
        )

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return (117, 118, 119)

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_eyes_angle(cls):
        """
        Eyes Angle Opts
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
    def array_opts_eyes_angle(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eyes_angle()

    @classmethod
    def att_class_array_opts_eyes_length(cls):
        """
        Eyes Length Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                8: PlayerAttributeOption.OPT_2,
                16: PlayerAttributeOption.OPT_1,
                24: PlayerAttributeOption.OPT_0,
                32: PlayerAttributeOption.OPT_M1,
                40: PlayerAttributeOption.OPT_M2,
                48: PlayerAttributeOption.OPT_M3,
                56: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_eyes_length(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eyes_length()

    @classmethod
    def att_class_array_opts_eyes_width(cls):
        """
        Eyes Width Opts
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
    def array_opts_eyes_width(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eyes_width()

    @classmethod
    def att_class_array_opts_brows_height(cls):
        """
        Brows Height Opts
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
    def array_opts_brows_height(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_brows_height()

    @classmethod
    def att_class_array_opts_eyebrow_spacing(cls):
        """
        Eyebrow Spacing Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_3,
                16: PlayerAttributeOption.OPT_2,
                32: PlayerAttributeOption.OPT_1,
                48: PlayerAttributeOption.OPT_0,
                64: PlayerAttributeOption.OPT_M1,
                80: PlayerAttributeOption.OPT_M2,
                96: PlayerAttributeOption.OPT_M3,
                112: PlayerAttributeOption.OPT_M4,
            }
        )
        return options_by_value

    @property
    def array_opts_eyebrow_spacing(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eyebrow_spacing()

    @classmethod
    def att_class_array_opts_brows_angle(cls):
        """
        Brows Angle Opts
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
    def array_opts_brows_angle(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_brows_angle()

    @classmethod
    def att_class_array_opts_cheek_shape(cls):
        """
        Cheek Shape Opts
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
    def array_opts_cheek_shape(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_cheek_shape()

    @classmethod
    def att_class_array_opts_cheek_type(cls):
        """
        Cheek Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                4: PlayerAttributeOption.OPT_2,
                8: PlayerAttributeOption.OPT_3,
                12: PlayerAttributeOption.OPT_4,
                16: PlayerAttributeOption.OPT_5,
                20: PlayerAttributeOption.OPT_6,
                24: PlayerAttributeOption.OPT_7,
                28: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_cheek_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_cheek_type()

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

    def get_cheek_type_label(self):
        value = self.get_value()[2]
        value = get_lowest_byte_value(value, 32)
        value = get_base_byte_value(value, 4)
        return self.array_opts_cheek_type[value]

    def get_cheek_shape_label(self):
        value = self.get_value()[2]
        value = get_base_byte_value(value, 32)
        return self.array_opts_cheek_shape[value]

    def get_brows_height_label(self):
        value = self.get_value()[1]
        value = get_lowest_byte_value(value, 16)
        value = get_base_byte_value(value, 2)
        return self.array_opts_brows_height[value]

    def get_eyebrow_spacing_label(self):
        value = self.get_value()[1]
        value = get_lowest_byte_value(value, 128)
        value = get_base_byte_value(value, 16)
        return self.array_opts_eyebrow_spacing[value]

    def get_brows_angle_label(self):
        value118, value119 = self.get_value()[-2:]
        value118 = get_base_byte_value(value118, 128)
        value119 = get_lowest_byte_value(value119, 4)
        return self.array_opts_brows_angle[(value118, value119)]

    def get_eyes_angle_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_eyes_angle[value]

    def get_eyes_length_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 64)
        value = get_base_byte_value(value, 8)
        return self.array_opts_eyes_length[value]

    def get_eyes_width_label(self):
        value117, value118 = self.get_value()[:2]
        value117 = get_base_byte_value(value117, 64)
        value118 = get_lowest_byte_value(value118, 2)
        return self.array_opts_eyes_width[(value117, value118)]

    def get_label(self):
        cheek_type_label = self.get_cheek_type_label()
        cheek_shape_label = self.get_cheek_shape_label()
        brows_height_label = self.get_brows_height_label()
        eyebrow_spacing_label = self.get_eyebrow_spacing_label()
        brows_angle_label = self.get_brows_angle_label()
        eyes_angle_label = self.get_eyes_angle_label()
        eyes_length_label = self.get_eyes_length_label()
        eyes_width_label = self.get_eyes_width_label()

        return (
            cheek_type_label,
            cheek_shape_label,
            brows_height_label,
            eyebrow_spacing_label,
            brows_angle_label,
            eyes_angle_label,
            eyes_length_label,
            eyes_width_label,
        )

    def set_value(self, value):
        val_117, val_118, val_119 = value
        of_data = self.player.option_file.data

        of_data[self.player.address + self.array_pos[0]] = val_117
        of_data[self.player.address + self.array_pos[1]] = val_118
        of_data[self.player.address + self.array_pos[2]] = val_119
        return True

    def get_value_from_label(self, label):
        val_117 = 0
        val_118 = 0
        val_119 = 0

        cheek_type_value = self.array_opts_cheek_type.inverse[label[0]]
        cheek_shape_value = self.array_opts_cheek_shape.inverse[label[1]]
        brows_height_value = self.array_opts_brows_height.inverse[label[2]]
        eyebrow_spacing_value = self.array_opts_eyebrow_spacing.inverse[
            label[3]
        ]
        brows_angle_values = self.array_opts_brows_angle.inverse[label[4]]
        eyes_angle_value = self.array_opts_eyes_angle.inverse[label[5]]
        eyes_length_value = self.array_opts_eyes_length.inverse[label[6]]
        eyes_width_values = self.array_opts_eyes_width.inverse[label[7]]

        val_117 += eyes_angle_value
        val_117 += eyes_length_value
        val_117 += eyes_width_values[0]

        val_118 += brows_height_value
        val_118 += eyebrow_spacing_value
        val_118 += brows_angle_values[0]
        val_118 += eyes_width_values[1]

        val_119 += cheek_type_value
        val_119 += cheek_shape_value
        val_119 += brows_angle_values[1]

        return (val_117, val_118, val_119)

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Cheek Type/Shape and Brows Height and Eyebrow Spacing and
        Brows Angle and Eyes Angle/Length/Width and link to this attribute
        """
        self.cheek_type = PlayerAttributeCheekType(self.player, parent=self)
        self.cheek_shape = PlayerAttributeCheekShape(self.player, parent=self)
        self.brows_height = PlayerAttributeBrowsHeight(self.player, parent=self)
        self.eyebrow_spacing = PlayerAttributeEyebrowSpacing(
            self.player, parent=self
        )
        self.brows_angle = PlayerAttributeBrowsAngle(self.player, parent=self)
        self.eyes_angle = PlayerAttributeEyesAngle(self.player, parent=self)
        self.eyes_length = PlayerAttributeEyesLength(self.player, parent=self)
        self.eyes_width = PlayerAttributeEyesWidth(self.player, parent=self)
