import flet as ft
# flutter so funny
def main(page: ft.Page):
    #title
    page.title = "Flet counter example"
    
    #vertial 세로 가운데 정렬
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #텍스트 오른쪽에서 시작 
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)