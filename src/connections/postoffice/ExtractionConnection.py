import copy

from connections import Connections
from connections.postoffice import ConnectionPostOfficeEnd, MyQueue
from generators.result.extraction import Extraction
import constants as c


class ExtractionConnection(object):
    def receiveExtractionMessages(self):
        result = {}
        for connection in self.connections:
            message = connection.receiveExtractionMessages()
            if message is not None:
                result[connection.id] = message
        return result if result != {} else None
    
    def setupConnection(self, connection, options, id):
        connection.setup(options)
        connection.setId(id)


class ExtractionTabConnection(ExtractionConnection, Connections.MultipleConnections):
    def __init__(self):
        ExtractionConnection.__init__(self)
        Connections.MultipleConnections.__init__(self)

    def getConnection(self):
        return ExtractionMethodConnection()

    def getMessages(self):
        message = self.receiveExtractionMessages()
        if message is not None:
            return message

    def setup(self, all_options):
        self.close()  # In the first execution of setup, MultipleConnections does not have any connections, thus nothing gets closed
        for tab_id, tab_options in all_options[c.DATA_EXTRACTION].items():
            new_connection = self.getConnection()
            new_options = self.changeOptions(tab_options, tab_id, all_options)
            self.setupConnection(new_connection, new_options, tab_id)
            self.connections.append(new_connection)
    
    def changeOptions(self, tab_options, tab_id, all_options):
        dict_copy = copy.deepcopy(tab_options)
        dict_copy[c.DATA_FREQS] = tab_options[c.DATA_EXTRACTION_TARGETS]
        dict_copy[c.DATA_HARMONICS] = all_options[c.DATA_HARMONICS][tab_id]
        dict_copy[c.DATA_PROCESS_SHORT_SIGNAL] = all_options[c.DATA_PROCESS_SHORT_SIGNAL]
        return dict_copy


class TrainingExtractionTabConnection(ExtractionTabConnection):
    def __init__(self):
        ExtractionTabConnection.__init__(self)

    def getConnection(self):
        return TrainingExtractionMethodConnection()


class ExtractionMethodConnection(ExtractionConnection, Connections.MultipleConnections):
    def __init__(self):
        ExtractionConnection.__init__(self)
        Connections.MultipleConnections.__init__(self)

    def getConnection(self, method):
        if method == c.SUM_PSDA:
            return self.getSumPsda()
        elif method == c.CCA:
            return self.getCca()
        elif method in (c.PSDA,):
            return ExtractionSensorConnection()
        else:
            raise ValueError("Illegal argument in getConnection: " + str(method))

    def getSumPsda(self):
        return ConnectionPostOfficeEnd.ExtractionConnection(Extraction.SumPsda)

    def getCca(self):
        return ConnectionPostOfficeEnd.ExtractionConnection(Extraction.Cca)

    def setup(self, all_options):
        self.close()  # In the first execution of setup, MultipleConnections does not have any connections, thus nothing gets closed
        for method in all_options[c.DATA_EXTRACTION_METHODS]:
            new_connection = self.getConnection(method)
            new_options = self.changeOptions(method, all_options)
            self.setupConnection(new_connection, new_options, self.getId(method, all_options))
            self.connections.append(new_connection)
    
    def getId(self, method, all_options):
        return (method, tuple(all_options[c.DATA_EXTRACTION_SENSORS]))
    
    def changeOptions(self, method, all_options):
        dict_copy = copy.deepcopy(all_options)
        dict_copy[c.DATA_METHOD] = method
        return dict_copy


class TrainingExtractionMethodConnection(ExtractionMethodConnection):
    def __init__(self):
        ExtractionMethodConnection.__init__(self)

    def getSumPsda(self):
        return MyQueue.PostOfficeQueueConnection(Extraction.SumPsda)

    def getCca(self):
        return MyQueue.PostOfficeQueueConnection(Extraction.Cca)


class ExtractionSensorConnection(ExtractionConnection, Connections.MultipleConnections):
    def __init__(self):
        ExtractionConnection.__init__(self)
        Connections.MultipleConnections.__init__(self)

    def getConnection(self, method):
        if method == c.PSDA:
            return self.getPsda()
        else:
            raise ValueError("Illegal argument in getConnection: " + str(method))

    def getPsda(self):
        return ConnectionPostOfficeEnd.ExtractionConnection(Extraction.Psda)

    def setup(self, all_options):
        self.close()  # In the first execution of setup, MultipleConnections does not have any connections, thus nothing gets closed
        for sensor in all_options[c.DATA_EXTRACTION_SENSORS]:
            new_connection = self.getConnection(all_options[c.DATA_METHOD])
            new_options = self.changeOptions(sensor, all_options)
            self.setupConnection(new_connection, new_options, sensor)
            self.connections.append(new_connection)
    
    def changeOptions(self, sensor, all_options):
        dict_copy = copy.deepcopy(all_options)
        dict_copy[c.DATA_SENSORS] = [sensor]
        return dict_copy


class TrainingExtractionSensorConnection(ExtractionSensorConnection):
    def __init__(self):
        ExtractionSensorConnection.__init__(self)

    def getPsda(self):
        return MyQueue.PostOfficeQueueConnection(Extraction.SumPsda)
