from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.editor_config import EditorConfig


class PlayerAttributeNationality(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Nationality"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.NationalTeam

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 112

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

    def get_nationality(self):
        value = self.get_value()
        return EditorConfig.NATIONALITIES[value]

    def get_label(self):
        nationality = self.get_nationality()
        return nationality

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        label = label.upper()
        return EditorConfig.NATIONALITIES.inverse[label]

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True
