import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import showwarning
from numpy import sum, percentile, mean, array
import statistics as stats
from scipy.stats import skew
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from seaborn import kdeplot

# global variables
INPUT_TEXTBOX = None
DATAGROUP_OPTION = None

DEFAULT_FONTSIZE = 15
DEFAULT_FONTSTYLE = "Calibri Light"

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


class CalculateAndShow:

    def __init__(self, window: ctk.CTk, result_var: ctk.IntVar, x: int, y: int):
        self.window = window
        self.result_var = result_var
        self.x = x
        self.y = y

    @staticmethod
    def calculate_stats(master: ctk.CTk, **tkvariables_: ctk.IntVar) -> None:
        global INPUT_TEXTBOX
        RETRIEVED_USER_INPUT = INPUT_TEXTBOX.get("1.0", 'end-1c')
        LIST_OF_NUMBERS = []

        for numbers in RETRIEVED_USER_INPUT.split(','):
            numbers = numbers.strip()
            if numbers.lstrip('-').isnumeric():
                LIST_OF_NUMBERS.append(int(numbers))

        if len(LIST_OF_NUMBERS) > 2_500:
            WARNING_TITLE = "Warning!"
            WARNING_MESSEGE = "Please, Enter less than 2,500 values!"
            showwarning(WARNING_TITLE, WARNING_MESSEGE)
        elif len(LIST_OF_NUMBERS) <= 1:
            WARNING_TITLE = "Warning!"
            WARNING_MESSEGE = "Please, Enter more than 1 values!"
            showwarning(WARNING_TITLE, WARNING_MESSEGE)
        else:
            tkvariables_['SUMM'].set(sum(LIST_OF_NUMBERS))
            tkvariables_['MINN'].set(min(LIST_OF_NUMBERS))
            tkvariables_['MAXX'].set(max(LIST_OF_NUMBERS))
            tkvariables_['AVG'].set(round(mean(LIST_OF_NUMBERS), 3))
            tkvariables_['MEDIAN'].set(stats.median(LIST_OF_NUMBERS))
            tkvariables_['MODE'].set(stats.mode(LIST_OF_NUMBERS))
            tkvariables_['RANGE'].set(tkvariables_['MAXX'].get() - tkvariables_['MINN'].get())
            tkvariables_['MIDRANGE'].set(tkvariables_['RANGE'].get() / 2)

            global DATAGROUP_OPTION
            if DATAGROUP_OPTION == 'Population':
                tkvariables_['STD'].set((round(stats.pstdev(LIST_OF_NUMBERS), 3)))
                tkvariables_['VAR'].set((round(stats.pvariance(LIST_OF_NUMBERS), 3)))
            elif DATAGROUP_OPTION == 'Sample':
                tkvariables_['STD'].set((round(stats.stdev(LIST_OF_NUMBERS), 3)))
                tkvariables_['VAR'].set((round(stats.variance(LIST_OF_NUMBERS)), 3))

            tkvariables_['SKEW'].set((round(skew(LIST_OF_NUMBERS, axis=0, bias=True), 3)))
            tkvariables_['SIZE_'].set(len(LIST_OF_NUMBERS))

            PERCENTILE_25TH = 25
            PERCENTILE_50TH = 50
            PERCENTILE_75TH = 75
            Q25_, Q50_, Q75_ = percentile(LIST_OF_NUMBERS, [PERCENTILE_25TH, PERCENTILE_50TH, PERCENTILE_75TH])

            tkvariables_['Q25'].set(Q25_)
            tkvariables_['Q50'].set(Q50_)
            tkvariables_['Q75'].set(Q75_)
            tkvariables_['IQR'].set(tkvariables_['Q75'].get() - tkvariables_['Q25'].get())

            global DEFAULT_FONTSIZE, DEFAULT_FONTSTYLE
            PLOT_WIDTH = 5.5
            PLOT_HEIGHT = 3.5
            PLOT_TITLE = 'Kernel Density Plot'
            PLOT_FONTSIZE = 12

            FIGURE, AXES = plt.subplots(figsize=(PLOT_WIDTH, PLOT_HEIGHT))

            plt.title(PLOT_TITLE, fontsize=PLOT_FONTSIZE, font=DEFAULT_FONTSTYLE)

            KDE_PLOT = FigureCanvasTkAgg(FIGURE, master)
            KDE_PLOT.get_tk_widget().place(x=390, y=205)

            SEABORN_PLOT = kdeplot(array(LIST_OF_NUMBERS), color='#2FA572')
            SEABORN_PLOT.set(ylabel=None)
            plt.close('all')

    def show_calculations(self):
        global DEFAULT_FONTSIZE, DEFAULT_FONTSTYLE

        RESULT_OUTPUT = ctk.CTkLabel(self.window, textvariable=self.result_var)
        RESULT_OUTPUT.configure(font=(DEFAULT_FONTSTYLE, DEFAULT_FONTSIZE))
        RESULT_OUTPUT.place(x=self.x, y=self.y)


def textbox_input(frame: ctk.CTkFrame) -> None:
    global INPUT_TEXTBOX
    INPUT_TEXTBOX = ctk.CTkTextbox(frame, height=100, width=300, undo=True, autoseparators=True, maxundo=-1)
    INPUT_TEXTBOX.place(x=20, y=15)


def option_setter(variable: ctk.StringVar) -> None:
    global DATAGROUP_OPTION
    DATAGROUP_OPTION = variable.get()


def population_button(frame: ctk.CTkFrame, population_option: ctk.StringVar) -> None:
    global DEFAULT_FONTSIZE, DEFAULT_FONTSTYLE
    CHANGE_DATAGROUP_OPTION = 'Population'
    RADIOBUTTON_TITLE = 'Population'
    POPULATION_RADIOBUTTON = ctk.CTkRadioButton(master=frame, variable=population_option,
                                                value=CHANGE_DATAGROUP_OPTION,
                                                text=RADIOBUTTON_TITLE, radiobutton_height=15, radiobutton_width=15,
                                                command=lambda: option_setter(
                                                    population_option), font=(DEFAULT_FONTSTYLE, DEFAULT_FONTSIZE))
    POPULATION_RADIOBUTTON.place(x=17, y=125)


def sample_button(frame: ctk.CTkFrame, sample_option: ctk.StringVar) -> None:
    global DEFAULT_FONTSIZE, DEFAULT_FONTSTYLE
    CHANGE_DATAGROUP_OPTION = 'Sample'
    RADIOBUTTON_TITLE = 'Sample'
    SAMPLE_RADIOBUTTON = ctk.CTkRadioButton(master=frame,
                                            variable=sample_option, value=CHANGE_DATAGROUP_OPTION,
                                            text=RADIOBUTTON_TITLE, radiobutton_height=15, radiobutton_width=15,
                                            command=lambda: option_setter(
                                                sample_option), font=(DEFAULT_FONTSTYLE, DEFAULT_FONTSIZE))
    SAMPLE_RADIOBUTTON.place(x=17, y=145)