import flet as ft 
import random
def main(page: ft.Page):
    page.title = 'juego de piedra papel o tijeras contra la CPU'
    page.vertical_aligment = ft.MainAxisAlignment.CENTER 
    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER 

    #Titulo
    titulo = ft.Text(
        value='Juego de piedra papel o tijera contra la CPU',
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
    )

    # Resultado del juego
    resultado = ft.Text(
        value='',
        size=25,
        color=ft.Colors.RED,
        text_align=ft.TextAlign.CENTER
    )

    # Lógica del Juego 
    opciones = ['piedra', 'papel', 'tijera']
    def jugar(val_jugador):
        val_cpu = random.choice(opciones)

        if val_jugador == val_cpu:
            resultado.value = f'jugador {val_jugador} vs CPU {val_cpu}\n¡Empatamos!'
        elif (val_jugador == 'piedra' and val_cpu == 'tijera') \
                or (val_jugador == 'papel' and val_cpu == 'piedra') \
                or (val_jugador == 'tijera' and val_cpu == 'papel'):
            resultado.value = f'jugador {val_jugador} vs CPU {val_cpu}\n¡Ganaste! 😃' 
        else:
            resultado.value = f'jugador {val_jugador} vs CPU {val_cpu}\n¡Perdiste! 🙁'

        page.update()
    
    # Botones 
    piedra_btn = ft. ElevatedButton(
       text='piedra',
       on_click=lambda e: jugar('piedra')
    )
    tijera_btn = ft. ElevatedButton(
        text='tijera',
        on_click=lambda e: jugar('tijera')
    )
    papel_btn = ft. ElevatedButton(
        text='papel',
        on_click=lambda e: jugar('papel')
    )
    botones = ft.Row(
        controls=[piedra_btn, papel_btn, tijera_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(titulo,botones, resultado)

if __name__ == '__main__' : 
    ft.app(target=main)