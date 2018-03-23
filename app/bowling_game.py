class Game(object):
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)
        if pins == 10:
            self._rolls.append(0)

    def score(self):
        score = 0
        for frame in range(0,10):
            score += self.score_for(frame)
        return score

    def score_for(self, frame):
        if self.isStrike(frame):
            return self.normal_score_of(frame) + self.strike_bonus_of(frame)
        if self.isSpare(frame):
            return self.normal_score_of(frame) + self.spare_bonus_of(frame)
        return self.normal_score_of(frame)

    def strike_bonus_of(self, frame):
        if self.isStrike(frame+1):
            return self.first_roll_of(frame + 1) + self.first_roll_of(frame + 2)
        return self.first_roll_of(frame + 1) + self.second_roll_of(frame + 1)

    def isStrike(self, frame):
        return self.first_roll_of(frame) == 10

    def spare_bonus_of(self, frame):
        return self.first_roll_of(frame + 1)

    def isSpare(self, frame):
        return self.first_roll_of(frame) + self.second_roll_of(frame) == 10

    def normal_score_of(self, frame):
        return self.first_roll_of(frame) + self.second_roll_of(frame)

    def first_roll_of(self, frame):
        return self.roll_at(frame * 2)

    def second_roll_of(self, frame):
        return self.roll_at(frame * 2 + 1)

    def roll_at(self, index):
        if len(self._rolls) > index:
            return self._rolls[index]
        return 0
