from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeOutside(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Outside"

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
        and return first value (covering is set seventh)
        """
        full_label = self.parent.get_label()
        return full_label[6]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        one_on_one_stopper_label = self.parent.one_on_one_stopper.get_label()
        penalty_stopper_label = self.parent.penalty_stopper.get_label()
        d_line_control_label = self.parent.d_line_control.get_label()
        covering_label = self.parent.covering.get_label()
        sliding_label = self.parent.sliding.get_label()
        marking_label = self.parent.marking.get_label()
        one_touch_pass_label = self.parent.one_touch_pass.get_label()

        full_label = (
            one_on_one_stopper_label,
            penalty_stopper_label,
            d_line_control_label,
            covering_label,
            sliding_label,
            marking_label,
            label,
            one_touch_pass_label,
        )
        return self.parent.set_value_from_label(full_label)
