from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributePkStyle(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "PK Style"

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
        and return third value (PK Style is set third)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        stronger_foot_label = self.parent.stronger_foot.get_label()
        fk_style_label = self.parent.fk_style.get_label()
        full_label = (stronger_foot_label, fk_style_label, label)

        return self.parent.set_value_from_label(full_label)
