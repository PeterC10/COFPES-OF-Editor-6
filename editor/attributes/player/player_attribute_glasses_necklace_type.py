from bidict import bidict

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_glasses_type import (
    PlayerAttributeGlassesType,
)

from editor.attributes.player.player_attribute_necklace_type import (
    PlayerAttributeNecklaceType,
)


class PlayerAttributeGlassesNecklaceType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Glasses/Necklace Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 97

    @classmethod
    def att_class_array_opts(cls):
        """
        Glasses/Necklace Type opts - N, 1, 2
        """
        # Note: 3 is not valid in-game
        options_by_value = bidict(
            {
                0: (PlayerAttributeOption.OPT_N, PlayerAttributeOption.OPT_N),
                1: (PlayerAttributeOption.OPT_1, PlayerAttributeOption.OPT_N),
                2: (PlayerAttributeOption.OPT_2, PlayerAttributeOption.OPT_N),
                4: (PlayerAttributeOption.OPT_N, PlayerAttributeOption.OPT_1),
                5: (PlayerAttributeOption.OPT_1, PlayerAttributeOption.OPT_1),
                6: (PlayerAttributeOption.OPT_2, PlayerAttributeOption.OPT_1),
                8: (PlayerAttributeOption.OPT_N, PlayerAttributeOption.OPT_2),
                9: (PlayerAttributeOption.OPT_1, PlayerAttributeOption.OPT_2),
                10: (PlayerAttributeOption.OPT_2, PlayerAttributeOption.OPT_2),
            }
        )
        return options_by_value

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
        """
        Get byte value via `get_raw_value`.

        Apply modulo 12 to byte value (to be used to identify label)
        """
        value = self.get_raw_value()
        value = value % 12
        return value

    def get_label(self):
        value = self.get_value()
        label = self.array_opts[value]
        return label

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def set_value_from_label(self, label):
        value = self.array_opts.inverse[label]
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Glasses Type and Necklace Type attributes
        and link to this attribute
        """
        self.glasses_type = PlayerAttributeGlassesType(self.player, parent=self)
        self.necklace_type = PlayerAttributeNecklaceType(
            self.player, parent=self
        )
