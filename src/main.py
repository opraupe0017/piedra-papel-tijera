import flet as ft
import random

def main(page: ft.Page):
    page.title ="Juego de piedra papel o tijera contra la CPU"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Titulo
    titulo = ft.Text(
        value="Juego de piedera papel o tijera contra la CPU",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED,
    )

    # resultado.value del juego
    resultado = ft.Text(
        value="",
        size=25,
        color=ft.Colors.BLUE,
        text_align=ft.TextAlign.CENTER

    )

    #logica del juego
    opciones = ["piedra","papel","tijera"]
    def jugar(val_jugador):
        val_cpu = random.choice(opciones)

        if val_jugador == val_cpu:
            resultado.value = f"Jugador{val_jugador}vs CPU {val_cpu}\n!empatamos"
        elif (val_jugador == 'piedra' and val_cpu == 'tijera') \
                or (val_jugador == 'papel' and val_cpu == 'piedra') \
                or (val_jugador == 'tijera' and val_cpu == 'papel'):
            resultado.value = f'jugador {val_jugador} vs CPU {val_cpu}\n!ganaste >:)'
        else:
             resultado.value = f'jugador {val_jugador} vs CPU {val_cpu}\n!perdiste >:(' 
        page.update()
    
    # botones
    piedra_btn = ft.ElevatedButton(
        text='Pierda',
        on_click=lambda e: jugar('piedra')
    )

    papel_btn = ft.ElevatedButton(
        text='Papel',
        on_click=lambda e: jugar('papel')
    )
    
    tijera_btn = ft.ElevatedButton(
        text='Tijera',
        on_click=lambda e: jugar('tijera')
    )

    botones = ft.Row(
        controls=[piedra_btn, papel_btn, tijera_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(titulo, botones, resultado)


if __name__ == '__main__':
    ft.app(target=main)



