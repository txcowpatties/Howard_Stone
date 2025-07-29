# ==================================================
# GAME DATA STRUCTURE
# ==================================================
# Each room has:
# - a description to set the scene for the player
# - a list of valid directions the player can move
# - optionally, an item that can be collected
rooms = {
    "Start/Exit": {
        "directions": {"east": "Hall of Fame Plaques"},
        "description": "You're in the museum's main entrance, your designated entry and exit point. It's dark and quiet, your only way out once the job is done."
    },
    "Hall of Fame Plaques": {
        "directions": {"north": "Dead Ball Era", "south": "Hitters Corner", "east": "Security Office", "west": "Start/Exit"},
        "description": "Bronze plaques of baseball legends line the walls. A faint glint of moonlight highlights Al Spalding’s slightly loose plaque...",
        "item": "Al Spalding Plaque"
    },
    "Dead Ball Era": {
        "directions": {"east": "Babe Ruth Gallery", "south": "Hall of Fame Plaques"},
        "description": "A gritty exhibit of early baseball history. A well-worn glove from Cy Young catches your eye.",
        "item": "Cy Young's Glove"
    },
    "Babe Ruth Gallery": {
        "directions": {"east": "Negro Leagues", "west": "Dead Ball Era", "south": "Security Office"},
        "description": "The shrine to Babe Ruth. His iconic 1927 bat rests in a central display behind velvet rope.",
        "item": "Babe's Bat from 1927"
    },
    "Negro Leagues": {
        "directions": {"south": "AAGPBL", "west": "Babe Ruth Gallery"},
        "description": "An emotional tribute to segregated stars. A signed photo of Satchel Paige, Jackie Robinson, and Josh Gibson stands out.",
        "item": "Signed photo of Satchel Paige, Jackie Robinson, and Josh Gibson"
    },
    "AAGPBL": {
        "directions": {"south": "Baseball Expansion", "north": "Negro Leagues", "west": "Security Office"},
        "description": "Honoring the women of wartime baseball. A pristine Rockford Peach uniform draws your attention.",
        "item": "Rockford Peach Uniform"
    },
    "Baseball Expansion": {
        "directions": {"west": "Pitchers Corner", "north": "AAGPBL"},
        "description": "A display on 1960s growth in baseball. The 1969 Mets’ World Series ring gleams in a glass case.",
        "item": "New York Mets 1969 World Series Ring"
    },
    "Pitchers Corner": {
        "directions": {"west": "Hitters Corner", "east": "Baseball Expansion", "north": "Security Office"},
        "description": "Dominant pitchers are honored here. Bob Gibson’s 1968 hat is encased with reverence.",
        "item": "Bob Gibson's 1968 Hat"
    },
    "Hitters Corner": {
        "directions": {"north": "Hall of Fame Plaques", "east": "Pitchers Corner"},
        "description": "Dedicated to the art of hitting. Pete Rose's record-breaking baseball sits center stage.",
        "item": "Pete Rose Baseball"
    },
    "Security Office": {
        "directions": {"west": "Hall of Fame Plaques", "north": "Babe Ruth Gallery", "east": "AAGPBL", "south": "Pitchers Corner"},
        "description": "The guard's domain. Surveillance monitors flicker. If you enter here, the game ends!"
    }
}


# ==================================================
# FUNCTION: Show Game Intro and Instructions
# ==================================================
def show_game_info():
    """
    Displays the game's introduction and instructions.
    Purpose: Set the theme and inform the player of goals and controls.
    """
    print("""
==================================================
   HEIST AT THE NATIONAL BASEBALL HALL OF FAME  
      A Game by Howard Stone IT-140 @SNHU 
==================================================

You play as a clever thief who has broken into the National Baseball Hall of Fame.
Your goal: Sneak through the museum and collect all 8 legendary pieces of memorabilia.
But beware! The Security Office is the guard's station. If you enter that room, 
you'll be caught.

Once you have all 8 items, return to the Start/Exit room to escape and win!
""")
    input("\nPress Enter for how to play...")
    print("""
==================================================
                   HOW TO PLAY   
==================================================

- Move: Type 'move' and then a direction (e.g., 'move north').
- Get: Type 'get' to pick up an item in the room.
- Quit: Type 'quit' to end the game.

==================================================""")
    input("\nPress Enter to start your heist...")


# ==================================================
# FUNCTION: Show Player Status
# ==================================================
def show_status(room_name, inventory, all_items_list):
    """
    Displays the current game state, including:
    - Room name and description
    - Any visible item
    - Player's inventory
    - Possible movement directions
    """
    print("\n--------------------------------------------------")
    print(f"You are in the: {room_name}")
    print(f"Description: {rooms[room_name]['description']}")

    # Display item if present and not yet picked up
    if "item" in rooms[room_name] and rooms[room_name]["item"] not in inventory:
        print(f"You see the '{rooms[room_name]['item']}' here.")

    print(f"\nInventory ({len(inventory)}/{len(all_items_list)}):")
    if not inventory:
        print("  Your inventory is empty.")
    else:
        for item in inventory:
            print(f"  - {item}")

    print("\nAvailable directions:")
    for direction in rooms[room_name]['directions']:
        print(f"  - {direction}")
    print("--------------------------------------------------")


# ==================================================
# FUNCTION: Determine New Room After Move
# ==================================================
def get_new_state(direction, current_room):
    """
    Validates and processes player movement.
    Purpose: Check if the given direction is valid from the current room and return the next room.
    """
    valid_directions = ["north", "south", "east", "west"]  # Only allow compass directions
    if direction.lower() in valid_directions:
        # Validate against room's available exits
        if direction in rooms[current_room]['directions']:
            return rooms[current_room]['directions'][direction]
        else:
            print("\nYou can't go that way! Try another direction.")
    else:
        print("\nInvalid direction. Please use 'north', 'south', 'east', or 'west'.")
    return current_room


# ==================================================
# MAIN GAME LOOP
# ==================================================
def main():
    """
    Runs the primary gameplay loop.
    Handles player input, status updates, and win/loss condition checks.
    """
    show_game_info()

    items_to_collect = [data["item"] for data in rooms.values() if "item" in data]
    current_room = "Start/Exit"
    inventory = []

    print("\nWelcome to the Heist!")

    while True:
        show_status(current_room, inventory, items_to_collect)

        # Get and process user command
        action = input("\n> What is your next move? ('move north', 'get', 'quit'): ").strip().lower()
        words = action.split()
        if not words:
            print("\nYou need to enter a command.")
            continue

        command = words[0]

        if command == "quit":
            print("\nYou slip back into the shadows and abandon the heist. Goodbye!")
            break

        elif command == "get":
            # Attempt to collect an item from the room
            if "item" in rooms[current_room] and rooms[current_room]["item"] not in inventory:
                item = rooms[current_room]["item"]
                inventory.append(item)
                print(f"\nYou picked up the {item}!")
            else:
                print("\nThere's nothing here to get.")

        elif command == "move":
            # Ensure a direction is specified
            if len(words) > 1:
                direction = words[1]
                current_room = get_new_state(direction, current_room)
            else:
                print("\nYou need to specify a direction after 'move'.")
        else:
            print("\nInvalid command. Please use 'move', 'get', or 'quit'.")

        # LOSS: Entering the Security Office results in capture
        if current_room == "Security Office":
            print("\nOh no! You walked right into the Security Office and were caught by the guard! Game Over!")
            break

        # WIN: Collected all items and returned to the Start/Exit room
        if current_room == "Start/Exit" and len(inventory) == len(items_to_collect):
            print("\nCongratulations! You've collected all the items and made it back to the exit. You win!")
            break


# ==================================================
# RUN GAME
# ==================================================
if __name__ == "__main__":
    # Loop to allow player to replay the game
    while True:
        main()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing!")
            break
