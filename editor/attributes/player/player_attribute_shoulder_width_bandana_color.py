from bidict import bidict

from editor.utils.common_functions import get_base_byte_value

from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)

from editor.attributes.player.player_attribute_shoulder_width import (
    PlayerAttributeShoulderWidth,
)

from editor.attributes.player.player_attribute_bandana_color import (
    PlayerAttributeBandanaColor,
)

from editor.attributes.player.player_attribute_physical_opts import (
    PlayerAttributePhysicalLinkedOpts,
)


class PlayerAttributeShoulderWidthBandanaColor(PlayerAttribute):
    opt_white = "White"
    opt_black = "Black"
    opt_red = "Red"
    opt_blue = "Blue"
    opt_purple = "Purple"
    opt_cyan = "Cyan"
    opt_yellow = "Yellow"
    opt_green = "Green"

    @classmethod
    def att_class_name(cls):
        return "Shoulder Width/Bandana Color"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return 109

    @classmethod
    def att_class_array_opts(cls):
        """
        Bandana Color Opts
        """
        options_by_value = bidict(
            {
                0: cls.opt_white,
                16: cls.opt_black,
                32: cls.opt_red,
                48: cls.opt_blue,
                64: cls.opt_purple,
                80: cls.opt_cyan,
                96: cls.opt_yellow,
                112: cls.opt_green,
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
        value = self.get_raw_value()
        return value

    def get_bandana_color_label(self, value):
        value = get_base_byte_value(value, 16)

        # Bandana colors are repeated
        byte_split = 127
        if value > byte_split:
            value = value - byte_split

        return self.array_opts[value]

    def get_label(self):
        value = self.get_value()
        shoulder_width_label = (
            PlayerAttributePhysicalLinkedOpts.get_first_opt_label(value)
        )
        bandana_color_label = self.get_bandana_color_label(value)
        return (shoulder_width_label, bandana_color_label)

    def set_value(self, value):
        of_data = self.player.option_file.data
        of_data[self.player.address + self.array_pos] = value
        return True

    def get_value_from_label(self, label):
        first_opt_value = (
            PlayerAttributePhysicalLinkedOpts.FIRST_OPT_BY_VALUE.inverse[
                label[0]
            ]
        )
        second_opt_value = self.array_opts.inverse[label[1]]
        return first_opt_value + second_opt_value

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Shoulder Width and Bandana Color attributes
        and link to this attribute
        """
        self.shoulder_width = PlayerAttributeShoulderWidth(
            self.player, parent=self
        )
        self.bandana_color = PlayerAttributeBandanaColor(
            self.player, parent=self
        )
