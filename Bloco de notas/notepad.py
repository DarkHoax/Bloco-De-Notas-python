import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import  messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText

#BORDA DA JANELA
janela = Tk()
janela.title("Bloco de notas")
janela.resizable(0, 0)

#TELA DESCE/SOBE
blocodenotas = ScrolledText(janela, width=90, height=40) #blocodenotas == notepad
nomearq = "" #fileName

#DEFININDO OS DIRETÓRIOS DO SOFTWARE
def novo():
    global nomearq
    if len(blocodenotas.get("1.0", END+"-1c")) > 0:
        if messagebox.askyesno("bloco de notas", "Não quer salvar antes de sair?"):
            salvar()
        else:
            blocodenotas.delete("0.0", END)
    janela.title("Bloco de Notas!")

def abrir():
    arq = filedialog.askopenfile(parent=janela, mode="r")
    t = arq.read() #LEITOR DO TEXTOR
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)

def salvar():
    arq = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if(arq != None):
        data = blocodenotas.get("1.0", END)
    try:
        arq.write(data)
    except:
        messagebox.showerror(title="Erro", message="Impossível salvar arquivo")

def salvarcomo():
    arq = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    t = blocodenotas.get(0.0, END) #TEXTO PEGO DO BLOCO DE NOTAS
    try:
        arq.write(t.rstrip())
    except:
        messagebox.showerror(title="Erro", message="Impossível salvar arquivo")

def sair():
    if messagebox.askyesno("bloco de notas", "Você quer sair?"):
        janela.destroy()

def cortar():
    blocodenotas.event_generate("<<Cut>>")

def copiar():
    blocodenotas.event_generate("<<Copy>>")

def colar():
    blocodenotas.event_generate("<<Paste>>")

def apagar():
    blocodenotas.event_generate("<<Clear>>")

def procurar():
    blocodenotas.tag_remove("Found", "1.0", END)
    procura = simpledialog.askstring("Procurar", "Procurar o que?")
    if procura:
        indice = "1.0"

    while 1:
        indice = blocodenotas.search(procura, indice, nocase = 1, stopindex = END)
        if not indice:
            break
        ultimoindice = "%s+%dc" % (idx, len(procura))
        blocodenotas.tag_add("Encontrado", indice, ultimoindice)
        indice = ultimoindice
        blocodenotas.tag_config("Encontrado", foreground = 'white', background = 'blue')
        blocodenotas.bind("<1>", clique)

def clique(event):
    blocodenotas.tag_config("Encontrado", background='white', foreground='black')

def selecionartudo():
    blocodenotas.event_generate("<<SelectAll>>")

def hora():
    now = datetime.now()
    datestring = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Time/Date", datestring)

def sobre():
    label = messagebox.showinfo("Sobre o bloco de notas", "Criado por Argos A. Maia")

menu = Menu(janela) # menu == notepadMenu
janela.configure(menu=menu)

#MENU DE ARQUIVOS
arqmenu = Menu(menu, tearoff=False) #arqmenu == fileMenu
menu.add_cascade(label="Arquivo", menu=arqmenu)
arqmenu.add_command(label='Novo', command=novo())
arqmenu.add_command(label='Abrir...', command=abrir())
arqmenu.add_command(label='Salvar', command=salvar())
arqmenu.add_command(label='Salvar como', command=salvarcomo())
arqmenu.add_separator()
arqmenu.add_command(label='Sair', command=sair())

#MENU DE EDICOES
editar = Menu(menu, tearoff = False)
menu.add_cascade(label="Editar", menu=editar)
editar.add_command(label="Cortar", command=cortar())
editar.add_command(label="Copiar", command=copiar())
editar.add_command(label="Colar", command=colar())
editar.add_command(label="Apagar", command=apagar())
editar.add_separator()
editar.add_command(label='Procurar...', command=procurar())
editar.add_separator()
editar.add_command(label='Selecionar tudo', command=selecionartudo())
editar.add_command(label='Hora', command=hora())

#MENU AJUDA
ajuda = Menu(menu, tearoff=False)
menu.add_cascade(label='Ajuda', menu=ajuda)
ajuda.add_command(label='Sobre o bloco de notas', command=sobre())

blocodenotas.pack()
janela.mainloop()
