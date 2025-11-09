import flet as ft 
import random 

def main(page: ft.Page):
    page.title = "Game Rock, paper, scissors against the CPU"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Ttile
    title = ft.Text(
        value="Game Rock, paper, scissors against the CPU",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED
    )

    #Resultado de juego 
    resultado = ft.Text(
        value="",
        size=25,
        color=ft.Colors.GREEN,
        text_align=ft.TextAlign.CENTER 
    )

    #Logic of the game 
    options = ["Rock", "paper", "scissors"]
    def play(val_player):
        val_cpu = random.choice(options)

        if val_player == val_cpu:
            resultado.value = f"Player {val_player} vs CPU {val_cpu} \n¡Empatamos!"
        elif(val_player == "rock" and val_cpu == "scissors") \
                or  (val_player == "paper" and val_cpu == "rock") \
                or (val_player == "scissors" and val_cpu == "paper"):
            resultado.value = f"Player {val_player} vs CPU {val_cpu}\n¡Ganaste! >:("
        
        else: 
           resultado.value = f"Player {val_player} vs CPU {val_cpu}\n¡Perdiste! XD"
        page.update()
        

    
    #Buttons
    rock_btn = ft.ElevatedButton(
        text="rock",
        on_click=lambda e: play("Rock")
    )

    scissors_btn = ft.ElevatedButton(
        text="Scissors",
        on_click=lambda e: play("scissors")
    )

    paper_btn = ft.ElevatedButton(
        text="Paper",
        on_click=lambda e: play("paper")
    )

    button = ft.Row(
        controls=[rock_btn, paper_btn, scissors_btn], 
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(title, button, resultado)


if __name__ == "__main__":
    ft.app(target=main)

        
        


