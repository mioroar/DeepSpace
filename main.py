import random
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class ConsoleWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsoleWidget, self).__init__(**kwargs)
        self.orientation = "vertical"

        # Поле для вывода (консоль)
        self.output = TextInput(readonly=True, font_size=14, size_hint_y=0.9)
        self.add_widget(self.output)

        # Поле для ввода
        self.input = TextInput(multiline=False, font_size=14, size_hint_y=0.1)
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

        self.input_disabled = True
        self.input.disabled = True
        self.input_callback = None

    def write(self, text):
        Clock.schedule_once(lambda dt: self._update_output(text))

    def _update_output(self, text):
        self.output.text += text

    def flush(self):
        pass

    def on_enter(self, instance):
        if not self.input_disabled and self.input_callback:
            input_text = self.input.text
            self.input.text = ""
            self.disable_input()
            self.input_callback(input_text)

    def enable_input(self, callback):
        self.input_disabled = False
        self.input.disabled = False
        self.input_callback = callback

    def disable_input(self):
        self.input_disabled = True
        self.input.disabled = True


class DeepSpaceGame(App):
    def build(self):
        self.console = ConsoleWidget()
        self.state = "start"
        self.vars = {}
        self.main()
        return self.console

    def main(self):
        self.console.write(
            " " * 24
            + "DEEPSPACE\n"
            + " " * 20
            + "CREATIVE COMPUTING\n"
            + " " * 18
            + "MORRISTOWN, NEW JERSEY\n\n\n"
            + "THIS IS DEEPSPACE, A TACTICAL"
            " SIMULATION OF SHIP TO SHIP\n"
            + "COMBAT IN DEEP SPACE.\n"
            + "DO YOU WISH INSTRUCTIONS? "
        )
        self.state = "instructions"
        self.console.enable_input(self.on_enter)

    def on_enter(self, text):
        text = text.upper()
        if self.state == "instructions":
            self.process_instructions(text)
        elif self.state == "select_system":
            self.process_select_system(text)
        elif self.state == "select_spacecraft":
            self.process_select_spacecraft(text)
        elif self.state == "load_weapons":
            self.process_load_weapons(text)
        elif self.state == "combat":
            self.process_combat(text)
        elif self.state == "self_destruct":
            self.process_self_destruct(text)
        elif self.state == "change_velocity":
            self.process_change_velocity(text)

    def process_instructions(self, text):
        if text != "NO":
            self.console.write(
                "YOU ARE ONE OF A GROUP OF CAPTAINS "
                "ASSIGNED TO PATROL A\n" + "SECTION OF "
                                           "YOUR STAR EMPIRE'S BORDER "
                "AGAINST HOSTILE\n" + "ALIENS. ALL "
                                      "YOUR ENCOUNTERS HERE WILL "
                "BE AGAINST HOSTILE\n" + "VESSELS. "
                                         "YOU WILL FIRST BE REQUIRED TO "
                "SELECT A VESSEL\n" + "FROM ONE OF "
                                      "THREE TYPES, EACH WITH ITS "
                "OWN CHARACTERISTICS:\n"
                + "\nTYPE        SPEED   CARGO SPACE   PROTECTION\n"
                + "1 SCOUT      10X     16            1\n"
                + "2 CRUISER    4X      24            2\n"
                + "3 BATTLESHIP 2X      30            5\n"
                + "\nSPEED IS GIVEN RELATIVE TO THE OTHER SHIPS.\n"
                + "CARGO SPACE IS IN UNITS OF "
                "SPACE ABOARD SHIP WHICH CAN BE\n"
                + "FILLED WITH WEAPONS.\n"
                + "PROTECTION IS "
                "THE RELATIVE STRENGTH OF THE SHIP'S ARMOR\n"
                + "AND FORCE FIELDS.\n"
                + "\nONCE A SHIP HAS BEEN SELECTED,"
                " YOU WILL BE INSTRUCTED TO ARM\n"
                + "IT WITH WEAPONRY FROM THE FOLLOWING LIST:\n\n"
                + "TYPE                        CARGO SPACE    REL. STRENGTH\n"
                + "1 PHASER BANKS                  12                4\n"
                + "2 ANTI-MATTER MISSILE            4               20\n"
                + "3 HYPERSPACE LANCE               4               16\n"
                + "4 PHOTON TORPEDO                 2               10\n"
                + "5 HYPERON NEUTRALIZATION FIELD   20               6\n"
                + "\nWEAPONS #1 & #5 CAN BE FIRED 100 TIMES EACH;"
                " ALL OTHERS CAN\n"
                + "BE FIRED ONCE FOR EACH ON BOARD.\n"
                + "A TYPICAL LOAD FOR A CRUISER MIGHT CONSIST OF:\n"
                + "          1-#1 PHASER BANK          = 12\n"
                + "          2-#3 HYPERSPACE LANCES    =  8\n"
                + "          2-#4 PHOTON TORPEDOES     =  4\n"
                + "                                  ---------\n"
                + "                           24 UNITS OF CARGO\n"
                + " A WORD OF CAUTION: "
                  "FIRING HIGH YIELD WEAPONS AT CLOSE (<100)\n"
                + "RANGE CAN BE DANGEROUS "
                  "TO YOUR SHIP AND MINIMAL DAMAGE CAN\n"
                + "OCCUR AS FAR OUT "
                  "AS 200 IN SOME CIRCUMSTANCES.\n"
                + "\nRANGE IS GIVEN IN THOUSANDS OF KILOMETERS.\n"
            )

        self.console.write(
            "\nYOU HAVE A CHOICE OF"
            " THREE SYSTEMS TO PATROL.\n"
            + "1 ORION\n"
            + "2 DENEB\n"
            + "3 ARCTURUS\n"
            + "SELECT A SYSTEM(1-3): "
        )
        self.state = "select_system"
        self.console.enable_input(self.on_enter)

    def process_select_system(self, text):
        s9 = int(text)
        if s9 == 1:
            e1, e2, e3, e4 = 150, 500, 3, 4
        elif s9 == 2:
            e1, e2, e3, e4 = 200, 350, 4, 3
        else:
            e1, e2, e3, e4 = 150, 400, 5, 2
        self.vars.update(
            {
                "e1": e1,
                "e2": e2,
                "e3": e3,
                "e4": e4,
                "d0": 0,
                "d1": 0,
                "n1": 0,
                "n2": 0,
                "n3": 0,
                "n4": 0,
                "d": 0,
            }
        )
        self.console.write("WHICH SPACECRAFT"
                           " WOULD YOU LIKE(1-3)? ")
        self.state = "select_spacecraft"
        self.console.enable_input(self.on_enter)

    def process_select_spacecraft(self, text):
        s = int(text)
        if s == 1:
            s0, c0, p0 = 10, 16, 1
        elif s == 2:
            s0, c0, p0 = 4, 24, 2
        else:
            s0, c0, p0 = 2, 30, 5
        self.vars.update({"s0": s0, "c0": c0, "p0": p0, "c": c0})
        self.console.write(
            f"YOU HAVE {self.vars['c']} UNITS "
            f"OF CARGO SPACE TO FILL WITH WEAPONRY.\n"
            f"CHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
        )
        self.state = "load_weapons"
        self.console.enable_input(self.on_enter)

    def process_load_weapons(self, text):
        try:
            w, n = map(int, text.split())
        except ValueError:
            self.console.write(
                "INVALID INPUT. RESELECT.\n" 
                "CHOOSE A WEAPON AND THE AMOUNT YOU WISH: "
            )
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
        if n * c1 > self.vars["c"]:
            self.console.write(
                f"NOT ENOUGH SPACE. YOU HAVE {self.vars['c']} "
                f"UNITS REMAINING.\nCHOOSE AGAIN: "
            )
            return
        self.vars["c"] -= n * c1
        self.vars[f"n{w}"] += n
        if self.vars["c"] > 0:
            self.console.write(
                f"YOU HAVE {self.vars['c']} UNITS OF CARGO"
                f" SPACE REMAINING. CHOOSE AGAIN: "
            )
        else:
            s1 = self.vars["s0"] * random.random()
            r = (3 * random.random() + 5) * 100
            self.vars.update({"s1": s1, "r": r})
            self.console.write(
                f"\nRANGE TO TARGET: {r}\n" 
                f"RELATIVE VELOCITY: {s1}\nACTION: "
            )
            self.state = "combat"
            self.console.enable_input(self.on_enter)


if __name__ == "__main__":
    DeepSpaceGame().run()
