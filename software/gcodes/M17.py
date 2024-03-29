'''
GCode M17
Enable steppers

Author: Mathieu Monney
email: zittix(at)xwaves(dot)net
Website: http://www.xwaves.net
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
'''

from GCodeCommand import GCodeCommand
from Stepper import Stepper

class M17(GCodeCommand):

    def execute(self,g):
        self.printer.path_planner.wait_until_done()
        for name, stepper in self.printer.steppers.iteritems():
            if self.printer.config.getboolean('Steppers', 'enabled_'+name):
                stepper.set_enabled()
        Stepper.commit()  

    def get_description(self):
        return "Power on and enable all steppers. Motors are active after this command."
