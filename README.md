# Braise

Want to know what's for lunch @ Braze from the terminal?

This package scrapes https://www.fooda.com/braze to return today's lunch.

## Install

**If you had the old `lunchboy` gem, `pip uninstall lunchboy` before doing this.**


1. Install the `braise` package

```bash
pip install braise
```

2. Make your own GCM key following the instructions [here](https://support.google.com/cloud/answer/6158862?hl=en), and then add this line to your Bash profile.

```bash
export GCM_KEY=your_newly_created_super_secret_gcm_key
```

## Commands

`lunch`: Returns the day's menus, e.g.,


```
$ lunch
Yay lunch


--------------- Menu 1 ----------------

taïm
COMBINATION
FALAFEL PLATTER
Assorted Green and
Harissa Falafel, Hummus,
Tahini, Tabouli, Israeli
Salad, Pita
Signature Sauces Amba
& S'rug
vegetarian
fooda.com


--------------- Menu 2 ----------------

EATOS
STREET GRILL
MEATOSS FOOD TRUCK
ENTREES
GF
CHORIZO LUNCH
Chorizo sausage served with your choice of one side
BBQ DRUMSTICKS LUNCH
Smokey BBQ drumsticks served with your choice of one side
GF
BEEF AND CHEESE EMPANADA
Homemade beef and cheese empanada
with your choice of one side
CHICKEN BREAST LUNCH
Tender chicken breast served with your choice of one side
GF
CHICKEN THIGH LUNCH
GF
Hot and delicious chicken thigh served with your choice of one side
MEATOSS SALAD
Mixed greens, tomatoes, cucumbers, quinoa, corn and beets with
vour choice of side
SIDES
BAKED POTATOES D
COLE SLAW GF
YELLOW RICECP
-Gluten Free
-Vegan
GF
Vegetarian
fooda.com
```
