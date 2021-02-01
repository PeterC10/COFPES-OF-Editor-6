from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeOneTouchPass(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "1-Touch Pass"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.SpecialAbilities

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return first value (covering is set eigth)
        """
        full_label = self.parent.get_label()
        return full_label[7]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        one_on_one_stopper_label = self.parent.one_on_one_stopper.get_label()
        penalty_stopper_label = self.parent.penalty_stopper.get_label()
        d_line_control_label = self.parent.d_line_control.get_label()
        covering_label = self.parent.covering.get_label()
        sliding_label = self.parent.sliding.get_label()
        marking_label = self.parent.marking.get_label()
        outside_label = self.parent.outside.get_label()

        full_label = (
            one_on_one_stopper_label,
            penalty_stopper_label,
            d_line_control_label,
            covering_label,
            sliding_label,
            marking_label,
            outside_label,
            label,
        )
        return self.parent.set_value_from_label(full_label)
