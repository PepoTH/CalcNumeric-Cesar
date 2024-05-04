import flet as ft

class ButtonObject:
    def __init__(self, fecha, **kwargs):
        self.fecha = fecha
        self.kwargs = kwargs

def main(page):
    buttons = []
    objects = [
        ButtonObject("2022-01-01", name="Button 1", description="This is button 1"),
        ButtonObject("2022-01-02", name="Button 2", description="This is button 2"),
        ButtonObject("2022-01-03", name="Button 3", description="This is button 3"),
    ]

    for obj in objects:
        btn = ft.ElevatedButton(obj.fecha, on_click=lambda e, obj=obj: show_details(page, obj))
        buttons.append(btn)

    page.add(ft.Column(buttons))

def show_details(page, obj):
    page.update()
    page.add(ft.Text(f"Fecha: {obj.fecha}"))
    page.add(ft.Text(f"Name: {obj.kwargs.get('name')}"))
    page.add(ft.Text(f"Description: {obj.kwargs.get('description')}"))

ft.app(main)