from gui.widgets import Buttons, Textboxes
from gui.widgets.frames import Frame
from gui.widgets.frames.tabs import DisableDeleteNotebookTab
import constants as c
import Savable
import Recording
import datetime
import time
import os


class RecordTab(DisableDeleteNotebookTab.Delete):
    def __init__(self, parent, deleteTab, **kwargs):
        DisableDeleteNotebookTab.Delete.__init__(self, parent, c.RECORD_TAB, **kwargs)
        self.addChildWidgets((
            ResultsFrame(self, 0, 0, columnspan=3),
            TimestampFrame(self, 1, 0, columnspan=3),
            DirectoryFrame(self, 2, 0, columnspan=3),
            EegFrame(self, 3, 0, columnspan=3),
            RecordFrame(self, 4, 0),
            self.getDeleteButton(4, 1, deleteTab)
        ))

    def setDirectory(self, directory):
        self.widgets_dict[c.DIRECTORY_FRAME].setDirectory(directory)

    def saveEegEvent(self, directory):
        if self.saveMe():
            file = open(os.path.join(directory, "results.txt"), "w")
            self.sendEventToChildren(lambda x: x.saveBciSettingsEvent(file))
            self.setDirectory(directory)
        else:
            return c.STOP_EVENT_SENDING

    def saveMe(self):
        return self.widgets_dict[c.RECORD_FRAME].saveMe()

    def loadEegEvent(self, directory):
        file_name = os.path.join(directory, "results.txt")
        if os.path.isfile(file_name):
            file = open(file_name, "r")
            self.sendEventToChildren(lambda x: x.loadBciSettingsEvent(file))
            self.setDirectory(directory)
        else:
            print file_name, "does not exist!"


class TimestampFrame(Frame.Frame):
    def __init__(self, parent, row, column, **kwargs):
        Frame.Frame.__init__(self, parent, c.TIMESTAMP_FRAME, row, column, **kwargs)
        self.addChildWidgets((
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_TIMESTAMP, 0, 0, width=30, columnspan=3),
        ))

    def trialEndedEvent(self):
        self.widgets_dict[c.RESULTS_DATA_TIMESTAMP].setValue(self.getTimestamp())

    def getTimestamp(self):
        return datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S %d.%m.%Y')


class EegFrame(Frame.Frame):
    def __init__(self, parent, row, column, **kwargs):
        Frame.Frame.__init__(self, parent, c.EEG_FRAME, row, column, **kwargs)
        self.addChildWidgets((
            Textboxes.DisabledTextLabelTextbox(self, c.EEG_LENGTH, 0, 0),
        ))
        self.eeg = Recording.Eeg()

    def recordedEegReceivedEvent(self, eeg):
        self.eeg = eeg
        self.widgets_dict[c.EEG_LENGTH].setValue(eeg.getLength())

    def getFilePath(self, directory):
        return os.path.join(directory, "eeg.csv")

    def loadEegEvent(self, directory):
        self.eeg.load(self.getFilePath(directory))

    def saveEegEvent(self, directory):
        self.eeg.save(self.getFilePath(directory))


class DirectoryFrame(Frame.Frame):
    def __init__(self, parent, row, column, **kwargs):
        Frame.Frame.__init__(self, parent, c.DIRECTORY_FRAME, row, column, **kwargs)
        self.addChildWidgets((
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_DIRECTORY, 0, 0, width=30, columnspan=3),
        ))

    def setDirectory(self, directory):
        self.widgets_dict[c.RESULTS_DATA_DIRECTORY].setValue(directory)

    def saveBciSettingsEvent(self, file):
        pass

    def loadBciSettingsEvent(self, file):
        pass


class RecordFrame(Frame.Frame, Savable.SavableDirectory):
    def __init__(self, parent, row, column, **kwargs):
        Frame.Frame.__init__(self, parent, c.RECORD_FRAME, row, column, **kwargs)
        self.addChildWidgets((
            Buttons.Button(self, c.TRAINING_SAVE_EEG, 0, 0, command=self.saveEegClicked),
        ))
        self.save_me = False

    def saveMe(self):
        return self.save_me

    def saveEegClicked(self):
        self.askSaveFile()

    def saveToFile(self, file):
        """
        askSaveFile calls this function when corresponding button is pressed.
        :param file:
        :return:
        """
        self.save_me = True
        self.sendEventToRoot(lambda x: x.saveEegEvent(file), True)
        self.save_me = False


class ResultsFrame(Frame.Frame):
    def __init__(self, parent, row, column, **kwargs):
        Frame.Frame.__init__(self, parent, c.RESULTS_FRAME, row, column, **kwargs)
        self.addChildWidgets((
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_TRUE_POSITIVES, 0, 0),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_FALSE_POSITIVES, 0, 2),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_PRECISION, 0, 4),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_ITR_BIT_PER_TRIAL, 1, 2),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_ITR_BIT_PER_MIN, 1, 4),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_TOTAL_TIME_SECONDS, 2, 0),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_TOTAL_TIME_PACKETS, 2, 2),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_TIME_PER_TARGET, 2, 4),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_MACRO_F1, 3, 0),
            Textboxes.DisabledTextLabelTextbox(self, c.RESULTS_DATA_F1, 3, 2, width=25, columnspan=3),
        ))
        self.results = None

    def resultsReceivedEvent(self, results):
        self.results = results
        for key in self.widgets_dict:
            self.widgets_dict[key].setValue(results[key])
