from random import randint


class CatDb:
    cat_states = {'happy_cat': 'images/happy_cat.png',
                  'sad_cat': 'images/sad_cat.png',
                  'neutral_cat': 'images/neutral_cat.png',
                  'sleeping_cat': 'images/sleeping_cat.png'}
    name = ''
    age = 1
    fullness = 40
    happiness = 40
    current_state = None
    is_sleeping = False

    @classmethod
    def set_state(cls):
        if cls.is_sleeping:
            cls.current_state = cls.cat_states['sleeping_cat']
        else:
            if cls.happiness <= 30:
                cls.current_state = cls.cat_states['sad_cat']
            elif cls.happiness <= 70:
                cls.current_state = cls.cat_states['neutral_cat']
            elif cls.happiness <= 100:
                cls.current_state = cls.cat_states['happy_cat']

    @classmethod
    def normalize_stats(cls):
        if cls.fullness > 100:
            cls.happiness -= 30
            cls.fullness = 100
        if cls.fullness < 0:
            cls.fullness = 0
        if cls.happiness > 100:
            cls.happiness = 100
        if cls.happiness < 0:
            cls.happiness = 0

    @classmethod
    def play(cls):
        if cls.is_sleeping:
            cls.is_sleeping = False
            cls.happiness -= 5
        cls.happiness += 15
        cls.fullness -= 10
        rage_chance = randint(1, 100)
        if rage_chance <= 33:
            cls.happiness = 0
        cls.normalize_stats()

    @classmethod
    def feed(cls):
        if not cls.is_sleeping:
            cls.fullness += 15
            cls.happiness += 5
        cls.normalize_stats()

    @classmethod
    def sleep(cls):
        cls.is_sleeping = True
