import flet as ft
from funciones import *
import numpy as np
import random

def main(page: ft.Page):
    #Creando Ventana
    page.window_resizable = False
    page.window_width = 450
    page.window_height = 400
    page.padding = 30
    page.window_title_bar_hidden = True
    
    page.theme_mode = ft.ThemeMode.LIGHT
    azul = '#6F86FF'

    def temas(e):
        if(e.control.value):
            page.theme_mode = ft.ThemeMode.LIGHT
            contentMat.bgcolor = 'white'
            azul = '#6F86FF'
        else:

            page.theme_mode = ft.ThemeMode.DARK
            contentMat.bgcolor = '#252525'
            
        page.update()
    
    #Creacion de Eventos --------------------------------
    #Evento para transportar desde main hasta gauss
    def gauss(e):
        _main_.visible = False
        gaussiana.visible = True
        page.update()

    #Evento para validar la entrada del tamano de la matriz
    def size(e):
        if(len(txtSize.value)>1):
            txtSize.value = txtSize.value[1:]
        if not(txtSize.value in ['2','3','4','5']):
            txtSize.value = ''
        txtSize.update()

    #Evento para validar el textField de las conversiones
    def validConvert(e):
        if not(e.control.value == ''):
            if not(e.control.value[-1] in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']):
                e.control.value = e.control.value[0:len(e.control.value) - 1]
                e.control.update()

    #Evento para validar los numeros de la matriz
    def validNum(e):
        if(e.control.value != ''):
            if(len(e.control.value)>3):
                e.control.value = e.control.value[3:]
            if not(e.control.value[-1] in ['1','2','3','4','5','6','7','8','9','0','-','.']):
                e.control.value = ''
        e.control.update()

    #Evento para rellenar aleatorio
    def aleatorio(e):
        cuadro.controls.clear()
        n = random.randint(2,5)
        for i in range(0,n):
            fila = ft.Row([],alignment='center')
            for j in range(0,n + 1):
                numeros = ft.TextField(width=20,height=20,text_size=10
                ,content_padding=0,text_align='center'
                ,border_color='#f0f0f0',value=str(random.randint(1,99)),on_change=validNum)
                fila.controls.append(numeros)
                if(j == n - 1):
                    fila.controls.append(ft.Text('='))
            cuadro.controls.append(fila)
        page.update()
        pass

    #Evento para transportar desde main hasta Conversiones
    def conv(e):
        _main_.visible = False
        conversiones.visible = True
        page.update()

    #Evento para volver al main
    def back(e):
        _main_.visible = True
        gaussiana.visible = False
        conversiones.visible = False
        page.update()     

    #Evento para convertir y vincular con la clase(funciones.py)
    def convert(e):
        if(txt.value != '' and desde.value != None and hacia.value != None):
            txt.value = str(sistemas(txt.value,desde.value,hacia.value))
            txt.update()

    #Evento para limpiar conversiones
    def clear(e):
        txt.value = ''
        desde.value = None
        hacia.value = None
        page.update()

    #Evento para crear la matriz a base del numero dado
    def crear(e):
        cuadro.controls.clear()
        
        if(txtSize.value != ''):
            for i in range(0,int(txtSize.value)):
                fila = ft.Row([],alignment='center')
                for j in range(0,int(txtSize.value) + 1):
                    numeros = ft.TextField(width=20,height=20,text_size=10
                     ,content_padding=0,text_align='center'
                     ,border_color='#f0f0f0',value='',on_change=validNum)
                    fila.controls.append(numeros)
                    if(j == int(txtSize.value) - 1):
                        fila.controls.append(ft.Text('='))
                cuadro.controls.append(fila)
            page.update()
            
        pass

    #Evento para resover matriz
    def resolver():
        try:
            A = np.zeros((len(cuadro.controls),len(cuadro.controls)))
            b = np.zeros((len(cuadro.controls),1))
            x = np.zeros((len(cuadro.controls),1))

            for i in range(0,len(cuadro.controls)):
                for j in range(0,len(cuadro.controls) + 1):
                    if(j == len(cuadro.controls)):
                        try:
                            b[i] = float(cuadro.controls[i].controls[j + 1].value)
                        except ValueError:
                            pass
                    else:
                        try:
                            A[i][j] = float(cuadro.controls[i].controls[j].value)  
                        except ValueError:
                            pass   
            
            soluciones = seidel(A,b,x)
            if(soluciones is None):
                soluciones = ['Sin Convergencia']

            txtSolucion.value = ''
            for i in range(0,len(soluciones)):
                txtSolucion.value += f'X{i + 1}='+str(soluciones[i]).replace('[','').replace(']','') + '\n'
            
            txtSolucion.update()

        except ValueError and RuntimeWarning and TypeError and UnboundLocalError:
            txtSolucion.value = 'Error: Sin Convergencia o Vacio'
            txtSolucion.update()

    #Evento para llamar al evento de resolver, evento usando para el boton Automatico
    def btnSolve(e):
        resolver()

    def borrar(e):
        cuadro.controls.clear()
        txtSize.value = ''
        txtSolucion.value = ''
        page.update()

    #Evento para apertura de las Intruccion o informacion
    def intructions(e):
        alerta = ft.BottomSheet(
                        ft.Container(
                            ft.Column([
                                ft.Text('1- Si desea automatico presione el boton "Automatico" y despues "Resolver"\n'+
                                        '2- Si Desea Manual siga los siguientes pasos:\n'+'   A-Ingrese un Numero para la matriz y presione"Crear"\n'+
                                        '   B- Ingrese los valores en la matriz(0-999)\n'+
                                        '   C- Presione Resolver\n')
                            ]), width=400, height=250, padding=30
                        ),
                        open=True
                    )
        page.overlay.append(alerta)
        page.update()
        
    #Creacion de Elementos graficos --------------------------------
    cuadro = ft.Column([],alignment=ft.MainAxisAlignment.CENTER)

    contentMat =ft.Container(width=220,height=200
        ,bgcolor='white',margin=ft.margin.only(top=30),border_radius=20,
        shadow=ft.BoxShadow(0.5,5,'#D0D0D8'),padding=15,content=cuadro)
    
    txtSize = ft.TextField(width=50
            ,height=50,content_padding=10,text_align='center',
            border_color='#D0D0D8'
            ,hint_text='n',border_radius=15,on_change=size)
    
    txtSolucion = ft.TextField(width=100
            ,height=90,content_padding=10,text_align='center',text_size=9,
            border_color='#D0D0D8',hint_text='Soluciones'
            ,border_radius=15,disabled=True,multiline=True,min_lines=7)
    
    toSolve = ft.FilledButton('Resolver'
            ,style=ft.ButtonStyle(bgcolor=azul)
            ,width=130,on_click=btnSolve)

    #Container con toda la interfaz de Gauss-Seidel
    gaussiana = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('Gauss-Seidel',weight=ft.FontWeight.W_500,
                    font_family='Poppins',size=15)
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.FilledButton('Automatico',style=ft.ButtonStyle(bgcolor=azul),on_click=aleatorio),
                ft.IconButton(ft.icons.INFO_OUTLINE,icon_color=azul,on_click=intructions)
            ],alignment='center'),
            ft.Row([
                ft.Column([
                    contentMat
                ]),
                ft.Column([
                    ft.Row([
                        txtSize,
                        ft.FilledButton('Crear',style=ft.ButtonStyle(color=azul,bgcolor='transparent'),on_click=crear)
                    ],alignment='center',width=170),
                    ft.Row([
                        toSolve
                    ],alignment='center',width=170),
                    ft.Row([
                        txtSolucion,
                        ft.Column([
                            ft.IconButton(ft.icons.DELETE,on_click=borrar,icon_color=azul),
                            ft.IconButton(ft.icons.EXIT_TO_APP,on_click=back,icon_color=azul)
                        ],spacing=0)
                    ],alignment='center',width=170)
                ],alignment='center',height=260)
            ],vertical_alignment='start')
            
        ])
    )

    txt = ft.TextField(width=page.width*0.25,label='Numero',
                       border_color='#E1E1E1',border_radius=10,on_change=validConvert)
    
    desde = ft.Dropdown(width=page.width*0.10,border_color='#E1E1E1'
                                ,border_radius=10,hint_text='N/A',options=[
                                    ft.dropdown.Option('Dec'),
                                    ft.dropdown.Option('Bin'),
                                    ft.dropdown.Option('Oct'),
                                    ft.dropdown.Option('Hex'),
                                    ft.dropdown.Option('Ter'),
                                    ft.dropdown.Option('Cuar'),
                                ])
    
    hacia = ft.Dropdown(width=page.width*0.10,border_color='#E1E1E1'
                                ,border_radius=10,hint_text='N/A',options=[
                                    ft.dropdown.Option('Dec'),
                                    ft.dropdown.Option('Bin'),
                                    ft.dropdown.Option('Oct'),
                                    ft.dropdown.Option('Hex'),
                                    ft.dropdown.Option('Ter'),
                                    ft.dropdown.Option('Cuar'),
                                ])
    
    #Container para toda la interfaz de las Conversiones
    conversiones = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('Sistemas Numericos',weight=ft.FontWeight.W_500,
                    font_family='Poppins',size=15)
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([
                ft.Row([
                    txt,desde,hacia
                        ],alignment='center'),
                ft.Row([
                    ft.FilledButton('Convertir'
                                ,style=ft.ButtonStyle(bgcolor=azul),
                                    width=200,on_click=convert),
                    ft.IconButton(ft.icons.DELETE,icon_color=azul,on_click=clear)
                    
                        ],alignment='center')
            ],alignment=ft.MainAxisAlignment.CENTER)

            ,ft.Row([
                ft.IconButton(ft.icons.EXIT_TO_APP,on_click=back,icon_color=azul)
            ],vertical_alignment=ft.MainAxisAlignment.END)
        ],spacing=75,alignment='center')
    )

    btns = ft.Row([
            ft.FilledButton('Gaussiana',style=ft.ButtonStyle(bgcolor=azul),on_click=gauss),
            ft.FilledButton('Convertir',style=ft.ButtonStyle(bgcolor=azul),on_click=conv)
    ],alignment=ft.MainAxisAlignment.CENTER)

    #Main
    _main_ = ft.Container(
        content=ft.Column([
            ft.Text('Evaluaciones',font_family='Poppins',size=20)
            ,btns,ft.Row([
                ft.Switch('Tema',active_color=azul,on_change=temas,value=True)
            ],alignment='center')
        ],alignment=ft.MainAxisAlignment.CENTER
        ,horizontal_alignment=ft.CrossAxisAlignment.CENTER,height=page.height/2)
    )

    conversiones.visible = False
    gaussiana.visible = False

    page.add(_main_,conversiones,gaussiana)
    
    #Agregar sugerencias e intrucciones a cada panel
    
ft.app(target=main)