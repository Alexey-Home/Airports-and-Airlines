from tkinter import *
from tkinter import ttk
from controller.controllerairports import *


def main():
    root = Tk()
    root.title("My App")
    root.geometry("560x500")

    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=BOTH)

    frame_airports = ttk.Frame(notebook)
    frame_airlines = ttk.Frame(notebook)

    frame_airports.pack(fill=BOTH, expand=True)
    frame_airlines.pack(fill=BOTH, expand=True)

    notebook.add(frame_airports, text="Аэропорты")
    notebook.add(frame_airlines, text='Аэролинии')

    cont = ControllerAirports(frame_airports)
    cont1 = ControllerAirlines(frame_airlines)
    root.mainloop()


if __name__ == "__main__":
    main()
