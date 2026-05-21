# Importando o Tkinter
from tkinter import *

# Importando o Tkcalendar
from tkcalendar import Calendar, DateEntry

# Cores
cor_branca = '#FFFAFA'
cor_verde = '#5FB861'
cor_vermelha = '#FF6E6E'
cor_azul = '#7AC6FF'
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
l_sobre = Label(frame_baixo, text='Informação extra *', anchor='nw', font=('Ivy 10 bold'), fg=cor_preta,bg=cor_branca, relief='flat')
l_sobre.place(x=10, y=260)
e_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_sobre.place(x=15, y=290)

janela.mainloop()


