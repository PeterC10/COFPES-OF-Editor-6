from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_goal_celebration import (
    PlayerAttributeCelebration,
)

from editor.attributes.player.player_attribute_long_throw import (
    PlayerAttributeLongThrow,
)

from editor.attributes.player.player_attribute_goal_celebration_two import (
    PlayerAttributeGoalCelebrationTwo,
)


class PlayerAttributeLongThrowGoalCelebrationTwo(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Long Throw/Goal Celebration Two"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 84

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_long_throw(cls):
        """
        Long Throw Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_long_throw(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_long_throw()

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

    def get_long_throw_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 128)
        return self.array_opts_long_throw[value]

    def get_goal_celebration_two_label(self):
        value = self.get_value()
        return PlayerAttributeCelebration.get_label(value)

    def get_label(self):
        long_throw_label = self.get_long_throw_label()
        goal_celebration_two_label = self.get_goal_celebration_two_label()
        return (long_throw_label, goal_celebration_two_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        long_throw_value = self.array_opts_long_throw.inverse[label[0]]
        goal_celebration_two_value = (
            PlayerAttributeCelebration.get_value_from_label(label[1])
        )

        return long_throw_value + goal_celebration_two_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Long Throw and Goal Celebration Two attributes
        and link to this attribute
        """
        self.long_throw = PlayerAttributeLongThrow(self.player, parent=self)
        self.get_goal_celebration_two = PlayerAttributeGoalCelebrationTwo(
            self.player, parent=self
        )
