import tkinter as tk
import customtkinter as ctk
import matplotlib.font_manager
import calculate
import sys


def main() -> None:
    MAIN_WINDOW = ctk.CTk()

    ROOT_GEOMETRY = "900x570"
    MAIN_WINDOW.geometry(ROOT_GEOMETRY)

    APP_TITLE = "PyCalStat"
    MAIN_WINDOW.title(APP_TITLE)

    MAX_WINDOW_WIDTH = 900
    MAX_WINDOW_HEIGHT = 570
    MAIN_WINDOW.minsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)
    MAIN_WINDOW.maxsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)

    DEFAULT_COLOR_THEME = 'green'
    ctk.set_default_color_theme(DEFAULT_COLOR_THEME)

    SUM_NUMBER = ctk.IntVar()
    MINIMUM_NUMBER = ctk.IntVar()
    MAXIMUM_NUMBER = ctk.IntVar()
    AVERAGE_NUMBER = ctk.IntVar()
    MEDIAN_NUMBER = ctk.IntVar()
    MODE_NUMBER = ctk.IntVar()
    RANGE_NUMBER = ctk.IntVar()
    MIDRANGE_NUMBER = ctk.IntVar()
    STANDARD_DEVIATION = ctk.IntVar()
    VARIANCE = ctk.IntVar()
    SKEWNESS = ctk.IntVar()
    SIZE = ctk.IntVar()
    QUARTILE_25 = ctk.IntVar()
    QUARTILE_50 = ctk.IntVar()
    QUARTILE_75 = ctk.IntVar()
    INTERQUARTILE_RANGE = ctk.IntVar()

    BOX_AND_BUTTON_FRAME = ctk.CTkFrame(master=MAIN_WINDOW, height=170, width=350)
    BOX_AND_BUTTON_FRAME.place(rely=0.07, relx=0.05)

    DEFAULT_FONTSTYLE = "Calibri Light"
    DEFAULT_FONTSIZE = 20

    DEFAULT_OPTION = 'Sample'
    SAMPLE_OR_POPULATION_OPTION = tk.StringVar(value=DEFAULT_OPTION)

    class ShowCalculationLabels:
        def __init__(self, x: int, y: int, LABEL_TITLE: str):
            self.x = x
            self.y = y
            self.LABEL_TITLE = LABEL_TITLE

        def window_labels(self) -> None:
            CALCULATION_LABELS = ctk.CTkLabel(MAIN_WINDOW, text=self.LABEL_TITLE,
                                              font=(DEFAULT_FONTSTYLE, DEFAULT_FONTSIZE))
            CALCULATION_LABELS.place(x=self.x, y=self.y)

    class ShowButton:

        @staticmethod
        def show_results(results_height: int, results_width: int, button_text: str) -> None:
            CALCULATION_BUTTON = ctk.CTkButton(master=BOX_AND_BUTTON_FRAME, height=results_height, width=results_width,
                                               text=button_text, command=lambda: [
                    calculate.CalculateAndShow.calculate_stats(MAIN_WINDOW, SUMM=SUM_NUMBER, MINN=MINIMUM_NUMBER,
                                                               MAXX=MAXIMUM_NUMBER, AVG=AVERAGE_NUMBER,
                                                               MEDIAN=MEDIAN_NUMBER, MODE=MODE_NUMBER,
                                                               RANGE=RANGE_NUMBER, MIDRANGE=MIDRANGE_NUMBER,
                                                               STD=STANDARD_DEVIATION, VAR=VARIANCE, SKEW=SKEWNESS,
                                                               SIZE_=SIZE, Q25=QUARTILE_25,
                                                               Q50=QUARTILE_50, Q75=QUARTILE_75,
                                                               IQR=INTERQUARTILE_RANGE)], font=(DEFAULT_FONTSTYLE, 15))
            CALCULATION_BUTTON.place(x=200, y=125)

    calculate.textbox_input(BOX_AND_BUTTON_FRAME)

    FRONT_TITLE = ShowCalculationLabels(370, 0, 'PyCalStat')

    calculate.option_setter(SAMPLE_OR_POPULATION_OPTION)
    calculate.population_button(BOX_AND_BUTTON_FRAME, SAMPLE_OR_POPULATION_OPTION)
    calculate.sample_button(BOX_AND_BUTTON_FRAME, SAMPLE_OR_POPULATION_OPTION)

    SUMMATION_LABEL = ShowCalculationLabels(x=405, y=42, LABEL_TITLE='Summation :')
    MIN_NUMBER_LABEL = ShowCalculationLabels(x=405, y=70, LABEL_TITLE='Minimum :')
    MAX_NUMBER_LABEL = ShowCalculationLabels(x=405, y=100, LABEL_TITLE='Maximum :')
    AVERAGE_LABEL = ShowCalculationLabels(x=405, y=130, LABEL_TITLE='Mean μ :')
    MEDIAN_LABEL = ShowCalculationLabels(x=405, y=160, LABEL_TITLE='Median :')
    MODE_LABEL = ShowCalculationLabels(x=45, y=210, LABEL_TITLE='Mode :')
    RANGE_LABEL = ShowCalculationLabels(x=45, y=240, LABEL_TITLE='Range :')
    MIDRANGE_LABEL = ShowCalculationLabels(x=45, y=270, LABEL_TITLE='Midrange :')
    VARIANCE_LABEL = ShowCalculationLabels(x=45, y=300, LABEL_TITLE='Variance :')
    STANDARD_DEV_LABEL = ShowCalculationLabels(x=45, y=330, LABEL_TITLE='Standard Dev :')
    SKEW_LABEL = ShowCalculationLabels(x=45, y=360, LABEL_TITLE='Skewness :')
    SIZE_LABEL = ShowCalculationLabels(x=45, y=390, LABEL_TITLE='Size :')
    QUARTILE_TITLE = ShowCalculationLabels(x=45, y=420, LABEL_TITLE='Quartiles')
    QUARTILE_25_LABEL = ShowCalculationLabels(x=100, y=445, LABEL_TITLE='Q25 :')
    QUARTILE_50_LABEL = ShowCalculationLabels(x=100, y=470, LABEL_TITLE='Q50 :')
    QUARTILE_75_LABEL = ShowCalculationLabels(x=100, y=500, LABEL_TITLE='Q75 :')
    INTERQUARTILE_RANGE_LABEL = ShowCalculationLabels(x=45, y=525, LABEL_TITLE='Interquartile Range :')

    SUMMATION_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, SUM_NUMBER, 515, 42)
    MINIMUM_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, MINIMUM_NUMBER, 500, 70)
    MAXIMUM_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, MAXIMUM_NUMBER, 500, 100)
    AVERAGE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, AVERAGE_NUMBER, 485, 130)
    MEDIAN_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, MEDIAN_NUMBER, 485, 160)
    MODE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, MODE_NUMBER, 110, 210)
    RANGE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, RANGE_NUMBER, 115, 240)
    MIDRANGE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, MIDRANGE_NUMBER, 140, 270)
    VARIANCE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, VARIANCE, 135, 300)
    STANDARD_DEVIATION_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, STANDARD_DEVIATION, 170, 330)
    SKEWNESS_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, SKEWNESS, 140, 360)
    SIZE_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, SIZE, 95, 390)
    QUARTILE_25_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, QUARTILE_25, 150, 445)
    QUARTILE_50_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, QUARTILE_50, 150, 470)
    QUARTILE_75_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, QUARTILE_75, 150, 500)
    IQR_OUTPUT = calculate.CalculateAndShow(MAIN_WINDOW, INTERQUARTILE_RANGE, 220, 525)

    ShowButton.show_results(32, 120, 'Calculate')

    FRONT_TITLE.window_labels()
    SUMMATION_LABEL.window_labels()
    MIN_NUMBER_LABEL.window_labels()
    MAX_NUMBER_LABEL.window_labels()
    AVERAGE_LABEL.window_labels()
    MEDIAN_LABEL.window_labels()
    MODE_LABEL.window_labels()
    RANGE_LABEL.window_labels()
    MIDRANGE_LABEL.window_labels()
    VARIANCE_LABEL.window_labels()
    STANDARD_DEV_LABEL.window_labels()
    SKEW_LABEL.window_labels()
    SIZE_LABEL.window_labels()
    QUARTILE_TITLE.window_labels()
    QUARTILE_25_LABEL.window_labels()
    QUARTILE_50_LABEL.window_labels()
    QUARTILE_75_LABEL.window_labels()
    INTERQUARTILE_RANGE_LABEL.window_labels()

    SUMMATION_OUTPUT.show_calculations()
    MINIMUM_OUTPUT.show_calculations()
    MAXIMUM_OUTPUT.show_calculations()
    AVERAGE_OUTPUT.show_calculations()
    MEDIAN_OUTPUT.show_calculations()
    MODE_OUTPUT.show_calculations()
    RANGE_OUTPUT.show_calculations()
    MIDRANGE_OUTPUT.show_calculations()
    STANDARD_DEVIATION_OUTPUT.show_calculations()
    VARIANCE_OUTPUT.show_calculations()
    SKEWNESS_OUTPUT.show_calculations()
    SIZE_OUTPUT.show_calculations()
    QUARTILE_25_OUTPUT.show_calculations()
    QUARTILE_50_OUTPUT.show_calculations()
    QUARTILE_75_OUTPUT.show_calculations()
    IQR_OUTPUT.show_calculations()

    MAIN_WINDOW.mainloop()


if __name__ == '__main__':
    sys.exit(main())
