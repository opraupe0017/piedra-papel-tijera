import flet as ft
import random

def main(page: ft.Page):
    page.title = "Piedra-papel-tijera vs CPU"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        value="Piedra, Papel o Tijera vs CPU",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="blue",
    )

    resultado = ft.Text(
        value="",
        size=25,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
        color="red",
    )

    opciones = ["Piedra", "Papel", "Tijera"]

    def jugar(Val_jugador):
        Val_cpu = random.choice(opciones)

        if Val_jugador == Val_cpu:
            resultado.value = f"jugador: {Val_jugador}  CPU: {Val_cpu}\n ¡Empate!"
        elif (Val_jugador == "Piedra" and Val_cpu == "Tijera") \
            or (Val_jugador == "Papel" and Val_cpu == "Piedra") \
            or (Val_jugador == "Tijera" and Val_cpu == "Papel"):
            resultado.value = f"jugador: {Val_jugador}  CPU: {Val_cpu}\n ¡Ganaste! >:("
        else:
            resultado.value = f"jugador: {Val_jugador}  CPU: {Val_cpu}\n ¡Perdiste! XD"

        page.update()

    piedra_btn = ft.ElevatedButton(
        text="Piedra",
        on_click=lambda e: jugar("Piedra")
    )
    papel_btn = ft.ElevatedButton(
        text="Papel",
        on_click=lambda e: jugar("Papel")
    )
    tijera_btn = ft.ElevatedButton(
        text="Tijera",
        on_click=lambda e: jugar("Tijera")
    )

    botones = ft.Row(
        controls=[piedra_btn, papel_btn, tijera_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(titulo, botones, resultado)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
