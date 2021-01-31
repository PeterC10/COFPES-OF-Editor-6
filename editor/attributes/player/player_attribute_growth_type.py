from bidict import bidict

from editor.utils.common_functions import get_random_value_from_list

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)


class PlayerAttributeGrowthType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Growth Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 86

    @classmethod
    def att_class_array_opts(cls):
        # Each growth type by their default value
        # (i.e what would get set via in-game editor)
        options_by_value = bidict(
            {
                9: PlayerAttributeOption.OPT_EARLY,
                51: PlayerAttributeOption.OPT_EARLY_LASTING,
                55: PlayerAttributeOption.OPT_STANDARD,
                11: PlayerAttributeOption.OPT_STANDARD_LASTING,
                8: PlayerAttributeOption.OPT_LATE,
                10: PlayerAttributeOption.OPT_LATE_LASTING,
            }
        )
        return options_by_value

    @classmethod
    def growth_types_early(cls):
        growth_type_vals = (
            128,
            130,
            141,
            146,
            149,
            154,
            164,
            166,
            168,
            170,
            174,
            175,
            176,
            178,
            188,
            190,
            210,
            212,
            244,
            248,
            9,
            49,
            105,
            118,
            123,
            124,
            126,
        )
        return growth_type_vals

    @classmethod
    def growth_types_early_lasting(cls):
        growth_type_vals = (
            136,
            142,
            148,
            161,
            172,
            173,
            189,
            193,
            202,
            204,
            242,
            247,
            25,
            51,
            67,
            70,
            82,
            88,
            89,
            107,
            121,
            127,
        )
        return growth_type_vals

    @classmethod
    def growth_types_standard(cls):
        growth_type_vals = (
            132,
            139,
            144,
            145,
            147,
            150,
            152,
            153,
            155,
            159,
            162,
            165,
            169,
            177,
            179,
            180,
            181,
            183,
            187,
            192,
            194,
            198,
            200,
            201,
            203,
            208,
            221,
            234,
            243,
            245,
            0,
            1,
            3,
            4,
            6,
            12,
            16,
            18,
            19,
            20,
            26,
            28,
            29,
            30,
            31,
            40,
            42,
            52,
            53,
            54,
            55,
            56,
            57,
            58,
            59,
            60,
            61,
            62,
            63,
            65,
            68,
            69,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            83,
            84,
            85,
            87,
            94,
            95,
            97,
            100,
            101,
            104,
            106,
            112,
            114,
            115,
            116,
            119,
            120,
            122,
            125,
        )
        return growth_type_vals

    @classmethod
    def growth_types_standard_lasting(cls):
        growth_type_vals = (
            129,
            131,
            135,
            138,
            143,
            151,
            160,
            182,
            186,
            191,
            195,
            196,
            211,
            216,
            223,
            237,
            5,
            7,
            11,
            13,
            14,
            15,
            23,
            32,
            34,
            36,
            38,
            47,
            48,
            81,
            91,
            92,
            96,
            99,
            108,
            110,
            113,
        )
        return growth_type_vals

    @classmethod
    def growth_types_late(cls):
        growth_type_vals = (
            133,
            137,
            140,
            156,
            157,
            163,
            171,
            184,
            185,
            199,
            206,
            207,
            209,
            215,
            217,
            218,
            225,
            232,
            233,
            252,
            2,
            8,
            17,
            21,
            22,
            33,
            35,
            37,
            39,
            43,
            44,
            46,
            64,
            66,
            71,
            86,
            93,
            98,
            102,
            103,
            109,
            111,
            117,
        )
        return growth_type_vals

    @classmethod
    def growth_types_late_lasting(cls):
        growth_type_vals = (
            134,
            167,
            197,
            205,
            228,
            10,
            24,
            41,
            90,
        )
        return growth_type_vals

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

    def get_label(self):
        label = ""
        value = self.get_value()

        for growth_type_info in (
            (PlayerAttributeOption.OPT_EARLY, self.growth_types_early()),
            (PlayerAttributeOption.OPT_EARLY_LASTING, self.growth_types_early_lasting()),
            (PlayerAttributeOption.OPT_STANDARD, self.growth_types_standard()),
            (PlayerAttributeOption.OPT_STANDARD_LASTING, self.growth_types_standard_lasting()),
            (PlayerAttributeOption.OPT_LATE, self.growth_types_late()),
            (PlayerAttributeOption.OPT_LATE_LASTING, self.growth_types_late_lasting()),
        ):
            growth_type_label, growth_type_vals = growth_type_info
            if value in growth_type_vals:
                label = growth_type_label
                break

        return label

    def set_value(self, value):
        value_updated = False

        # Don't update growth type for classic players or ML defaults
        if not self.player.is_ml and not self.player.is_edit:
            of_data = self.player.option_file.data
            of_data[self.player.address + self.array_pos] = value
            value_updated = True

        return value_updated

    def set_value_from_label(self, label):
        value_updated = False

        # Don't update growth type if existing growth type is the same
        # as specified label
        current_growth_type = self.get_label()
        if current_growth_type != label:
            value = self.array_opts.inverse[label]
            self.set_value(value)
            value_updated = True

        return value_updated

    def set_random_value_from_label(self, label):
        value = self.array_opts.inverse[PlayerAttributeOption.OPT_STANDARD]

        if label == PlayerAttributeOption.OPT_EARLY:
            value = get_random_value_from_list(self.growth_types_early())
        elif label == PlayerAttributeOption.OPT_EARLY_LASTING:
            value = get_random_value_from_list(
                self.growth_types_early_lasting()
            )
        elif label == PlayerAttributeOption.OPT_STANDARD:
            value = get_random_value_from_list(self.growth_types_standard())
        elif label == PlayerAttributeOption.OPT_STANDARD_LASTING:
            value = get_random_value_from_list(
                self.growth_types_standard_lasting()
            )
        elif label == PlayerAttributeOption.OPT_LATE:
            value = get_random_value_from_list(self.growth_types_late())
        elif label == PlayerAttributeOption.OPT_LATE_LASTING:
            value = get_random_value_from_list(self.growth_types_late_lasting())

        self.set_value(value)
        return True
