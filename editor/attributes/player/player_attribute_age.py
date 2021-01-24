from editor.utils.common_functions import get_lowest_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeAge(PlayerAttribute):
    min_age = 15
    max_age = 46

    @classmethod
    def att_class_name(cls):
        return "Age"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 113

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

    def get_age(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)

        # If value is an odd number then it has been set oddly
        # and most likely nationality has not been set or is messed up
        # Takeaway 1 to get a "correct" value
        if (value % 2) != 0:
            value -= 1
        return (value // 2) + self.min_age

    def get_label(self):
        age = self.get_age()
        return str(age)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        # formula: (age−min_age) × 2
        # e.g. (45−15) × 2 = 60 for age 45
        age = int(label)

        if age < self.min_age:
            age = self.min_age
        elif age > self.max_age:
            age = self.max_age

        return (age - self.min_age) * 2

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True
