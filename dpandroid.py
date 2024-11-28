import random
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DeepSpaceGame(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.output_label = TextInput(size_hint_y=0.9, multiline=True, readonly=True)
        self.input_field = TextInput(size_hint_y=0.1, multiline=False)
        self.input_field.bind(on_text_validate=self.on_enter)
        self.layout.add_widget(self.output_label)
        self.layout.add_widget(self.input_field)
        self.state = 'start'
        self.vars = {}
        self.deepspace_game()
        return self.layout

    def deepspace_game(self):
        self.output_label.text = (" " * 24 + "DEEPSPACE\n" +
                                  " " * 20 + "CREATIVE COMPUTING\n" +
                                  " " * 18 + "MORRISTOWN, NEW JERSEY\n\n\n" +
                                  "THIS IS DEEPSPACE, A TACTICAL SIMULATION OF SHIP TO SHIP\n" +
                                  "COMBAT IN DEEP SPACE.\n" +
                                  "DO YOU WISH INSTRUCTIONS? ")
        self.state = 'instructions'

    def on_enter(self, instance):
        text = self.input_field.text.upper()
        self.input_field.text = ''
        if self.state == 'instructions':
            if text != "NO":
                self.output_label.text += ("YOU ARE ONE OF A GROUP OF CAPTAINS ASSIGNED TO PATROL A\n" +
                                           "SECTION OF YOUR STAR EMPIRE'S BORDER AGAINST HOSTILE\n" +
                                           "ALIENS. ALL YOUR ENCOUNTERS HERE WILL BE AGAINST HOSTILE\n" +
                                           "VESSELS. YOU WILL FIRST BE REQUIRED TO SELECT A VESSEL\n" +
                                           "FROM ONE OF THREE TYPES, EACH WITH ITS OWN CHARACTERISTICS:\n" +
                                           "\nTYPE        SPEED   CARGO SPACE   PROTECTION\n" +
                                           "1 SCOUT      10X     16            1\n" +
                                           "2 CRUISER    4X      24            2\n" +
                                           "3 BATTLESHIP 2X      30            5\n" +
                                           "\nSPEED IS GIVEN RELATIVE TO THE OTHER SHIPS.\n" +
                                           "CARGO SPACE IS IN UNITS OF SPACE ABOARD SHIP WHICH CAN BE\n" +
                                           "FILLED WITH WEAPONS.\n" +
                                           "PROTECTION IS THE RELATIVE STRENGTH OF THE SHIP'S ARMOR\n" +
                                           "AND FORCE FIELDS.\n" +
                                           "\nONCE A SHIP HAS BEEN SELECTED, YOU WILL BE INSTRUCTED TO ARM\n" +
                                           "IT WITH WEAPONRY FROM THE FOLLOWING LIST:\n\n" +
                                           "TYPE                         CARGO SPACE    REL. STRENGTH\n" +
                                           "1 PHASER BANKS                   12                4\n" +
                                           "2 ANTI-MATTER MISSILE             4               20\n" +
                                           "3 HYPERSPACE LANCE                4               16\n" +
                                           "4 PHOTON TORPEDO                  2               10\n" +
                                           "5 HYPERON NEUTRALIZATION FIELD   20                6\n" +
                                           "\nWEAPONS #1 & #5 CAN BE FIRED 100 TIMES EACH; ALL OTHERS CAN\n" +
                                           "BE FIRED ONCE FOR EACH ON BOARD.\n" +
                                           "A TYPICAL LOAD FOR A CRUISER MIGHT CONSIST OF:\n" +
                                           "          1-#1 PHASER BANK          = 12\n" +
                                           "          2-#3 HYPERSPACE LANCES    =  8\n" +
                                           "          2-#4 PHOTON TORPEDOES     =  4\n" +
                                           "                                  ---------\n" +
                                           "                                      24 UNITS OF CARGO\n" +
                                           " A WORD OF CAUTION: FIRING HIGH YIELD WEAPONS AT CLOSE (<100)\n" +
                                           "RANGE CAN BE DANGEROUS TO YOUR SHIP AND MINIMAL DAMAGE CAN\n" +
                                           "OCCUR AS FAR OUT AS 200 IN SOME CIRCUMSTANCES.\n" +
                                           "\nRANGE IS GIVEN IN THOUSANDS OF KILOMETERS.\n")
            else:
                self.output_label.text += "DO YOU WISH A MANUEVER CHART? "
                self.state = 'maneuver_chart'
                return
            self.output_label.text += ("\nYOU HAVE A CHOICE OF THREE SYSTEMS TO PATROL.\n" +
                                       "1 ORION\n" +
                                       "2 DENEB\n" +
                                       "3 ARCTURUS\n" +
                                       "SELECT A SYSTEM(1-3): ")
            self.state = 'select_system'
        elif self.state == 'maneuver_chart':
            if text != "NO":
                self.output_label.text += ("     **************\n" +
                                           "     MANUEVER CHART\n\n" +
                                           " 1      FIRE PHASERS\n" +
                                           " 2      FIRE ANTI-MATTER MISSILE\n" +
                                           " 3      FIRE HYPERSPACE LANCE\n" +
                                           " 4      FIRE PHOTON TORPEDO\n" +
                                           " 5      ACTIVE HYPERON NEUTRALIZATION FIELD\n" +
                                           " 6      SELF-DESTRUCT\n" +
                                           " 7      CHANGE VELOCITY\n" +
                                           " 8      DISENGAGE\n" +
                                           " 9      PROCEED\n")
            self.output_label.text += ("\nYOU HAVE A CHOICE OF THREE SYSTEMS TO PATROL.\n" +
                                       "1 ORION\n" +
                                       "2 DENEB\n" +
                                       "3 ARCTURUS\n" +
                                       "SELECT A SYSTEM(1-3): ")
            self.state = 'select_system'
        elif self.state == 'select_system':
            s9 = int(text)
            if s9 == 1:
                e1, e2, e3, e4 = 150, 500, 3, 4
            elif s9 == 2:
                e1, e2, e3, e4 = 200, 350, 4, 3
            else:
                e1, e2, e3, e4 = 150, 400, 5, 2
            self.vars.update({'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'd0': 0, 'd1': 0, 'n1': 0, 'n2': 0, 'n3': 0, 'n4': 0, 'd': 0})
            self.output_label.text += "WHICH SPACECRAFT WOULD YOU LIKE(1-3)? "
            self.state = 'select_spacecraft'
        elif self.state == 'select_spacecraft':
            s = int(text)
            if s == 1:
                s0, c0, p0 = 10, 16, 1
            elif s == 2:
                s0, c0, p0 = 4, 24, 2
            else:
                s0, c0, p0 = 2, 30, 5
            self.vars.update({'s0': s0, 'c0': c0, 'p0': p0, 'c': c0})
            self.output_label.text += f"YOU HAVE {self.vars['c']} UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.\nCHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
            self.state = 'load_weapons'
        elif self.state == 'load_weapons':
            try:
                w, n = map(int, text.split())
            except ValueError:
                self.output_label.text += "INVALID INPUT. RESELECT.\nCHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
                return
            c1 = 0
            if w == 1:
                c1 = 12
            elif w in [2, 3]:
                c1 = 4
            elif w == 4:
                c1 = 2
            elif w == 5:
                c1 = 20
                n = 100
            if n * c1 > self.vars['c']:
                self.output_label.text += "NOT ENOUGH SPACE. RESELECT\n"
                self.output_label.text += f"YOU HAVE {self.vars['c']} UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.\nCHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
                return
            self.vars['c'] -= n * c1
            if w == 1:
                self.vars['n1'] += n
            elif w == 2:
                self.vars['n2'] += n
            elif w == 3:
                self.vars['n3'] += n
            elif w == 4:
                self.vars['n4'] += n
            elif w == 5:
                self.vars['n5'] = n
            if self.vars['c'] > 1:
                self.output_label.text += f"YOU HAVE {self.vars['c']} UNITS OF CARGO SPACE TO FILL WITH WEAPONRY.\nCHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
            else:
                s1 = self.vars['s0'] * random.random()
                r = (3 * random.random() + 5) * 100
                self.vars.update({'s1': s1, 'r': r})
                self.output_label.text += f"\nRANGE TO TARGET: {r}\nRELATIVE VELOCITY: {s1}\nACTION: "
                self.state = 'combat'
        elif self.state == 'combat':
            m = int(text)
            self.vars['m'] = m
            if m == 6:
                self.output_label.text += "SELF DESTRUCT FAILSAFE ACTIVATED!!\nINPUT 1 TO RELEASE FAILSAFE: "
                self.state = 'self_destruct'
            elif m == 7:
                self.output_label.text += "CHANGE TO BE EFFECTED: "
                self.state = 'change_velocity'
            elif m == 8:
                self.output_label.text += "TRY AGAIN LATER!\n"
                self.stop()
            elif m == 9:
                if self.vars['r'] < 500:
                    self.vars['d0'] = 0
                if self.vars['s1'] > 0:
                    self.vars['r'] -= (self.vars['s1'] * 8.3) ** 1.25
                else:
                    self.vars['r'] += (self.vars['s1'] * 8.3) ** 1.25
                if self.vars['r'] > 1500:
                    self.output_label.text += "OUT OF SENSOR RANGE. AUTOMATIC DISENGAGE.\n"
                    self.stop()
                elif self.vars['r'] < 0:
                    self.vars['r'] = -self.vars['r']
                self.output_label.text += f"\nRANGE TO TARGET: {self.vars['r']}\nRELATIVE VELOCITY: {self.vars['s1']}\nACTION: "
            else:
                self.process_weapon_action()
        elif self.state == 'self_destruct':
            u = int(text)
            if u == 1:
                self.output_label.text += "SELF DESTRUCT ACCOMPLISHED\n"
                if self.vars['r'] <= 60:
                    self.output_label.text += "ENEMY VESSEL ALSO DESTROYED\n"
                else:
                    d4 = 3200 / self.vars['r']
                    self.vars['d'] += d4
                    if self.vars['d'] > 99:
                        self.output_label.text += "ENEMY VESSEL ALSO DESTROYED\n"
                    else:
                        self.output_label.text += f"ENEMY VESSEL SURVIVES WITH {self.vars['d']} DAMAGE\n"
                self.stop()
            else:
                self.output_label.text += "SELF DESTRUCT ABORTED\nACTION: "
                self.state = 'combat'
        elif self.state == 'change_velocity':
            s2 = float(text)
            if self.vars['s1'] + s2 > self.vars['s0']:
                self.output_label.text += "CHANGE BEYOND MAXIMUM POSSIBLE\nINCREASING TO MAXIMUM\n"
                self.vars['s1'] = self.vars['s0']
            else:
                self.vars['s1'] += s2
            self.output_label.text += f"\nRANGE TO TARGET: {self.vars['r']}\nRELATIVE VELOCITY: {self.vars['s1']}\nACTION: "
            self.state = 'combat'
        elif self.state == 'another_battle':
            if text.upper() != "YES":
                self.output_label.text += "TRY AGAIN LATER!\n"
                self.stop()
            else:
                self.deepspace_game()
        else:
            self.process_weapon_action()

    def process_weapon_action(self):
        m = self.vars['m']
        n1 = self.vars.get('n1', 0)
        n2 = self.vars.get('n2', 0)
        n3 = self.vars.get('n3', 0)
        n4 = self.vars.get('n4', 0)
        n5 = self.vars.get('n5', 0)
        z = p1 = 0
        if m == 1:
            if n1 == 0:
                self.output_label.text += "PHASER BANKS DRAINED\nSELECT ANOTHER COURSE OF ACTION\nACTION: "
                return
            self.vars['n1'] -= 1
            z, p1 = 200, 4
        elif m == 2:
            if n2 == 0:
                self.output_label.text += "ALL ANTI-MATTER MISSILES EXPENDED\nSELECT ANOTHER COURSE OF ACTION\nACTION: "
                return
            self.vars['n2'] -= 1
            z, p1 = 500, 20
        elif m == 3:
            if n3 == 0:
                self.output_label.text += "ALL HYPERSPACE LANCES EXPENDED\nSELECT ANOTHER COURSE OF ACTION\nACTION: "
                return
            self.vars['n3'] -= 1
            z, p1 = 550, 16
        elif m == 4:
            if n4 == 0:
                self.output_label.text += "ALL PHOTON TORPEDO TUBES EMPTY\nSELECT ANOTHER COURSE OF ACTION\nACTION: "
                return
            self.vars['n4'] -= 1
            z, p1 = 400, 10
        elif m == 5:
            if n5 == 0:
                self.output_label.text += "HYPERON NEUTRALIZATION FIELD DRAINED\nSELECT ANOTHER COURSE OF ACTION\nACTION: "
                return
            self.vars['n5'] -= 1
            z, p1 = 250, 6
        f0 = p1 * (z / self.vars['r']) ** 1.5
        d0 = (2 * f0 + 3 * f0 * random.random()) / 5
        self.vars['d0'] = d0
        self.vars['d'] += d0
        self.output_label.text += f"SCANNERS REPORT ENEMY DAMAGE NOW: {self.vars['d']}\n"
        if self.vars['d'] > 99:
            self.output_label.text += "ENEMY VESSEL DESTROYED\n"
            self.stop()
            return
        e1 = self.vars['e1']
        e2 = self.vars['e2']
        e3 = self.vars['e3']
        e4 = self.vars['e4']
        p0 = self.vars['p0']
        z = z  # Use same z as above
        k = e1 + e2 * random.random()
        e = e3 + e4 * random.random() + 5 / p0 * random.random()
        f3 = e * (k / self.vars['r']) ** 1.85
        d2 = (3 * f3 + 3 * f3 * random.random()) / 5.5
        self.vars['d1'] += d2
        if (z * d0) / (self.vars['r'] * 500) > 2.2:
            d3 = d0 * 2 / (self.vars['r'] * 2 * p0)
            self.vars['d1'] += d3
        self.output_label.text += f"DAMAGE CONTROL REPORTS YOUR VESSEL DAMAGE AT: {self.vars['d1']}\n"
        if self.vars['d1'] > 99:
            self.output_label.text += "YOUR VESSEL HAS BEEN DESTROYED\n"
            self.stop()
            return
        self.output_label.text += f"\nRANGE TO TARGET: {self.vars['r']}\nRELATIVE VELOCITY: {self.vars['s1']}\nACTION: "
        self.state = 'combat'

if __name__ == "__main__":
    DeepSpaceGame().run()
