import flet as ft

def main(page: ft.Page):

    page.window_resizable = False
    page.window_width = 300
    page.window_height = 300
    page.padding = 30

    #Poner todo centrado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Con este metodo pones la ventana al medio
    page.window_center()

    def log(e):
        contenedor.visible = False
        contenedor.update()
        initLog()
        
    def initLog():

        def verifymail(e):
            if(txt.value == ""):
                txt.border_color = "red"
                txt.update()
            else:
                txt.visible = False
                btnpass.visible = False

                def finalog(e):
                    if(txtPass.value == ""):
                        txtPass.border_color = "red"
                        txtPass.update()
                    else:
                        txtPass.visible = False
                        btnFinal.visible = False

                        page.add(ft.Text("Completed!"))

                def reactivar(e):
                    txtPass.border_color = ""
                    txtPass.update()

                txtPass = ft.TextField(label="Password",password=True,can_reveal_password=True,on_focus=reactivar)
                btnFinal = ft.ElevatedButton("Login",on_click=finalog)

                page.add(txtPass,btnFinal)
                txt.update()

        def reactivar(e):
            txt.border_color = ""
            txt.update()

        
        txt = ft.TextField(label="Correo",on_focus=reactivar)
        btnpass = ft.ElevatedButton("Ready",on_click=verifymail)
        page.add(txt,btnpass)

    contenedor = ft.Container(ft.Column([
        ft.ElevatedButton("Iniciar Sesion",width=150,on_click=log),
        ft.ElevatedButton("Registrar",width=150)
    ]))

    page.add(contenedor)

    
ft.app(target=main)

