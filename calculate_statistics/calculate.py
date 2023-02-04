import tkinter as tk
from tkinter.messagebox import showwarning
from numpy import sum, percentile, mean, array
import statistics as stats
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

INPUT_TEXTBOX = None

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "#242424",
    "text.color": "white",
    "axes.facecolor": "#242424",
    "axes.edgecolor": "#242424",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "#242424",
    "figure.facecolor": "#242424",
    "figure.edgecolor": "#242424",
    "savefig.facecolor": "#242424",
    "savefig.edgecolor": "#242424"})


def calculate_and_show_stats(window) -> None:
    SUM_NUMBER = tk.IntVar()
    MINIMUM_NUMBER = tk.IntVar()
    MAXIMUM_NUMBER = tk.IntVar()
    AVERAGE_NUMBER = tk.IntVar()
    MEDIAN_NUMBER = tk.IntVar()
    MODE_NUMBER = tk.IntVar()
    RANGE_NUMBER = tk.IntVar()
    MIDRANGE_NUMBER = tk.IntVar()
    POPULATION_STANDARD_DEVIATION = tk.IntVar()
    SAMPLE_STANDARD_DEVIATION = tk.IntVar()
    POPULATION_VARIANCE = tk.IntVar()
    SAMPLE_VARIANCE = tk.IntVar()
    QUARTILE_25 = tk.IntVar()
    QUARTILE_50 = tk.IntVar()
    QUARTILE_75 = tk.IntVar()
    INTERQUARTILE_RANGE = tk.IntVar()

    OUTPUT_FONTSIZE = 15
    DEFAULT_FONTSTYLE = "Courier New"
    global INPUT_TEXTBOX

    RETRIEVED_USER_INPUT = INPUT_TEXTBOX.get("1.0", 'end-1c')
    LIST_OF_NUMBERS = []

    for numbers in RETRIEVED_USER_INPUT.split(','):
        numbers = numbers.strip()
        if numbers.lstrip('-').isnumeric():
            LIST_OF_NUMBERS.append(int(numbers))

    if len(LIST_OF_NUMBERS) > 2_500:
        WARNING_TITLE = "Warning!"
        WARNING_MESSEGE = "Please, Enter less than 10,000 values!"
        showwarning(WARNING_TITLE, WARNING_MESSEGE)
    elif len(LIST_OF_NUMBERS) <= 1:
        WARNING_TITLE = "Warning!"
        WARNING_MESSEGE = "Please, Enter more than 1 values!"
        showwarning(WARNING_TITLE, WARNING_MESSEGE)
    else:
        SUM_NUMBER.set(sum(LIST_OF_NUMBERS))
        SUMMATION_OUTPUT = customtkinter.CTkLabel(window, textvariable=SUM_NUMBER)
        SUMMATION_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        SUMMATION_OUTPUT.place(x=555, y=42)

        MINIMUM_NUMBER.set(min(LIST_OF_NUMBERS))
        MINIMUM_NUMBER_OUTPUT = customtkinter.CTkLabel(window, textvariable=MINIMUM_NUMBER)
        MINIMUM_NUMBER_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MINIMUM_NUMBER_OUTPUT.place(x=515, y=70)

        MAXIMUM_NUMBER.set(max(LIST_OF_NUMBERS))
        MAXIMUM_NUMBER_OUTPUT = customtkinter.CTkLabel(window, textvariable=MAXIMUM_NUMBER)
        MAXIMUM_NUMBER_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MAXIMUM_NUMBER_OUTPUT.place(x=515, y=100)

        AVERAGE_NUMBER.set(round(mean(LIST_OF_NUMBERS), 3))
        MEAN_LABEL_OUTPUT = customtkinter.CTkLabel(window, textvariable=AVERAGE_NUMBER)
        MEAN_LABEL_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MEAN_LABEL_OUTPUT.place(x=494, y=130)

        MEDIAN_NUMBER.set(stats.median(LIST_OF_NUMBERS))
        MEDIAN_LABEL_OUTPUT = customtkinter.CTkLabel(window, textvariable=MEDIAN_NUMBER)
        MEDIAN_LABEL_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MEDIAN_LABEL_OUTPUT.place(x=505, y=160)

        MODE_NUMBER.set(stats.mode(LIST_OF_NUMBERS))
        MODE_NUMBER_OUTPUT = customtkinter.CTkLabel(window, textvariable=MODE_NUMBER)
        MODE_NUMBER_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MODE_NUMBER_OUTPUT.place(x=140, y=210)

        RANGE_NUMBER.set(MAXIMUM_NUMBER.get() - MINIMUM_NUMBER.get())
        RANGE_NUMBER_OUTPUT = customtkinter.CTkLabel(window, textvariable=RANGE_NUMBER)
        RANGE_NUMBER_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        RANGE_NUMBER_OUTPUT.place(x=144, y=240)

        MIDRANGE_NUMBER.set(RANGE_NUMBER.get() / 2)
        MIDRANGE_NUMBER_OUTPUT = customtkinter.CTkLabel(window, textvariable=MIDRANGE_NUMBER)
        MIDRANGE_NUMBER_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        MIDRANGE_NUMBER_OUTPUT.place(x=170, y=270)

        POPULATION_STANDARD_DEVIATION.set((round(stats.pstdev(LIST_OF_NUMBERS), 3)))
        POPULATION_STANDARD_DEVIATION_OUTPUT = customtkinter.CTkLabel(window,
                                                                      textvariable=POPULATION_STANDARD_DEVIATION)
        POPULATION_STANDARD_DEVIATION_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        POPULATION_STANDARD_DEVIATION_OUTPUT.place(x=250, y=300)

        SAMPLE_STANDARD_DEVIATION.set((round(stats.stdev(LIST_OF_NUMBERS), 3)))
        SAMPLE_STANDARD_DEVIATION_OUTPUT = customtkinter.CTkLabel(window, textvariable=SAMPLE_STANDARD_DEVIATION)
        SAMPLE_STANDARD_DEVIATION_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        SAMPLE_STANDARD_DEVIATION_OUTPUT.place(x=205, y=330)

        POPULATION_VARIANCE.set((round(stats.pvariance(LIST_OF_NUMBERS), 3)))
        POPULATION_VARIANCE_OUTPUT = customtkinter.CTkLabel(window, textvariable=POPULATION_VARIANCE)
        POPULATION_VARIANCE_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        POPULATION_VARIANCE_OUTPUT.place(x=325, y=360)

        SAMPLE_VARIANCE.set((round(stats.variance(LIST_OF_NUMBERS), 3)))
        SAMPLE_VARIANCE_OUTPUT = customtkinter.CTkLabel(master=window, textvariable=SAMPLE_VARIANCE)
        SAMPLE_VARIANCE_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        SAMPLE_VARIANCE_OUTPUT.place(x=275, y=390)

        PERCENTILE_25TH = 25
        PERCENTILE_50TH = 50
        PERCENTILE_75TH = 75

        Q25, Q50, Q75 = percentile(LIST_OF_NUMBERS, [PERCENTILE_25TH, PERCENTILE_50TH, PERCENTILE_75TH])

        QUARTILE_25.set(Q25)
        QUARTILE_25_OUTPUT = customtkinter.CTkLabel(window, textvariable=QUARTILE_25)
        QUARTILE_25_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        QUARTILE_25_OUTPUT.place(x=175, y=445)

        QUARTILE_50.set(Q50)
        QUARTILE_50_OUTPUT = customtkinter.CTkLabel(window, textvariable=QUARTILE_50)
        QUARTILE_50_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        QUARTILE_50_OUTPUT.place(x=175, y=470)

        QUARTILE_75.set(Q75)
        QUARTILE_75_OUTPUT = customtkinter.CTkLabel(window, textvariable=QUARTILE_75)
        QUARTILE_75_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        QUARTILE_75_OUTPUT.place(x=175, y=500)

        INTERQUARTILE_RANGE.set(QUARTILE_75.get() - QUARTILE_25.get())
        INTERQUARTILE_RANGE_OUTPUT = customtkinter.CTkLabel(window, textvariable=INTERQUARTILE_RANGE)
        INTERQUARTILE_RANGE_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, OUTPUT_FONTSIZE, 'underline'))
        INTERQUARTILE_RANGE_OUTPUT.place(x=305, y=525)

        PLOT_WIDTH = 5.5
        PLOT_HEIGHT = 3.5
        PLOT_TITLE = 'KDE Plot'
        PLOT_XLABEL = 'Density'
        PLOT_FONTSIZE = 12

        FIGURE, AXES = plt.subplots(figsize=(PLOT_WIDTH, PLOT_HEIGHT))

        plt.title(PLOT_TITLE, fontsize=PLOT_FONTSIZE, font=DEFAULT_FONTSTYLE)
        plt.ylabel(PLOT_XLABEL, fontsize=PLOT_FONTSIZE, font=DEFAULT_FONTSTYLE)

        HISTOGRAM = FigureCanvasTkAgg(FIGURE, window)
        HISTOGRAM.get_tk_widget().place(x=390, y=205)

        sns.kdeplot(array(LIST_OF_NUMBERS))


def textbox_input(FRAME) -> None:
    global INPUT_TEXTBOX
    INPUT_TEXTBOX = customtkinter.CTkTextbox(FRAME, height=100, width=300)
    INPUT_TEXTBOX.place(x=20, y=15)
