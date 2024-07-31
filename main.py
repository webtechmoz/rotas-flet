import flet as ft
from views.home import home # Importando a view home
from views.login import login # Importando a view login
from views.error404 import error404 # Importando a view error404

def main(page: ft.Page):
    page.title = page.route

    WIDTH = page.width
    HEIGHT = page.height

    def router(route):
        """
            Esta função visão fazer a manipulação das views wm conformidade com a rota definida pelo usuário
        """
        page.views.clear() # Estou a limpar as views da page

        if page.route == '/':
            page.views.append(home(page, WIDTH, HEIGHT)) # Estou a adicionar a view na rota home
        
        elif page.route == '/login':
            page.views.append(login(page, WIDTH, HEIGHT))
        
        else:
            page.views.append(error404(page, WIDTH, HEIGHT))

        page.title = page.route
        page.update() # Estou a actualizar a pagina visível no usuário
    
    page.on_route_change = router # Evento que escuta a alteração da rota no navegador
    page.go(page.route) # Evento que vai para a tora especificada

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)