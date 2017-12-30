"""
Module to calculate daily blocks per users.
Provides zone per meal recommendations as well.
"""


def calc_fat(weight, body_fat_perc):
    body_fat_perc = body_fat_perc / 100
    return weight * body_fat_perc


def calc_lean_mass(weight, fat_weight):
    return weight - fat_weight


def cal_daily_protein(lean_mass, activity_level, activity_dict):
    act_level = activity_dict[activity_level][1]
    return lean_mass * act_level


def calc_daily_blocks(daily_protein):
    return int( round(daily_protein / 7) )


def block_breakdown(daily_blocks):

    # Define breakfast, lunch, dinner blocks
    b = l = d = round(daily_blocks / 4)

    # How many blocks are left?
    remaining = daily_blocks - (b + l + d)

    # Define snack 1
    s1 = round(remaining / 3)
    remaining = remaining - s1

    # Define snack 2
    s2 = round(remaining / 2)

    # Define snack 3
    s3 = remaining - s2

    # Print recommendation
    print(
        'Breakfast: {b}  \n'
        'Snack 1:   {s1} \n'
        'Lunch:     {l}  \n'
        'Snack 2:   {s2} \n'
        'Dinner:    {d}  \n'
        'Snack 3:   {s3} \n'
        .format(**locals())
    )


def main():
    # Ask user for Body Weight
    wgt = float( input('Enter Body Weight in lbs (Ex: 200.0): ') )

    # Ask user for Body Fat Percentage
    bfp = float( input('Enter Body Fat % (Ex: 25.0): ')          )

    # Define activity lookup dictionary
    activity_dict = {
        1: ('Little to no physical activity'       , 0.5),
        2: ('Light activity      1-2x      / week' , 0.6),
        3: ('Light  to Medium    2-3x      / week' , 0.7),
        4: ('Medium to Hard      3-4x      / week' , 0.8),
        5: ('Medium to Hard      4-5x      / week' , 0.9),
        6: ('1+ hours Aerobic    6-7x      / week' , 1.0),
        7: ('Competitive Athlete 10-20 hrs / week' , 1.1),
        8: ('Competitive Athlete 20+ hrs   / week' , 1.2),
    }
    # Ask user for activity level
    print('\nActivity Level Definitions:\n')
    for k,v in activity_dict.items():
        print(k,v[0])

    activity_level = float( input('Choose integer value for activity level (Ex: 1): ') )

    # Calculate inputs
    print('\nUser Summary:')
    fat_wgt       = calc_fat(wgt, bfp)
    lean_mass     = calc_lean_mass(wgt, fat_wgt)
    daily_protein = cal_daily_protein(lean_mass, activity_level, activity_dict)
    daily_blocks  = calc_daily_blocks(daily_protein)
    print(
        'Body Weight (lbs)        : {wgt:.2f}           \n'
        'Body Fat Percentage      : {bfp:.2f} %        \n'
        'Fat Weight (lbs)         : {fat_wgt:.2f}       \n'
        'Lean Body Mass (lbs)     : {lean_mass:.2f}     \n'
        'Daily Protein Intake (g) : {daily_protein:.2f} \n'
        'Daily Blocks             : {daily_blocks}     \n'
        .format(**locals())
    )
    print('-------------- Recommended Daily Blocks --------------')

    # Show recommended meals
    block_breakdown(daily_blocks)


if __name__ == '__main__':
    main()
