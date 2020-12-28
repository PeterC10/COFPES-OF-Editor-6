from bidict import bidict

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.utils.common_functions import (
    get_base_byte_value,
    get_lowest_byte_value,
)


class PlayerAttributePhysicalLinkedOpts():
    FIRST_OPT_BY_VALUE = bidict(
        {
            0: PlayerAttributeOption.OPT_M7,
            1: PlayerAttributeOption.OPT_M6,
            2: PlayerAttributeOption.OPT_M5,
            3: PlayerAttributeOption.OPT_M4,
            4: PlayerAttributeOption.OPT_M3,
            5: PlayerAttributeOption.OPT_M2,
            6: PlayerAttributeOption.OPT_M1,
            7: PlayerAttributeOption.OPT_0,
            8: PlayerAttributeOption.OPT_1,
            9: PlayerAttributeOption.OPT_2,
            10: PlayerAttributeOption.OPT_3,
            11: PlayerAttributeOption.OPT_4,
            12: PlayerAttributeOption.OPT_5,
            13: PlayerAttributeOption.OPT_6,
            14: PlayerAttributeOption.OPT_7,
        }
    )

    SECOND_OPT_BY_VALUE = bidict(
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
