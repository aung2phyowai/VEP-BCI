from gui.widgets.frames.notebooks import Notebook
from gui.widgets.frames.tabs import TargetsTab, ExtractionTab, PlotTab
import constants as c


class SameTabsNotebook(Notebook.Notebook):
    def __init__(self, parent, name, row, column, **kwargs):
        Notebook.Notebook.__init__(self, parent, name, row, column, **kwargs)
        self.tab_count = -1
        self.last_tab = None
        self.widget.bind("<<NotebookTabChanged>>", self.tabChangedEvent)

    def tabChangedEvent(self, event):
        if event.widget.index("current") == self.tab_count+1:
            self.plusTabClicked()
            self.tabDefaultValues(-1)

    def addInitialTabs(self):
        self.last_tab = self.addTab("+")
        self.plusTabClicked()

    def newTab(self, deleteTab):
        raise NotImplementedError("newTab not implemented!")

    def addTab(self, text):
        tab = self.newTab(self.deleteTab)
        self.widget.add(tab.widget, text=text)
        return tab

    def tabDefaultValues(self, tab_index):
        self.widgets_list[tab_index].loadDefaultValue()

    def loadDefaultValue(self):
        Notebook.Notebook.loadDefaultValue(self)
        self.addInitialTabs()
        for i in range(self.tab_count+1):
            self.tabDefaultValues(i)

    def save(self, file):
        file.write(str(self.tab_count)+"\n")
        Notebook.Notebook.save(self, file)

    def load(self, file):
        if self.tab_count == -1:
            self.addInitialTabs()
        self.deleteAllTabs()
        tab_count = int(file.readline())
        for i in range(tab_count):
            self.plusTabClicked()
        Notebook.Notebook.load(self, file)

    def deleteAllTabs(self):
        if self.tab_count != -1:
            self.widget.select(0)
            while self.tab_count > 0:
                self.deleteTab()

    def getCurrentTab(self):
        return self.widget.index("current")

    def deleteTab(self):
        current = self.getCurrentTab()
        del self.widgets_list[current]
        self.tab_count -= 1
        if self.tab_count != -1:
            self.changeActiveTab(current)
        self.widget.forget(current)
        return current

    def changeActiveTab(self, current):
        if current == self.tab_count+1:
            self.widget.select(current-1)
        else:
            while current < self.tab_count+2:
                self.widget.tab(current, text=self.widget.tab(current, "text")-1)
                current += 1

    def plusTabClicked(self):
        self.tab_count += 1
        self.widgets_list.append(self.last_tab)
        self.widget.tab(self.tab_count, text=self.tab_count+1)
        self.last_tab = self.addTab(c.PLUS_TAB)

    def getValue(self):
        return {i+1: widget.getValue() for i, widget in enumerate(self.widgets_list) if not widget.disabled}


class ExtractionNotebook(SameTabsNotebook):
    def __init__(self, parent, row, column, target_notebook_widgets, **kwargs):
        SameTabsNotebook.__init__(self, parent, c.EXTRACTION_NOTEBOOK, row, column, **kwargs)
        self.target_notebook_widgets = target_notebook_widgets

    def newTab(self, deleteTab):
        return ExtractionTab.ExtractionTab(self.widget, deleteTab, self.target_notebook_widgets)


class PlotNotebook(SameTabsNotebook):
    def __init__(self, parent, row, column, **kwargs):
        SameTabsNotebook.__init__(self, parent, c.PLOT_NOTEBOOK, row, column, **kwargs)

    def newTab(self, deletaTab):
        return PlotTab.PlotTab(self.widget, deletaTab)


class TargetNotebook(SameTabsNotebook):
    def __init__(self, parent, row, column, addTarget, removeTarget, disableTarget, enableTarget, getMonitorFreq, **kwargs):
        SameTabsNotebook.__init__(self, parent, c.TARGETS_NOTEBOOK, row, column, **kwargs)
        self.getMonitorFreq = getMonitorFreq
        self.addTarget = addTarget
        self.removeTarget = removeTarget
        self.disableTarget = disableTarget
        self.enableTarget = enableTarget

    def changeFreq(self):
        for widget in self.widgets_list:
            widget.changeFreq()

    def plusTabClicked(self):  # Updates TargetChoosingMenus
        self.addTarget()   # MainNotebook's targetAdded method which calls TargetChoosingMenu's targetAdded
        SameTabsNotebook.plusTabClicked(self)

    def getEnabledTabs(self):
        return list(tab.disabled for tab in self.widgets_list)

    def newTab(self, deleteTab):
        return TargetsTab.TargetsTab(self.widget, self.disableTarget, self.enableTarget, self.getMonitorFreq, deleteTab, self.getEnabledTabs, self.getCurrentTab)

    def deleteTab(self):  # Updates TargetChoosingMenus
        deleted_tab = SameTabsNotebook.deleteTab(self)
        self.removeTarget(deleted_tab)  # MainNotebook's targetRemoved method which calls TargetChoosingMenu's targetAdded
