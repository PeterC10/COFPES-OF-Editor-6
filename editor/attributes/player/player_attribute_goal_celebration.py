from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)


class PlayerAttributeCelebration:
    @classmethod
    def _check_value(cls, value):
        no_celebration_value = 0
        min_value = 1
        max_value = 76
        byte_split = 128

        # Most players have values between 1-76, but some start at 128.
        # Might be a hidden stat or just co-incidence, but if value is
        # 128 or greater, take 128 away to get relevant celebration number.
        if value >= byte_split:
            value -= byte_split

        if value < min_value or value > max_value:
            value = no_celebration_value

        return value

    @classmethod
    def get_label(cls, value):
        label = PlayerAttributeOption.OPT_N
        value = cls._check_value(value)
        if value:
            label = str(value)
        return label

    @classmethod
    def get_value_from_label(cls, label):
        value = 0
        if label != PlayerAttributeOption.OPT_N:
            value = int(label)
            value = cls._check_value(value)
        return value
