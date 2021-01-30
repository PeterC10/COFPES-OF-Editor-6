from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeStrongerFoot(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Stronger Foot"

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
        and return first value (stronger foot is set first)
        """
        full_label = self.parent.get_label()
        return full_label[0]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        fk_style_label = self.parent.fk_style.get_label()
        pk_style_label = self.parent.pk_style.get_label()
        full_label = (label, fk_style_label, pk_style_label)

        return self.parent.set_value_from_label(full_label)
