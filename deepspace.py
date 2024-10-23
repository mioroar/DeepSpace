import random

def deepspace_battle():
    print(" " * 24 + "DEEPSPACE")
    print(" " * 20 + "CREATIVE COMPUTING")
    print(" " * 18 + "MORRISTOWN NEW JERSEY\n\n\n")
    print("THIS IS DEEPSPACE, A TACTICAL SIMULATION OF SHIP TO SHIP")
    print("COMBAT IN DEEP SPACE.")
    print("DO YOU WISH INSTRUCTIONS?")
    # i = input("DO YOU WISH INSTRUCTIONS? ")
    i = input()
    if i.upper() != "NO":
        print("YOU ARE ONE OF A GROUP OF CAPTAINS ASSIGNED TO PATROL A")
        print("SECTION OF YOUR STAR EMPIRE'S BORDER AGAINST HOSTILE")
        print("ALIENS. ALL YOUR ENCOUNTERS HERE WILL BE AGAINST HOSTILE")
        print("VESSELS. YOU WILL FIRST BE REQUIRED TO SELECT A VESSEL")
        print("FROM ONE OF THREE TYPES, EACH WITH ITS OWN CHARACTERISTICS:")
        print("\nTYPE        SPEED   CARGO SPACE   PROTECTION")
        print("1 SCOUT      10X     16            1")
        print("2 CRUISER    4X      24            2")
        print("3 BATTLESHIP 2X      30            5")
        print("\nSPEED IS GIVEN RELATIVE TO THE OTHER SHIPS.")
        print("CARGO SPACE IS IN UNITS OF SPACE ABOARD SHIP WHICH CAN BE")
        print("FILLED WITH WEAPONS.")
        print("PROTECTION IS THE RELATIVE STRENGTH OF THE SHIP'S ARMOR")
        print("AND FORCE FIELDS.")
        print("\nONCE A SHIP HAS BEEN SELECTED, YOU WILL BE INSTRUCTED TO ARM")
        print("IT WITH WEAPONRY FROM THE FOLLOWING LIST:")
        print()
        print("TYPE                         CARGO SPACE    REL. STRENGTH")
        print("1 PHASER BANKS                   12                4")
        print("2 ANTI-MATTER MISSILE             4               20")
        print("3 HYPERSPACE LANCE                4               16")
        print("4 PHOTON TORPEDO                  2               10")
        print("5 HYPERON NEUTRALIZATION FIELD   20                6")
        print("\nWEAPONS #1 & #5 CAN BE FIRED 100 TIMES EACH; ALL OTHERS CAN")
        print("BE FIRED ONCE FOR EACH ON BOARD.")
        print("A TYPICAL LOAD FOR A CRUISER MIGHT CONSIST OF:")
        print("          1-#1 PHASER BANK          = 12")
        print("          2-#3 HYPERSPACE LANCES    =  8")
        print("          2-#4 PHOTON TORPEDOES     =  4")
        print("                                  ---------")
        print("                                      24 UNITS OF CARGO")
        print(" A WORD OF CAUTION: FIRING HIGH YIELD WEAPONS AT CLOSE (<100)")
        print("RANGE CAN BE DANGEROUS TO YOUR SHIP AND MINIMAL DAMAGE CAN")
        print("OCCUR AS FAR OUT AS 200 IN SOME CIRCUMSTANCES.")
        print("\nRANGE IS GIVEN IN THOUSANDS OF KILOMETERS.")
    else:
        m = input("DO YOU WISH A MANUEVER CHART? ")
        if m.upper() != "NO":
            print("     **************")
            print("     MANUEVER CHART\n")
            print(" 1      FIRE PHASERS")
            print(" 2      FIRE ANTI-MATTER MISSILE")
            print(" 3      FIRE HYPERSPACE LANCE")
            print(" 4      FIRE PHOTON TORPEDO")
            print(" 5      ACTIVE HYPERON NEUTRALIZATION FIELD")
            print(" 6      SELF-DESTRUCT")
            print(" 7      CHANGE VELOCITY")
            print(" 8      DISENGAGE")
            print(" 9      PROCEED")

    print("\nYOU HAVE A CHOICE OF THREE SYSTEMS TO PATROL.")
    print("1 ORION")
    print("2 DENEB")
    print("3 ARCTURUS")
    s9 = int(input("SELECT A SYSTEM(1-3): "))

    if s9 == 1:
        e1, e2, e3, e4 = 150, 500, 3, 4
    elif s9 == 2:
        e1, e2, e3, e4 = 200, 350, 4, 3
    else:
        e1, e2, e3, e4 = 150, 400, 5, 2

    d0 = d1 = n1 = n2 = n3 = n4 = d = 0

    while True:
        s = int(input("WHICH SPACECRAFT WOULD YOU LIKE(1-3)? "))
        if s in [1, 2, 3]:
            break

    if s == 1:
        s0, c0, p0 = 10, 16, 1
    elif s == 2:
        s0, c0, p0 = 4, 24, 2
    else:
        s0, c0, p0 = 2, 30, 5

    c = c0
    while c > 1:
        print(f"YOU HAVE {c} UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.")
        w, n = map(int, input("CHOOSE A WEAPON AND THE AMOUNT YOU WISH: ").split())

        if w == 1:
            c1 = 12
        elif w in [2, 3]:
            c1 = 4
        elif w == 4:
            c1 = 2
        elif w == 5:
            c1 = 20
            n = 100

        if n * c1 > c:
            print("NOT ENOUGH SPACE. RESELECT")
            continue

        c -= n * c1

        if w == 1:
            n1 += n
        elif w == 2:
            n2 += n
        elif w == 3:
            n3 += n
        elif w == 4:
            n4 += n
        elif w == 5:
            n5 = n

    s1 = s0 * random.random()
    r = (3 * random.random() + 5) * 100

    while True:
        print(f"\nRANGE TO TARGET: {r}")
        print(f"RELATIVE VELOCITY: {s1}")
        m = int(input("ACTION: "))

        if m == 6:
            print("SELF DESTRUCT FAILSAFE ACTIVATED!!")
            u = int(input("INPUT 1 TO RELEASE FAILSAFE: "))
            if u == 1:
                print("SELF DESTRUCT ACCOMPLISHED")
                if r <= 60:
                    print("ENEMY VESSEL ALSO DESTROYED")
                    break
                d4 = 3200 / r
                d += d4
                if d > 99:
                    print("ENEMY VESSEL ALSO DESTROYED")
                else:
                    print(f"ENEMY VESSEL SURVIVES WITH {d} DAMAGE")
                break
        elif m == 7:
            s2 = float(input("CHANGE TO BE EFFECTED: "))
            if s1 + s2 > s0:
                print("CHANGE BEYOND MAXIMUM POSSIBLE")
                print("INCREASING TO MAXIMUM")
                s1 = s0
            else:
                s1 += s2
        elif m == 8:
            break
        elif m == 9:
            if r < 500:
                d0 = 0
            if s1 > 0:
                r -= (s1 * 8.3) ** 1.25
            else:
                r += (s1 * 8.3) ** 1.25
            if r > 1500:
                print("OUT OF SENSOR RANGE. AUTOMATIC DISENGAGE.")
                break
            if r < 0:
                r = -r
        else:
            if m == 1:
                if n1 == 0:
                    print("PHASER BANKS DRAINED")
                    print("SELECT ANOTHER COURSE OF ACTION")
                    continue
                n1 -= 1
                z, p1 = 200, 4
            elif m == 2:
                if n2 == 0:
                    print("ALL ANTI-MATTER MISSILES EXPENDED")
                    print("SELECT ANOTHER COURSE OF ACTION")
                    continue
                n2 -= 1
                z, p1 = 500, 20
            elif m == 3:
                if n3 == 0:
                    print("ALL HYPERSPACE LANCES EXPENDED")
                    print("SELECT ANOTHER COURSE OF ACTION")
                    continue
                n3 -= 1
                z, p1 = 550, 16
            elif m == 4:
                if n4 == 0:
                    print("ALL PHOTON TORPEDO TUBES EMPTY")
                    print("SELECT ANOTHER COURSE OF ACTION")
                    continue
                n4 -= 1
                z, p1 = 400


if __name__ == "__main__":
    deepspace_battle()