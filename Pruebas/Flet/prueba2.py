import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=200,
            height=200,
            bgcolor=ft.colors.GREEN_200,
            border_radius=10,
            content=ft.Container(
                width=100,
                height=100,
                bgcolor=ft.colors.BLUE_200,
                border_radius=5,
                alignment=ft.alignment.center,  # center the second container inside the first container
            ),
        )
    )

ft.app(target=main)