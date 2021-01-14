from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_facial_hair import (
    PlayerAttributeFacialHair,
)

from editor.attributes.player.player_attribute_cap import (
    PlayerAttributeCap,
)


class PlayerAttributeFacialHairCap(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Facial Hair/Cap"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 95

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_cap(cls):
        """
        Cap Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_cap(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_cap()

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

    def get_facial_hair_value(self):
        value = self.get_value()
        cap_label = self.get_cap_label()
        cap_value = self.array_opts_cap.inverse[cap_label]
        return value - cap_value

    def get_facial_hair_label(self):
        facial_hair_number = self.get_facial_hair_value()
        return str(facial_hair_number)

    def get_cap_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 128)
        return self.array_opts_cap[value]

    def get_label(self):
        facial_hair_label = self.get_facial_hair_label()
        cap_label = self.get_cap_label()
        return (facial_hair_label, cap_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        facial_hair_value = int(label[0])
        min_facial_hair_value = 0
        max_facial_hair_value = 116

        # Set facial hair to minimum value if not valid
        if (
            not min_facial_hair_value
            <= facial_hair_value
            <= max_facial_hair_value
        ):
            facial_hair_value = min_facial_hair_value

        cap_value = self.array_opts_cap.inverse[label[1]]
        return facial_hair_value + cap_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Facial Hair and Cap attributes
        and link to this attribute
        """
        self.facial_hair = PlayerAttributeFacialHair(self.player, parent=self)
        self.cap = PlayerAttributeCap(self.player, parent=self)
