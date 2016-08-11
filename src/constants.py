MAIN_NOTEBOOK = "MainNotebook"

# Tab names
MAIN_NOTEBOOK_TARGETS_TAB = "Targets"
MAIN_NOTEBOOK_PLOT_TAB = "Plot"
MAIN_NOTEBOOK_EXTRACTION_TAB = "Extraction"
MAIN_NOTEBOOK_RECORD_TAB = "Record"
MAIN_NOTEBOOK_TEST_TAB = "Test"
MAIN_NOTEBOOK_ROBOT_TAB = "Robot"
MAIN_NOTEBOOK_CLASSIFICATION_TAB = "Class"
MAIN_NOTEBOOK_MODELS_TAB = "Models"


MAIN_NOTEBOOK_TRAINING_TAB = "Train"


MODELS_NOTEBOOK = "ModelsNotebook"
MODELS_NOTEBOOK_TAB = "ModelsNotebookTab"

MODELS_TAB_LOAD_MODEL = "Load"
MODELS_TAB_SAVE_MODEL = "Save"
MODELS_TAB_TRAIN_MODEL = "Train"

MODELS_TAB_MODEL_FRAME = "ModelsTabPlotFrame"
MODELS_TAB_SHOW_TRAINING_ROC = "Training ROC"
MODELS_TAB_SHOW_VALIDATION_ROC = "Validation ROC"
MODELS_TAB_SHOW_TRAINING_LDA = "Training LDA"
MODELS_TAB_SHOW_VALIDATION_LDA = "Validation LDA"

MODELS_TAB_MODEL_DATA = "ModelsTabModelData"
MODELS_TAB_MODEL = "Model"
MODELS_TAB_MIN_MAX = "MinMax"
MODELS_TAB_THRESHOLDS = "Thresholds"

MODELS_TAB_CONTROL_FRAME = "ModelsTabControlFrame"
MODELS_TAB_RECORDING_FOR_TRAINING = "Training"
MODELS_TAB_RECORDING_FOR_VALIDATION = "Validation"

MODELS_TAB_OPTIONS_FRAME = "ClassificationTabOptionsFrame"
MODELS_TAB_LOOK_BACK_LENGTH = "Look back"
MODELS_TAB_CV_FOLDS = "Folds"
MODELS_TAB_FEATURES_TO_USE = "Features"

MODELS_PARSE_OPTIONS = "Options"
MODELS_PARSE_LOOK_BACK_LENGTH = "Look back"
MODELS_PARSE_CV_FOLDS = "Folds"
MODELS_PARSE_FEATURES_TO_USE = "Features"
MODELS_PARSE_RECORDING_FOR_TRAINING = "Training"
MODELS_PARSE_RECORDING_FOR_VALIDATION = "Validation"

MODEL_TRAINED_DISABLER = "Trained"


RECORD_NOTEBOOK = "Results"
RECORD_NOTEBOOK_TAB = "Record"
RECORD_NOTEBOOK_TAB_RESULTS_FRAME = "Results"


CLASSIFICATION_TAB_FRAME = "ClassificationTabFrame"

CLASSIFICATION_TAB_FILTER_OPTIONS_FRAME = "ClassificationTabFilterOptionsFrame"
CLASSIFICATION_TAB_RESULT_FILTER_FRAME = "Results"
CLASSIFICATION_TAB_PREV_RESULT_FILTER_FRAME = "Prev results"

CLASSIFICATION_TAB_ALWAYS_DELETE = "Always delete"
CLASSIFICATION_TAB_RESULT_COUNTER = "No of results"
CLASSIFICATION_TAB_RESULT_THRESHOLD = "Threshold"

CLASSIFICATION_TAB_CONTROL_FRAME = "ClassificationTabControlFrame"

CLASSIFICATION_TAB_TYPE_OPTION_MENU = "Type"
CLASSIFICATION_TYPE_NEW = "New"
CLASSIFICATION_TYPE_OLD = "Old"
CLASSIFICATION_TYPE_NAMES = (CLASSIFICATION_TYPE_NEW, CLASSIFICATION_TYPE_OLD)

CLASSIFICATION_TAB_MODEL_OPTION_MENU = "Model"
CLASSIFICATION_MODEL_NONE = "None"
CLASSIFICATION_MODEL_NAMES = (CLASSIFICATION_MODEL_NONE,)


CLASSIFICATION_PARSE_ACTUAL_RESULTS = "ActualResults"
CLASSIFICATION_PARSE_PREV_RESULTS = "PrevResults"
CLASSIFICATION_PARSE_TYPE = "Type"
CLASSIFICATION_PARSE_MODEL = "Model"


WINDOW_TAB_MONITOR_FRAME = "WindowTabMonitorFrame"
WINDOW_TAB_TARGETS_NOTEBOOK = "WindowTabTargetsNotebook"

TARGETS_NOTEBOOK_TAB = "TargetsTab"
PLOT_NOTEBOOK_TAB = "PlotTab"
EXTRACTION_NOTEBOOK_TAB = "ExtractionTab"

EXTRACTION_TAB_NOTEBOOK = "ExtractionTabNotebook"

# Extraction tab notebook tab names
EXTRACTION_TAB_HARMONICS_TAB = "Harmonics"
EXTRACTION_TAB_OPTIONS_TAB = "Options"
EXTRACTION_TAB_ACTIVE_TAB = "Active"

EXTRACTION_TAB_TARGETS_FRAME = "TargetsFrame"

EXTRACTION_TAB_HARMONIC_WEIGHT = "Weight"
EXTRACTION_TAB_HARMONIC_DIFFERENCE = "Difference"

# Test tab buttons
TEST_TAB_TOTAL_TIME = "Total Time"
TEST_TAB_TIME_PER_TARGET = "Per Target"
TEST_TAB_TIME_PER_TARGET_PLUS_MINUS = "+/-"
TEST_TAB_STANDBY = "Standby"
TEST_TAB_UNLIMITED = "Unlimited"
TEST_TAB_COLOR = "Color"
TEST_TAB_CLEAR_BUFFERS = "Clear buffers"
TEST_TAB_PROCESS_SHORT_SIGNALS = "Process short signals"
TEST_TAB_ALLOW_REPEATING = "Allow repeating"

TEST_TAB_EEG_SOURCE_OPTION_MENU = "Source"
EEG_SOURCE_DEVICE = "Device"
EEG_SOURCE_RECORDED = "Recorded"
EEG_SOURCE_NAMES = (EEG_SOURCE_DEVICE, EEG_SOURCE_RECORDED)

TEST_TAB_TARGET_OPTION_MENU = "Test target"
TEST_TARGET_NONE = "None"
TEST_TARGET_RANDOM = "Random"
TEST_TARGET_TIMED = "Timed"
TEST_TARGET_RECORDING = "Record"
TEST_TARGET_OPTIONS = (TEST_TARGET_NONE, TEST_TARGET_RANDOM, TEST_TARGET_TIMED, TEST_TARGET_RECORDING)

# Window tab buttons
WINDOW_WIDTH = "Width"
WINDOW_HEIGHT = "Height"
WINDOW_COLOR = "Color"
WINDOW_FREQ = "Freq"
WINDOW_REFRESH = "Refresh"
WINDOW_MONITOR = "Monitor"

# Training tab buttons
TRAINING_RECORD = "Record"
TRAINING_SAVE_EEG = "Save"
TRAINING_LOAD_EEG = "Load"

# Training tab options menu
TRAINING_RECORD_NORMAL = "Normal"
TRAINING_RECORD_NEUTRAL = "Neutral"
TRAINING_RECORD_DISABLED = "Disabled"

TRAINING_RECORD_NAMES = (TRAINING_RECORD_DISABLED, TRAINING_RECORD_NORMAL, TRAINING_RECORD_NEUTRAL)

TRAINING_METHOD = "Method"

TRAINING_METHOD_SINGLE = "Single"
TRAINING_METHOD_DE = "DE"
TRAINING_METHOD_BRUTE_FORCE = "Brute force"
TRAINING_METHOD_DE_IDENTIFICATION = "DE Identification"
TRAINING_METHOD_SAVE = "Save"

TRAINING_METHOD_NAMES = (TRAINING_METHOD_SINGLE, TRAINING_METHOD_DE, TRAINING_METHOD_BRUTE_FORCE, TRAINING_METHOD_DE_IDENTIFICATION, TRAINING_METHOD_SAVE)

RECORDING_LENGTH = "Packets"

# Window function names
WINDOW_NONE = "None"
WINDOW_HANNING = "Hann"
WINDOW_HAMMING = "Hamming"
WINDOW_BLACKMAN = "Blackman"
WINDOW_KAISER = "Kaiser"
WINDOW_BARTLETT = "Bartlett"

WINDOW_FUNCTION_NAMES = (WINDOW_NONE, WINDOW_HANNING, WINDOW_HAMMING, WINDOW_BLACKMAN, WINDOW_KAISER, WINDOW_BARTLETT)

# Arguments for sgipy.signal.get_window()
# boxcar, triang, blackman, hamming, hann, bartlett, flattop, parzen,
# bohman, blackmanharris, nuttall, barthann, kaiser (needs beta), gaussian (needs std),
# general_gaussian (needs power, width), slepian (needs width), chebwin (needs attenuation)

SCIPY_WINDOW_HANNING = "hann"
SCIPY_WINDOW_HAMMING = "hamming"
SCIPY_WINDOW_BLACKMAN = "blackmanharris"
SCIPY_WINDOW_KAISER = "kaiser"
SCIPY_WINDOW_BARTLETT = "bartlett"

# Interpolation function names
INTERPOLATE_LINEAR = "Linear"
INTERPOLATE_NEAREST = "Nearest"
INTERPOLATE_ZERO = "Zero"
INTERPOLATE_SLINEAR = "Slinear"
INTERPOLATE_QUADRATIC = "Quadratic"
INTERPOLATE_CUBIC = "Cubic"
INTERPOLATE_BARYCENTRIC = "Barycentric"

INTERPOLATE_NAMES = (INTERPOLATE_LINEAR, INTERPOLATE_NEAREST, INTERPOLATE_ZERO, INTERPOLATE_SLINEAR, INTERPOLATE_QUADRATIC, INTERPOLATE_CUBIC, INTERPOLATE_BARYCENTRIC)

# Arguments for scipy.interpolate.interp1d
# linear, nearest, zero, slinear, quadratic, cubic

SCIPY_INTERPOLATE_LINEAR = "linear"
SCIPY_INTERPOLATE_NEAREST = "nearest"
SCIPY_INTERPOLATE_ZERO = "zero"
SCIPY_INTERPOLATE_SLINEAR = "slinear"
SCIPY_INTERPOLATE_QUADRATIC = "quadratic"
SCIPY_INTERPOLATE_CUBIC = "cubic"

# Plot and Extraction tab options frame buttons
OPTIONS_NORMALISE = "Normalise"
OPTIONS_LOG10 = "Log10"
OPTIONS_DETREND = "Detrend"
OPTIONS_FILTER = "Filter"
OPTIONS_STEP = "Step"
OPTIONS_LENGTH = "Length"
OPTIONS_FROM = "From"
OPTIONS_TO = "To"
OPTIONS_TAPS = "Taps"
OPTIONS_ARG = "Arg"
OPTIONS_WINDOW = "Window"
OPTIONS_BREAK = "Break"
OPTIONS_INTERPOLATE = "Interp"

METHODS_FRAME = "Methods"

MAIN_FRAME = "MainFrame"
BOTTOM_FRAME = "BottomFrame"

PLUS_MINUS_FRAME = "PlusMinusFrame"
RADIOBUTTON_FRAME = "RadiobuttonFrame"
DISABLE_DELETE_FRAME = "DisableDeleteFrame"

TARGET_FRAME = "TargetFrame"
RESULT_FRAME = "ResultFrame"

# Color textbox's textbox name
TEXTBOX = "Textbox"

# Target tab buttons
TARGET_FREQ = "Freq"
TARGET_DELAY = "Delay"
TARGET_WIDTH = "Width"
TARGET_HEIGHT = "Height"
TARGET_COLOR1 = "Color1"
TARGET_X = "x"
TARGET_Y = "y"
TARGET_COLOR0 = "Color0"
TARGET_SEQUENCE = "Sequence"
TARGET_TYPE = "Type"

# Target types optionmenu
RECTANGLE_TARGET = "Rectangle"
CHECKERBOARD_TARGET = "Checkerboard"

TARGET_TYPE_NAMES = (CHECKERBOARD_TARGET, RECTANGLE_TARGET)

# Detrend optionmenu
CONSTANT_DETREND = "Constant"
LINEAR_DETREND = "Linear"
NONE_DETREND = "None"

DETREND_NAMES = (LINEAR_DETREND, CONSTANT_DETREND, NONE_DETREND)

# Filter optionmenu
NONE_FILTER = "None"
LOWPASS_FILTER = "Low-pass"
HIGHPASS_FILTER = "High-pass"
BANDPASS_FILTER = "Band-pass"

FILTER_NAMES = (NONE_FILTER, LOWPASS_FILTER, HIGHPASS_FILTER, BANDPASS_FILTER)

# Plus minus frame buttons
PLUS = "+"
MINUS = " -"

# Disable and Delete frame buttons
DISABLE = "Disable"
DELETE = "Delete"

# Bottom frame buttons
START_BUTTON = "Start"
STOP_BUTTON = "Stop"
SAVE_BUTTON = "Save"
LOAD_BUTTON = "Load"
EXIT_BUTTON = "Exit"
SETUP_BUTTON = "Setup"

# Extraction method buttons
PSDA = "PSDA"
SUM_PSDA = "Sum PSDA"
SNR_PSDA = "SNR PSDA"
CCA = "CCA"
LRT = "LRT"

EXTRACTION_METHOD_NAMES = (PSDA, SUM_PSDA, SNR_PSDA, CCA, LRT)  # Fixes the order for CSV files

# Plot type buttons
SIGNAL = "Signal"
SUM_SIGNAL = "Sum signal"
AVG_SIGNAL = "Avg signal"
SUM_AVG_SIGNAL = "Sum avg signal"
POWER = "Power"
SUM_POWER = "Sum power"
AVG_POWER = "Avg power"
SUM_AVG_POWER = "Sum avg power"

# Names of the classes
MULTIPLE_REGULAR = "MultipleRegular"
MULTIPLE_AVERAGE = "MultipleAverage"
SINGLE_REGULAR = "SingleRegular"
SINGLE_AVERAGE = "SingleAverage"

# Same tab notebook tab initial buttons
ALL_TAB = "All"
PLUS_TAB = "+"

SENSORS_FRAME = "Sensors"
OPTIONS_FRAME = "Options"

# Sensor names in Plot and Extraction tab
# NB order is important, it is used in writing csv files
SENSORS = ("AF3", "F7", "F3", "FC5","T7", "P7", "O1", "O2", "P8", "T8", "FC6","F4", "F8", "AF4")

HEADSET_FREQ = 128

# Messages to PostOffice
START_MESSAGE = "Start"
STOP_MESSAGE = "Stop"
EXIT_MESSAGE = "Exit"
CLOSE_MESSAGE = "Close"  # TODO What is this?
SETUP_MESSAGE = "Setup"

BCI_CONTROL_MESSAGES = (START_MESSAGE, STOP_MESSAGE, SETUP_MESSAGE)

GET_RESULTS_MESSAGE = "Get results"
GET_NEW_RESULTS_MESSAGE = "Get new results"
GET_RECORDED_EEG_MESSAGE = "Get EEG"
GET_RECORDED_FEATURES_MESSAGE = "Get features"
GET_RECORDED_FREQUENCIES_MESSAGE = "Get target frequencies"

BCI_DATA_EXCHANGE_MESSAGES = (GET_RESULTS_MESSAGE, GET_NEW_RESULTS_MESSAGE, GET_RECORDED_EEG_MESSAGE, GET_RECORDED_FEATURES_MESSAGE, GET_RECORDED_FREQUENCIES_MESSAGE)

SEND_RECORDED_FEATURES_MESSAGE = "sendFeatures"
SEND_CLASSIFICATION_OPTIONS = "sendClassificationOptions"
TRAINING_START_MESSAGE = "TrainingStart"

GET_MODEL_MESSAGE = "GetModel"
GET_VALIDATION_DATA_MESSAGE = "GetValidationData"
GET_VALIDATION_LABELS_MESSAGE = "GetValidationLabels"
GET_TRAINING_DATA_MESSAGE = "GetTrainingData"
GET_TRAINING_LABELS_MESSAGE = "GetTrainingLabels"
GET_THRESHOLDS_MESSAGE = "GetThresholds"
GET_TRAINING_ROC_MESSAGE = "GetTrainingRoc"
GET_VALIDATION_ROC_MESSAGE = "GetValidationRoc"
GET_MIN_MAX_MESSAGE = "GetMinMax"
GET_USED_FEATURES_MESSAGE = "GetUsedFeatures"

SETUP_FAILED_MESSAGE = "Failed"
SETUP_SUCCEEDED_MESSAGE = "Success"
BCI_STOPPED_MESSAGE = "BciStopped"
TRAINING_STOPPED_MESSAGE = "TrainingStopped"

MAIN_WINDOW_MESSAGES = (BCI_STOPPED_MESSAGE, SETUP_SUCCEEDED_MESSAGE, SETUP_FAILED_MESSAGE, TRAINING_STOPPED_MESSAGE)

TRAINING_SEND_DATA_MESSAGES = (SEND_RECORDED_FEATURES_MESSAGE, SEND_CLASSIFICATION_OPTIONS)
TRAINING_GET_DATA_MESSAGES = (GET_MODEL_MESSAGE, GET_VALIDATION_DATA_MESSAGE, GET_VALIDATION_LABELS_MESSAGE, GET_TRAINING_DATA_MESSAGE, GET_TRAINING_LABELS_MESSAGE, GET_THRESHOLDS_MESSAGE, GET_MIN_MAX_MESSAGE, GET_TRAINING_ROC_MESSAGE, GET_VALIDATION_ROC_MESSAGE, GET_USED_FEATURES_MESSAGE)
TRAINING_DATA_EXCHANGE_MESSAGES = TRAINING_SEND_DATA_MESSAGES + TRAINING_GET_DATA_MESSAGES
TRAINING_CONTROL_MESSAGES = (TRAINING_START_MESSAGE,)

TRAINING_MESSAGES = TRAINING_DATA_EXCHANGE_MESSAGES + TRAINING_CONTROL_MESSAGES

BCI_MESSAGES = BCI_CONTROL_MESSAGES + BCI_DATA_EXCHANGE_MESSAGES

MOVE_LEFT = "1"
MOVE_RIGHT = "2"
MOVE_FORWARD = "3"
MOVE_BACKWARD = "4"
MOVE_STOP = "0"

ROBOT_MESSAGES = (MOVE_BACKWARD, MOVE_FORWARD, MOVE_LEFT, MOVE_RIGHT, MOVE_STOP)

POST_OFFICE_MESSAGES = BCI_MESSAGES + TRAINING_MESSAGES + (EXIT_MESSAGE,) + ROBOT_MESSAGES

CLEAR_BUFFER_MESSAGE = "ClearBuffer"

# By default load values from this file
DEFAULT_SETTINGS_FILE_NAME = "default123.txt"  # TODO change back
DEFAULT_TRAINING_SETTINGS_FILE_NAME = "traindefault.txt"

DATA_BACKGROUND = "Background"
DATA_TARGETS = "Targets"
DATA_FREQS = "Freqs"
DATA_PLOTS = "Plots"
DATA_EXTRACTION = "Extraction"
DATA_CLASSIFICATION = "Classification"
DATA_MODEL = "Model"
DATA_HARMONICS = "Harmonics"
DATA_ROBOT = "Robot"
DATA_TEST = "Test"
DATA_RECORD = "Record"
DATA_TRAINING = "Training"

DATA_SENSORS = SENSORS_FRAME
DATA_OPTIONS = OPTIONS_FRAME
DATA_METHODS = METHODS_FRAME

DATA_METHOD = "Method"

DATA_FREQ = "Freq"

DATA_EXTRACTION_WEIGHTS = "Weights"
DATA_EXTRACTION_DIFFERENCES = "Differences"

DATA_EXTRACTION_TARGETS = DATA_FREQS
DATA_EXTRACTION_SENSORS = DATA_SENSORS
DATA_EXTRACTION_METHODS = DATA_METHODS
DATA_EXTRACTION_OPTIONS = DATA_OPTIONS

DATA_WEIGHT_THRESHOLD = "Counter"
DATA_TARGET_THRESHOLD = "Result"
DATA_CLEAR_BUFFERS = "ClearBuffer"
DATA_ALWAYS_DELETE = "AlwaysDelete"
DATA_PROCESS_SHORT_SIGNAL = "ProcessShortSignal"

CONNECTION_EMOTIV = "Emotiv"
CONNECTION_PSYCHOPY = "Psychopy"
CONNECTION_ROBOT = "Robot"
CONNECTION_PLOT = "Plot"
CONNECTION_EXTRACTION = "Extraction"

CONNECTION_EMOTIV_NAME = "Emotiv"
CONNECTION_PSYCHOPY_NAME = "Psychopy"
CONNECTION_PLOT_NAME = "Plot"
CONNECTION_EXTRACTION_NAME = "Extraction"
CONNECTION_MAIN_NAME = "Main"
CONNECTION_ROBOT_NAME = "Robot"

RESULT_SUM = "Sum"

ROBOT_OPTION_FORWARD = "Forward"
ROBOT_OPTION_BACKWARD = "Backward"
ROBOT_OPTION_RIGHT = "Right"
ROBOT_OPTION_LEFT = "Left"
ROBOT_OPTION_STOP = "Stop"

ROBOT_TEST = "Test"
ROBOT_NONE = "None"

ROBOT_STREAM = "Stream"
STREAM_X = "x"
STREAM_Y = "y"
STREAM_WIDTH = "Width"
STREAM_HEIGHT = "Height"


EEG_RECORDING_FREQS = "TargetFreqs"
EEG_RECORDING_PACKETS = "Packets"
EEG_RECORDING_EXPECTED_TARGETS = "ExpectedTargets"


# Results data dict keys

RESULTS_DATA_TOTAL_TIME_PACKETS = "Packets"
RESULTS_DATA_TOTAL_TIME_SECONDS = "Time"
RESULTS_DATA_TIME_PER_TARGET = "sec/trial"
RESULTS_DATA_ACCURACY = "Accuracy"
RESULTS_DATA_DIAGONAL_ELEMENTS = "Diagonal"
RESULTS_DATA_OFF_DIAGONAL_ELEMENTS = "Off"
RESULTS_DATA_ITR_BIT_PER_TRIAL = "bit/trial"
RESULTS_DATA_ITR_BIT_PER_MIN = "bit/min"
RESULTS_DATA_MACRO_F1 = "Macro F1"
RESULTS_DATA_F1 = "F1"

TIMESTAMP_TEXTBOX = "Timestamp"
DIRECTORY_TEXTBOX = "Directory"

EEG_FRAME = "EegFrame"
PACKET_COUNT = "Packets"
SAMPLE_COUNT = "Samples"


CSV_TRUE_LABEL = "True"
CSV_PREDICTED_LABEL = "Predicted"
CSV_PACKET_NUMBER = "Packet"

CSV_LABEL_FILE_HEADER = (CSV_PACKET_NUMBER, CSV_TRUE_LABEL, CSV_PREDICTED_LABEL)


STOP_EVENT_SENDING = "StopSending"
