# Importando o Tkinter
import tkinter.ttk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando o Tkcalendar
from tkcalendar import Calendar, DateEntry

# Importando view

from view import *

# Cores
cor_branca = '#FFFAFA'
cor_verde = '#5FB861'
cor_vermelha = '#FF6E6E'
cor_azul = '#4A89FF'
cor_cinza = '#D4D4D4'
cor_preta = '#303030'

# Criando a janela

janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=cor_cinza)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg=cor_verde, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=cor_branca, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=cor_branca, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label Cima

app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor='nw', font=('Ivy 13 bold'), fg=cor_branca,bg=cor_verde, relief='flat')
app_nome.place(x=10, y=20)

# Variável global tree
global tree

# Função inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_telefone.get()
    data = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()

    lista = [nome, email, tel, data, estado, assunto]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode estar vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso.')

    e_nome.delete(0, 'end')
    e_email.delete(0, 'end')
    e_telefone.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_estado.delete(0, 'end')
    e_assunto.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dict = tree.item(treev_dados)
        tree_lista = treev_dict['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_telefone.insert(0, tree_lista[3])
        e_cal.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_assunto.insert(0, tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            tel = e_telefone.get()
            data = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()

            lista = [nome, email, tel, data, estado, assunto, valor_id]

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode estar vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso.')

            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_estado.delete(0, 'end')
            e_assunto.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 7 bold'), fg=cor_branca, bg=cor_verde, relief='raised', overrelief='ridge')
        b_confirmar.place(x=120, y=370)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

# Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dict = tree.item(treev_dados)
        tree_lista = treev_dict['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram apagados com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')

# Configurando Frame baixo

## Nome
l_nome = Label(frame_baixo, text='Nome *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

## Email
l_email = Label(frame_baixo, text='Email *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

## Telefone
l_telefone = Label(frame_baixo, text='Telefone *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160)

## Data da Consulta
l_cal = Label(frame_baixo, text='Data da consulta *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy', year=2026)
e_cal.place(x=15, y=220)

## Estado
l_estado = Label(frame_baixo, text='Estado da consulta *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)

## Sobre
l_assunto = Label(frame_baixo, text='Informação extra *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_assunto.place(x=10, y=260)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=290)

# Botão inserir

b_inserir = Button(frame_baixo, command=inserir,text='Inserir', width=10, font=('Ivy 9 bold'), fg=cor_branca, bg=cor_azul, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

# Botão atualizar

b_atualizar = Button(frame_baixo, command=atualizar,text='Atualizar', width=10, font=('Ivy 9 bold'), fg=cor_branca, bg=cor_verde, relief='raised', overrelief='ridge')
b_atualizar.place(x=115, y=340)

# Botão deletar

b_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), fg=cor_branca, bg=cor_vermelha, relief='raised', overrelief='ridge')
b_deletar.place(x=215, y=340)

# Frame direita
def mostrar():
    global tree

    lista = mostrar_info()

    ## Lista para cabeçalho
    tabela_head = ['ID', 'Nome', 'e-mail', 'Telefone', 'Data', 'Estado', 'Sobre']

    # Criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

    # Scrollbar vertical
    v_scrollb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)

    # Scrollbar horizontal
    h_scrollb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=v_scrollb.set, xscrollcommand=h_scrollb.set)

    # Organização das Scrollbars
    tree.grid(column=0, row=0, sticky='nsew')
    v_scrollb.grid(column=1, row=0, sticky='ns')
    h_scrollb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    # Orientação dos textos
    hd=['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor='center')
        # Ajustar a largura da coluna pro tamanho do texto do cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# Chamando a função mostrar()
mostrar()

janela.mainloop()


