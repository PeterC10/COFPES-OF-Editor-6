from bidict import bidict

from editor.utils.common_functions import (
    get_base_byte_value,
    get_lowest_byte_value,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_stronger_foot import (
    PlayerAttributeStrongerFoot,
)

from editor.attributes.player.player_attribute_favoured_side import (
    PlayerAttributeFavouredSide,
)

from editor.attributes.player.player_attribute_weak_foot_accuracy import (
    PlayerAttributeWeakFootAccuracy,
)

from editor.attributes.player.player_attribute_condition import (
    PlayerAttributeCondition,
)


class PlayerAttributeFavouredSideWeakFootAccCondition(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Favoured Side/Weak Foot Accuracy/Condition"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 81

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_favoured_side(cls):
        """
        Favoured Side Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_S,
                64: PlayerAttributeOption.OPT_O,
                128: PlayerAttributeOption.OPT_B,
            }
        )
        return options_by_value

    @property
    def array_opts_favoured_side(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_favoured_side()

    @classmethod
    def att_class_array_opts_weak_foot_accuracy(cls):
        """
        Weak Foot Accuracy Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                8: PlayerAttributeOption.OPT_2,
                16: PlayerAttributeOption.OPT_3,
                24: PlayerAttributeOption.OPT_4,
                32: PlayerAttributeOption.OPT_5,
                40: PlayerAttributeOption.OPT_6,
                48: PlayerAttributeOption.OPT_7,
                56: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_weak_foot_accuracy(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_weak_foot_accuracy()

    @classmethod
    def att_class_array_opts_condition(cls):
        """
        Condition Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_1,
                1: PlayerAttributeOption.OPT_2,
                2: PlayerAttributeOption.OPT_3,
                3: PlayerAttributeOption.OPT_4,
                4: PlayerAttributeOption.OPT_5,
                5: PlayerAttributeOption.OPT_6,
                6: PlayerAttributeOption.OPT_7,
                7: PlayerAttributeOption.OPT_8,
            }
        )
        return options_by_value

    @property
    def array_opts_condition(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_condition()

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

    def get_favoured_side_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 64)
        return self.array_opts_favoured_side[value]

    def get_weak_foot_accuracy_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)
        value = get_base_byte_value(value, 8)
        return self.array_opts_weak_foot_accuracy[value]

    def get_condition_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_condition[value]

    def get_label(self):
        favoured_side_label = self.get_favoured_side_label()
        weak_foot_accuracy_label = self.get_weak_foot_accuracy_label()
        condition_label = self.get_condition_label()
        return (
            favoured_side_label,
            weak_foot_accuracy_label,
            condition_label,
        )

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        favoured_side_label = label[0]

        if favoured_side_label in [
            PlayerAttributeOption.OPT_R,
            PlayerAttributeOption.OPT_L,
        ]:
            stronger_foot_attribute = PlayerAttributeStrongerFoot(self.player)

            if favoured_side_label == stronger_foot_attribute.get_label():
                favoured_side_label = PlayerAttributeOption.OPT_S
            else:
                favoured_side_label = PlayerAttributeOption.OPT_O

        first_opt_value = self.array_opts_favoured_side.inverse[
            favoured_side_label
        ]
        second_opt_value = self.array_opts_weak_foot_accuracy.inverse[label[1]]
        third_opt_value = self.array_opts_condition.inverse[label[2]]

        return first_opt_value + second_opt_value + third_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Favoured Side and Weak Foot Accuracy and Condition
        attributes and link to this attribute
        """
        self.favoured_side = PlayerAttributeFavouredSide(
            self.player, parent=self
        )
        self.weak_foot_accuracy = PlayerAttributeWeakFootAccuracy(
            self.player, parent=self
        )
        self.condition = PlayerAttributeCondition(self.player, parent=self)
