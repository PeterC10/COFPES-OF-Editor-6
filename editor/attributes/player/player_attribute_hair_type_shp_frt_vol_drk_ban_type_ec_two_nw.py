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

from editor.attributes.player.player_attribute_hair_type import (
    PlayerAttributeHairType,
)

from editor.attributes.player.player_attribute_hair_shape import (
    PlayerAttributeHairShape,
)

from editor.attributes.player.player_attribute_hair_front import (
    PlayerAttributeHairFront,
)

from editor.attributes.player.player_attribute_hair_volume import (
    PlayerAttributeHairVolume,
)

from editor.attributes.player.player_attribute_hair_darkness import (
    PlayerAttributeHairDarkness,
)

from editor.attributes.player.player_attribute_bandana_type import (
    PlayerAttributeBandanaType,
)

from editor.attributes.player.player_attribute_eye_color_two import (
    PlayerAttributeEyeColorTwo,
)

from editor.attributes.player.player_attribute_neck_warmer import (
    PlayerAttributeNeckWarmer,
)


class PlayerAttributeHairTypeShpFrtVolDrkBanTypeEcTwoNw(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return (
            "Hair Type/Shape/Front/Volume/Darkness/Bandana Type/Eye Color 2/"
            "Neck Warmer"
        )

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return (92, 93)

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_eye_color_two(cls):
        """
        Eye Color 2 Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_BLACK_1,
                8: PlayerAttributeOption.OPT_BLACK_2,
                16: PlayerAttributeOption.OPT_DARK_GREY_1,
                24: PlayerAttributeOption.OPT_DARK_GREY_2,
                32: PlayerAttributeOption.OPT_BROWN_1,
                40: PlayerAttributeOption.OPT_BROWN_2,
                48: PlayerAttributeOption.OPT_LIGHT_BLUE_1,
                56: PlayerAttributeOption.OPT_LIGHT_BLUE_2,
                64: PlayerAttributeOption.OPT_BLUE_1,
                72: PlayerAttributeOption.OPT_BLUE_2,
                80: PlayerAttributeOption.OPT_GREEN_1,
                88: PlayerAttributeOption.OPT_GREEN_2,
            }
        )
        return options_by_value

    @property
    def array_opts_eye_color_two(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_eye_color_two()

    @classmethod
    def att_class_array_opts_neck_warmer(cls):
        """
        Neck Warmer Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_neck_warmer(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_neck_warmer()

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
        return (value1, value2)

    def get_value(self):
        value = self.get_raw_value()
        return value

    def get_hair_key_bald(self, value):
        hair_type = PlayerAttributeOption.OPT_BALD
        hair_shape = str(value + 1)
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_buzz_cut(self, value):
        darkness_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
            2: PlayerAttributeOption.OPT_3,
            3: PlayerAttributeOption.OPT_4,
        }

        darkness_value = get_lowest_byte_value(value, 4)
        darkness_value = darkness_by_value[darkness_value]

        front_by_value = {
            4: PlayerAttributeOption.OPT_1,
            8: PlayerAttributeOption.OPT_2,
            12: PlayerAttributeOption.OPT_3,
            16: PlayerAttributeOption.OPT_4,
            0: PlayerAttributeOption.OPT_5,
        }

        front_value = get_lowest_byte_value(value, 20)
        front_value = get_base_byte_value(front_value, 4)
        front_value = front_by_value[front_value]

        shape_by_value = {
            0: PlayerAttributeOption.OPT_1,
            20: PlayerAttributeOption.OPT_2,
            40: PlayerAttributeOption.OPT_3,
            60: PlayerAttributeOption.OPT_4,
        }

        shape_value = get_base_byte_value(value - 4, 20)
        shape_value = shape_by_value[shape_value]

        hair_type = PlayerAttributeOption.OPT_BUZZ_CUT
        hair_shape = str(shape_value)
        hair_front = str(front_value)
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = str(darkness_value)
        bandana_type = PlayerAttributeOption.OPT_NA

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_very_short_1(self, value):
        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
            2: PlayerAttributeOption.OPT_3,
            3: PlayerAttributeOption.OPT_4,
            4: PlayerAttributeOption.OPT_5,
            5: PlayerAttributeOption.OPT_6,
        }

        front_value = get_lowest_byte_value(value, 6)
        front_value = front_by_value[front_value]

        shape_by_value = {
            84: PlayerAttributeOption.OPT_1,
            90: PlayerAttributeOption.OPT_2,
            96: PlayerAttributeOption.OPT_3,
            102: PlayerAttributeOption.OPT_4,
        }

        shape_value = get_base_byte_value(value, 6)
        shape_value = shape_by_value[shape_value]

        hair_type = PlayerAttributeOption.OPT_VERY_SHORT_1
        hair_shape = str(shape_value)
        hair_front = str(front_value)
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_very_short_2(self, value):
        front_value = ""

        # Options start at byte val 108, need to get to nearest 10
        # as there are 5 or 10 hair front options depending on the shape
        shape_offset = 2

        if value <= 137:
            # Shapes 1-3 have 10 hair front options
            front_by_value_1 = {
                8: PlayerAttributeOption.OPT_1,
                9: PlayerAttributeOption.OPT_2,
                0: PlayerAttributeOption.OPT_3,
                1: PlayerAttributeOption.OPT_4,
                2: PlayerAttributeOption.OPT_5,
                3: PlayerAttributeOption.OPT_6,
                4: PlayerAttributeOption.OPT_7,
                5: PlayerAttributeOption.OPT_8,
                6: PlayerAttributeOption.OPT_9,
                7: PlayerAttributeOption.OPT_10,
            }

            front_value = get_lowest_byte_value(value, 10)
            front_value = front_by_value_1[front_value]

            shape_by_value_1 = {
                110: PlayerAttributeOption.OPT_1,
                120: PlayerAttributeOption.OPT_2,
                130: PlayerAttributeOption.OPT_3,
            }

            shape_value = get_base_byte_value(value + shape_offset, 10)
            shape_value = shape_by_value_1[shape_value]
        else:
            # Shapes 4-6 have 5 hair front options
            front_by_value_2 = {
                3: PlayerAttributeOption.OPT_1,
                4: PlayerAttributeOption.OPT_2,
                0: PlayerAttributeOption.OPT_3,
                1: PlayerAttributeOption.OPT_4,
                2: PlayerAttributeOption.OPT_5,
            }

            front_value = get_lowest_byte_value(value, 5)
            front_value = front_by_value_2[front_value]

            shape_by_value_2 = {
                140: PlayerAttributeOption.OPT_4,
                145: PlayerAttributeOption.OPT_5,
                150: PlayerAttributeOption.OPT_6,
            }

            shape_value = get_base_byte_value(value + shape_offset, 5)
            shape_value = shape_by_value_2[shape_value]

        hair_type = PlayerAttributeOption.OPT_VERY_SHORT_2
        hair_shape = str(shape_value)
        hair_front = str(front_value)
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_straight_1(self, value):
        hair_type = PlayerAttributeOption.OPT_STRAIGHT_1
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        # Each shape has 102 vals, need to get offset to nearest 102 (153->102)
        shape_1_base = 153
        shape_val_count = 102
        shape_offset = 51

        shape_base_offset_by_value = {
            102: (PlayerAttributeOption.OPT_1, 0),
            204: (PlayerAttributeOption.OPT_2, 1),
            306: (PlayerAttributeOption.OPT_3, 2),
            408: (PlayerAttributeOption.OPT_4, 3),
        }

        shape_base_offset = get_base_byte_value(
            value - shape_offset, shape_val_count
        )
        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)
        front_1_to_9_count = 81

        if value < shape_base + front_1_to_9_count:
            # Front 1-9

            # Front 1-9 can have bandana set
            bandana_type_by_value = {
                0: PlayerAttributeOption.OPT_N,
                1: PlayerAttributeOption.OPT_1,
                2: PlayerAttributeOption.OPT_2,
            }

            bandana_value = get_lowest_byte_value(value, 3)
            bandana_type = bandana_type_by_value[bandana_value]

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                3: PlayerAttributeOption.OPT_2,
                6: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_base_byte_value(value - shape_base, 3)
            volume_value = get_lowest_byte_value(volume_value, 9)
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_1,
                9: PlayerAttributeOption.OPT_2,
                18: PlayerAttributeOption.OPT_3,
                27: PlayerAttributeOption.OPT_4,
                36: PlayerAttributeOption.OPT_5,
                45: PlayerAttributeOption.OPT_6,
                54: PlayerAttributeOption.OPT_7,
                63: PlayerAttributeOption.OPT_8,
                72: PlayerAttributeOption.OPT_9,
            }

            front_value = get_base_byte_value(value - shape_base, 9)
            hair_front = front_by_value[front_value]

        else:
            # Front 10-16

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_lowest_byte_value(
                value - (shape_base + front_1_to_9_count), 3
            )
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_10,
                3: PlayerAttributeOption.OPT_11,
                6: PlayerAttributeOption.OPT_12,
                9: PlayerAttributeOption.OPT_13,
                12: PlayerAttributeOption.OPT_14,
                15: PlayerAttributeOption.OPT_15,
                18: PlayerAttributeOption.OPT_16,
            }

            front_value = get_base_byte_value(
                value - (shape_base + front_1_to_9_count), 3
            )
            hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_straight_2(self, value):
        hair_type = PlayerAttributeOption.OPT_STRAIGHT_2
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 561
        shape_val_count = 33

        shape_base_offset_by_value = {
            561: (PlayerAttributeOption.OPT_1, 0),
            594: (PlayerAttributeOption.OPT_2, 1),
            627: (PlayerAttributeOption.OPT_3, 2),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)
        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)
        front_1_to_2_count = 18

        if value < shape_base + front_1_to_2_count:
            # Front 1-2

            # Front 1-2 can have bandana set
            bandana_type_by_value = {
                0: PlayerAttributeOption.OPT_N,
                1: PlayerAttributeOption.OPT_1,
                2: PlayerAttributeOption.OPT_2,
            }

            bandana_value = get_lowest_byte_value(value, 3)
            bandana_type = bandana_type_by_value[bandana_value]

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                3: PlayerAttributeOption.OPT_2,
                6: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_base_byte_value(value - shape_base, 3)
            volume_value = get_lowest_byte_value(volume_value, 9)
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_1,
                9: PlayerAttributeOption.OPT_2,
            }

            front_value = get_base_byte_value(value - shape_base, 9)
            hair_front = front_by_value[front_value]

        else:
            # Front 3-7

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_lowest_byte_value(
                value - (shape_base + front_1_to_2_count), 3
            )
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_3,
                3: PlayerAttributeOption.OPT_4,
                6: PlayerAttributeOption.OPT_5,
                9: PlayerAttributeOption.OPT_6,
                12: PlayerAttributeOption.OPT_7,
            }

            front_value = get_base_byte_value(
                value - (shape_base + front_1_to_2_count), 3
            )
            hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_curly_1(self, value):
        hair_type = PlayerAttributeOption.OPT_CURLY_1
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        # Each shape has 51 vals, need to get offset to nearest 51 (660->612)
        shape_1_base = 660
        shape_val_count = 51
        shape_offset = 48

        shape_base_offset_by_value = {
            612: (PlayerAttributeOption.OPT_1, 0),
            663: (PlayerAttributeOption.OPT_2, 1),
            714: (PlayerAttributeOption.OPT_3, 2),
            765: (PlayerAttributeOption.OPT_4, 3),
        }

        shape_base_offset = get_base_byte_value(
            value - shape_offset, shape_val_count
        )

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)
        front_1_to_5_count = 45

        if value < shape_base + front_1_to_5_count:
            # Front 1-5

            # Front 1-5 can have bandana set
            bandana_type_by_value = {
                0: PlayerAttributeOption.OPT_N,
                1: PlayerAttributeOption.OPT_1,
                2: PlayerAttributeOption.OPT_2,
            }

            bandana_value = get_lowest_byte_value(value, 3)
            bandana_type = bandana_type_by_value[bandana_value]

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                3: PlayerAttributeOption.OPT_2,
                6: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_base_byte_value(value - shape_base, 3)
            volume_value = get_lowest_byte_value(volume_value, 9)
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_1,
                9: PlayerAttributeOption.OPT_2,
                18: PlayerAttributeOption.OPT_3,
                27: PlayerAttributeOption.OPT_4,
                36: PlayerAttributeOption.OPT_5,
            }

            front_value = get_base_byte_value(value - shape_base, 9)
            hair_front = front_by_value[front_value]

        else:
            # Front 6-7

            volume_by_value = {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
            }

            volume_value = get_lowest_byte_value(
                value - (shape_base + front_1_to_5_count), 3
            )
            hair_volume = volume_by_value[volume_value]

            front_by_value = {
                0: PlayerAttributeOption.OPT_6,
                3: PlayerAttributeOption.OPT_7,
            }

            front_value = get_base_byte_value(
                value - (shape_base + front_1_to_5_count), 3
            )
            hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_curly_2(self, value):
        hair_type = PlayerAttributeOption.OPT_CURLY_2
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 864
        shape_val_count = 12

        shape_base_offset_by_value = {
            864: (PlayerAttributeOption.OPT_1, 0),
            876: (PlayerAttributeOption.OPT_2, 1),
            888: (PlayerAttributeOption.OPT_3, 2),
            900: (PlayerAttributeOption.OPT_4, 3),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)

        volume_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
        }

        volume_value = get_lowest_byte_value(value - (shape_base), 2)
        hair_volume = volume_by_value[volume_value]

        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            2: PlayerAttributeOption.OPT_2,
            4: PlayerAttributeOption.OPT_3,
            6: PlayerAttributeOption.OPT_4,
            8: PlayerAttributeOption.OPT_5,
            10: PlayerAttributeOption.OPT_6,
        }

        front_value = get_base_byte_value(value - (shape_base), 2)
        hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_ponytail_1(self, value):
        hair_type = PlayerAttributeOption.OPT_PONYTAIL_1
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 912
        shape_val_count = 12

        shape_base_offset_by_value = {
            912: (PlayerAttributeOption.OPT_1, 0),
            924: (PlayerAttributeOption.OPT_2, 1),
            936: (PlayerAttributeOption.OPT_3, 2),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)

        volume_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
            2: PlayerAttributeOption.OPT_3,
        }

        volume_value = get_lowest_byte_value(value - (shape_base), 3)
        hair_volume = volume_by_value[volume_value]

        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            3: PlayerAttributeOption.OPT_2,
            6: PlayerAttributeOption.OPT_3,
            9: PlayerAttributeOption.OPT_4,
        }

        front_value = get_base_byte_value(value - (shape_base), 3)
        hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_ponytail_2(self, value):
        hair_type = PlayerAttributeOption.OPT_PONYTAIL_2
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 948
        shape_val_count = 12

        shape_base_offset_by_value = {
            948: (PlayerAttributeOption.OPT_1, 0),
            960: (PlayerAttributeOption.OPT_2, 1),
            972: (PlayerAttributeOption.OPT_3, 2),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)

        volume_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
            2: PlayerAttributeOption.OPT_3,
        }

        volume_value = get_lowest_byte_value(value - (shape_base), 3)
        hair_volume = volume_by_value[volume_value]

        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            3: PlayerAttributeOption.OPT_2,
            6: PlayerAttributeOption.OPT_3,
            9: PlayerAttributeOption.OPT_4,
        }

        front_value = get_base_byte_value(value - (shape_base), 3)
        hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_dreadlocks(self, value):
        hair_type = PlayerAttributeOption.OPT_DREADLOCKS
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 984
        shape_val_count = 8

        shape_base_offset_by_value = {
            984: (PlayerAttributeOption.OPT_1, 0),
            992: (PlayerAttributeOption.OPT_2, 1),
            1000: (PlayerAttributeOption.OPT_3, 2),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)

        volume_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
        }

        volume_value = get_lowest_byte_value(value - (shape_base), 2)
        hair_volume = volume_by_value[volume_value]

        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            2: PlayerAttributeOption.OPT_2,
            4: PlayerAttributeOption.OPT_3,
            6: PlayerAttributeOption.OPT_4,
        }

        front_value = get_base_byte_value(value - (shape_base), 2)
        hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_pulled_back(self, value):
        hair_type = PlayerAttributeOption.OPT_PULLED_BACK
        hair_shape = PlayerAttributeOption.OPT_NA
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        shape_1_base = 1008
        shape_val_count = 6

        shape_base_offset_by_value = {
            1008: (PlayerAttributeOption.OPT_1, 0),
            1014: (PlayerAttributeOption.OPT_2, 1),
            1020: (PlayerAttributeOption.OPT_3, 2),
        }

        shape_base_offset = get_base_byte_value(value, shape_val_count)

        hair_shape, shape_base_multiplier = shape_base_offset_by_value[
            shape_base_offset
        ]

        shape_base = shape_1_base + (shape_val_count * shape_base_multiplier)

        front_by_value = {
            0: PlayerAttributeOption.OPT_1,
            1: PlayerAttributeOption.OPT_2,
            2: PlayerAttributeOption.OPT_3,
            3: PlayerAttributeOption.OPT_4,
            4: PlayerAttributeOption.OPT_5,
            5: PlayerAttributeOption.OPT_6,
        }

        front_value = get_base_byte_value(value - (shape_base), 1)
        hair_front = front_by_value[front_value]

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key_special(self, value):
        shape_1_base = 1026
        shape_start_value = 1
        shape_value = shape_start_value + (value - shape_1_base)

        hair_type = PlayerAttributeOption.OPT_SPECIAL
        hair_shape = str(shape_value)
        hair_front = PlayerAttributeOption.OPT_NA
        hair_volume = PlayerAttributeOption.OPT_NA
        hair_darkness = PlayerAttributeOption.OPT_NA
        bandana_type = PlayerAttributeOption.OPT_NA

        return (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        )

    def get_hair_key(self):
        value1, value2 = self.get_raw_value()
        value2 = get_lowest_byte_value(value2, 128)
        value2 = get_lowest_byte_value(value2, 8)

        # Value with offset applied
        value = value1 + (value2 * 256)

        key = False

        if value >= 0 and value <= 3:
            key = self.get_hair_key_bald(value)

        elif value >= 4 and value <= 83:
            key = self.get_hair_key_buzz_cut(value)

        elif value >= 84 and value <= 107:
            key = self.get_hair_key_very_short_1(value)

        elif value >= 108 and value <= 152:
            key = self.get_hair_key_very_short_2(value)

        elif value >= 153 and value <= 560:
            key = self.get_hair_key_straight_1(value)

        elif value >= 561 and value <= 659:
            key = self.get_hair_key_straight_2(value)

        elif value >= 660 and value <= 863:
            key = self.get_hair_key_curly_1(value)

        elif value >= 864 and value <= 911:
            key = self.get_hair_key_curly_2(value)

        elif value >= 912 and value <= 947:
            key = self.get_hair_key_ponytail_1(value)

        elif value >= 948 and value <= 983:
            key = self.get_hair_key_ponytail_2(value)

        elif value >= 984 and value <= 1007:
            key = self.get_hair_key_dreadlocks(value)

        elif value >= 1008 and value <= 1025:
            key = self.get_hair_key_pulled_back(value)

        else:
            key = self.get_hair_key_special(value)

        return key

    def get_eye_color_two_label(self):
        value = self.get_value()[1]
        value = get_lowest_byte_value(value, 128)
        value = get_base_byte_value(value, 8)
        return self.array_opts_eye_color_two[value]

    def get_neck_warmer_label(self):
        value = self.get_value()[1]
        value = get_base_byte_value(value, 128)
        return self.array_opts_neck_warmer[value]

    def get_label(self):
        hair_key = self.get_hair_key()

        hair_type_label = hair_key[0]
        hair_shape_label = hair_key[1]
        hair_front_label = hair_key[2]
        hair_volume_label = hair_key[3]
        hair_darkness_label = hair_key[4]
        hair_bandana_type_label = hair_key[5]

        eye_color_two_label = self.get_eye_color_two_label()
        neckwarmer_label = self.get_neck_warmer_label()

        return (
            hair_type_label,
            hair_shape_label,
            hair_front_label,
            hair_volume_label,
            hair_darkness_label,
            hair_bandana_type_label,
            eye_color_two_label,
            neckwarmer_label,
        )

    def set_value(self, value):
        val_92, val_93 = value
        of_data = self.player.option_file.data

        of_data[self.player.address + self.array_pos[0]] = val_92
        of_data[self.player.address + self.array_pos[1]] = val_93
        return True

    def get_hair_value_bald(self, hair_shape):
        value = 0

        hair_shape_int = int(hair_shape)
        if hair_shape_int >= 1 and hair_shape_int <= 4:
            value = hair_shape_int - 1

        return value

    def get_hair_value_buzz_cut(self, hair_shape, hair_front, hair_darkness):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 4,
            PlayerAttributeOption.OPT_2: 24,
            PlayerAttributeOption.OPT_3: 44,
            PlayerAttributeOption.OPT_4: 64,
        }
        value = shape_values_by_label.get(hair_shape, 4)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 4,
            PlayerAttributeOption.OPT_3: 8,
            PlayerAttributeOption.OPT_4: 12,
            PlayerAttributeOption.OPT_5: 16,
        }
        value += front_values_by_label.get(hair_front, 0)

        darkness_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
            PlayerAttributeOption.OPT_4: 3,
        }
        value += darkness_values_by_label.get(hair_darkness, 0)

        return value

    def get_hair_value_very_short_1(self, hair_shape, hair_front):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 84,
            PlayerAttributeOption.OPT_2: 90,
            PlayerAttributeOption.OPT_3: 96,
            PlayerAttributeOption.OPT_4: 102,
        }
        value = shape_values_by_label.get(hair_shape, 84)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
            PlayerAttributeOption.OPT_4: 3,
            PlayerAttributeOption.OPT_5: 4,
            PlayerAttributeOption.OPT_6: 5,
        }
        value += front_values_by_label.get(hair_front, 0)

        return value

    def get_hair_value_very_short_2(self, hair_shape, hair_front):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 108,
            PlayerAttributeOption.OPT_2: 118,
            PlayerAttributeOption.OPT_3: 128,
            PlayerAttributeOption.OPT_4: 138,
            PlayerAttributeOption.OPT_5: 143,
            PlayerAttributeOption.OPT_6: 148,
        }
        value = shape_values_by_label.get(hair_shape, 108)

        hair_shape_int = int(hair_shape)
        hair_front_int = int(hair_front)

        # Hair shapes 1-3 have 10 front options, 4-6 only have 5
        if hair_shape_int <= 3 or hair_front_int <= 5:
            front_values_by_label = {
                PlayerAttributeOption.OPT_1: 0,
                PlayerAttributeOption.OPT_2: 1,
                PlayerAttributeOption.OPT_3: 2,
                PlayerAttributeOption.OPT_4: 3,
                PlayerAttributeOption.OPT_5: 4,
                PlayerAttributeOption.OPT_6: 5,
                PlayerAttributeOption.OPT_7: 6,
                PlayerAttributeOption.OPT_8: 7,
                PlayerAttributeOption.OPT_9: 8,
                PlayerAttributeOption.OPT_10: 9,
            }
            value += front_values_by_label.get(hair_front, 0)

        return value

    def get_hair_value_straight_1(
        self, hair_shape, hair_front, hair_volume, bandana_type
    ):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 153,
            PlayerAttributeOption.OPT_2: 255,
            PlayerAttributeOption.OPT_3: 357,
            PlayerAttributeOption.OPT_4: 459,
        }
        value = shape_values_by_label.get(hair_shape, 153)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 9,
            PlayerAttributeOption.OPT_3: 18,
            PlayerAttributeOption.OPT_4: 27,
            PlayerAttributeOption.OPT_5: 36,
            PlayerAttributeOption.OPT_6: 45,
            PlayerAttributeOption.OPT_7: 54,
            PlayerAttributeOption.OPT_8: 63,
            PlayerAttributeOption.OPT_9: 72,
            PlayerAttributeOption.OPT_10: 81,
            PlayerAttributeOption.OPT_11: 84,
            PlayerAttributeOption.OPT_12: 87,
            PlayerAttributeOption.OPT_13: 90,
            PlayerAttributeOption.OPT_14: 93,
            PlayerAttributeOption.OPT_15: 96,
            PlayerAttributeOption.OPT_16: 99,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_front_int = int(hair_front)

        # Hair fronts 1-9 can have bandana type set
        if hair_front_int <= 9:
            bandana_type_values_by_label = {
                PlayerAttributeOption.OPT_N: 0,
                PlayerAttributeOption.OPT_1: 1,
                PlayerAttributeOption.OPT_2: 2,
            }
            value += bandana_type_values_by_label.get(bandana_type, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
        }
        # Hair fronts 1-9 use more bytes as they can have bandana type set
        hair_volume_multiplier = 3 if hair_front_int <= 9 else 1
        value += (
            hair_volume_values_by_label.get(hair_volume, 0)
            * hair_volume_multiplier
        )

        return value

    def get_hair_value_straight_2(
        self, hair_shape, hair_front, hair_volume, bandana_type
    ):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 561,
            PlayerAttributeOption.OPT_2: 594,
            PlayerAttributeOption.OPT_3: 627,
        }
        value = shape_values_by_label.get(hair_shape, 561)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 9,
            PlayerAttributeOption.OPT_3: 18,
            PlayerAttributeOption.OPT_4: 21,
            PlayerAttributeOption.OPT_5: 24,
            PlayerAttributeOption.OPT_6: 27,
            PlayerAttributeOption.OPT_7: 30,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_front_int = int(hair_front)

        # Hair fronts 1-2 can have bandana type set
        if hair_front_int <= 2:
            bandana_type_values_by_label = {
                PlayerAttributeOption.OPT_N: 0,
                PlayerAttributeOption.OPT_1: 1,
                PlayerAttributeOption.OPT_2: 2,
            }
            value += bandana_type_values_by_label.get(bandana_type, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
        }
        # Hair fronts 1-2 use more bytes as they can have bandana type set
        hair_volume_multiplier = 3 if hair_front_int <= 2 else 1
        value += (
            hair_volume_values_by_label.get(hair_volume, 0)
            * hair_volume_multiplier
        )

        return value

    def get_hair_value_curly_1(
        self, hair_shape, hair_front, hair_volume, bandana_type
    ):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 660,
            PlayerAttributeOption.OPT_2: 711,
            PlayerAttributeOption.OPT_3: 762,
            PlayerAttributeOption.OPT_4: 813,
        }
        value = shape_values_by_label.get(hair_shape, 660)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 9,
            PlayerAttributeOption.OPT_3: 18,
            PlayerAttributeOption.OPT_4: 27,
            PlayerAttributeOption.OPT_5: 36,
            PlayerAttributeOption.OPT_6: 45,
            PlayerAttributeOption.OPT_7: 48,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_front_int = int(hair_front)

        # Hair fronts 1-5 can have bandana type set
        if hair_front_int <= 5:
            bandana_type_values_by_label = {
                PlayerAttributeOption.OPT_N: 0,
                PlayerAttributeOption.OPT_1: 1,
                PlayerAttributeOption.OPT_2: 2,
            }
            value += bandana_type_values_by_label.get(bandana_type, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
        }
        # Hair fronts 1-2 use more bytes as they can have bandana type set
        hair_volume_multiplier = 3 if hair_front_int <= 5 else 1
        value += (
            hair_volume_values_by_label.get(hair_volume, 0)
            * hair_volume_multiplier
        )

        return value

    def get_hair_value_curly_2(self, hair_shape, hair_front, hair_volume):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 864,
            PlayerAttributeOption.OPT_2: 876,
            PlayerAttributeOption.OPT_3: 888,
            PlayerAttributeOption.OPT_4: 900,
        }
        value = shape_values_by_label.get(hair_shape, 864)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 2,
            PlayerAttributeOption.OPT_3: 4,
            PlayerAttributeOption.OPT_4: 6,
            PlayerAttributeOption.OPT_5: 8,
            PlayerAttributeOption.OPT_6: 10,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
        }
        value += hair_volume_values_by_label.get(hair_volume, 0)

        return value

    def get_hair_value_ponytail_1(self, hair_shape, hair_front, hair_volume):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 912,
            PlayerAttributeOption.OPT_2: 924,
            PlayerAttributeOption.OPT_3: 936,
        }
        value = shape_values_by_label.get(hair_shape, 912)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 3,
            PlayerAttributeOption.OPT_3: 6,
            PlayerAttributeOption.OPT_4: 9,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
        }
        value += hair_volume_values_by_label.get(hair_volume, 0)

        return value

    def get_hair_value_ponytail_2(self, hair_shape, hair_front, hair_volume):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 948,
            PlayerAttributeOption.OPT_2: 960,
            PlayerAttributeOption.OPT_3: 972,
        }
        value = shape_values_by_label.get(hair_shape, 948)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 3,
            PlayerAttributeOption.OPT_3: 6,
            PlayerAttributeOption.OPT_4: 9,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
        }
        value += hair_volume_values_by_label.get(hair_volume, 0)

        return value

    def get_hair_value_dreadlocks(self, hair_shape, hair_front, hair_volume):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 984,
            PlayerAttributeOption.OPT_2: 992,
            PlayerAttributeOption.OPT_3: 1000,
        }
        value = shape_values_by_label.get(hair_shape, 984)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 2,
            PlayerAttributeOption.OPT_3: 4,
            PlayerAttributeOption.OPT_4: 6,
        }
        value += front_values_by_label.get(hair_front, 0)

        hair_volume_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
        }
        value += hair_volume_values_by_label.get(hair_volume, 0)

        return value

    def get_hair_value_pulled_back(self, hair_shape, hair_front):
        shape_values_by_label = {
            PlayerAttributeOption.OPT_1: 1008,
            PlayerAttributeOption.OPT_2: 1014,
            PlayerAttributeOption.OPT_3: 1020,
        }
        value = shape_values_by_label.get(hair_shape, 1008)

        front_values_by_label = {
            PlayerAttributeOption.OPT_1: 0,
            PlayerAttributeOption.OPT_2: 1,
            PlayerAttributeOption.OPT_3: 2,
            PlayerAttributeOption.OPT_4: 3,
            PlayerAttributeOption.OPT_5: 4,
            PlayerAttributeOption.OPT_6: 5,
        }
        value += front_values_by_label.get(hair_front, 0)

        return value

    def get_hair_value_special(self, hair_shape):
        value = 1026

        hair_shape_int = int(hair_shape)

        # 473 is the highest valid
        if hair_shape_int > 0 and hair_shape_int <= 473:
            value += hair_shape_int - 1

        return value

    def get_hair_value(self, key):
        (
            hair_type,
            hair_shape,
            hair_front,
            hair_volume,
            hair_darkness,
            bandana_type,
        ) = key

        value = 0

        if hair_type == PlayerAttributeOption.OPT_BALD:
            value = self.get_hair_value_bald(hair_shape)

        elif hair_type == PlayerAttributeOption.OPT_BUZZ_CUT:
            value = self.get_hair_value_buzz_cut(
                hair_shape, hair_front, hair_darkness
            )

        elif hair_type == PlayerAttributeOption.OPT_VERY_SHORT_1:
            value = self.get_hair_value_very_short_1(hair_shape, hair_front)

        elif hair_type == PlayerAttributeOption.OPT_VERY_SHORT_2:
            value = self.get_hair_value_very_short_2(hair_shape, hair_front)

        elif hair_type == PlayerAttributeOption.OPT_STRAIGHT_1:
            value = self.get_hair_value_straight_1(
                hair_shape, hair_front, hair_volume, bandana_type
            )

        elif hair_type == PlayerAttributeOption.OPT_STRAIGHT_2:
            value = self.get_hair_value_straight_2(
                hair_shape, hair_front, hair_volume, bandana_type
            )

        elif hair_type == PlayerAttributeOption.OPT_CURLY_1:
            value = self.get_hair_value_curly_1(
                hair_shape, hair_front, hair_volume, bandana_type
            )

        elif hair_type == PlayerAttributeOption.OPT_CURLY_2:
            value = self.get_hair_value_curly_2(
                hair_shape, hair_front, hair_volume
            )

        elif hair_type == PlayerAttributeOption.OPT_PONYTAIL_1:
            value = self.get_hair_value_ponytail_1(
                hair_shape, hair_front, hair_volume
            )

        elif hair_type == PlayerAttributeOption.OPT_PONYTAIL_2:
            value = self.get_hair_value_ponytail_2(
                hair_shape, hair_front, hair_volume
            )

        elif hair_type == PlayerAttributeOption.OPT_DREADLOCKS:
            value = self.get_hair_value_dreadlocks(
                hair_shape, hair_front, hair_volume
            )

        elif hair_type == PlayerAttributeOption.OPT_PULLED_BACK:
            value = self.get_hair_value_pulled_back(hair_shape, hair_front)

        elif hair_type == PlayerAttributeOption.OPT_SPECIAL:
            value = self.get_hair_value_special(hair_shape)

        # Split values into chunks of 256
        val_92 = value % 256
        val_93 = int(value / 256)

        return (val_92, val_93)

    def get_value_from_label(self, label):
        hair_key = (label[0], label[1], label[2], label[3], label[4], label[5])
        val_92, val_93 = self.get_hair_value(hair_key)

        eye_color_two_value = self.array_opts_eye_color_two.inverse[label[6]]
        neck_warmer_value = self.array_opts_neck_warmer.inverse[label[7]]

        val_93 += eye_color_two_value
        val_93 += neck_warmer_value

        return (val_92, val_93)

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Hair Type/Shape/Front/Volume/Darkness/Bandana Type/Eye Color 2/
        Neck Warmer attributes and link to this attribute
        """
        self.hair_type = PlayerAttributeHairType(self.player, parent=self)
        self.hair_shape = PlayerAttributeHairShape(self.player, parent=self)
        self.hair_front = PlayerAttributeHairFront(self.player, parent=self)
        self.hair_volume = PlayerAttributeHairVolume(self.player, parent=self)
        self.hair_darkness = PlayerAttributeHairDarkness(
            self.player, parent=self
        )
        self.bandana_type = PlayerAttributeBandanaType(self.player, parent=self)
        self.eye_color_two = PlayerAttributeEyeColorTwo(
            self.player, parent=self
        )
        self.neck_warmer = PlayerAttributeNeckWarmer(self.player, parent=self)
