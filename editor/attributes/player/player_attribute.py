from abc import ABC, abstractmethod
from enum import Enum

from editor.utils.common_functions import string_to_code_value


class PlayerAttributeType:
    def __init__(self, name):
        self.name = name


class PlayerAttributeTypes(Enum):
    PlayerName = PlayerAttributeType("Player Name")
    BasicSettings = PlayerAttributeType("Basic Settings")
    Position = PlayerAttributeType("Position")
    NationalTeam = PlayerAttributeType("National Team")
    ClubTeam = PlayerAttributeType("Club Team")
    ClassicTeam = PlayerAttributeType("Classic Team")
    Appearance = PlayerAttributeType("Appearance")
    Physique = PlayerAttributeType("Physique")
    Accessories = PlayerAttributeType("Accessories")
    StandardAbilities = PlayerAttributeType("Standard Abilities")
    SpecialAbilities = PlayerAttributeType("Special Abilities")
    Mixed = PlayerAttributeType("Mixed")


class PlayerAttribute(ABC):
    def __init__(self, player, parent=None):
        self.player = player
        self.parent = parent

        self.create_child_attributes()

        super().__init__()

    @classmethod
    @abstractmethod
    def att_class_name(cls):
        """
        Set the name of the attribute
        """
        raise NotImplementedError

    @property
    def name(self):
        """
        Return the name of the attribute
        """
        return self.att_class_name()

    @classmethod
    def att_class_type(cls):
        """
        Set the attribute type (PlayerAttributeType instance)
        """
        raise NotImplementedError

    @property
    def attribute_type(self):
        """
        Return the attribute type
        """
        return self.att_class_type()

    @classmethod
    def att_class_hex_info(cls):
        """
        For attributes managed by hex.

        Set a dict of the following keys (int):

        * type
        * offset
        * shift
        * mask
        """
        raise NotImplementedError

    @property
    def hex_info(self):
        """
        Return dict of hex info to get/set attribute value
        """
        return self.att_class_hex_info()

    @classmethod
    def att_class_array_pos(cls):
        """
        For attributes managed by bytes.

        Set the position (int) of the attribute in a player's byte array.
        """
        raise NotImplementedError

    @property
    def array_pos(self):
        """
        Return attribute position in a player's byte array
        """
        if self.parent:
            return self.parent.att_class_array_pos()
        else:
            return self.att_class_array_pos()

    @classmethod
    def att_class_array_opts(cls):
        """
        For attributes managed by bytes.

        Set a bidict of byte array options by the following:

        * value (int)
        * label (str or tuple of str for linked attributes)
        """
        raise NotImplementedError

    @property
    def array_opts(self):
        """
        Return byte array options.
        """
        if self.parent:
            return self.parent.att_class_array_opts()
        else:
            return self.att_class_array_opts()

    @classmethod
    def att_class_code(cls):
        """
        Set code name for attribute
        """
        return string_to_code_value(cls.att_class_name())

    @property
    def code(self):
        """
        Return code name for attribute
        """
        return self.att_class_code()

    @classmethod
    def att_class_hidden(cls):
        """
        Set whether the attribute is hidden,
        e.g. if it a linking attribute used to manage multiple child attributes.

        Defaults to False.
        """
        return False

    @property
    def hidden(self):
        """
        Return whether the attribute is hidden
        """
        return self.att_class_hidden()

    @abstractmethod
    def get_value(self):
        """
        Return value of attribute for player's byte array
        """
        raise NotImplementedError

    @abstractmethod
    def get_label(self):
        """
        Return label used by the in-game editor to identify the value
        """
        raise NotImplementedError

    @abstractmethod
    def set_value(self, value):
        """
        Update attribute with the supplied value (int)
        """
        raise NotImplementedError

    @abstractmethod
    def set_value_from_label(self, label):
        """
        Get value (int) from supplied label (str or tuple of str)
        and update attribute
        """
        raise NotImplementedError

    def create_child_attributes(self):
        """
        Create any child attributes managed by this attribute.

        e.g. for a linking attribute that manages multiple attributes
        that share the same byte in the player's byte array.
        """
        return False
