'''
GCode M18 and M84
Disable all steppers

Author: Mathieu Monney
email: zittix(at)xwaves(dot)net
Website: http://www.xwaves.net
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
'''

from GCodeCommand import GCodeCommand
from Stepper import Stepper

class M18(GCodeCommand):

    def execute(self,g):
        self.printer.path_planner.wait_until_done()
        if g.num_tokens() == 0:
            g.set_tokens(["X", "Y", "Z", "E", "H"])         # If no token is present, do this for all
                                         # All steppers 
        for i in range(g.num_tokens()):                          # Run through all tokens
            axis = g.token_letter(i)                             # Get the axis, X, Y, Z or E
            self.printer.steppers[axis].set_disabled()

        Stepper.commit()  

    def get_description(self):
        return "Disable all steppers. No more current is applied to the stepper motors after this command."

class M84(M18):
	pass
