import math
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

from editor.attributes.player.player_attribute_preset_face import (
    PlayerAttributePresetFace,
)

from editor.attributes.player.player_attribute_undershorts_color import (
    PlayerAttributeUndershortsColor,
)

from editor.attributes.player.player_attribute_socks_type import (
    PlayerAttributeSocksType,
)


class PlayerAttributePresetFaceUndershortsColorSocksType(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Preset Face/Undershorts Color/Socks Type"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Mixed

    @classmethod
    def att_class_hex_info(cls):
        return None

    @classmethod
    def att_class_array_pos(cls):
        return (100, 101)

    @classmethod
    def att_class_array_opts(cls):
        return None

    @classmethod
    def att_class_array_opts_preset_face(cls):
        options_by_value = bidict(
            {
                0: 1,
                32: 2,
                64: 3,
                96: 4,
                128: 5,
                160: 6,
                192: 7,
                224: 8,
            }
        )
        return options_by_value

    @property
    def array_opts_preset_face(self):
        return self.att_class_array_opts_preset_face()

    @classmethod
    def att_class_array_opts_undershorts_color(cls):
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_WHITE,
                1: PlayerAttributeOption.OPT_BLACK,
                2: PlayerAttributeOption.OPT_RED,
                3: PlayerAttributeOption.OPT_BLUE,
                4: PlayerAttributeOption.OPT_YELLOW,
                5: PlayerAttributeOption.OPT_GREEN,
                6: PlayerAttributeOption.OPT_PURPLE,
                7: PlayerAttributeOption.OPT_SAME,
            }
        )
        return options_by_value

    @property
    def array_opts_undershorts_color(self):
        return self.att_class_array_opts_undershorts_color()

    @classmethod
    def att_class_array_opts_socks_type(cls):
        options_by_value = bidict(
            {
                0: PlayerAttributeOption.OPT_LONG,
                8: PlayerAttributeOption.OPT_STANDARD,
                16: PlayerAttributeOption.OPT_SHORT,
            }
        )
        return options_by_value

    @property
    def array_opts_socks_type(self):
        return self.att_class_array_opts_socks_type()

    @classmethod
    def att_class_hidden(cls):
        return True

    def get_raw_value(self):
        """
        Get byte value currently set in player's byte array
        """
        of_data = self.player.option_file.data
        value1 = of_data[self.player.address + self.array_pos[0]]
        value2 = of_data[self.player.address + self.array_pos[1]]
        return (value1, value2)

    def get_value(self):
        value = self.get_raw_value()
        return value

    def get_preset_face_value(self):
        value_100, value_101 = self.get_value()
        value_100 = get_base_byte_value(value_100, 32)
        value_100 = self.array_opts_preset_face[value_100]

        face_number = value_100 + (value_101 * 8)
        return face_number


    def get_preset_face_label(self):
        face_number = self.get_preset_face_value()
        return str(face_number)

    def get_undershorts_color_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 8)
        return self.array_opts_undershorts_color[value]

    def get_socks_type_label(self):
        value = self.get_value()[0]
        value = get_lowest_byte_value(value, 32)
        value = get_base_byte_value(value, 8)
        return self.array_opts_socks_type[value]

    def get_label(self):
        preset_face_label = self.get_preset_face_label()
        undershorts_color_label = self.get_undershorts_color_label()
        socks_type_label = self.get_socks_type_label()
        return (preset_face_label, undershorts_color_label, socks_type_label)

    def set_value(self, value):
        value_100, value_101 = value
        of_data = self.player.option_file.data

        of_data[self.player.address + self.array_pos[0]] = value_100
        of_data[self.player.address + self.array_pos[1]] = value_101
        return True

    def get_value_from_label(self, label):
        face_number = int(label[0])
        multiple_factor = math.ceil(face_number / 8) - 1
        base_face_number = face_number - (multiple_factor * 8)

        value_100 = self.array_opts_preset_face.inverse[base_face_number]
        value_101 = multiple_factor

        value_100 += self.array_opts_undershorts_color.inverse[label[1]]
        value_100 += self.array_opts_socks_type.inverse[label[2]]

        return (value_100, value_101)

    def set_value_from_label(self, label):
        value = self.get_value_from_label(label)
        self.set_value(value)
        return True

    def create_child_attributes(self):
        """
        Create Preset Face, Undershorts color and Socks Type attributes
        and link to this attribute
        """
        self.preset_face = PlayerAttributePresetFace(self.player, parent=self)
        self.undershorts_color = PlayerAttributeUndershortsColor(
            self.player, parent=self
        )
        self.socks_type = PlayerAttributeSocksType(self.player, parent=self)
