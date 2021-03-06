import constants as c
import BCI
import ParameterHandler
import TargetIdentification

import copy
import os
import scipy.optimize


class Training(BCI.BCI):
    def __init__(self, connections, main_connection, recording):
        BCI.BCI.__init__(self, connections, main_connection, recording)
        self.packets = []
        self.expected_targets = []
        self.expected_target_index = 0
        self.target_freqs = {}
        # self.difference_finder = TargetIdentification.DifferenceFinder()
        # self.weight_finder = TargetIdentification.WeightFinder()
        self.result_finder = ResultAdder()
        self.result = 0
        self.difference_finder = DifferenceFinder()

    def setupPackets(self):  # Currently uses always first data entry in the lists
        self.packets = self.recording.normal_eeg.list[1][c.EEG_RECORDING_PACKETS]
        self.target_freqs = self.recording.normal_eeg.list[1][c.EEG_RECORDING_FREQS]
        self.expected_targets = self.recording.expected_targets.list[1]
        self.expected_target_index = 0

    def setupResultsParsers(self, options):
        # self.difference_finder.setup(options[c.DATA_EXTRACTION_DIFFERENCES])
        # self.weight_finder.setup(options[c.DATA_EXTRACTION_WEIGHTS])
        self.result_finder.setup(options[c.DATA_EXTRACTION_WEIGHTS])
        self.difference_finder.setup(options[c.DATA_EXTRACTION_DIFFERENCES])

    def setup(self, options):
        self.setupPackets()
        self.setupResultsParsers(options)
        return BCI.BCI.setup(self, self.changeOptions(options))

    def start(self, options):
        method = options[c.DATA_TRAINING][c.TRAINING_METHOD]
        if method == c.TRAINING_METHOD_SINGLE:
            return BCI.BCI.start(self, self.changeOptions(options))
        elif method == c.TRAINING_METHOD_DE:
            return self.differentialEvolution(self.changeOptions(options))
        elif method == c.TRAINING_METHOD_BRUTE_FORCE:
            return self.bruteForce(self.changeOptions(options))
        elif method == c.TRAINING_METHOD_DE_IDENTIFICATION:
            return self.differentialEvolutionIdentification(self.changeOptions(options))
        elif method == c.TRAINING_METHOD_SAVE:
            return self.saveDataMethod(self.changeOptions(options))

    def saveDataMethod(self, options):
        self.file_content = ""
        self.handleExtractionMessages = self.saveDataHandleExtraction
        BCI.BCI.start(self, options)
        open("C:\\Users\\Anti\\Desktop\\PycharmProjects\\VEP-BCI\\src\\save\\test5_results_2_psda.txt", "w").write(self.file_content)

    def saveDataHandleExtraction(self, target_freqs, current_target):
        results = self.connections.receiveExtractionMessage()
        if results is not None:
            self.file_content += str(results) + "\n"

    def differentialEvolutionIdentification(self, options):
        options_handler = ParameterHandler.DifferentialEvolution4Params()
        self.counter = 1
        self.directory = "C:\\Users\\Anti\\Desktop\\PycharmProjects\\VEP-BCI\\src\\results_4params\\"
        self.data = ""
        f = open(self.directory + "options.txt", "w")
        f.write(str(options))
        f.close()
        # For timing cost function evaluation
        # for i in range(10):
        #     self.differentialEvolutionIdentificationCostFunction((1,1,1,1,1,0.1,0.1,0.1,0.1,0.1,1,3), options_handler, options)
        scipy.optimize.differential_evolution(
            self.differentialEvolutionIdentificationCostFunction,
            options_handler.getBounds(),
            args=(options_handler, options),
            popsize=20,
        )

    def differentialEvolutionIdentificationCostFunction(self, numbers, options_handler, all_options):
        self.expected_target_index = 0
        new_options = options_handler.numbersToOptions(numbers)
        #all_options[c.DATA_EXTRACTION_WEIGHTS] = new_options[c.DATA_EXTRACTION_WEIGHTS]
        all_options[c.DATA_EXTRACTION_DIFFERENCES] = new_options[c.DATA_EXTRACTION_DIFFERENCES]
        # new_options[c.DATA_ACTUAL_RESULTS][c.DATA_ALWAYS_DELETE] = all_options[c.DATA_ACTUAL_RESULTS][c.DATA_ALWAYS_DELETE]
        new_options[c.DATA_PREV_RESULTS][c.DATA_ALWAYS_DELETE] = all_options[c.DATA_PREV_RESULTS][c.DATA_ALWAYS_DELETE]
        # all_options[c.DATA_ACTUAL_RESULTS] = new_options[c.DATA_ACTUAL_RESULTS]
        all_options[c.DATA_PREV_RESULTS] = new_options[c.DATA_PREV_RESULTS]
        BCI.BCI.setup(self, all_options)
        BCI.BCI.start(self, all_options)
        wrong_result_count = self.target_identification.results.list[-1]["Wrong"]
        correct_result_count = self.target_identification.results.list[-1]["Correct"]
        result = self.target_identification.results.list[-1]["Wrong"] - self.target_identification.results.list[-1]["Correct"]
        result = len(self.packets) if wrong_result_count == 0 and correct_result_count == 0 else result
        self.data += str(new_options) + "\n" + str(wrong_result_count) + " " + str(correct_result_count) + "\n" + str(result) + "\nMARKER\n"
        if self.counter % 100 == 0:
            f = open(self.directory + str(self.counter) + ".txt", "w")
            f.write(self.data)
            f.close()
            self.data = ""
        self.counter += 1
        print(self.counter, result, new_options)
        return result

    def differentialEvolution(self, options):
        options_handler = ParameterHandler.DifferentialEvolution()
        scipy.optimize.differential_evolution(
            self.differentialEvolutionCostFunction,
            options_handler.getBounds(),
            args=(options_handler, options),
        )

    def differentialEvolutionCostFunction(self, numbers, options_handler, all_options):
        signal_processing_options = options_handler.numbersToOptions(numbers)
        return self.costFunction(all_options, signal_processing_options)

    def costFunction(self, options, signal_processing_options):
        self.expected_target_index = 0
        self.result = 0
        for tab in options[c.DATA_EXTRACTION]:
            options[c.DATA_EXTRACTION][tab][c.DATA_EXTRACTION_OPTIONS] = copy.deepcopy(signal_processing_options)
        options[c.DATA_EXTRACTION][2][c.DATA_EXTRACTION_OPTIONS][c.OPTIONS_WINDOW] = c.WINDOW_NONE
        BCI.BCI.setup(self, options)
        BCI.BCI.start(self, options)
        # self.result *= signal_processing_options[c.OPTIONS_STEP]
        # print signal_processing_options, self.result
        return self.result

    def bruteForce(self, options):
        options_generator = ParameterHandler.BruteForce().optionsGenerator()
        counter = 1
        self.handleExtractionMessages = self.handleExtractionMessages3
        for signal_processing_options in options_generator:
            file_name = "C:\\Users\\Anti\\Desktop\\PycharmProjects\\VEP-BCI\\src\\results_brute\\" + str(counter) + ".txt"
            results_file = open(file_name, "w")
            results_file.write(str(signal_processing_options) + "\n")
            result = self.costFunction(options, signal_processing_options)
            results_file.write(str(result))
            results_file.close()
            counter += 1

    def changeOptions(self, options):
        options = copy.deepcopy(options)
        self.disableUnnecessaryOptions(options)
        self.setTrainingTime(options)
        self.fixFrequencies(options)
        return options

    def fixFrequencies(self, options):
        options[c.DATA_FREQS] = self.target_freqs
        for tab in options[c.DATA_EXTRACTION]:
            options[c.DATA_EXTRACTION][tab][c.DATA_EXTRACTION_TARGETS] = self.target_freqs  # TODO allow disabling

    def disableUnnecessaryOptions(self, options):
        options[c.DATA_RECORD][c.TRAINING_RECORD] = c.TRAINING_RECORD_DISABLED
        options[c.DATA_TEST][c.TEST_STANDBY] = c.TEST_NONE
        options[c.DATA_BACKGROUND] = {c.DISABLE: 1}
        options[c.DATA_ROBOT] = {c.DISABLE: 1}
        options[c.DATA_EMOTIV] = {c.DISABLE: 1}
        options[c.DATA_PLOTS] = {}

    def setTrainingTime(self, options):
        options[c.DATA_TEST][c.TEST_UNLIMITED] = False
        options[c.DATA_TEST][c.TEST_TIME] = self.getTotalTrainingTime()

    def getTotalTrainingTime(self):
        return len(self.packets)

    def getTarget(self, test_target, target_freqs, previous_target):
        if self.expected_target_index < len(self.expected_targets):
            if self.expected_targets[self.expected_target_index][1] == self.message_counter:
                self.expected_target_index += 1
                return self.expected_targets[self.expected_target_index-1][0]
        return previous_target

    def getNextPacket(self):
        return self.packets[self.message_counter]

    def startPacketSending(self, target_freqs, current_target, total_time):
        while not self.target_identification.need_new_target and self.message_counter < total_time:
            main_message = self.main_connection.receiveMessageInstant()
            if main_message in c.ROBOT_COMMANDS:
                self.connections.sendRobotMessage(main_message)
            elif main_message is not None:
                print main_message + "!!!"
                return main_message
            current_target = self.getTarget(None, None, current_target)  # Override for this line
            self.handleEmotivMessages(target_freqs, current_target)

    # def handleExtractionMessages2(self, target_freqs, current_target):  # for brute force and DE
    #     results = self.connections.receiveExtractionMessage()
    #     if results is not None:
    #         # self.results_file.write(str(results) + "\n")
    #         added = self.result_finder.parseResults(results)
    #         current = target_freqs[current_target]
    #         for freq in added:
    #             if freq == current:
    #                 self.result -= added[freq]
    #             else:
    #                 self.result += added[freq]

    def handleExtractionMessages3(self, target_freqs, current_target):  # for brute force and DE
        results = self.connections.receiveExtractionMessage()
        if results is not None:
            current = target_freqs[current_target]
            self.difference_finder.setCurrentTarget(current)
            self.difference_finder.reset()
            self.difference_finder.parseResults(results)
            self.result += self.difference_finder.result


class ResultAdder(TargetIdentification.WeightFinder):
    def parseFrequencyResults(self, parse_result, result, data):
        if len(result) != 0:
            if result[0][0] in parse_result:
                parse_result[result[0][0]] += result[0][1] * data
            else:
                parse_result[result[0][0]] = result[0][1] * data


class DifferenceFinder(TargetIdentification.DifferenceFinder):
    def __init__(self):
        TargetIdentification.DifferenceFinder.__init__(self)
        self.result = None
        self.current_target = None

    def setCurrentTarget(self, current_target):
        self.current_target = current_target

    def reset(self):
        self.result = 0

    def parseFrequencyResults(self, parse_result, result, data):
        if len(result) > 1:  # If we have at least 2 targets in the result dict
            difference = result[0][1]-result[1][1]
            parse_result[result[0][0], result[1][0]] = difference
            if result[0][0] == self.current_target:
                self.result -= difference * data
            else:
                self.result += difference * data
