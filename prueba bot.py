import flet

def main(page: flet.Page):
    def button_clicked(e):
        button = e.control
        textfield.text = button.text

    textfield = flet.TextField()
    buttons = [flet.ElevatedButton(f"Button {i}", on_click=lambda e: button_clicked(e)) for i in range(9)]
    for button in buttons:
        page.add(button)
    page.add(textfield)

flet.app(target=main)