__author__ = 'Anti'

import random
import numpy as np
import constants as c
from connections import MasterConnection, ConnectionPostOfficeEnd


class PostOffice(object):
    def __init__(self):
        self.main_connection = ConnectionPostOfficeEnd.MainConnection()
        self.connections = MasterConnection.MasterConnection()
        self.options = None
        self.results = None
        self.resetResults()
        self.standby = None
        self.standby_freq = None
        self.recorded_signals = [None for _ in range(7)]
        self.waitConnections()

    def waitConnections(self):
        setup_successful = False
        message = None
        while True:
            if message is not None:
                if message == c.START_MESSAGE:
                    if setup_successful:
                        message = self.start()
                        continue
                    else:
                        print("Setup was not successful!")
                elif message == c.SETUP_MESSAGE:
                    if self.setup() == c.SUCCESS_MESSAGE:
                        setup_successful = True
                        print("Setup successful!")
                    else:
                        setup_successful = False
                        print("Setup failed!")
                elif message == c.STOP_MESSAGE:
                    print("Stop PostOffice")
                elif message == "Threshold":
                    self.calculateThreshold()
                elif message == "Record neutral":
                    self.sendMessage(self.emotiv_connection, "Start")
                    self.recordSignal(self.main_connection.recv(), self.main_connection.recv())
                    self.sendMessage(self.emotiv_connection, "Stop")
                elif message == "Record target":
                    self.sendMessage(self.psychopy_connection, "Start")
                    self.sendMessage(self.psychopy_connection, self.main_connection.recv())
                    self.sendMessage(self.psychopy_connection, self.main_connection.recv())
                    self.sendMessage(self.emotiv_connection, "Start")
                    self.recordSignal(self.main_connection.recv(), self.main_connection.recv())
                    self.sendMessage(self.emotiv_connection, "Stop")
                    self.sendMessage(self.psychopy_connection, "Stop")
                elif message == "Reset results":
                    self.resetResults()
                elif message == "Show results":
                    self.printResults()
                elif message == c.EXIT_MESSAGE:
                    self.exit()
                    return
                else:
                    print("Unknown message in PostOffice: " + str(message))
            message = self.main_connection.receiveMessagePoll(0.1)

    def handleFreqMessages(self, message, no_standby, target_freqs, current_target):
        # Use only the first method in the first tab
        # Assume that for each method we have 2 connections, original and short
        print(message)
        # orig_result_freq = None
        # short_result_freq = None
        # orig_result, short_result = message
        # if orig_result != [[]] and orig_result[0][0] is not None:
        #     orig_result_freq, method = orig_result[0][0]
        # if short_result != [[]] and short_result[0][0] is not None:
        #     short_result_freq, method = short_result[0][0]
        # if orig_result_freq is not None and short_result_freq is not None:
        #     if orig_result_freq == short_result_freq:
        #         self.results[method][str(target_freqs)][current_target][orig_result_freq] += 1
        #         if orig_result_freq == self.standby_freq:
        #             # self.connections.sendPlotMessage(self.standby and not no_standby)
        #             self.standby = not self.standby
        #         if not self.standby or no_standby:
        #             self.connections.sendTargetMessage(orig_result_freq)
        #             # self.connections.sendGameMessage(orig_result)

        # for j, tab_message in enumerate(message):
        #     for i, method_message in enumerate(tab_message):
        #         for extraction_message in method_message:
        #             if extraction_message is not None:
        #                 freq, method = extraction_message
        #                 if freq is not None:
        #                     print(message)
        #                     self.results[method][str(target_freqs)][current_target][freq] += 1
        #                     if freq == self.standby_freq:
        #                         # self.connections.sendPlotMessage(self.standby and not no_standby)
        #                         self.standby = not self.standby
        #                     if not self.standby or no_standby:
        #                         # if not "short" in method:
        #                         self.connections.sendTargetMessage(freq)
        #                         # self.connections.sendGameMessage(freq)

    def randomSequence(self, total, min_value, max_value, target_freqs):
        data = []
        initial_values = {i: total for i in range(len(target_freqs))}
        while True:
            target = random.choice(initial_values.keys())
            time = random.randint(min_value, max_value)
            if initial_values[target] - time < min_value:
                time = initial_values[target]
            initial_values[target] = initial_values[target]-time
            if len(data) > 0 and data[-1][0] == target:
                data[-1][1] += time
            else:
                data.append([target, time])
            if initial_values[target] == 0:
                del initial_values[target]
                if initial_values == {}:
                    break
        return data

    def normalSequence(self, target, time):
        return [[target, time]]

    def getSequence(self, options, target_freqs):
        if options[c.TEST_TARGET] == c.TEST_RANDOM:
            return self.randomSequence(options[c.TEST_TIME], options[c.TEST_MIN], options[c.TEST_MAX], target_freqs)
        elif options[c.TEST_UNLIMITED]:
            return self.normalSequence(options[c.TEST_TARGET], float("inf"))
        else:
            return self.normalSequence(options[c.TEST_TARGET], options[c.TEST_TIME])

    def resetResults(self):
        self.results = {name: {} for name in c.EXTRACTION_METHOD_NAMES}

    def setupResults(self, target_freqs):
        for key in self.results:
            if str(target_freqs) not in self.results[key]:
                self.results[key][str(target_freqs)] = \
                    {i+1: {freq: 0 for freq in target_freqs} for i in range(len(target_freqs))}
                self.results[key][str(target_freqs)]["None"] = {freq: 0 for freq in target_freqs}

    def printResults(self):
        for method in self.results:
            print method
            for freqs in self.results[method]:
                print freqs
                for row in sorted(self.results[method][freqs]):
                    print row, self.results[method][freqs][row]

    def targetChangingLoop(self, sequence, target_freqs, no_standby):
        # print(sequence)
        message = None
        for target, time in sequence:
            self.connections.sendTargetMessage(target)
            message = self.startPacketSending(time, no_standby, target_freqs, target)
            if message is not None:
                break
        return message

    def setup(self):
        self.options = self.main_connection.receiveMessageBlock()
        self.connections.setup(self.options)
        if self.connections.setupSuccessful():
            self.setupResults(self.options[c.DATA_FREQS])
            return c.SUCCESS_MESSAGE
        else:
            return c.FAIL_MESSAGE

    def exit(self):
        self.connections.close()

    def start(self):
        self.connections.sendStartMessage()
        message = self.targetChangingLoop(
            self.getSequence(self.options[c.DATA_TEST], self.options[c.DATA_FREQS]),
            self.options[c.DATA_FREQS],
            not self.options[c.DATA_TEST][c.TEST_STANDBY]
        )
        self.connections.sendStopMessage()
        return message

    def handleEmotivMessages(self, no_standby):
        message = self.connections.receiveEmotivMessage()
        if message is not None:
            self.connections.sendExtractionMessage(message)
            self.connections.sendPlotMessage(message)
            if not self.standby or no_standby:
                return 1
        return 0

    def startPacketSending(self, length, no_standby, target_freqs, current_target):
        count = 0
        self.standby = True
        self.standby_freq = target_freqs[-1]
        while count < length:
            main_message = self.main_connection.receiveMessageInstant()
            if main_message is not None:
                return main_message
            count += self.handleEmotivMessages(no_standby)
            self.handleFreqMessages(
                self.connections.receiveExtractionMessage(),
                no_standby,
                target_freqs,
                current_target
            )
        # Wait for the last result
        # self.handleFreqMessages(
        #     self.connections[c.CONNECTION_EXTRACTION].receiveMessageBlock(),
        #     no_standby,
        #     target_freqs,
        #     current_target
        # )




    def calculateThreshold(self):
        target_freqs = self.main_connection.recv()
        all_results = []
        for signal in self.recorded_signals:
            if signal is not None:
                self.sendMessage(self.extraction_connection, "Start")
                self.sendMessage(self.extraction_connection, target_freqs)
                for packet in signal:
                    self.sendMessage(self.extraction_connection, packet)
                self.sendMessage(self.extraction_connection, "Stop")
                self.sendMessage(self.extraction_connection, "Results")
                while True:
                    if "Results" in self.getMessages(self.extraction_connection, "Extraction", poll=lambda connection: True):
                        break
                all_results.append(self.getMessages(self.extraction_connection, "Extraction", poll=lambda connection: True))
            else:
                all_results.append(None)
        shaped_results = []
        print "results", all_results
        index = 0
        for i in range(len(all_results)):  # target
            if all_results[i] is not None:
                for window in range(len(all_results[i])):  # window
                    if len(shaped_results) != len(all_results[i]):
                        shaped_results.append({})
                    for method in all_results[i][window]:  # method
                        print method
                        transposed_result = np.transpose(all_results[i][window][method])
                        if method not in shaped_results[window]:
                            shaped_results[window][method] = {True:  [[] for _ in range(len(transposed_result))],
                                                  False: [[] for _ in range(len(transposed_result))]}
                        for target in range(len(transposed_result)):  # target
                            if index == 0:
                                shaped_results[window][method][False][target] = np.append(shaped_results[window][method][False][target], transposed_result[target][16:], 1)
                            elif index-1 == target:
                                shaped_results[window][method][True][target] = np.append(shaped_results[window][method][True][target], transposed_result[target][16:], 1)
                            else:
                                shaped_results[window][method][False][target] = np.append(shaped_results[window][method][False][target], transposed_result[target][16:], 1)
                            print transposed_result[target]
                index += 1
        print shaped_results
        thresholds = []
        for window in shaped_results:
            thresholds.append({})
            for method in window:
                thresholds[-1][method] = {}
                for boolean in window[method]:
                    thresholds[-1][method][boolean] = []
                    for target in window[method][boolean]:
                        thresholds[-1][method][boolean].append([])
                        if len(target) != 0:
                            thresholds[-1][method][boolean][-1].append(min(target))
                            thresholds[-1][method][boolean][-1].append(sum(target)/len(target))
                            thresholds[-1][method][boolean][-1].append(max(target))
        print thresholds

    def recordSignal(self, length, target_n):
        signal = []
        while len(signal) < length:
            if self.main_connection.poll():
                message = self.main_connection.recv()
                return message
            if self.emotiv_connection[0].poll():
                message = self.emotiv_connection[0].recv()
                signal.append(message)
        self.recorded_signals[target_n] = signal

    def getMessages(self, connections, name, poll=lambda connection: connection.poll()):
        ret = []
        for i in range(len(connections)-1, -1, -1):
            if poll(connections[i]):
                message = connections[i].recv()
                if message == "Close":
                    print name, "pipe closed"
                    connections[i].close()
                    del connections[i]
                elif isinstance(message, tuple):  # elif name == "Extraction" and isinstance(message, float):
                    ret.append(message)
                else:  # elif isinstanse(message, list)
                    ret.append(message)
        return ret