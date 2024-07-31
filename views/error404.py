import flet as ft

def error404(page: ft.Page, width: int, height: int):

    """
        Esta página é chamada sempre que o usuario informa uma rota que não existe no sistema.
    """

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
                        height=height * 0.20,
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
                                    value='404'.upper(),
                                    size=40,
                                    weight='bold',
                                    color=ft.colors.with_opacity(0.7, 'red')
                                ),

                                ft.Text(
                                    value="Oop's, a página não existe",
                                    size=20,
                                    weight='bold',
                                    color=ft.colors.with_opacity(0.5, 'black'),
                                    text_align='center'
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