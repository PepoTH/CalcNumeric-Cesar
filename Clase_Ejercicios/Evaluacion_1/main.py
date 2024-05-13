import flet as ft
from funciones import *
import numpy as np

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 450
    page.window_height = 400
    page.padding = 30
    
    page.theme_mode = ft.ThemeMode.LIGHT

    def gauss(e):
        _main_.visible = False
        gaussiana.visible = True
        page.update()

    def size(e):
        if(len(txtSize.value)>1):
            txtSize.value = txtSize.value[1:]
        if not(txtSize.value in ['2','3','4','5']):
            txtSize.value = ''
        txtSize.update()

    def validNum(e):
        if(len(e.control.value)>3):
            e.control.value = e.control.value[3:]
        if not(e.control.value[-1] in ['1','2','3','4','5','6','7','8','9']):
            e.control.value = ''
        e.control.update()

    def random(e):
        pass

    def conv(e):
        _main_.visible = False
        conversiones.visible = True
        page.update()

    def back(e):
        _main_.visible = True
        gaussiana.visible = False
        conversiones.visible = False
        page.update()     

    def convert(e):
        if(txt.value != '' and desde.value != None and hacia.value != None):
            txt.value = str(sistemas(txt.value,desde.value,hacia.value))
            txt.update()

    def clear(e):
        txt.value = ''
        desde.value = None
        hacia.value = None
        page.update()

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
            
            if(''.join(cuadro.controls)==''):
                if(''.join(A)!='' and ''.join(b)!=''):
                    soluciones = seidel(A,b,x)
            
            txtSolucion.value = ''
            for i in range(0,len(soluciones)):
                txtSolucion.value += f'X{i + 1}='+str(soluciones[i]).replace('[','').replace(']','') + '\n'
            
            txtSolucion.update()
        except ValueError and RuntimeWarning and TypeError and UnboundLocalError:
            txtSolucion.value = 'Error: Sin Convergencia o Vacio'
            txtSolucion.update()

    def btnSolve(e):
        resolver()
        pass

    def borrar(e):
        cuadro.controls.clear()
        txtSize.value = ''
        txtSolucion.value = ''
        page.update()

    cuadro = ft.Column([],alignment=ft.MainAxisAlignment.CENTER)

    contentMat =ft.Container(width=220,height=200
        ,bgcolor='white',margin=ft.margin.only(top=30),border_radius=20,
        shadow=ft.BoxShadow(0.5,5,'#D0D0D8'),padding=15,content=cuadro)
        
    #Forma de Capturar 
    #print(cuadro.controls[0].controls[0].value)
    
    txtSize = ft.TextField(width=50
            ,height=50,content_padding=10,text_align='center',
            border_color='#D0D0D8',hint_text='n',border_radius=15,on_change=size)
    
    txtSolucion = ft.TextField(width=100
            ,height=90,content_padding=10,text_align='center',text_size=9,
            border_color='#D0D0D8',hint_text='Soluciones'
            ,border_radius=15,disabled=True,multiline=True,min_lines=7)

    gaussiana = ft.Container(
        ft.Column([
            ft.Row([
                ft.Text('Gauss-Seidel',weight=ft.FontWeight.W_500,
                    font_family='Poppins',size=15)
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.FilledButton('Automatico',style=ft.ButtonStyle(bgcolor='#6F86FF'),on_click=random)
            ],alignment='center'),
            ft.Row([
                ft.Column([
                    contentMat
                ]),
                ft.Column([
                    ft.Row([
                        txtSize,
                        ft.FilledButton('Crear',style=ft.ButtonStyle(color='#6F86FF',bgcolor='white'),on_click=crear)
                    ],alignment='center',width=170),
                    ft.Row([
                        ft.FilledButton('Resolver',style=ft.ButtonStyle(bgcolor='#6F86FF'),width=130,on_click=btnSolve)
                    ],alignment='center',width=170),
                    ft.Row([
                        txtSolucion,
                        ft.Column([
                            ft.IconButton(ft.icons.DELETE,on_click=borrar,icon_color='#6F86FF'),
                            ft.IconButton(ft.icons.EXIT_TO_APP,on_click=back,icon_color='#6F86FF')
                        ],spacing=0)
                    ],alignment='center',width=170)
                ],alignment='center',height=260)
            ],vertical_alignment='start')
            
        ])
    )

    txt = ft.TextField(width=page.width*0.25,label='Numero',
                       border_color='#E1E1E1',border_radius=10)
    
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
                                ,style=ft.ButtonStyle(bgcolor='#6F86FF'),
                                    width=200,on_click=convert),
                    ft.IconButton(ft.icons.DELETE,icon_color='#6F86FF',on_click=clear)
                    
                        ],alignment='center')
            ],alignment=ft.MainAxisAlignment.CENTER)

            ,ft.Row([
                ft.IconButton(ft.icons.EXIT_TO_APP,on_click=back,icon_color='#6F86FF')
            ],vertical_alignment=ft.MainAxisAlignment.END)
        ],spacing=75,alignment='center')
    )

    btns = ft.Row([
            ft.FilledButton('Gaussiana',style=ft.ButtonStyle(bgcolor='#6F86FF'),on_click=gauss),
            ft.FilledButton('Convertir',style=ft.ButtonStyle(bgcolor='#6F86FF'),on_click=conv)
    ],alignment=ft.MainAxisAlignment.CENTER)

    _main_ = ft.Container(
        content=ft.Column([
            ft.Text('Evaluaciones',font_family='Poppins',size=20)
            ,btns
        ],alignment=ft.MainAxisAlignment.CENTER
        ,horizontal_alignment=ft.CrossAxisAlignment.CENTER,height=page.height/2)
    )

    conversiones.visible = False
    gaussiana.visible = False

    #
    page.add(_main_,conversiones,gaussiana)
    
ft.app(target=main)