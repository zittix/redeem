'''
GCode G0 and G1
Controlling printer head position

Author: Mathieu Monney
email: zittix(at)xwaves(dot)net
Website: http://www.xwaves.net
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
'''

from GCodeCommand import GCodeCommand
from Path import Path, RelativePath, AbsolutePath

class G0(GCodeCommand):

    def execute(self,g):
        if g.has_letter("F"):                                    # Get the feed rate                 
            self.printer.feed_rate = float(g.get_value_by_letter("F"))/60000.0 # Convert from mm/min to SI unit m/s
            g.remove_token_by_letter("F")
        smds = {}                                               
        for i in range(g.num_tokens()):                          
            axis = g.token_letter(i)                             
            smds[axis] = float(g.token_value(i))/1000.0          # Get the value, new position or vector             
        if g.has_letter("E") and self.printer.current_tool != "E":       # We are using a different tool, switch..
            smds[self.printer.current_tool] = smds["E"]
            del smds["E"]
        if self.printer.movement == Path.ABSOLUTE:
            path = AbsolutePath(smds, self.printer.feed_rate, self.printer.path_planner.acceleration)
        elif self.printer.movement == Path.RELATIVE:
            path = RelativePath(smds, self.printer.feed_rate, self.printer.path_planner.acceleration)
        self.printer.path_planner.add_path(path)                        # Add the path. This blocks until the path planner has capacity


    def get_description(self):
        return "Control the printer head position as well as the currently selected tool."


class G1(G0):
    pass

