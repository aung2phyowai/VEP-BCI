import Switchable
import constants as c

import csv


class DataAndExpectedTargets(Switchable.Switchable):
    def __init__(self):
        Switchable.Switchable.__init__(self)
        self.data = []
        self.expected_targets = []

    def add(self, data, expected_target):
        if self.enabled:
            self.data.append(data)
            self.expected_targets.append(expected_target)

    def getLength(self):
        return len(self.data)


class Eeg(DataAndExpectedTargets):
    def __init__(self):
        DataAndExpectedTargets.__init__(self)

    def save(self, file_name):
        with open(file_name, "w") as csv_file:
            writer = csv.DictWriter(csv_file, c.SENSORS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self, file_name):
        with open(file_name, "r") as csv_file:
            reader = csv.DictReader(csv_file, c.SENSORS)
            return list(reader)[1:]


class Features(DataAndExpectedTargets):
    def __init__(self):
        DataAndExpectedTargets.__init__(self)


class Recording(object):
    def __init__(self, target_freqs, record_option):
        self.normal_eeg = Eeg()
        self.features = Features()
        self.target_frequencies = target_freqs
        self.setRecordingState(record_option)

    def setRecordingState(self, record_option):
        if record_option == c.TRAINING_RECORD_NORMAL:
            self.enableNormal()
        elif record_option == c.TRAINING_RECORD_NEUTRAL:
            self.enableNeutral()
        elif record_option == c.TRAINING_RECORD_DISABLED:
            self.disableRecording()
        else:
            raise Exception("Recording option menu in invalid state!")

    def disableRecording(self):
        self.normal_eeg.disable()

    def enableNormal(self):
        self.normal_eeg.enable()

    def enableNeutral(self):
        """
        Currently not implemented
        :return:
        """
        self.normal_eeg.disable()

    def collectPacket(self, packet, expected_target):
        self.normal_eeg.add(packet, expected_target)

    def collectFeatures(self, features, expected_target):
        self.features.add(features, expected_target)

    def getEeg(self):
        return self.normal_eeg

    def getFeatures(self):
        return self.features

    def getFrequencies(self):
        return self.target_frequencies
