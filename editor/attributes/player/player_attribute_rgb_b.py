from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeRgbB(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Hair Color RGB-B"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.Appearance

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return third value (Hair Color RGB-B is set third)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        gloves_label = self.parent.gloves.get_label()
        ankle_tape_label = self.parent.ankle_tape.get_label()
        full_label = (gloves_label, ankle_tape_label, label)
        return self.parent.set_value_from_label(full_label)
