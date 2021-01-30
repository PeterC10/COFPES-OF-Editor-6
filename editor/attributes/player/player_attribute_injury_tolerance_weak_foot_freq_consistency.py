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

from editor.attributes.player.player_attribute_injury_tolerance import (
    PlayerAttributeInjuryTolerance,
)

from editor.attributes.player.player_attribute_weak_foot_frequency import (
    PlayerAttributeWeakFootFrequency,
)

from editor.attributes.player.player_attribute_consistency import (
    PlayerAttributeConsistency,
)


class PlayerAttributeInjuryToleranceWeakFootFreqConsistency(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Injury Tolerance/Weak Foot Frequency/Consistency"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 80

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_injury_tolerance(cls):
        """
        Injury Tolerance Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_C,
                64: PlayerAttributeOption.OPT_B,
                128: PlayerAttributeOption.OPT_A,
            }
        )
        return options_by_value

    @property
    def array_opts_injury_tolerance(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_injury_tolerance()

    @classmethod
    def att_class_array_opts_weak_foot_frequency(cls):
        """
        Weak Foot Frequency Opts
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
    def array_opts_weak_foot_frequency(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_weak_foot_frequency()

    @classmethod
    def att_class_array_opts_consistency(cls):
        """
        Consistency Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
                3: PlayerAttributeOption.OPT_4,
                4: PlayerAttributeOption.OPT_5,
                5: PlayerAttributeOption.OPT_6,
                6: PlayerAttributeOption.OPT_7,
                7: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_consistency(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_consistency()

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
        value = self.get_raw_value()
        return value

    def get_injury_tolerance_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        return self.array_opts_injury_tolerance[value]

    def get_weak_foot_frequency_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)
        value = get_base_byte_value(value, 8)
        return self.array_opts_weak_foot_frequency[value]

    def get_consistency_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_consistency[value]

    def get_label(self):
        injury_tolerance_label = self.get_injury_tolerance_label()
        weak_foot_frequency_label = self.get_weak_foot_frequency_label()
        consistency_label = self.get_consistency_label()
        return (
            injury_tolerance_label,
            weak_foot_frequency_label,
            consistency_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = self.array_opts_injury_tolerance.inverse[label[0]]
        second_opt_value = self.array_opts_weak_foot_frequency.inverse[label[1]]
        third_opt_value = self.array_opts_consistency.inverse[label[2]]

        return first_opt_value + second_opt_value + third_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Injury Tolerance and Weak Foot Frequency and Consistency
        attributes and link to this attribute
        """
        self.injury_tolerance = PlayerAttributeInjuryTolerance(
            self.player, parent=self
        )
        self.weak_foot_frequency = PlayerAttributeWeakFootFrequency(
            self.player, parent=self
        )
        self.consistency = PlayerAttributeConsistency(self.player, parent=self)
