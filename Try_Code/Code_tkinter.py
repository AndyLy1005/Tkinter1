import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, FLAT

class BMI_calculator(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("BMI Calculator")
        self.geometry("620x790+400+0")
        self.resizable(width=False, height=False)
        self.frames = {}
        for F in (FirstPage, Man, Woman):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FirstPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        bg1 = "#a6a6a6"
        fg1 = "White"
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img0 = tk.PhotoImage(file = 'Page1.png')        
        self.LabelImage = tk.Label(self, image=self.img0).pack(side="top", fill="x")
        female = tk.Button(self, text="Female", fg = fg1, font=("Bungee", 40), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1,
                            command=lambda: controller.show_frame("Woman"))
        male = tk.Button(self, text="Male", fg = fg1, font=("Bungee", 40), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1,
                            command=lambda: controller.show_frame("Man"))
        female.place(x= 33, y = 656, width = 244, height=60)
        male.place(x = 311, y = 656, width = 244, height=60)


class Man(tk.Frame):

    def __init__(self, parent, controller):
        fg1="#1B344B"
        bg1="#FFD154"
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img = tk.PhotoImage(file = 'Andy1.1.png')        
        self.LabelImage = tk.Label(self, image=self.img).pack(side="top", fill="x")
        self.button = tk.Button(self, text="Back", fg = fg1, font=("Bodoni MT Black", 35), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1, command=lambda: controller.show_frame("FirstPage")).place(x = 465, y = 635, width= 155 , height=85)
        self.create_widgets()
        
    def create_widgets(self):
        self.weight = tk.StringVar()
        self.height = tk.StringVar()
        self.BMI_result = tk.StringVar()
        self.advice = tk.StringVar()
        w1 = 100
        h1 = 50
        w2 = 180
        h2 = 33
        bg1="#FFD154"
        fg1="#1B344B"

        #Weight
        self.text_weight = tk.Entry(self, textvariable =self.weight, background=bg1, fg =fg1, font=("Arial Black", 27), relief = FLAT).place(x=295, y=192, width=w1-25, height=h1)

        #Height
        self.text_height = tk.Entry(self,textvariable=self.height, font=("Arial Black", 25), fg = fg1, bg =bg1, relief = FLAT).place(x=282, y=337, width=w1-10, height=h1)

        #Button
        self.button_calculate = tk.Button(self,text="Calculate", command=self.BMI, fg = fg1, font=("Bodoni MT Black", 28), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1).place(x = 15, y = 467, width=w2, height=h2)
        self.button_clear = tk.Button(self, text="Clear", command=self.Clear, fg = fg1, font=("Bodoni MT Black", 30), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1).place(x = 226, y = 467, width=w2, height=h2)    


    def BMI(self):
        bg1="#FFD154"
        fg1="#1B344B"
        self.img1 = tk.PhotoImage(file = 'Andy_thin.png')        
        self.LabelImage1 = tk.Label(self, image=self.img1)
        self.img2 = tk.PhotoImage(file = 'Andy_chubby.png')        
        self.LabelImage2 = tk.Label(self, image=self.img2)
        self.img3 = tk.PhotoImage(file = 'Andy_fat.png')        
        self.LabelImage3 = tk.Label(self, image=self.img3)
        if self.weight.get() == "" or self.height.get() == "":
            messagebox.showerror("Error", "Nothing to calculate!")
        else:
            self.w = float(self.weight.get())
            self.h = float(self.height.get())
            self.result = round(self.w/(self.h*self.h))
            self.label_result = tk.Label(self, fg = fg1)
            self.label_result.configure(text = str(self.result), font=("Arial Black", 32),background =bg1)
            self.label_result.place(x=272,y=550,width=69, height=50)
            self.label_advice_text = tk.Label(self, fg = fg1)
            self.label_advice_text.configure(background = bg1, font=("Arial Black", 19))
            if self.result < 18.5:
                self.label_advice_text.configure(text ="Too thin! Eat more!")
                self.label_advice_text.place(x=75, y=726)
                self.LabelImage1.place(x= 418, y=0, width = 202, height = 790)

            elif self.result >= 18.5 and self.result < 24.9:
                self.label_advice_text.configure(text ="Normal! Maintain it!")
                self.label_advice_text.place(x=72, y=726)   

            elif self.result >= 25 and self.result < 29.9:
                self.label_advice_text.configure(text="So Chubby! Still OK!")
                self.label_advice_text.place(x=72, y=726)
                self.LabelImage2.place(x= 418, y=0, width = 202, height = 790)

            elif self.result >= 30:
                self.label_advice_text.configure(text="Too fat! Diet now!", font=("Arial Black", 20))
                self.label_advice_text.place(x=77, y=726)
                self.LabelImage3.place(x= 418, y=0, width = 202, height = 790)  
    def Clear(self):
        if self.weight.get() == "" and self.height.get() == "":
            messagebox.showinfo("Note", "Nothing to clear!")
        else:
            self.weight.set("")
            self.height.set("")
            self.label_result.destroy()
            self.label_advice_text.destroy()
            self.LabelImage1.destroy() or self.LabelImage2.destroy() or self.LabelImage3.destroy()


class Woman(tk.Frame):

    def __init__(self, parent, controller):
        fg1="#1B344B"
        bg1="#FFD154"
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img = tk.PhotoImage(file = 'TT43.png')        
        self.LabelImage = tk.Label(self, image=self.img).pack(side="top", fill="x")
        self.button = tk.Button(self, text="Back", fg = fg1, font=("Bodoni MT Black", 35), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1, command=lambda: controller.show_frame("FirstPage")).place(x = 465, y = 635, width= 155 , height=85)
        self.create_widgets()
        
    def create_widgets(self):
        self.weight = tk.StringVar()
        self.height = tk.StringVar()
        self.BMI_result = tk.StringVar()
        self.advice = tk.StringVar()
        w1 = 100
        h1 = 50
        w2 = 180
        h2 = 33
        bg1="#FFD154"
        fg1="#1B344B"

        #Weight
        self.text_weight = tk.Entry(self, textvariable =self.weight, background=bg1, fg =fg1, font=("Arial Black", 27), relief = FLAT).place(x=295, y=190, width=w1-25, height=h1)

        #Height
        self.text_height = tk.Entry(self,textvariable=self.height, font=("Arial Black", 25), fg = fg1, bg =bg1, relief = FLAT).place(x=280, y=335, width=w1-10, height=h1)

        #Button
        self.button_calculate = tk.Button(self,text="Calculate", command=self.BMI, fg = fg1, font=("Bodoni MT Black", 28), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1).place(x = 15, y = 467, width=w2, height=h2)
        self.button_clear = tk.Button(self, text="Clear", command=self.Clear, fg = fg1, font=("Bodoni MT Black", 30), background = bg1, relief = FLAT, activebackground = bg1, activeforeground = fg1).place(x = 226, y = 467, width=w2, height=h2)    


    def BMI(self):
        bg1="#FFD154"
        fg1="#1B344B"
        self.img1 = tk.PhotoImage(file = 'TT_thin.png')        
        self.LabelImage1 = tk.Label(self, image=self.img1)
        self.img2 = tk.PhotoImage(file = 'TT_chubby.png')        
        self.LabelImage2 = tk.Label(self, image=self.img2)
        self.img3 = tk.PhotoImage(file = 'TT_fat.png')        
        self.LabelImage3 = tk.Label(self, image=self.img3)
        if self.weight.get() == "" or self.height.get() == "":
            messagebox.showerror("Error", "Nothing to calculate!")
        else:
            self.w = float(self.weight.get())
            self.h = float(self.height.get())
            self.result = round(self.w/(self.h*self.h))
            self.label_result = tk.Label(self, fg = fg1)
            self.label_result.configure(text = str(self.result), font=("Arial Black", 32),background =bg1)
            self.label_result.place(x=274,y=552,width=69, height=50)
            self.label_advice_text = tk.Label(self, fg = fg1)
            self.label_advice_text.configure(background = bg1, font=("Arial Black", 19))
            if self.result < 18.5:
                self.label_advice_text.configure(text ="Little thin! Eat more bae!", font=("Arial Black", 17))
                self.label_advice_text.place(x=47, y=728)
                self.LabelImage1.place(x= 418, y=0, width = 202, height = 790)

            elif self.result >= 18.5 and self.result < 23.4:
                self.label_advice_text.configure(text ="Wonderful! Maintain it!")
                self.label_advice_text.place(x=48, y=728, width = 323)   

            elif self.result >= 23.5 and self.result < 25.9:
                self.label_advice_text.configure(text="Chubby but no problem!")
                self.label_advice_text.place(x=48, y=728, width = 323)
                self.LabelImage2.place(x= 418, y=0, width = 202, height = 790)

            elif self.result >= 26:
                self.label_advice_text.configure(text="Beautiful in your way!")
                self.label_advice_text.place(x=48, y=728, width = 323)
                self.LabelImage3.place(x= 418, y=0, width = 202, height = 790)  
    def Clear(self):
        if self.weight.get() == "" and self.height.get() == "":
            messagebox.showinfo("Note", "Nothing to clear!")
        else:
            self.weight.set("")
            self.height.set("")
            self.label_result.destroy()
            self.label_advice_text.destroy()
            self.LabelImage1.destroy() or self.LabelImage2.destroy() or self.LabelImage3.destroy()



if __name__ == "__main__":
    app = BMI_calculator()
    app.mainloop()