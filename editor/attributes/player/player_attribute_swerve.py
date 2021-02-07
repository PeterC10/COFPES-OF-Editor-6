from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeSwerve(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Swerve"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.StandardAbilities

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return second value (shot accuracy is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        playmaking_label = self.parent.playmaking.get_label()
        full_label = (playmaking_label, label)

        return self.parent.set_value_from_label(full_label)
