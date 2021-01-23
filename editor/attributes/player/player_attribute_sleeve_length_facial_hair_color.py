from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_sleeve_length import (
    PlayerAttributeSleeveLength,
)

from editor.attributes.player.player_attribute_facial_hair_color import (
    PlayerAttributeFacialHairColor,
)


class PlayerAttributeSleeveLengthFacialHairColor(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Sleeve Length/Facial Hair Color"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 96

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_sleeve_length(cls):
        """
        Sleeve Length Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_AUTO,
                64: PlayerAttributeOption.OPT_SHORT,
                128: PlayerAttributeOption.OPT_LONG,
            }
        )
        return options_by_value

    @property
    def array_opts_sleeve_length(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_sleeve_length()

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

    def get_sleeve_length_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        # Auto sleeve length is repeated
        if value == 192:
            value = 0
        return self.array_opts_sleeve_length[value]

    def get_facial_hair_color_value(self):
        value = self.get_value()

        sleeve_length_label = self.get_sleeve_length_label()
        sleeve_length_value = self.array_opts_sleeve_length.inverse[
            sleeve_length_label
        ]
        value -= sleeve_length_value

        # 62 is same as hair color
        if value == 62:
            return PlayerAttributeOption.OPT_SAME
        else:
            # 0 is 1, 1 is 2...61 is 62
            value += 1
            return value

    def get_facial_hair_color_label(self):
        facial_hair_color_number = self.get_facial_hair_color_value()
        return str(facial_hair_color_number)

    def get_label(self):
        sleeve_length_label = self.get_sleeve_length_label()
        facial_hair_color_label = self.get_facial_hair_color_label()
        return (sleeve_length_label, facial_hair_color_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        # Use same as hair color as default
        default_value = 62

        facial_hair_color = label[0]
        if facial_hair_color == PlayerAttributeOption.OPT_SAME:
            facial_hair_color_value = 62
        else:
            min_facial_hair_color_value = 1
            max_facial_hair_color_value = 62

            if (
                not min_facial_hair_color_value
                <= facial_hair_color_value
                <= max_facial_hair_color_value
            ):
                facial_hair_color_value = default_value

            # 0 is 1, 1 is 2...61 is 62
            facial_hair_color_value -= 1

        sleeve_length_value = self.array_opts_sleeve_length.inverse[label[1]]
        return facial_hair_color_value + sleeve_length_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Sleeve Length and Facial Hair Color attributes
        and link to this attribute
        """
        self.sleeve_length = PlayerAttributeSleeveLength(
            self.player, parent=self
        )
        self.facial_hair_color = PlayerAttributeFacialHairColor(
            self.player, parent=self
        )
