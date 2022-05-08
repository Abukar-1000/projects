
gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # game board 
winningCombos = [
            # horizontal winning combos
            (0,1,2),
            (3,4,5),
            (6,7,8),
            # Vertical winning combos
            (0,3,6),
            (1,4,7),
            (2,5,8),
            # diagnal winning combos 
            (0,4,8),
            (2,4,6),
        ]

positions = [4]

bestMatch = [0.0,0] # decimal evaluation of each combo, index of the best match
index = 0
for combos in winningCombos:
    counter = 0
    for combo in range(3):
        if combos[combo] in positions:
            counter += 1
        if (counter/3) > bestMatch[0]:
            bestMatch[0] = counter/3
            bestMatch[1] = index
    index += 1      

print([x for x in range(0,9)])