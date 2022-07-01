from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Csv import exportingInCsv
from tcScrapping import tcScrapping
from datetime import date

class Tc:
  
  def exportingCsvTk(self, csv_columns, dict_data, fileName):
    exportingInCsv(csv_columns, dict_data, fileName)
    messagebox.showinfo("Information", "¡La exportación fue exitosa!")

  def __init__(self, window):
    self.wind = window
    self.wind.title("Tipos de Cambio")
    self.wind.geometry('490x350')
    self.wind.configure(bg='#2C3639')
    self.wind.resizable(False, False)

    self.heading = ttk.Label(
      self.wind, 
      text='Tipo de Cambio al ' + str(date.today()),
      style='Heading.TLabel', 
      background='#FBB454',
      foreground='white',
      font=('Monospace',16)  
    )
    self.heading.grid(column=0, row=1, columnspan=2, pady=10, sticky=N)

    dict_data = []
    dict_data = tcScrapping(dict_data)
  
    self.currTree = ttk.Treeview(self.wind)
    self.currTree['columns'] = ('Currency', 'Buy', 'Sell')
    self.currTree.column('#0', width = 0, stretch = NO)
    self.currTree.column('Currency', width=150, anchor=CENTER)
    self.currTree.column('Buy', width=150, anchor=CENTER)
    self.currTree.column('Sell', width=150, anchor=CENTER)

    self.currTree.heading('Currency', text = 'MONEDA', anchor=CENTER)
    self.currTree.heading('Buy', text = 'COMPRA',anchor=CENTER)
    self.currTree.heading('Sell', text = 'VENTA',anchor=CENTER)
    self.currTree.grid(row = 2, column = 0, padx=20)
    self.currTree.bind('<Motion>', 'break')

    dict_columns = ['currency', 'buy', 'sell']
    
    self.button = Button(
      self.wind,
      text="EXPORTAR", 
      background="#FBB454",
      foreground='white',
      command= lambda: self.exportingCsvTk(dict_columns, dict_data, 'currencies_' + str(date.today())))

    self.button.grid(column=0, row=3, columnspan=2, pady=10, sticky=N, ipadx=4, ipady=4)
      
    if(dict_data):
      for curr in range(len(dict_data)):
        self.currTree.insert(
          '', 
          END, 
          str(curr), 
          values = (
            dict_data[curr]['currency'],
            dict_data[curr]['buy'],
            dict_data[curr]['sell'],
          ),
          text = '0' + str(curr)
        )
    else:
      messagebox.showerror('Error', 'No se pudo extraer las divisas')
      self.button['state'] = 'disabled'

if __name__ == "__main__":
  window = Tk()
  app = Tc(window)
  window.mainloop()