import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk
from functools import reduce

bono_car = {1: -30, 2: -20, 3: -10, 4: -5, 5: 0, 6: 5, 7: 5,
            8: 10, 9: 10, 10: 15, 11: 20, 12: 20, 13: 25,
            14: 25, 15: 30, 16: 35, 17: 35, 18: 40, 19: 40, 20: 45}

AGI_temp_car = 0
CON_temp_car = 0
DES_temp_car = 0
FUE_temp_car = 0
INT_temp_car = 0
PER_temp_car = 0
POD_temp_car = 0
VOL_temp_car = 0

AGI_totalAtributes = 0
CON_totalAtributes = 0
DES_totalAtributes = 0
FUE_totalAtributes = 0
INT_totalAtributes = 0
PER_totalAtributes = 0
POD_totalAtributes = 0
VOL_totalAtributes = 0
total_Atributes = {"AGI_totalAtributes" : 0, "CON_totalAtributes": 0, "DES_totalAtributes": 0, "FUE_totalAtributes": 0, "INT_totalAtributes": 0, "POD_totalAtributes": 0, "PER_totalAtributes": 0, "VOL_totalAtributes": 0}

def total_Atributos():
    total = reduce(lambda x, y:x+y, total_Atributes.values())
    totalAtributes_lb.config(text=total)
    return total_Atributes

def show_AGI(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_AGI = 0
    show_AGI = sd.askinteger(parent=hoja_prima, title="Agilidad", prompt="AGI", initialvalue=0)
    while show_AGI is None or show_AGI < 0:

        show_AGI = sd.askinteger(parent=hoja_prima, title="Agilidad", prompt="AGI", initialvalue=0)
   
    if show_AGI >= 0:
        input_AGI(show_AGI)
        agi_lb2.config(text=show_AGI)
        AGI_totalAtributes = show_AGI
        if show_AGI == 10:
            AGI_totalAtributes += 1
    total_Atributes["AGI_totalAtributes"] = AGI_totalAtributes
    total_Atributos()
    return total_Atributes

def show_CON(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_CON = 0
    show_CON = sd.askinteger(parent=hoja_prima, title="Constitucion", prompt="CON", initialvalue=0)
    while show_CON is None or show_CON < 0:

        show_CON = sd.askinteger(parent=hoja_prima, title="Constitucion", prompt="CON", initialvalue=0)
    
    if show_CON >= 0:
        input_CON(show_CON)
        con_lb2.config(text=show_CON)
        CON_totalAtributes = show_CON
        if show_CON == 10:
            CON_totalAtributes += 1
        print(total_Atributes)
    total_Atributes["CON_totalAtributes"] = CON_totalAtributes
    total_Atributos()
    return total_Atributes
    
def show_DES(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_DES = 0
    show_DES = sd.askinteger(parent=hoja_prima, title="Destreza", prompt="DES", initialvalue=0)
    while show_DES is None or show_DES < 0:

        show_DES = sd.askinteger(parent=hoja_prima, title="Destreza", prompt="DES", initialvalue=0)
    
    if show_DES >= 0:
        input_DES(show_DES)
        des_lb2.config(text=show_DES)
        DES_totalAtributes = show_DES
        if show_DES == 10:
            DES_totalAtributes += 1
    total_Atributes["DES_totalAtributes"] = DES_totalAtributes
    total_Atributos()
    return total_Atributes

def show_FUE(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_FUE = 0
    show_FUE = sd.askinteger(parent=hoja_prima, title="Fuerza", prompt="FUE", initialvalue=0)
    while show_FUE is None or show_FUE < 0:

        show_FUE = sd.askinteger(parent=hoja_prima, title="Fuerza", prompt="FUE", initialvalue=0)
    
    if show_FUE >= 0:
        input_FUE(show_FUE)
        fue_lb2.config(text=show_FUE)
        FUE_totalAtributes = show_FUE
        if show_FUE == 10:
            FUE_totalAtributes += 1
    total_Atributes["FUE_totalAtributes"] = FUE_totalAtributes
    total_Atributos()
    return total_Atributes

def show_INT(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_INT = 0
    show_INT = sd.askinteger(parent=hoja_prima, title="Inteligencia", prompt="INT", initialvalue=0)
    while show_INT is None or show_INT < 0:

        show_INT = sd.askinteger(parent=hoja_prima, title="Inteligencia", prompt="INT", initialvalue=0)
    
    if show_INT >= 0:
        input_INT(show_INT)
        int_lb2.config(text=show_INT)
        INT_totalAtributes = show_INT
        if show_INT == 10:
            INT_totalAtributes += 1
    total_Atributes["INT_totalAtributes"] = INT_totalAtributes
    total_Atributos()
    return total_Atributes

def show_PER(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_PER = 0
    show_PER = sd.askinteger(parent=hoja_prima, title="Percepcion", prompt="PER", initialvalue=0)
    while show_PER is None or show_PER < 0:

        show_PER = sd.askinteger(parent=hoja_prima, title="Percepcion", prompt="PER", initialvalue=0)
    
    if show_PER >= 0:
        input_PER(show_PER)
        per_lb2.config(text=show_PER)
        PER_totalAtributes = show_PER
        if show_PER == 10:
            PER_totalAtributes += 1
    total_Atributes["PER_totalAtributes"] = PER_totalAtributes
    total_Atributos()
    return total_Atributes

def show_POD(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_POD = 0
    show_POD = sd.askinteger(parent=hoja_prima, title="Poder", prompt="POD", initialvalue=0)
    while show_POD is None or show_POD < 0:

        show_POD = sd.askinteger(parent=hoja_prima, title="Poder", prompt="POD", initialvalue=0)
    
    if show_POD >= 0:
        input_POD(show_POD)
        pod_lb2.config(text=show_POD)
        POD_totalAtributes = show_POD
        if show_POD == 10:
            POD_totalAtributes += 1
    total_Atributes["POD_totalAtributes"] = POD_totalAtributes
    total_Atributos()
    return total_Atributes

def show_VOL(event):
    # Crear un cuadro de diálogo personalizado con un lb2ry usando la clase lb2ryDialog
    show_VOL = 0
    show_VOL = sd.askinteger(parent=hoja_prima, title="Voluntad", prompt="VOL", initialvalue=0)
    while show_VOL is None or show_VOL < 0:

        show_VOL = sd.askinteger(parent=hoja_prima, title="Voluntad", prompt="VOL", initialvalue=0)
    
    if show_VOL >= 0:
        input_VOL(show_VOL)
        vol_lb2.config(text=show_VOL)
        VOL_totalAtributes = show_VOL
        if show_VOL == 10:
            VOL_totalAtributes += 1
    total_Atributes["VOL_totalAtributes"] = VOL_totalAtributes
    total_Atributos()
    return total_Atributes


def input_AGI(AGI_car):
    bono = int(AGI_car)
    if bono <=5:
        if bono ==3:
            agi_lb3.config(text=-10)
        elif bono ==4:
            agi_lb3.config(text=-5)
        elif bono ==5:
            agi_lb3.config(text=0)
    elif bono <=7:
        agi_lb3.config(text=5)
    elif bono <=9:
        agi_lb3.config(text=10)
    elif bono ==10:
        agi_lb3.config(text=15)
    elif bono <=12:
        agi_lb3.config(text=20)
    elif bono <=14:
        agi_lb3.config(text=25)
    elif bono ==15:
        agi_lb3.config(text=30)
    elif bono <=17:
        agi_lb3.config(text=35)
    elif bono <=19:
        agi_lb3.config(text=40)
    else:
        agi_lb3.config(text=45)

def input_CON(CON_car):
    bono = int(CON_car)
    if bono <=5:
        if bono ==3:
            con_lb3.config(text=-10)
        elif bono ==4:
            con_lb3.config(text=-5)
        elif bono ==5:
            con_lb3.config(text=0)
    elif bono <=7:
        con_lb3.config(text=5)
    elif bono <=9:
        con_lb3.config(text=10)
    elif bono ==10:
        con_lb3.config(text=15)
    elif bono <=12:
        con_lb3.config(text=20)
    elif bono <=14:
        con_lb3.config(text=25)
    elif bono ==15:
        con_lb3.config(text=30)
    elif bono <=17:
        con_lb3.config(text=35)
    elif bono <=19:
        con_lb3.config(text=40)
    else:
        con_lb3.config(text=45)

def input_DES(DES_car):
    bono = int(DES_car)
    if bono <=5:
        if bono ==3:
            des_lb3.config(text=-10)
        elif bono ==4:
            des_lb3.config(text=-5)
        elif bono ==5:
            des_lb3.config(text=0)
    elif bono <=7:
        des_lb3.config(text=5)
    elif bono <=9:
        des_lb3.config(text=10)
    elif bono ==10:
        des_lb3.config(text=15)
    elif bono <=12:
        des_lb3.config(text=20)
    elif bono <=14:
        des_lb3.config(text=25)
    elif bono ==15:
        des_lb3.config(text=30)
    elif bono <=17:
        des_lb3.config(text=35)
    elif bono <=19:
        des_lb3.config(text=40)
    else:
        des_lb3.config(text=45)

def input_FUE(FUE_car):
    bono = int(FUE_car)
    if bono <=5:
        if bono ==3:
            fue_lb3.config(text=-10)
        elif bono ==4:
            fue_lb3.config(text=-5)
        elif bono ==5:
            fue_lb3.config(text=0)
    elif bono <=7:
        fue_lb3.config(text=5)
    elif bono <=9:
        fue_lb3.config(text=10)
    elif bono ==10:
        fue_lb3.config(text=15)
    elif bono <=12:
        fue_lb3.config(text=20)
    elif bono <=14:
        fue_lb3.config(text=25)
    elif bono ==15:
        fue_lb3.config(text=30)
    elif bono <=17:
        fue_lb3.config(text=35)
    elif bono <=19:
        fue_lb3.config(text=40)
    else:
        fue_lb3.config(text=45)

def input_INT(INT_car):
    bono = int(INT_car)
    if bono <=5:
        if bono ==3:
            int_lb3.config(text=-10)
        elif bono ==4:
            int_lb3.config(text=-5)
        elif bono ==5:
            int_lb3.config(text=0)
    elif bono <=7:
        int_lb3.config(text=5)
    elif bono <=9:
        int_lb3.config(text=10)
    elif bono ==10:
        int_lb3.config(text=15)
    elif bono <=12:
        int_lb3.config(text=20)
    elif bono <=14:
        int_lb3.config(text=25)
    elif bono ==15:
        int_lb3.config(text=30)
    elif bono <=17:
        int_lb3.config(text=35)
    elif bono <=19:
        int_lb3.config(text=40)
    else:
        int_lb3.config(text=45)

def input_PER(PER_car):
    bono = int(PER_car)
    if bono <=5:
        if bono ==3:
            per_lb3.config(text=-10)
        elif bono ==4:
            per_lb3.config(text=-5)
        elif bono ==5:
            per_lb3.config(text=0)
    elif bono <=7:
        per_lb3.config(text=5)
    elif bono <=9:
        per_lb3.config(text=10)
    elif bono ==10:
        per_lb3.config(text=15)
    elif bono <=12:
        per_lb3.config(text=20)
    elif bono <=14:
        per_lb3.config(text=25)
    elif bono ==15:
        per_lb3.config(text=30)
    elif bono <=17:
        per_lb3.config(text=35)
    elif bono <=19:
        per_lb3.config(text=40)
    else:
        per_lb3.config(text=45)

def input_POD(POD_car):
    bono = int(POD_car)
    if bono <=5:
        if bono ==3:
            pod_lb3.config(text=-10)
        elif bono ==4:
            pod_lb3.config(text=-5)
        elif bono ==5:
            pod_lb3.config(text=0)
    elif bono <=7:
        pod_lb3.config(text=5)
    elif bono <=9:
        pod_lb3.config(text=10)
    elif bono ==10:
        pod_lb3.config(text=15)
    elif bono <=12:
        pod_lb3.config(text=20)
    elif bono <=14:
        pod_lb3.config(text=25)
    elif bono ==15:
        pod_lb3.config(text=30)
    elif bono <=17:
        pod_lb3.config(text=35)
    elif bono <=19:
        pod_lb3.config(text=40)
    else:
        pod_lb3.config(text=45)

def input_VOL(VOL_car):
    bono = int(VOL_car)
    if bono <=5:
        if bono ==3:
            vol_lb3.config(text=-10)
        elif bono ==4:
            vol_lb3.config(text=-5)
        elif bono ==5:
            vol_lb3.config(text=0)
    elif bono <=7:
        vol_lb3.config(text=5)
    elif bono <=9:
        vol_lb3.config(text=10)
    elif bono ==10:
        vol_lb3.config(text=15)
    elif bono <=12:
        vol_lb3.config(text=20)
    elif bono <=14:
        vol_lb3.config(text=25)
    elif bono ==15:
        vol_lb3.config(text=30)
    elif bono <=17:
        vol_lb3.config(text=35)
    elif bono <=19:
        vol_lb3.config(text=40)
    else:
        vol_lb3.config(text=45)


hoja_prima = tk.Tk()

caracteristcas_fm = ttk.Frame(hoja_prima)
caracteristcas_fm.grid(column=0, row=0)


#Label caracteristica
titleAtributes_lb = ttk.Label(caracteristcas_fm, text="Atributos", relief = "groove")
totalAtributes_lb = ttk.Label(caracteristcas_fm)
agi_lb = ttk.Label(caracteristcas_fm, width=5, text="  AGI", borderwidth=2, relief="raised")
con_lb = ttk.Label(caracteristcas_fm, width=5, text=" CON", borderwidth=2, relief="raised")
des_lb = ttk.Label(caracteristcas_fm, width=5, text="  DES", borderwidth=2, relief="raised")
fue_lb = ttk.Label(caracteristcas_fm, width=5, text="  FUE", borderwidth=2, relief="raised")
int_lb = ttk.Label(caracteristcas_fm, width=5, text="  INT", borderwidth=2, relief="raised")
per_lb = ttk.Label(caracteristcas_fm, width=5, text="  PER", borderwidth=2, relief="raised")
pod_lb = ttk.Label(caracteristcas_fm, width=5, text="  POD", borderwidth=2, relief="raised")
vol_lb = ttk.Label(caracteristcas_fm, width=5, text="  VOL", borderwidth=2, relief="raised")

titleAtributes_lb.grid(column=0, row=0, padx= 5, pady= 4, ipadx= 2, ipady= 1, columnspan = 4)
totalAtributes_lb.grid(column=0, row=1, padx= 5, pady= 4, ipadx= 2, ipady= 1)
agi_lb.grid(column=0, row=2, padx= 5, pady= 4, ipadx= 2, ipady= 1)
con_lb.grid(column=0, row=3, padx= 5, pady= 4, ipadx= 2, ipady= 1)
des_lb.grid(column=0, row=4, padx= 5, pady= 4, ipadx= 2, ipady= 1)
fue_lb.grid(column=0, row=5, padx= 5, pady= 4, ipadx= 2, ipady= 1)
int_lb.grid(column=0, row=6, padx= 5, pady= 4, ipadx= 2, ipady= 1)
per_lb.grid(column=0, row=7, padx= 5, pady= 4, ipadx= 2, ipady= 1)
pod_lb.grid(column=0, row=8, padx= 5, pady= 4, ipadx= 2, ipady= 1)
vol_lb.grid(column=0, row=9, padx= 5, pady= 4, ipadx= 2, ipady= 1)

#lb2ry caracteristicas
base_la2 = ttk.Label(caracteristcas_fm, text="Base")
agi_lb2 = ttk.Label(caracteristcas_fm, width=3)
con_lb2 = ttk.Label(caracteristcas_fm, width=3)
des_lb2 = ttk.Label(caracteristcas_fm, width=3)
fue_lb2 = ttk.Label(caracteristcas_fm, width=3)
int_lb2 = ttk.Label(caracteristcas_fm, width=3)
per_lb2 = ttk.Label(caracteristcas_fm, width=3)
pod_lb2 = ttk.Label(caracteristcas_fm, width=3)
vol_lb2 = ttk.Label(caracteristcas_fm, width=3)

base_la2.grid(column= 1, row=1)
agi_lb2.grid(column= 1, row=2, pady=2, padx=2)
con_lb2.grid(column= 1, row=3, pady=2, padx=2)
des_lb2.grid(column= 1, row=4, pady=2, padx=2)
fue_lb2.grid(column= 1, row=5, pady=2, padx=2)
int_lb2.grid(column= 1, row=6, pady=2, padx=2)
per_lb2.grid(column= 1, row=7, pady=2, padx=2)
pod_lb2.grid(column= 1, row=8, pady=2, padx=2)
vol_lb2.grid(column= 1, row=9, pady=2, padx=2)

# agi_lb2.bind('<BackSpace>', lambda x : agi_lb2.delete(0, Tk.END))
# con_lb2.bind('<BackSpace>', lambda x : con_lb2.delete(0, Tk.END))
# des_lb2.bind('<BackSpace>', lambda x : des_lb2.delete(0, Tk.END))
# fue_lb2.bind('<BackSpace>', lambda x : fue_lb2.delete(0, Tk.END))
# int_lb2.bind('<BackSpace>', lambda x : int_lb2.delete(0, Tk.END))
# per_lb2.bind('<BackSpace>', lambda x : per_lb2.delete(0, Tk.END))
# pod_lb2.bind('<BackSpace>', lambda x : pod_lb2.delete(0, Tk.END))
# vol_lb2.bind('<BackSpace>', lambda x : vol_lb2.delete(0, Tk.END))

agi_lb.bind("<Button-1>", show_AGI)
con_lb.bind("<Button-1>", show_CON)
des_lb.bind("<Button-1>", show_DES)
fue_lb.bind("<Button-1>", show_FUE)
int_lb.bind("<Button-1>", show_INT)
per_lb.bind("<Button-1>", show_PER)
pod_lb.bind("<Button-1>", show_POD)
vol_lb.bind("<Button-1>", show_VOL)

#Label Bono
bono_la3 = ttk.Label(caracteristcas_fm, text="Bono")
agi_lb3 = ttk.Label(caracteristcas_fm, width=5)
con_lb3 = ttk.Label(caracteristcas_fm, width=5)
des_lb3 = ttk.Label(caracteristcas_fm, width=5)
fue_lb3 = ttk.Label(caracteristcas_fm, width=5)
int_lb3 = ttk.Label(caracteristcas_fm, width=5)
per_lb3 = ttk.Label(caracteristcas_fm, width=5)
pod_lb3 = ttk.Label(caracteristcas_fm, width=5)
vol_lb3 = ttk.Label(caracteristcas_fm, width=5)

bono_la3.grid(column= 3, row=1)
agi_lb3.grid(column=3, row=2, padx= 5, pady= 4, ipadx= 2, ipady= 1)
con_lb3.grid(column=3, row=3, padx= 5, pady= 4, ipadx= 2, ipady= 1)
des_lb3.grid(column=3, row=4, padx= 5, pady= 4, ipadx= 2, ipady= 1)
fue_lb3.grid(column=3, row=5, padx= 5, pady= 4, ipadx= 2, ipady= 1)
int_lb3.grid(column=3, row=6, padx= 5, pady= 4, ipadx= 2, ipady= 1)
per_lb3.grid(column=3, row=7, padx= 5, pady= 4, ipadx= 2, ipady= 1)
pod_lb3.grid(column=3, row=8, padx= 5, pady= 4, ipadx= 2, ipady= 1)
vol_lb3.grid(column=3, row=9, padx= 5, pady= 4, ipadx= 2, ipady= 1)


hoja_prima.mainloop()