from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_tactical_dribble import (
    PlayerAttributeTacticalDribble,
)

from editor.attributes.player.player_attribute_shot_power import (
    PlayerAttributeShotPower,
)

from editor.attributes.player.player_attribute_ability_special_ability_opts import (
    PlayerAttributeAbilitySpcAbilityOpts,
)


class PlayerAttributeTacticalDribbleShotPower(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Tactical Dribble/Shot Power"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 69

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
        Create TacticalDribble and Shot Accuracy attributes
        and link to this attribute
        """
        self.tactical_dribble = PlayerAttributeTacticalDribble(
            self.player, parent=self
        )
        self.shot_power = PlayerAttributeShotPower(self.player, parent=self)
