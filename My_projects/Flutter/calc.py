import flet as ft
# flutter so funny
def main(page: ft.Page):
    #title
    page.title = "Flet counter example"
    #vertial 세로 가운데 정렬
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #텍스트 오른쪽에서 시작 
    txt_number = ft.TextField(value="0",text_align=ft.TextAlign.RIGHT,width=250)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row([
               txt_number],
               alignment=ft.MainAxisAlignment.CENTER),
               
        ft.Row(
            [
                ft.TextButton("7"),
                ft.TextButton("8"),
                ft.TextButton("9"),
                ft.TextButton("*")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextButton("4"),
                ft.TextButton("5"),
                ft.TextButton("6"),
                ft.TextButton("-")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextButton("1"),
                ft.TextButton("2"),
                ft.TextButton("3"),
                ft.TextButton("+")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),  
        ft.Row(
            [
                ft.TextButton("0"),
                ft.TextButton("."),
                ft.TextButton("="),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)