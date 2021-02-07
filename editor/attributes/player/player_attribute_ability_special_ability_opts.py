from bidict import bidict

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.utils.common_functions import get_base_byte_value


class PlayerAttributeAbilitySpcAbilityOpts:
    FIRST_OPT_BY_VALUE = bidict(
        {
            0: PlayerAttributeOption.OPT_N,
            128: PlayerAttributeOption.OPT_Y,
        }
    )

    min_second_opt_value = 1
    max_second_opt_value = 127
    second_opt_byte_split = 128

    @classmethod
    def get_first_opt_label(cls, value):
        value = get_base_byte_value(value, 128)
        return PlayerAttributeAbilitySpcAbilityOpts.FIRST_OPT_BY_VALUE[value]

    @classmethod
    def get_second_opt_label(cls, value):
        min_value = PlayerAttributeAbilitySpcAbilityOpts.min_second_opt_value
        max_value = PlayerAttributeAbilitySpcAbilityOpts.max_second_opt_value
        byte_split = PlayerAttributeAbilitySpcAbilityOpts.second_opt_byte_split

        if value >= byte_split:
            value -= byte_split

        if value < min_value:
            value = min_value
        elif value > max_value:
            value = max_value

        return str(value)

    @classmethod
    def get_full_label(cls, value):
        first_label = cls.get_first_opt_label(value)
        second_label = cls.get_second_opt_label(value)
        return (first_label, second_label)

    @classmethod
    def get_value_from_label(cls, label):
        first_opt_value = (
            PlayerAttributeAbilitySpcAbilityOpts.FIRST_OPT_BY_VALUE.inverse[
                label[0]
            ]
        )
        second_opt_value = int(label[1])

        min_value = PlayerAttributeAbilitySpcAbilityOpts.min_second_opt_value
        max_value = PlayerAttributeAbilitySpcAbilityOpts.max_second_opt_value

        if second_opt_value < min_value:
            second_opt_value = min_value
        elif second_opt_value > max_value:
            second_opt_value = max_value

        return first_opt_value + second_opt_value
