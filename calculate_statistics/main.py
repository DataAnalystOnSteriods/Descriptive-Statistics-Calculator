import tkinter
import tkinter as tk
import customtkinter as ctk
import calculate
import sys


def main() -> None:
    WINDOW = ctk.CTk()

    ROOT_GEOMETRY = "900x570"
    WINDOW.geometry(ROOT_GEOMETRY)

    APP_TITLE = "Descriptive Statistics Calculator"
    WINDOW.title(APP_TITLE)

    MAX_WINDOW_WIDTH = 900
    MAX_WINDOW_HEIGHT = 570
    WINDOW.maxsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)

    DEFAULT_COLOR_THEME = 'blue'
    ctk.set_default_color_theme(DEFAULT_COLOR_THEME)

    BOX_AND_BUTTON_FRAME = ctk.CTkFrame(master=WINDOW, height=170, width=350)
    BOX_AND_BUTTON_FRAME.place(rely=0.07, relx=0.05)

    INPUT_TEXTBOX = calculate.INPUT_TEXTBOX

    class ShowCalculationLabels:
        def __init__(self, x: int, y: int, LABEL_TITLE: str):
            self.x = x
            self.y = y
            self.LABEL_TITLE = LABEL_TITLE

        def window_labels(self) -> None:
            FONT_STYLE = "Courier New"
            FONT_SIZE = 20
            CALCULATION_LABELS = ctk.CTkLabel(WINDOW, text=self.LABEL_TITLE, font=(FONT_STYLE, FONT_SIZE))
            CALCULATION_LABELS.place(x=self.x, y=self.y)

    class ShowButton:

        def show_results(BUTTON_HEIGHT, BUTTON_WIDTH, text_) -> None:
            CALCULATION_BUTTON = ctk.CTkButton(master=BOX_AND_BUTTON_FRAME, height=BUTTON_HEIGHT, width=BUTTON_WIDTH, text=text_,
                                                         command=lambda: calculate.calculate_and_show_stats(WINDOW))
            CALCULATION_BUTTON.place(x=200, y=125)


    calculate.textbox_input(BOX_AND_BUTTON_FRAME)
    ShowButton.show_results(32, 120, 'Calculate')

    FRONT_TITLE = ShowCalculationLabels(240, 0, 'Descriptive Statistics Calculator')

    SUMMATION_LABEL = ShowCalculationLabels(x=405, y=42, LABEL_TITLE='Summation Σ:')
    MIN_NUMBER_LABEL = ShowCalculationLabels(x=405, y=70, LABEL_TITLE='Minimum :')
    MAX_NUMBER_LABEL = ShowCalculationLabels(x=405, y=100, LABEL_TITLE='Maximum :')
    AVERAGE_LABEL = ShowCalculationLabels(x=405, y=130, LABEL_TITLE='Mean μ:')
    MEDIAN_LABEL = ShowCalculationLabels(x=405, y=160, LABEL_TITLE='Median :')
    MODE_LABEL = ShowCalculationLabels(x=45, y=210, LABEL_TITLE='Mode :')
    RANGE_LABEL = ShowCalculationLabels(x=45, y=240, LABEL_TITLE='Range :')
    MIDRANGE_LABEL = ShowCalculationLabels(x=45, y=270, LABEL_TITLE='Midrange :')
    POPULATION_STANDARD_DEV_LABEL = ShowCalculationLabels(x=45, y=300, LABEL_TITLE='Population STD σ:')
    SAMPLE_STANDARD_DEV_LABEL = ShowCalculationLabels(x=45, y=330, LABEL_TITLE='Sample STD σ:')
    POPULATION_VARIANCE_LABEL = ShowCalculationLabels(x=45, y=360, LABEL_TITLE='Population Variance σ2:')
    SAMPLE_VARIANCE_LABEL = ShowCalculationLabels(x=45, y=390, LABEL_TITLE='Sample Variance σ2:')
    QUARTILE_TITLE = ShowCalculationLabels(x=45, y=420, LABEL_TITLE='Quartiles')
    QUARTILE_25_LABEL = ShowCalculationLabels(x=100, y=445, LABEL_TITLE='Q25 :')
    QUARTILE_50_LABEL = ShowCalculationLabels(x=100, y=470, LABEL_TITLE='Q50 :')
    QUARTILE_75_LABEL = ShowCalculationLabels(x=100, y=500, LABEL_TITLE='Q75 :')
    INTERQUARTILE_RANGE_LABEL = ShowCalculationLabels(x=45, y=525, LABEL_TITLE='Interquartile Range :')

    FRONT_TITLE.window_labels()
    SUMMATION_LABEL.window_labels()
    MIN_NUMBER_LABEL.window_labels()
    MAX_NUMBER_LABEL.window_labels()
    AVERAGE_LABEL.window_labels()
    MEDIAN_LABEL.window_labels()
    MODE_LABEL.window_labels()
    RANGE_LABEL.window_labels()
    MIDRANGE_LABEL.window_labels()
    POPULATION_STANDARD_DEV_LABEL.window_labels()
    SAMPLE_STANDARD_DEV_LABEL.window_labels()
    POPULATION_VARIANCE_LABEL.window_labels()
    SAMPLE_VARIANCE_LABEL.window_labels()
    QUARTILE_TITLE.window_labels()
    QUARTILE_25_LABEL.window_labels()
    QUARTILE_50_LABEL.window_labels()
    QUARTILE_75_LABEL.window_labels()
    INTERQUARTILE_RANGE_LABEL.window_labels()

    WINDOW.mainloop()


if __name__ == '__main__':
    sys.exit(main())