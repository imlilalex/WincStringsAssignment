# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1 of Assignment
player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_1 + " " + str(goal_0) +", "+ player_2 + " " + str(goal_1)

report = (f"{player_1} scored in the {goal_0}nd minute\n{player_2} scored in the {goal_1}th minute")

#Part 2 of Assignment

player = "Jan Wouters"
first_name = player[0:3]

last_name_len = len(player[4:])

name_short = player[0:1] + ". " + player[4:]

chant = (first_name + "! ") * (len(first_name)-1) + (first_name + "!")

good_chant = chant[-1] != " "

print(chant)
