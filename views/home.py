import flet as ft
from controls.Strings import strings # Importando o texto da pagina inicial

def home(page: ft.Page, width: int, height: int):

    view = ft.View(
        route='/',
        bgcolor=ft.colors.with_opacity(0.08, 'black'),
        controls=[
            ft.ResponsiveRow(
                width=width,
                height=height,

                controls=[
                    ft.Container(
                        col={'xs': 11, 'sm': 11, 'md': 5},
                        height=height * 0.42,
                        bgcolor=ft.colors.WHITE,
                        border_radius=ft.border_radius.only(
                            top_right=12,
                            bottom_left=12
                        ),
                        padding=ft.padding.only(
                            top=12,
                            left=10,
                            right=10
                        ),

                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value='Bem Vindo'.upper(),
                                    size=20,
                                    weight='bold',
                                    color=ft.colors.with_opacity(0.5, 'black')
                                ),

                                ft.Divider(
                                    height=1,
                                    thickness=2
                                ),

                                ft.Text(
                                    value=strings['Bem Vindo'],
                                    size=18,
                                    weight='bold',
                                    color=ft.colors.with_opacity(0.5, 'black'),
                                    text_align='center'
                                ),

                                ft.IconButton(
                                    icon=ft.icons.LOGIN,
                                    icon_size=30,
                                    icon_color=ft.colors.BLUE,
                                    tooltip='Login',
                                    on_click= lambda e: page.go('/login')
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )

    return view