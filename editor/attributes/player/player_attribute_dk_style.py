from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeDkStyle(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Dropkick Style"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.BasicSettings

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return second value (Dropkick Style is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        registered_postion_label = self.parent.registered_position.get_label()
        dribble_style_label = self.parent.dribble_style.get_label()
        full_label = (registered_postion_label, label, dribble_style_label)

        return self.parent.set_value_from_label(full_label)
