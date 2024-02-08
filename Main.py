import flet as ft
from random import randint


def main(page: ft.Page):
    page.title = "GUESS ME"
    page.padding = 40
    page.bgcolor = "#f1f1f1"
    page.theme_mode = "light"

    answer = randint(1, 5)
    print(answer)

    page.fonts = {
        'MontserratAlternates-Black': 'fonts/MontserratAlternates-Bold.otf',
        'Montserrat-Bold': 'fonts/Montserrat-Bold.otf'
    }

    result = ft.Text(font_family='Montserrat-Bold', size=25, color="#5a205d", text_align='center')

    player_1 = ft.TextField(
        hint_text='Guess the number between 1 - 5',
        label='  player - 1', border_radius=100, text_align='center', border_color='#261827'
    )
    player_2 = ft.TextField(
        hint_text='Guess the number between 1 - 5',
        label='  player - 2', border_radius=100, text_align='center', border_color='#271918'
    )

    def check_player1(p1):
        if int(player_1.value) < answer:
            result.value = "Enter higher number"
        elif int(player_1.value) > answer:
            result.value = "Enter smaller number"
        else:
            result.value = "Congrats player-1 won the game!"
        page.update()

    def check_player2(p1):
        if int(player_2.value) < answer:
            result.value = "Enter higher number"
        elif int(player_2.value) > answer:
            result.value = "Enter smaller number"
        else:
            result.value = "Congrats player-2 won the game!"
        page.update()

    check_player_1 = ft.ElevatedButton("Check your guess", on_click=check_player1)
    check_player_2 = ft.ElevatedButton("Check your guess", on_click=check_player2)

    page.add(
        ft.Card(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            value="Guess me", color='white',
                            font_family='MontserratAlternates-Black',
                            size=40,
                        )
                    ],
                    alignment="center",
                ),
                padding=30
            ),
            color='#5a205d',
        ),

        ft.Column(
            controls=[
                ft.Row(controls=[player_1, check_player_1]),
                ft.Row(controls=[player_2, check_player_2]),
                result
            ], horizontal_alignment='center'
        )
    )

ft.app(target=main, assets_dir='Assets')