import random

# Инициализация состояния игры
game_state = {
    'output': "",
    'step': 'start',
    'ship_type': None,
    'cargo_space': 0,
    'weapons': {
        'phasers': 0,
        'missiles': 0,
        'lances': 0,
        'torpedoes': 0,
        'field': 0
    },
    'range': 0,
    'relative_velocity': 0
}


def deepspace_battle(user_input=None):
    global game_state

    output = ""

    if game_state['step'] == 'start':
        output += " " * 35 + "DEEPSPACE\n"
        output += " " * 30 + "CREATIVE COMPUTING\n"
        output += " " * 29 + "MORRISTOWN NEW JERSEY\n\n\n"
        output += "THIS IS DEEPSPACE, A TACTICAL SIMULATION OF SHIP TO SHIP COMBAT IN DEEP SPACE.\n"
        output += "DO YOU WISH INSTRUCTIONS?\n"
        game_state['step'] = 'instructions'

    elif game_state['step'] == 'instructions':
        if user_input and user_input.upper() != "NO":
            output += "YOU ARE ONE OF A GROUP OF CAPTAINS ASSIGNED TO PATROL A SECTION OF YOUR STAR EMPIRE'S BORDER AGAINST HOSTILE ALIENS. YOU WILL FIRST BE REQUIRED TO SELECT A VESSEL FROM ONE OF THREE TYPES, EACH WITH ITS OWN CHARACTERISTICS:\n"
            output += "TYPE        SPEED   CARGO SPACE   PROTECTION\n1 SCOUT      10X     16            1\n2 CRUISER    4X      24            2\n3 BATTLESHIP 2X      30            5\n"
            output += "ONCE A SHIP HAS BEEN SELECTED, YOU WILL BE INSTRUCTED TO ARM IT WITH WEAPONRY FROM THE FOLLOWING LIST:\n"
            output += "TYPE                         CARGO SPACE    REL. STRENGTH\n1 PHASER BANKS                   12                4\n2 ANTI-MATTER MISSILE             4               20\n3 HYPERSPACE LANCE                4               16\n4 PHOTON TORPEDO                  2               10\n5 HYPERON NEUTRALIZATION FIELD   20                6\n"
            game_state['step'] = 'select_ship'
        else:
            output += "SKIPPING INSTRUCTIONS. PLEASE SELECT A SHIP.\n"
            game_state['step'] = 'select_ship'

    elif game_state['step'] == 'select_ship':
        output += "WHICH SPACECRAFT WOULD YOU LIKE (1-3)?\n"
        if user_input:
            if user_input == '1':
                game_state['ship_type'] = 'SCOUT'
                game_state['cargo_space'] = 16
            elif user_input == '2':
                game_state['ship_type'] = 'CRUISER'
                game_state['cargo_space'] = 24
            elif user_input == '3':
                game_state['ship_type'] = 'BATTLESHIP'
                game_state['cargo_space'] = 30
            game_state['step'] = 'select_weapons'
            output += f"{game_state['ship_type']} SELECTED. YOU HAVE {game_state['cargo_space']} UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.\n"

    elif game_state['step'] == 'select_weapons':
        output += "CHOOSE A WEAPON AND THE AMOUNT YOU WISH (TYPE AMOUNT)\n"
        if user_input:
            weapon_type, amount = map(int, user_input.split())
            space_needed = amount * (
                12 if weapon_type == 1 else 4 if weapon_type in [2, 3] else 2 if weapon_type == 4 else 20)
            if space_needed <= game_state['cargo_space']:
                if weapon_type == 1:
                    game_state['weapons']['phasers'] += amount
                elif weapon_type == 2:
                    game_state['weapons']['missiles'] += amount
                elif weapon_type == 3:
                    game_state['weapons']['lances'] += amount
                elif weapon_type == 4:
                    game_state['weapons']['torpedoes'] += amount
                elif weapon_type == 5:
                    game_state['weapons']['field'] = 100
                game_state['cargo_space'] -= space_needed
                output += f"WEAPON LOADED. {game_state['cargo_space']} UNITS OF CARGO SPACE REMAINING.\n"
            else:
                output += "NOT ENOUGH SPACE. RESELECT WEAPON AND AMOUNT.\n"
            if game_state['cargo_space'] <= 0:
                game_state['step'] = 'battle_start'

    elif game_state['step'] == 'battle_start':
        output += "BATTLE STARTING...\n"
        game_state['range'] = 1000  # Начальная дистанция
        game_state['relative_velocity'] = 0
        output += f"RANGE TO TARGET: {game_state['range']} KM\n"
        output += f"RELATIVE VELOCITY: {game_state['relative_velocity']} KM/S\n"
        output += "ENTER COMMAND (1: FIRE PHASERS, 2: FIRE MISSILE, 3: FIRE LANCE, 4: FIRE TORPEDO, 5: ACTIVATE FIELD, 6: CHANGE VELOCITY, 7: DISENGAGE):\n"
        game_state['step'] = 'battle_actions'

    elif game_state['step'] == 'battle_actions':
        if user_input:
            command = int(user_input)
            if command == 1 and game_state['weapons']['phasers'] > 0:
                game_state['weapons']['phasers'] -= 1
                damage = random.randint(10, 50)
                output += f"FIRED PHASERS. DAMAGE: {damage}\n"
            elif command == 2 and game_state['weapons']['missiles'] > 0:
                game_state['weapons']['missiles'] -= 1
                damage = random.randint(50, 150)
                output += f"FIRED MISSILE. DAMAGE: {damage}\n"
            elif command == 3 and game_state['weapons']['lances'] > 0:
                game_state['weapons']['lances'] -= 1
                damage = random.randint(40, 120)
                output += f"FIRED LANCE. DAMAGE: {damage}\n"
            elif command == 4 and game_state['weapons']['torpedoes'] > 0:
                game_state['weapons']['torpedoes'] -= 1
                damage = random.randint(30, 100)
                output += f"FIRED TORPEDO. DAMAGE: {damage}\n"
            elif command == 5 and game_state['weapons']['field'] > 0:
                game_state['weapons']['field'] -= 1
                output += "ACTIVATED HYPERON NEUTRALIZATION FIELD.\n"
            elif command == 6:
                output += "CHANGE VELOCITY. ENTER NEW VELOCITY:\n"
                game_state['step'] = 'change_velocity'
            elif command == 7:
                output += "DISENGAGED FROM BATTLE.\n"
                game_state['step'] = 'start'
            else:
                output += "INVALID COMMAND OR NO WEAPONS LEFT.\n"

            if game_state['step'] == 'battle_actions':
                game_state['range'] -= game_state['relative_velocity']
                output += f"RANGE TO TARGET: {game_state['range']} KM\n"
                output += f"RELATIVE VELOCITY: {game_state['relative_velocity']} KM/S\n"
                output += "ENTER COMMAND (1: FIRE PHASERS, 2: FIRE MISSILE, 3: FIRE LANCE, 4: FIRE TORPEDO, 5: ACTIVATE FIELD, 6: CHANGE VELOCITY, 7: DISENGAGE):\n"

    elif game_state['step'] == 'change_velocity':
        if user_input:
            new_velocity = int(user_input)
            game_state['relative_velocity'] = new_velocity
            output += f"NEW VELOCITY SET TO: {game_state['relative_velocity']} KM/S\n"
            game_state['step'] = 'battle_actions'
            output += "ENTER COMMAND (1: FIRE PHASERS, 2: FIRE MISSILE, 3: FIRE LANCE, 4: FIRE TORPEDO, 5: ACTIVATE FIELD, 6: CHANGE VELOCITY, 7: DISENGAGE):\n"

    game_state['output'] = output
    return output
