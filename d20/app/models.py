from django.db import models

# Create your models here.

# Model: character (values that cant be enhanced, manually editable)
    # TODO: name, race, class, xp

# Model: stats (all values that can be enhanced)
    # TODO: characterstats, hp, bab, AC, initiative, speed, fort/reflex/will, attack, damage, skills, level (auto from xp)

# Model: enhancement
    # TODO: name, active (checkbox), type (armor, weapon, magic), dmg, att, count (f.eks. ammo), ac,

# Model: enhancement-stat
    # TODO: name, enhancement-stat-type, enhancement-stat, notes

# Model: inventory
    # TODO: name, count, value_buy, value_sell

# Model: gold coin
    # TODO: cp, sp, gp, pl, gems, valuables, total (in gp)