import customtkinter as ctk  # type: ignore
from icecream import ic  # type: ignore

ctk.set_appearance_mode("system")


class App(ctk.CTk):
    def __init__(self):
        self.font = ("Helvetica", 50, "normal")
        self.btn_font = ("Helvetica", 50, "bold")
        self.main_color = "#0053a5"
        self.second_color = "#3fa3ff"
        self.result_flag = True
        self.curl_flag = True
        self.temp = []
        super().__init__()

        # title, icon, size
        self.title("Calculator")
        self.iconbitmap("./assets/ico.ico")
        self.resizable(False, False)
        self.center_window()

        # widgets Frames
        self.main_frame = MainFrame(self)
        self.secondary_frame = SecondaryFrame(self)

        # run
        self.mainloop()

    # region
    # methods / functions
    def center_window(self):
        self.update_idletasks()
        width = 1000
        height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        y = screen_height // 2 - height // 2
        x = screen_width // 2 - width // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def clear_text(self):
        self.main_frame.input.delete(0, ctk.END)
        self.main_frame.input.insert(0, "")

    def negative(self):
        if self.main_frame.input.get():
            vstup = self.main_frame.input.get()
            try:
                vstup = int(vstup) * -1
                self.main_frame.input.delete(0, ctk.END)
                self.main_frame.input.insert(0, vstup)
            except ValueError:
                vstup = float(vstup) * -1
                self.main_frame.input.delete(0, ctk.END)
                self.main_frame.input.insert(0, vstup)
        else:
            self.main_frame.input.insert(0, "")

    def add_num(self, value):
        if not self.result_flag:
            self.main_frame.input.delete(0, ctk.END)
            self.main_frame.input.insert(0, value)
            self.secondary_frame.label_1.configure(text=value)
            self.result_flag = True
        else:
            vstup = self.main_frame.input.get()
            self.main_frame.input.delete(0, ctk.END)
            self.secondary_frame.label_1.configure(text=vstup + value)
            self.main_frame.input.insert(0, vstup + value)

    def add_operator(self, operator):
        vstup = self.main_frame.input.get()
        self.result_flag = True
        if vstup:
            self.main_frame.input.delete(0, ctk.END)
            self.main_frame.input.insert(0, vstup + operator)
            self.secondary_frame.label_1.configure(text=vstup + operator)

    def add_curl(self):
        pass

    def do_math(self):
        vstup = self.main_frame.input.get()
        result = eval(self.main_frame.input.get())
        self.main_frame.input.delete(0, ctk.END)
        self.main_frame.input.insert(0, result)
        self.secondary_frame.label_1.configure(text=f"{vstup} = {result}")
        self.result_flag = False

    # endregion


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=493)
        self.parent = parent
        self.pack(side=ctk.LEFT, fill=ctk.BOTH, padx=(5, 2), pady=10)

        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0, uniform="a")

        # region
        self.input = ctk.CTkEntry(
            self,
            font=parent.font,
            border_width=2,
            border_color="#5c5f63",
            width=490,
        )
        self.input.get()
        self.input.insert(0, "")

        self.button_1 = ctk.CTkButton(
            self,
            text="1",
            font=parent.btn_font,
            fg_color=parent.main_color,
            command=lambda: parent.add_num("1"),
        )
        self.button_2 = ctk.CTkButton(
            self,
            text="2",
            font=parent.btn_font,
            fg_color=parent.main_color,
            command=lambda: parent.add_num("2"),
        )
        self.button_3 = ctk.CTkButton(
            self,
            text="3",
            font=parent.btn_font,
            fg_color=parent.main_color,
            command=lambda: parent.add_num("3"),
        )
        self.button_4 = ctk.CTkButton(
            self,
            text="4",
            font=parent.btn_font,
            fg_color=parent.main_color,
            command=lambda: parent.add_num("4"),
        )
        self.button_5 = ctk.CTkButton(
            self,
            text="5",
            font=parent.btn_font,
            fg_color=parent.main_color,
            command=lambda: parent.add_num("5"),
        )
        self.button_6 = ctk.CTkButton(
            self,
            text="6",
            fg_color=parent.main_color,
            font=parent.btn_font,
            command=lambda: parent.add_num("6"),
        )
        self.button_7 = ctk.CTkButton(
            self,
            text="7",
            fg_color=parent.main_color,
            font=parent.btn_font,
            command=lambda: parent.add_num("7"),
        )
        self.button_8 = ctk.CTkButton(
            self,
            text="8",
            fg_color=parent.main_color,
            font=parent.btn_font,
            command=lambda: parent.add_num("8"),
        )
        self.button_9 = ctk.CTkButton(
            self,
            text="9",
            fg_color=parent.main_color,
            font=parent.btn_font,
            command=lambda: parent.add_num("9"),
        )
        self.button_0 = ctk.CTkButton(
            self,
            text="0",
            fg_color=parent.main_color,
            font=parent.btn_font,
            command=lambda: parent.add_num("0"),
        )
        self.button_neg = ctk.CTkButton(
            self, text="+/-", font=parent.btn_font, command=lambda: parent.negative()
        )
        self.button_eqa = ctk.CTkButton(
            self,
            text="=",
            fg_color=parent.second_color,
            font=parent.btn_font,
            command=lambda: parent.do_math(),
        )
        self.button_plus = ctk.CTkButton(
            self,
            text="+",
            font=parent.btn_font,
            command=lambda: parent.add_operator(" + "),
        )
        self.button_minus = ctk.CTkButton(
            self,
            text="-",
            font=parent.btn_font,
            command=lambda: parent.add_operator(" - "),
        )
        self.button_multy = ctk.CTkButton(
            self,
            text="*",
            font=parent.btn_font,
            command=lambda: parent.add_operator(" * "),
        )
        self.button_divide = ctk.CTkButton(
            self,
            text="/",
            font=parent.btn_font,
            command=lambda: parent.add_operator(" / "),
        )
        self.button_cls = ctk.CTkButton(
            self,
            text="cls",
            font=parent.btn_font,
            command=parent.clear_text,
        )

        self.button_curl = ctk.CTkButton(
            self,
            text="( )",
            font=parent.btn_font,
            command=lambda: parent.add_curl(),
        )
        self.button_dot = ctk.CTkButton(
            self,
            text=".",
            font=parent.btn_font,
            command=lambda: parent.add_num("."),
        )

        self.input.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=5)
        self.button_1.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.button_2.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.button_3.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
        self.button_4.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.button_5.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.button_6.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
        self.button_7.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.button_8.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        self.button_9.grid(row=3, column=2, sticky="ew", padx=5, pady=5)
        self.button_0.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        self.button_neg.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.button_dot.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
        self.button_plus.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
        self.button_minus.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        self.button_multy.grid(row=5, column=2, sticky="ew", padx=5, pady=5)
        self.button_divide.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        self.button_cls.grid(row=6, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        self.button_curl.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
        self.button_eqa.grid(row=7, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        # endregion


class SecondaryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        self.secondary = ["ahoj", "priklady", "a dalsi", "pravidla", "pomoc"]
        super().__init__(parent, width=493)
        self.parent = parent
        self.pack(side=ctk.LEFT, fill=ctk.BOTH, padx=(2, 5), pady=10)

        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure(0, weight=0, uniform="a")

        self.label_1 = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 20, "normal"),
            text_color="gray",
            width=483,
            anchor="w",
        )
        self.label_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)


if __name__ == "__main__":
    App()
