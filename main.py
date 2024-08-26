from tkinter import filedialog
import tkinter
import brain2

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tkinter.Tk()
window.title("Palette Analyser 1.0")
window.minsize(width=1150, height=590)


def open_a_log_file():
    file_path = filedialog.askopenfilename(filetypes=[("CMAT, FFT Log file-ok", ".log")], initialdir="Q:\\FFT\\")
    if len(file_path):
        data = brain2.Brain(file_path=file_path)
        text.delete("1.0", tkinter.END)
        text.insert("1.0", data.data)
        paletta_data.config(text=data.data_all, font=("Arial", 10))
        title.config(text=f"Paletta Analizátor - {data.system_id} {data.date}")


        def show_diagram(pallett, fail_parts, pass_parts):

            fig, ax = plt.subplots(figsize=(4, 3))
            fig, ax.bar(pallett, fail_parts, width=0.5, bottom=pass_parts, color="red")
            fig, ax.bar(pallett, pass_parts, width=0.5, color="green")

            canvas = FigureCanvasTkAgg(fig)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=1, columnspan=2, pady=(190, 10),
                                        sticky='n')

        pass_parts = list(data.pass_rate_on_palett.values())
        fail_parts = list(data.failure_rate_on_palett.values())
        pallett = list(data.pass_part_on_pallet.keys())
        print(pallett)
        if "" in pallett:
            pass_parts = list(data.pass_rate_on_palett.values())
            fail_parts = list(data.failure_rate_on_palett.values())
            pallett = [pal for pal in pallett if pal != ""]
            show_diagram(pallett, fail_parts, pass_parts)
        else:
            show_diagram(pallett, fail_parts, pass_parts)


title = tkinter.Label(text="Paletta Analizátor ", font=("Arial", 30))
title.grid(column=1, row=0, columnspan=2, pady=10, sticky="N")

open_button = tkinter.Button(text="Megnyitás", command=open_a_log_file)
open_button.grid(column=0, row=0, padx=20, sticky="W")

text = tkinter.Text(width=140, height=31, font=("Arial", 10))
text.focus()
text.insert('1.0', "Tölts be egy ProcessHistory.log fájlt!")
text.grid(column=2, row=1, sticky="N")

_paletta_data = tkinter.Label(text="Paletták a gépben: ",  font=("Arial", 10))
_paletta_data.grid(column=0, row=1, columnspan=2, pady=20, sticky="N")

paletta_data = tkinter.Label(text="Nincs megjelenítendő adat!")
paletta_data.grid(column=0, row=1, columnspan=2, pady=50, sticky='N')


window.mainloop()
