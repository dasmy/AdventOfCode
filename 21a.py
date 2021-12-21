def play(position):
    points = [0, ] * len(position)
    dice = 0
    num_rolled = 0

    while True:
        for p in range(len(position)):
            roll = 0
            for _ in range(3):
                num_rolled += 1
                dice = dice % 100 + 1
                roll += dice

            position[p] += roll
            position[p] = ((position[p] - 1) % 10) + 1
            points[p] += position[p]

            if points[p] >= 1000:
                print(f'Winner: {p+1}, Points {points[p]}, Loser Points: {points[1-p]}, Dice Rolled: {num_rolled}, Score: {points[1-p] * num_rolled}')
                return


play([4, 8])
play([5, 8])
