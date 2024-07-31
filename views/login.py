import flet as ft

def login(page: ft.Page, width: int, height: int):

    # Propriedades do os texfields username e password, fizemos assim já que usamos for para gerar as TextFields
    textfiels = {
        'hint_text': ['Username', 'Password'],
        'autofocus': [True, False],
        'password': [False, True],
        'prefix_icon': [ft.icons.PERSON, ft.icons.KEY]
    }

    # View da rota login
    view = ft.View(
        route='/login',
        bgcolor=ft.colors.with_opacity(0.08, 'black'),
        controls=[
            ft.Container(
                width=width,
                height=height,
                content=ft.ResponsiveRow(
                    width=width,
                    height=height,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            col={'xs': 11, 'sm': 11, 'md': 3.5},
                            height=height * 0.40,
                            border_radius=10,
                            padding=ft.padding.only(
                                top=10,
                                right=8,
                                left=8
                            ),

                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        value='Login'.upper(),
                                        size=18,
                                        weight='bold',
                                        color=ft.colors.with_opacity(0.5, 'black')
                                    ),

                                    ft.Column(
                                        controls=[
                                            ft.TextField(
                                                hint_text=textfiels['hint_text'][i],
                                                prefix_icon=textfiels['prefix_icon'][i],
                                                autofocus=textfiels['autofocus'][i],
                                                password=textfiels['password'][i],
                                                hint_style=ft.TextStyle(
                                                    size=13,
                                                    color=ft.colors.with_opacity(0.5, 'black'),
                                                    weight='bold'
                                                ),
                                                text_style=ft.TextStyle(
                                                    size=13,
                                                    color=ft.colors.with_opacity(0.5, 'black'),
                                                    weight='bold'
                                                ),
                                                text_vertical_align=-0.40,
                                                border=ft.InputBorder.UNDERLINE
                                            ) for i in range(2) # Cria dois Texfields iguais em que as caracteristicas diferentes estão no dict acima
                                        ]
                                    ),

                                    ft.ResponsiveRow(
                                        controls=[
                                            ft.FloatingActionButton(
                                                text='Entrar'.upper(),
                                                icon=ft.icons.LOGIN,
                                                foreground_color=ft.colors.WHITE,
                                                bgcolor=ft.colors.BLUE,
                                                height=40,
                                                col={'xs': 12, 'sm': 12}
                                            )
                                        ]
                                    )
                                ],
                                spacing=8,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        )
                    ]
                )
            ),
            
        ]
    )

    return view