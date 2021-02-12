from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_shirt_type import (
    PlayerAttributeShirtType,
)

from editor.attributes.player.player_attribute_weight import (
    PlayerAttributeWeight,
)


class PlayerAttributeShirtTypeWeight(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Shirt Type/Weight"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 89

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_shirt_type(cls):
        """
        Shirt Type Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_STANDARD,
                128: PlayerAttributeOption.OPT_UNTUCKED,
            }
        )
        return options_by_value

    @property
    def array_opts_shirt_type(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_shirt_type()

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

    def get_shirt_type(self):
        value = self.get_value()
        value = get_base_byte_value(value, 128)
        return self.array_opts_shirt_type[value]

    def get_weight(self):
        value = self.get_value()
        print("value------------------>", value)
        shirt_type = self.get_shirt_type()
        shirt_type_byte_base = self.array_opts_shirt_type.inverse[shirt_type]
        print("shirt_type_byte_base--->", shirt_type_byte_base)
        return value - shirt_type_byte_base

    def get_shirt_type_label(self):
        label = str(self.get_shirt_type())
        return label

    def get_weight_label(self):
        label = str(self.get_weight())
        return label

    def get_label(self):
        shirt_type_label = self.get_shirt_type_label()
        weight_label = self.get_weight_label()
        return (shirt_type_label, weight_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        shirt_type = label[0]
        weight = int(label[1])

        min_weight = 66
        max_weight = 109

        if weight < min_weight:
            weight = min_weight
        elif weight > max_weight:
            weight = max_weight

        shirt_type_byte_base = self.array_opts_shirt_type.inverse[shirt_type]
        return shirt_type_byte_base + weight

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Shirt Type and Weight attributes
        and link to this attribute
        """
        self.shirt_type = PlayerAttributeShirtType(self.player, parent=self)
        self.weight = PlayerAttributeWeight(self.player, parent=self)
