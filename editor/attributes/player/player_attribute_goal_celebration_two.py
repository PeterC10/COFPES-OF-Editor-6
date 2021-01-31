from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_goal_celebration import (
    PlayerAttributeCelebration,
)


class PlayerAttributeGoalCelebrationTwo(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Goal Celebration 2"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 84

    @classmethod
    def att_class_array_opts(cls):
        return None

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
        value = self.get_value()
        return PlayerAttributeCelebration.get_label(value)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = PlayerAttributeCelebration.get_value_from_label(label)
        self.set_value(value)
        return True
