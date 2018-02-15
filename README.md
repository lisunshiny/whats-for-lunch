# Braise

Want to know what's for lunch @ Braze from the terminal?

This package scrapes https://www.fooda.com/braze to return today's lunch.

## Install

1. Install the gem

```bash
pip install lunchboy
```

2. Make your own GCM key following the instructions [here](https://support.google.com/cloud/answer/6158862?hl=en), and then add this line to your Bash profile.

```bash
export GCM_KEY=your_newly_created_super_secret_gcm_key
```

If you need a GCM key, ask me nicely

## Commands

`lunch`: Returns the day's menus, e.g.,


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
