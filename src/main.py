import flet as ft
import random

def main(page: ft.Page):
    page.title = 'Juego de Piedra, Papel o Tijera contra la CPU'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Título 
    titulo = ft.Text(
        value= 'Juego de Piedra, Papel o Tijera contra la CPU',
        size= 30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
    )


    #Resultado del juego
    resultado = ft.Text(
        value='',
        size=25,
        color=ft.Colors.RED,
        text_align=ft.TextAlign.CENTER,
    )

    # Lógica del juego
    opciones = ['Piedra', 'Papel', 'Tijera']
    def jugar(val_jugador):
        val_cpu = random.choice(opciones)

        if val_jugador == val_cpu:
            resultado.value = f'Jugador {val_jugador} vs CPU {val_cpu}\n ¡Empatamos!'

        elif val_jugador == ('Piedra' and val_cpu == 'Tijera')\
                or (val_jugador == 'Papel' and val_cpu == 'Piedra')\
                or (val_jugador == 'Tijera' and val_cpu == 'Papel'):
            resultado.value = f'Jugador {val_jugador} vs CPU {val_cpu}\n ¡Ganaste! >:('
        else: 
            resultado.value = f'Jugador {val_jugador} vs CPU {val_cpu}\n ¡Perdiste! XD'
        page.update()
    
    # Botones
    piedra_btn = ft.ElevatedButton(
        text='Piedra', 
        on_click=lambda e: jugar('Piedra')
    )

    Papel_btn = ft.ElevatedButton(
        text='Papel', 
        on_click=lambda e: jugar('Papel')
    )

    Tijera_btn = ft.ElevatedButton(
        text='Tijera', 
        on_click=lambda e: jugar('Tijera')
    )

    botones = ft.Row(
        controls=[piedra_btn, Papel_btn, Tijera_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
    )

    page.add(titulo, botones, resultado)


if __name__ == '__main__':
    ft.app(target=main)