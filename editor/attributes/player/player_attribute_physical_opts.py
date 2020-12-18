from bidict import bidict

from editor.utils.common_functions import (
    get_base_byte_value,
    get_lowest_byte_value,
)


class PlayerAttributePhysicalOpts:
    OPT_M7 = "-7"
    OPT_M6 = "-6"
    OPT_M5 = "-5"
    OPT_M4 = "-4"
    OPT_M3 = "-3"
    OPT_M2 = "-2"
    OPT_M1 = "-1"
    OPT_0 = "0"
    OPT_1 = "1"
    OPT_2 = "2"
    OPT_3 = "3"
    OPT_4 = "4"
    OPT_5 = "5"
    OPT_6 = "6"
    OPT_7 = "7"


class PlayerAttributePhysicalLinkedOpts(PlayerAttributePhysicalOpts):
    FIRST_OPT_BY_VALUE = bidict(
        {
            0: PlayerAttributePhysicalOpts.OPT_M7,
            1: PlayerAttributePhysicalOpts.OPT_M6,
            2: PlayerAttributePhysicalOpts.OPT_M5,
            3: PlayerAttributePhysicalOpts.OPT_M4,
            4: PlayerAttributePhysicalOpts.OPT_M3,
            5: PlayerAttributePhysicalOpts.OPT_M2,
            6: PlayerAttributePhysicalOpts.OPT_M1,
            7: PlayerAttributePhysicalOpts.OPT_0,
            8: PlayerAttributePhysicalOpts.OPT_1,
            9: PlayerAttributePhysicalOpts.OPT_2,
            10: PlayerAttributePhysicalOpts.OPT_3,
            11: PlayerAttributePhysicalOpts.OPT_4,
            12: PlayerAttributePhysicalOpts.OPT_5,
            13: PlayerAttributePhysicalOpts.OPT_6,
            14: PlayerAttributePhysicalOpts.OPT_7,
        }
    )

    SECOND_OPT_BY_VALUE = bidict(
        {
            0: PlayerAttributePhysicalOpts.OPT_M7,
            16: PlayerAttributePhysicalOpts.OPT_M6,
            32: PlayerAttributePhysicalOpts.OPT_M5,
            48: PlayerAttributePhysicalOpts.OPT_M4,
            64: PlayerAttributePhysicalOpts.OPT_M3,
            80: PlayerAttributePhysicalOpts.OPT_M2,
            96: PlayerAttributePhysicalOpts.OPT_M1,
            112: PlayerAttributePhysicalOpts.OPT_0,
            128: PlayerAttributePhysicalOpts.OPT_1,
            144: PlayerAttributePhysicalOpts.OPT_2,
            160: PlayerAttributePhysicalOpts.OPT_3,
            176: PlayerAttributePhysicalOpts.OPT_4,
            192: PlayerAttributePhysicalOpts.OPT_5,
            208: PlayerAttributePhysicalOpts.OPT_6,
            224: PlayerAttributePhysicalOpts.OPT_7,
        }
    )

    @classmethod
    def get_first_opt_label(cls, value):
        value = get_lowest_byte_value(value, 16)
        return PlayerAttributePhysicalLinkedOpts.FIRST_OPT_BY_VALUE[value]

    @classmethod
    def get_second_opt_label(cls, value):
        value = get_base_byte_value(value, 16)
        return PlayerAttributePhysicalLinkedOpts.SECOND_OPT_BY_VALUE[value]

    @classmethod
    def get_full_label(cls, value):
        first_label = cls.get_first_opt_label(value)
        second_label = cls.get_second_opt_label(value)
        return (first_label, second_label)

    @classmethod
    def get_value_from_label(self, label):
        first_opt_value = (
            PlayerAttributePhysicalLinkedOpts.FIRST_OPT_BY_VALUE.inverse[
                label[0]
            ]
        )
        second_opt_value = (
            PlayerAttributePhysicalLinkedOpts.SECOND_OPT_BY_VALUE.inverse[
                label[1]
            ]
        )
        return first_opt_value + second_opt_value
