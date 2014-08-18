__author__ = 'Anti'

from controllable_windows import PlotWindow
from signal_processing import FFT
from main_logic import Abstract


class FFTPlot(PlotWindow.PlotWindow):
    def __init__(self, title):
        PlotWindow.PlotWindow.__init__(self, title)

    def getScale(self):
        return 3.3, 0.2


class MultipleRegular(Abstract.Multiple, FFTPlot):
    def __init__(self):
        Abstract.Multiple.__init__(self)
        FFTPlot.__init__(self, "FFTs")

    def getGenerator(self):
        return FFT.MultipleRegular(self.options, self.window_function, self.channel_count, self.filter_coefficients).coordinates_generator()


class MultipleAverage(Abstract.Multiple, FFTPlot):
    def __init__(self):
        Abstract.Multiple.__init__(self)
        FFTPlot.__init__(self, "Average FFTs")

    def getGenerator(self):
        return FFT.MultipleAverage(self.options, self.window_function, self.channel_count, self.filter_coefficients).coordinates_generator()


class SingleAverage(Abstract.Single, FFTPlot):
    def __init__(self):
        Abstract.Single.__init__(self)
        FFTPlot.__init__(self, "Sum of average FFTs")

    def getGenerator(self):
        return FFT.SingleAverage(self.options, self.window_function, self.channel_count, self.filter_coefficients).coordinates_generator()


class SingleRegular(Abstract.Single, FFTPlot):
    def __init__(self):
        Abstract.Single.__init__(self)
        FFTPlot.__init__(self, "Sum of FFTs")

    def getGenerator(self):
        return FFT.SingleRegular(self.options, self.window_function, self.channel_count, self.filter_coefficients).coordinates_generator()