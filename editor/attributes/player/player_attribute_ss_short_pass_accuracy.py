from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_ss import (
    PlayerAttributeSs,
)

from editor.attributes.player.player_attribute_short_pass_accuracy import (
    PlayerAttributeShortPassAccuracy,
)

from editor.attributes.player.player_attribute_ability_special_ability_opts import (
    PlayerAttributeAbilitySpcAbilityOpts,
)


class PlayerAttributeSsShortPassAccuracy(PlayerAttribute):
    @classmethod
    def att_class_nsse(cls):
        return "SS/Short Pass Accuracy"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 64

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
        Create SS and Short Pass Accuracy attributes
        and link to this attribute
        """
        self.ss = PlayerAttributeSs(self.player, parent=self)
        self.short_pass_accuracy = PlayerAttributeShortPassAccuracy(
            self.player, parent=self
        )
