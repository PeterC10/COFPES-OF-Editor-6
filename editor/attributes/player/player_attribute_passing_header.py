from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_passing import (
    PlayerAttributePassing,
)

from editor.attributes.player.player_attribute_header import (
    PlayerAttributeHeader,
)

from editor.attributes.player.player_attribute_ability_special_ability_opts import (
    PlayerAttributeAbilitySpcAbilityOpts,
)


class PlayerAttributePassingHeader(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Passing/Header"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 73

    @classmethod
    def att_class_array_opts(cls):
        return None

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

    def get_label(self):
        value = self.get_value()
        label = PlayerAttributeAbilitySpcAbilityOpts.get_full_label(value)
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = PlayerAttributeAbilitySpcAbilityOpts.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Passing and Header attributes
        and link to this attribute
        """
        self.passing = PlayerAttributePassing(self.player, parent=self)
        self.header = PlayerAttributeHeader(self.player, parent=self)
