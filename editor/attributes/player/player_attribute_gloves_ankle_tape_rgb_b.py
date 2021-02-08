from bidict import bidict

from editor.utils.common_functions import (
    get_lowest_byte_value,
    get_base_byte_value,
)

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_option import (
    PlayerAttributeOption,
)

from editor.attributes.player.player_attribute_gloves import (
    PlayerAttributeGloves,
)

from editor.attributes.player.player_attribute_ankle_tape import (
    PlayerAttributeAnkleTape,
)

from editor.attributes.player.player_attribute_rgb_b import (
    PlayerAttributeRgbB,
)


class PlayerAttributeGlovesAnkleTapeRgbB(PlayerAttribute):
    MIN_RGB_B_VALUE = 0
    MAX_RGB_B_VALUE = 63

    @classmethod
    def att_class_name(cls):
        return "Gloves/Ankle Tape/Hair Color RGB-B"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 104

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_gloves(cls):
        """
        Gloves Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                128: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_gloves(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_gloves()

    @classmethod
    def att_class_array_opts_ankle_tape(cls):
        """
        Ankle Tape Opts
        """
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_N,
                64: PlayerAttributeOption.OPT_Y,
            }
        )
        return options_by_value

    @property
    def array_opts_ankle_tape(self):
        """
        Return byte array options.
        """
        return self.att_class_array_opts_ankle_tape()

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

    def get_gloves_label(self):
        value = self.get_value()
        value = get_base_byte_value(value, 128)
        return self.array_opts_gloves[value]

    def get_ankle_tape_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 128)
        value = get_base_byte_value(value, 64)
        return self.array_opts_ankle_tape[value]

    def get_rgb_b_label(self):
        value = self.get_value()
        value = get_lowest_byte_value(value, 64)
        value = self.MAX_RGB_B_VALUE - value
        return str(value)

    def get_label(self):
        gloves_label = self.get_gloves_label()
        ankle_tape_label = self.get_ankle_tape_label()
        rgb_b_label = self.get_rgb_b_label()
        return (gloves_label, ankle_tape_label, rgb_b_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        gloves_value = self.array_opts_gloves.inverse[label[0]]
        ankle_tape_value = self.array_opts_ankle_tape.inverse[label[1]]

        rgb_b_value = int(label[2])

        if (
            rgb_b_value < self.MIN_RGB_B_VALUE
            or rgb_b_value > self.MAX_RGB_B_VALUE
        ):
            rgb_b_value = self.MAX_RGB_B_VALUE

        rgb_b_value = self.MAX_RGB_B_VALUE - rgb_b_value

        return gloves_value + ankle_tape_value + rgb_b_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Gloves and Ankle Tape and RGB-B attributes
        and link to this attribute
        """
        self.gloves = PlayerAttributeGloves(self.player, parent=self)
        self.ankle_tape = PlayerAttributeAnkleTape(self.player, parent=self)
        self.rgb_b = PlayerAttributeRgbB(self.player, parent=self)
