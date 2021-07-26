import tkinter as tk
import cash_flow_analyzers
import depr_analysis

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.geometry( '1000x300' )
        
        #create new window 
        self.button1 = tk.Button(text = 'Depreciation Analysis', width = 40, command = self.new_window)
        self.button1.grid(row = 900)        
      
        #close window
        self.button2 = tk.Button(text = 'Quit', width = 25, command = self.master.quit)
        self.button2.grid(row = 1000)
      
        #cash flow 
        #entry bar  
        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row = 0, column = 1)
        self.entry2 = tk.Entry(self.master)
        self.entry2.grid(row=1, column=1)

        #market interest rate
        self.entry3 = tk.Entry(self.master)
        self.entry3.grid(row=2,column=1)
        self.entry4 = tk.Entry(self.master)
        self.entry4.grid(row=3, column=1)

        #label for entrybar
        self.label1 = tk.Label(self.master, text = 'enter cash flow as comma delimited list, first value being initial investment').grid(row = 0, column = 0)
        self.label2 = tk.Label(self.master, text = 'enter interest rate (5 percent as .05, 115 percent as 1.15, etc.)').grid(row=1 , column= 0)
        self.label3 = tk.Label(self.master, text = 'enter inflation for market interest rate').grid(row = 2, column = 0,pady = 20)
        self.label4 = tk.Label(self.master, text = 'enter interest rate for market interest rate').grid(row = 3, column = 0)
        #button for calculating entry 
        self.acceptentry1 = tk.Button(self.master, text = 'compute', command = self.return_result).grid(row = 1, column = 10) 
        self.acceptentry3_4 = tk.Button(self.master, text = 'compute', command = self.market_interest_rate).grid(row=2,column=2, pady = 20)

        #checkboxes
        self.CheckVar1 = tk.IntVar()
        self.CheckVar2 = tk.IntVar()
        self.CheckVar3 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(self.master, text = "Net Present Worth", variable = self.CheckVar1 ).grid(row=0,column=2)
        self.checkbox2 = tk.Checkbutton(self.master, text = "Present Worth", variable = self.CheckVar2 ).grid(row=0,column=3)
        self.checkbox3 = tk.Checkbutton(self.master, text = "Future Worth", variable = self.CheckVar3 ).grid(row=0,column=4)
        
        
    
    #apply function to entry bar
    def return_result(self):
        self.inputseries = str(self.entry1.get())
        self.inputinterest = float(self.entry2.get())
        if self.CheckVar1.get() == 1:
            self.answer = tk.Label(self.master, text = str(cash_flow_analyzers.net_present_worth(self.inputinterest,self.inputseries))).grid(row=1,column=2)
        elif self.CheckVar2.get() == 1:
            self.answer = tk.Label(self.master, text = str(cash_flow_analyzers.present_worth(self.inputinterest,self.inputseries))).grid(row=1,column=3)
        elif self.CheckVar3.get() == 1:
            self.answer = tk.Label(self.master, text = str(cash_flow_analyzers.future_worth(self.inputinterest,self.inputseries))).grid(row=1,column=4)
    def market_interest_rate(self):
        self.inputinflation = float(self.entry4.get())
        self.inputinterestm = float(self.entry3.get())
        self.answerm = tk.Label(self.master, text = str((cash_flow_analyzers.market_interest(self.inputinterestm, self.inputinflation))-1)).grid(row=5,column=1 )

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.quitButton = tk.Button(self.master, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.grid(row = 10)
        self.master.geometry('500x500')
        

        self.label1 = tk.Label(self.master, text = "enter annual profit" ).grid(row=0,column=0)
        self.label2 = tk.Label(self.master, text = 'enter project life in years').grid(row=1)
        self.label3 = tk.Label(self.master, text = 'enter intitial cost').grid(row=2)
        self.label4 = tk.Label(self.master, text = 'enter depreciation method SL, DB, or SOYD').grid(row=3)
        self.label5 = tk.Label(self.master, text = 'enter salvage value').grid(row=4)
        self.label6 = tk.Label(self.master, text = 'enter numerator for declining balance depreciation').grid(row=5)

        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row=0,column=1)
        self.entry2 = tk.Entry(self.master)
        self.entry2.grid(row=1,column=1)
        self.entry3 = tk.Entry(self.master)
        self.entry3.grid(row=2,column=1)
        self.entry4 = tk.Entry(self.master)
        self.entry4.grid(row=3,column=1)
        self.entry5 = tk.Entry(self.master)
        self.entry5.grid(row=4,column=1)
        self.entry6 = tk.Entry(self.master)
        self.entry6.grid(row=5,column=1)

        self.calculate = tk.Button(self.master, text = 'compute', command = self.analyze).grid(row = 10, column=2)

    def analyze(self):
        self.aprofit = float(self.entry1.get())
        self.years = int(self.entry2.get())
        self.icost = float(self.entry3.get())
        self.dmethod = str(self.entry4.get())
        self.svalue = float(self.entry5.get())
        self.alpha = float(self.entry6.get())

        self.result = depr_analysis.tax_with_depreciation(
            self.aprofit,
            self.years,
            self.icost ,
            self.dmethod, 
            self.svalue, 
            self.alpha)
        tk.Label(self.master, text = self.result).grid(row=7,column=1)


    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()