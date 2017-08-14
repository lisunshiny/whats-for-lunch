# Lunchboy

Want to know what's for lunch from the terminal?

This package scrapes http://foodamenus.com/appboy to return today's lunch.

## Install

```bash
pip install lunchboy
```

## Commands
`lunch`: Returns the day's lunch restaurant, e.g.,

```
$ lunch
today's lunch is alpha fusion!!!!!!!!!!!
```

`menu`: Returns the day's lunch restaurant AND the menu, e.g.,

**Note:** To use this command, you must first add this to your bash profile

```bash
export GCM_KEY=super_secret_gcm_key
```

If you need a GCM key, ask me nicely

```
$ menu
today's lunch is alpha fusion!!!!!!!!!!!

--------------- MENU ----------------

None
Alpha Fusion
ALPHA
Fusion
DUMPLINGS
ALL DUMPLINGS COME WITH YOUR CHOICE OF SAUCE-HAI SING, SWEET
CHILI, SRIRACHA
THE CLASSIC
Pan fried pork and leek dumplings
GREENS MACHINE
Vegetarian dumplings
FRIED CHICKEN
Pan fried chicken dumplings
DUMPLINGS OF THE SEA
Japanese shrimp shuma
NOODLES AND RICE
CHOW FUN
Vegetarian Cantonese stir fried rice
noodles, with carrots and Chinese
broccoli
SINGAPORE THIN NOODLES
Stir-fried curried rice vermicelli
noodles, with vegetables
BROWN RICE
COMBINATIONS
THE ALPHA COMBO
Choice of any 4 dumplings, noodles
or rice, partnered with steamed
vegetables
SIDES
DAILY ROTATING STEAMED
VEGETABLES
```
