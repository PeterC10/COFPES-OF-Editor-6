from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeCallName(PlayerAttribute):
    min_call_name_val = 0
    max_call_name_val = 65535

    @classmethod
    def att_class_name(cls):
        return "Call Name"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.PlayerName

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return (48, 49)

    @classmethod
    def att_class_array_opts(cls):
        return None

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

    def get_call_name(self):
        value_48, value_49 = self.get_raw_value()
        return value_48 + (value_49 * 256)

    def get_label(self):
        call_name = self.get_call_name()
        return str(call_name)

    def set_value(self, value):
        value_48, value_49 = value
        of_data = self.player.option_file.data

        of_data[self.player.address + self.array_pos[0]] = value_48
        of_data[self.player.address + self.array_pos[1]] = value_49
        return True

    def get_value_from_label(self, label):
        call_name = int(label)

        if call_name < self.min_call_name_val:
            call_name = self.min_call_name_val
        elif call_name > self.max_call_name_val:
            call_name = self.max_call_name_val

        value_48 = call_name % 256
        value_49 = int(call_name / 256)
        return (value_48, value_49)

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True
