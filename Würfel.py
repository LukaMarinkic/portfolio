
class dice():
    def __init__(self, sides:int, side_values:list):
        """
        :param sides: The amount of sides the dice has
        :param side_values: The values printed on each side.  [v1:float_or_str, v2:float_or_str, ... , vn:float_or_str]
        """
        if sides != len(side_values):
            ValueError("Number of sides doesn't match with amount of side values")

        self.sides = sides
        self.side_values = side_values
        self.prob_each_side = 1 / sides
        self.prob_same_side_twice = self.prob_each_side ** 2

    def prob_combo(self, combo:list):
        """

        :param combo: A list with two floats for that are in  the self.side_values list [0,3]
        :return:
        """




# useless/too complicated to use
