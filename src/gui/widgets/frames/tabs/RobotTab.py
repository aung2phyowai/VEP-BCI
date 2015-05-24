__author__ = 'Anti'

from gui.widgets.frames.tabs import DisableDeleteNotebookTab
from gui.widgets.frames import Frame
from gui.widgets import Buttons, OptionMenu
import constants as c


class RobotTab(DisableDeleteNotebookTab.Disable):
    def __init__(self, parent, sendMessage, **kwargs):
        Frame.Frame.__init__(self, parent, c.ROBOT_TAB, 0, 0, **kwargs)
        self.addChildWidgets((
            OptionMenu.TargetChoosingMenu(self.widget, c.ROBOT_OPTION_FORWARD, 0, 1, (c.ROBOT_NONE,)),
            OptionMenu.TargetChoosingMenu(self.widget, c.ROBOT_OPTION_BACKWARD, 1, 1, (c.ROBOT_NONE,)),
            OptionMenu.TargetChoosingMenu(self.widget, c.ROBOT_OPTION_RIGHT, 2, 1, (c.ROBOT_NONE,)),
            OptionMenu.TargetChoosingMenu(self.widget, c.ROBOT_OPTION_LEFT, 3, 1, (c.ROBOT_NONE,)),
            OptionMenu.TargetChoosingMenu(self.widget, c.ROBOT_OPTION_STOP, 4, 1, (c.ROBOT_NONE,)),
            Buttons.Button(self.widget, c.ROBOT_TEST, 0, 3, command=lambda: sendMessage(c.MOVE_FORWARD)),
            Buttons.Button(self.widget, c.ROBOT_TEST, 1, 3, command=lambda: sendMessage(c.MOVE_BACKWARD)),
            Buttons.Button(self.widget, c.ROBOT_TEST, 2, 3, command=lambda: sendMessage(c.MOVE_RIGHT)),
            Buttons.Button(self.widget, c.ROBOT_TEST, 3, 3, command=lambda: sendMessage(c.MOVE_LEFT)),
            Buttons.Button(self.widget, c.ROBOT_TEST, 4, 3, command=lambda: sendMessage(c.MOVE_STOP)),
            self.getDisableButton(5, 0)
        ))
