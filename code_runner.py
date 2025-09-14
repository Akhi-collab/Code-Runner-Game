import random

# Step 1: Setup
grid_size = 5
player_pos = [0, 0]
goal_pos = [grid_size - 1, grid_size - 1]

# Step 2: Place random bugs
bugs = []
while len(bugs) < 5:
    r = random.randint(0, grid_size - 1)
    c = random.randint(0, grid_size - 1)
    if [r, c] not in bugs and [r, c] != player_pos and [r, c] != goal_pos:
        bugs.append([r, c])

# Step 3: Display grid (bugs hidden)
def display_grid():
    print("\nGrid:")
    for r in range(grid_size):
        row = ""
        for c in range(grid_size):
            if [r, c] == player_pos:
                row += "🧍 "
            elif [r, c] == goal_pos:
                row += "🎯 "
            else:
                row += ". "
        print(row)
    print()

# Step 4: Reveal bugs after game over
def reveal_bugs():
    print("\n💀 BUGS REVEALED 💀")
    for r in range(grid_size):
        row = ""
        for c in range(grid_size):
            if [r, c] == player_pos:
                row += "🧍 "
            elif [r, c] == goal_pos:
                row += "🎯 "
            elif [r, c] in bugs:
                row += "🐞 "
            else:
                row += ". "
        print(row)
    print()

# Step 5: Game loop
while True:
    display_grid()
    move = input("Move (U/L/D/R): ").lower()

    # Calculate new position
    new_pos = player_pos.copy()
    if move == "u":
        new_pos[0] -= 1
    elif move == "d":
        new_pos[0] += 1
    elif move == "l":
        new_pos[1] -= 1
    elif move == "r":
        new_pos[1] += 1
    else:
        print("❌ Invalid move! Use U, L, D, or R.")
        continue


    # Check if move is inside the grid
    if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
        player_pos = new_pos
    else:
        print("🚫 Can't move outside the grid!")
        continue

    # Check if player hits a bug
    if player_pos in bugs:
        reveal_bugs()
        print("💀 Oh no! You hit a 🐞. Game Over!")
        break

    # Check if player reaches the goal
    if player_pos == goal_pos:
        display_grid()
        print("🎉 Congratulations! You reached the goal! 🎯")
        break

