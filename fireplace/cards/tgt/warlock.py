from ..utils import *


##
# Minions

# Dreadsteed
class AT_019:
	deathrattle = Summon(CONTROLLER, "AT_019")


# Tiny Knight of Evil
class AT_021:
	events = Discard(FRIENDLY).on(Buff(SELF, "AT_021e"))


# Wrathguard
class AT_026:
	events = Damage(SELF).on(Hit(FRIENDLY_HERO, Damage.Args.AMOUNT))

# Wilfred Fizzlebang
class AT_027:
	events = Draw(CONTROLLER).on(
		lambda self, target, card, source: source is self.controller.hero.power and Buff(card, "AT_027e")
	)

class AT_027e:
	cost = lambda self, i: 0


##
# Spells

# Demonfuse
class AT_024:
	play = Buff(TARGET, "AT_024e"), GainMana(OPPONENT, 1)


# Dark Bargain
class AT_025:
	play = Destroy(RANDOM(ENEMY_MINIONS) * 2), Discard(RANDOM(CONTROLLER_HAND) * 2)
