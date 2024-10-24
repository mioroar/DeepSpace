import subprocess


def process(command):
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )


def expect(proc, pattern):
    pattern = pattern.strip("\n")
    buffer = ""
    while True:
        buffer += proc.stdout.read(1).decode()
        if pattern.endswith(buffer):
            return True
        else:
            print(False)


def write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    proc.stdin.flush()
    return text


def test_greeting():
    print("Launching processes")
    # Запускаем BASIC и Python версии игры
    try:
        bas = process('deepspaceSOURCE.bas')
        py = process('python deepspace.py')

        # Ожидаемое приветственное сообщение
        expected_greeting = '''
                        DEEPSPACE                                  
                    CREATIVE COMPUTING                             
                  MORRISTOWN, NEW JERSEY                           


THIS IS DEEPSPACE, A TACTICAL SIMULATION OF SHIP TO SHIP
COMBAT IN DEEP SPACE.
DO YOU WISH INSTRUCTIONS? '''
        instruction = '''
YOU ARE ONE OF A GROUP OF CAPTAINS ASSIGNED TO PATROL A
SECTION OF YOUR STAR EMPIRE'S BORDER AGAINST HOSTILE
ALIENS. ALL YOUR ENCOUNTERS HERE WILL BE AGAINST HOSTILE
VESSELS. YOU WILL FIRST BE REQUIRED TO SELECT A VESSEL
FROM ONE OF THREE TYPES, EACH WITH ITS OWN CHARACTERISTICS:

TYPE        SPEED   CARGO SPACE   PROTECTION
1 SCOUT      10X     16            1
2 CRUISER    4X      24            2
3 BATTLESHIP 2X      30            5

SPEED IS GIVEN RELATIVE TO THE OTHER SHIPS.
CARGO SPACE IS IN UNITS OF SPACE ABOARD SHIP WHICH CAN BE
FILLED WITH WEAPONS.
PROTECTION IS THE RELATIVE STRENGTH OF THE SHIP'S ARMOR
AND FORCE FIELDS.

ONCE A SHIP HAS BEEN SELECTED, YOU WILL BE INSTRUCTED TO ARM
IT WITH WEAPONRY FROM THE FOLLOWING LIST:

TYPE                         CARGO SPACE    REL. STRENGTH
1 PHASER BANKS                   12                4
2 ANTI-MATTER MISSILE             4               20
3 HYPERSPACE LANCE                4               16
4 PHOTON TORPEDO                  2               10
5 HYPERON NEUTRALIZATION FIELD   20                6

WEAPONS #1 & #5 CAN BE FIRED 100 TIMES EACH; ALL OTHERS CAN
BE FIRED ONCE FOR EACH ON BOARD.
A TYPICAL LOAD FOR A CRUISER MIGHT CONSIST OF:
          1-#1 PHASER BANK          = 12
          2-#3 HYPERSPACE LANCES    =  8
          2-#4 PHOTON TORPEDOES     =  4
                                  ---------
                                      24 UNITS OF CARGO
 A WORD OF CAUTION: FIRING HIGH YIELD WEAPONS AT CLOSE (<100)
RANGE CAN BE DANGEROUS TO YOUR SHIP AND MINIMAL DAMAGE CAN
OCCUR AS FAR OUT AS 200 IN SOME CIRCUMSTANCES.

RANGE IS GIVEN IN THOUSANDS OF KILOMETERS.

YOU HAVE A CHOICE OF THREE SYSTEMS TO PATROL.
1 ORION
2 DENEB
3 ARCTURUS
SELECT A SYSTEM(1-3): 
'''
        choose_ship = '''WHICH SPACECRAFT WOULD YOU LIKE(1-3) '''
        cargo = '''YOU HAVE  30 UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.
CHOOSE A WEAPON AND THE AMOUNT YOU WISH. '''

        # Приветствие
        print("Expecting greetings...")
        expect(bas, expected_greeting)
        expect(py, expected_greeting)
        print("TEST 1 - PASS")
        # инструкции
        print("TEST send yes to inst")
        write(bas, "Y")
        write(py, "Y")
        expect(bas, instruction)
        expect(py, instruction)
        print("TEST 2 - PASS")
        # выбор системы
        print("TEST choose system")
        write(bas, "2")
        write(py, "2")
        expect(bas, choose_ship)
        expect(py, choose_ship)
        print("TEST 3 - PASS")

        # Выбор корабля
        print("TEST choose ship")
        write(bas, "3")  # Выбор battleship
        write(py, "3")
        expect(bas, cargo)
        expect(py, cargo)
        print("TEST 4 - PASS")

        # Выбор оружия
        print("TEST choose weapons")
        write(bas, "1 1")  # Выбор Phaser Banks на 12 единиц
        write(py, "1 1")
        expect(bas, "YOU HAVE  18 UNITS OF CARGO SPACE TO FILL WITH WEAPONRY."
                    "CHOOSE A WEAPON AND THE AMOUNT YOU WISH. ")
        expect(py, "YOU HAVE  18 UNITS OF CARGO SPACE TO FILL WITH WEAPONRY."
                   "CHOOSE A WEAPON AND THE AMOUNT YOU WISH. ")
        print("TEST 5 - PASS")

        write(bas, "2 4")  # Выбор Anti-Matter Missiles на 16 единиц
        write(py, "2 4")
        expect(bas, "YOU HAVE  2 UNITS OF CARGO SPACE TO FILL WITH WEAPONRY."
                    "CHOOSE A WEAPON AND THE AMOUNT YOU WISH. ")
        expect(py, "YOU HAVE  2 UNITS OF CARGO SPACE TO FILL WITH WEAPONRY."
                   "CHOOSE A WEAPON AND THE AMOUNT YOU WISH. ")
        print("TEST 6 - PASS")

        write(bas, "4 1")  # Выбор Photon Torpedoes на 2 единицы
        write(py, "4 1")
        expect(bas, "RANGE TO TARGET: 500"
                    "RELATIVE VELOCITY: 0"
                    "ACTION ")
        expect(py, "RANGE TO TARGET: 500"
                   "RELATIVE VELOCITY: 0"
                   "ACTION ")
        write(bas, 6)  # Завершение выбора
        write(py, 6)
        expect(bas, "SELF DESTRUCT FAILSAFE ACTIVATED!!"
                    "INPUT 1 TO RELEASE FAILSAFE ")
        expect(py, "SELF DESTRUCT FAILSAFE ACTIVATED!!"
                   "INPUT 1 TO RELEASE FAILSAFE ")
        print("TEST 7 - PASS")

    except Exception as ex:
        print(ex)


test_greeting()
