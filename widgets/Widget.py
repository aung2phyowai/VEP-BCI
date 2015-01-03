__author__ = 'Anti'

import Tkinter
import tkColorChooser


class Widget(object):
    def __init__(self, name, command, disabled_state, row, column, columnspan=1, padx=5, pady=5, command_on_load=True):
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.padx = padx
        self.pady = pady

        self.widget = None
        self.name = name
        self.command = command

        self.disabled_state = disabled_state
        self.enabled_state = Tkinter.NORMAL
        self.disabled = None
        self.command_on_load = command_on_load

    def createWidget(self, parent):
        raise NotImplementedError("createWidget not implemented!")

    def create(self, parent):
        self.widget = self.createWidget(parent)
        self.widget.grid(row=self.row, column=self.column, columnspan=self.columnspan, padx=self.padx, pady=self.pady)

    def loadDefaultValue(self):
        self.disabled = False
        if self.command is not None and self.command_on_load:
            self.command()

    def changeState(self):
        self.disabled = not self.disabled
        self.disable() if self.disabled else self.enable()

    def enable(self):
        self.widget.config(state=self.enabled_state)

    def disable(self):
        self.widget.config(state=self.disabled_state)


class WidgetWithVariable(Widget):
    def __init__(self, name, command, disabled_state, variable, default_value, row, column, columnspan=1, padx=5, pady=5, command_on_load=True):
        Widget.__init__(self, name, self.variablesCommand, disabled_state, row, column, columnspan, padx, pady, command_on_load)
        self.variable = variable
        self.default_value = default_value
        self.variables_command = command

    def loadDefaultValue(self):
        self.variable.set(self.default_value)
        Widget.loadDefaultValue(self)

    def variablesCommand(self):
        if self.variables_command is not None:
            self.variables_command(self.widget, self.variable)


class Textbox(Widget):
    def __init__(self, name, row, column, command=None, columnspan=1, padx=5, pady=5, width=5, default_value=0, command_on_load=True):
        Widget.__init__(self, name, self.validate, "readonly", row, column+1, columnspan, padx, pady, command_on_load)
        self.default_value = default_value
        self.width = width
        self.other_validation = command

    def loadDefaultValue(self):
        previous_state = self.widget.config("state")[4]
        self.widget.config(state=self.enabled_state)
        self.widget.delete(0, Tkinter.END)
        self.widget.insert(0, self.default_value)
        self.widget.config(state=previous_state)
        Widget.loadDefaultValue(self)

    def createWidget(self, parent):
        self.createOtherWidget(parent)
        return Tkinter.Entry(parent, validate="focusout", validatecommand=self.validate, width=self.width)

    def validate(self):
        try:
            self.validateOther()
            self.widget.configure(background="#ffffff")
            return True
        except:
            self.widget.configure(background="#ff0000")
            return False

    def validateOther(self):
        pass

    def createOtherWidget(self, parent):
        pass


class LabelTextbox(Textbox):
    def __init__(self, name, row, column, command=None, allow_negative=False, allow_zero=False, columnspan=1, padx=5, pady=5, width=5, default_value=0, command_on_load=True):
        Textbox.__init__(self, name, row, column, command, columnspan, padx, pady, width, default_value, command_on_load)
        self.allow_negative = allow_negative
        self.allow_zero = allow_zero

    def validateOther(self):
        if not self.allow_negative:
            assert float(self.widget.get()) >= 0
        if not self.allow_zero:
            assert float(self.widget.get()) != 0
        self.other_validation(self.widget.get())

    def createOtherWidget(self, parent):
        label = Tkinter.Label(parent, text=self.name)
        label.grid(row=self.row, column=self.column-1, columnspan=self.columnspan, padx=self.padx, pady=self.pady)


class ColorTextbox(Textbox):
    def __init__(self, name, row, column, command=None, columnspan=1, padx=5, pady=5, width=5, default_value="#eeeeee", command_on_load=True):
        Textbox.__init__(self, name, row, column, command, columnspan, padx, pady, width, default_value, command_on_load)
        self.button = None

    def createOtherWidget(self, parent):
        self.button = Tkinter.Button(parent, text=self.name, command=self.chooseColor)
        self.button.grid(row=self.row, column=self.column-1, columnspan=self.columnspan, padx=self.padx, pady=self.pady)

    def validateOther(self):
        self.button.configure(background=self.widget.get())

    def chooseColor(self):
        previous = self.widget.get()
        try:
            color = tkColorChooser.askcolor(previous)[1]
        except:
            color = tkColorChooser.askcolor()[1]
        if color is None:
            color = previous
        self.widget.delete(0, Tkinter.END)
        self.widget.insert(0, color)
        self.validate()


class Button(Widget):
    def __init__(self, name, row, column, command=None, columnspan=1, padx=5, pady=5, command_on_load=True):
        Widget.__init__(self, name, command, "disabled", row, column, columnspan, padx, pady, command_on_load)

    def createWidget(self, parent):
        return Tkinter.Button(parent, text=self.name, command=self.command)


class Checkbutton(WidgetWithVariable):
    def __init__(self, name, row, column, command=None, columnspan=1, padx=5, pady=5, default_value=0, command_on_load=True):
        WidgetWithVariable.__init__(self, name, command, "disabled", Tkinter.BooleanVar(), default_value, row, column, columnspan, padx, pady, command_on_load)

    def createWidget(self, parent):
        return Tkinter.Checkbutton(parent, text=self.name, command=self.command, variable=self.variable)


class OptionMenu(WidgetWithVariable):
    def __init__(self, name, row, column, command=None, values=None, columnspan=2, padx=5, pady=5, default_value=None, command_on_load=True):
        WidgetWithVariable.__init__(self, name, command, "disabled", Tkinter.StringVar(), self.getDefaultValue(default_value, values), row, column, columnspan, padx, pady, command_on_load)
        self.values = values

    def getDefaultValue(self, value, values):
        return value if value is not None else values[0]

    def createWidget(self, parent):
        return Tkinter.OptionMenu(parent, self.variable, *self.values, command=lambda x: self.command())


class SunkenButton(WidgetWithVariable):
    def __init__(self, name, row, column, command=None, columnspan=1, padx=5, pady=5, default_value=0, command_on_load=True):
        WidgetWithVariable.__init__(self, name, self.sunkenButtonCommand, "disabled", Tkinter.BooleanVar(), default_value, row, column, columnspan, padx, pady, command_on_load)
        self.sunken_button_command = command

    def sunkenButtonCommand(self, widget, variable):
        variable.set(not variable.get())
        widget.config(relief=Tkinter.RAISED) if variable.get() else widget.config(relief=Tkinter.SUNKEN)
        if self.sunken_button_command is not None:
            self.sunken_button_command(widget, variable)

    def createWidget(self, parent):
        return Tkinter.Button(parent, text=self.name, command=self.command)
