
import flet as ft
from flet import *
import asyncio


def main(page: ft. Page) -> None:
    page.title = 'Conferentes. 2024- CDQ / RJ'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page. window_height = 723
    page.scroll = ft.ScrollMode.ALWAYS
    page.window_top = 2
    page.window_left = 920
    page.window_resizable = False
    page.spacing = 25
    


    #botão 1
    estilo01 = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.BLUE_900,
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
        },

        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.GREEN,
        },

        padding={ ft.MaterialState.HOVERED: 12
        },

        animation_duration=500,

        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=5),
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=9)
        },

        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
        }

    )

    #botão 2
    estilo02 = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.WHITE70,
        },

        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.RED,
        },

        padding={ ft.MaterialState.HOVERED: 12
        },

        animation_duration=500,

        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=6),
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=9)
        },

        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
        }

    )

    
    #botão 3
    estilo03 = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
        },

        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.BLUE_700,
        },

        padding={ ft.MaterialState.HOVERED: 12
        },

        animation_duration=200,

        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=6),
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=9)
        },

        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.WHITE),
        }

    )


    async def animate(e = None):
        while True:
            img2.offset.y = -0.3
            img2.update()
            await asyncio.sleep(3)

            img2.offset.y = 0
            img2.update()
            await asyncio.sleep(3)


    img3 = ft.Image(
        src = f'https://images.stockopedia.com/security_images/bunzl-lse-bnzl.jpeg',
        border_radius=0,
        height=50,
        width=50,
        visible= True

    )
    
    img2 = ft.Image(
        src = f'https://tse4.mm.bing.net/th?id=OIP.6upCQYeA-Q2Bmz7e0O0LeAHaEK&pid=Api&P=0&h=180',
        offset = ft.Offset(x=0, y=0),
        animate_offset= ft.Animation(duration=2000, curve=ft.AnimationCurve.EASE),
        border_radius= 10,
        height= 180,
        width= 490,
        visible= True
        
    )
    page.run_task(animate)


    def apagar(e):
        text_username.value = text_username.clean()
        text_password.value = text_password.clean()
        Checkbox_signup.value = Checkbox_signup.clean()

        page.update()
    


    # cadastro dos logins
    login1 = 'tiagor'
    senha1 = '123'


    esp = Text()
    titulo = ft.Text(value='Minha performance', italic= True, size= 29, color= ft.colors.BLUE)
    titulo2 = ft.Text(value='Verificação dos conferentes',size=30, italic= True, color= ft.colors.BLUE_300)


    text_username:  TextField = TextField(label='Usuário:', text_align=ft.TextAlign.LEFT, width=250,border_width = 1, color= ft.colors.WHITE, border_color= ft.colors.BLUE)
    text_password:  TextField = TextField(label='Senha:', text_align=ft.TextAlign.LEFT, width=250,border_width = 1, color= ft.colors.WHITE, border_color= ft.colors.BLUE, password= True)
    Checkbox_signup: Checkbox = Checkbox(label='Não sou um robô!',value= False, check_color= ft.colors.BLUE)
    button_submit: ElevatedButton = ElevatedButton(text='Fazer login', width=250, disabled= True, style = estilo01,)
    button_submit3: ElevatedButton = ElevatedButton(text='Nossa empresa - Lanlimp', width=250,icon=ft.icons.CABIN, url='http://lanlimp.com.br/',style= estilo03)
    button_submit4: ElevatedButton = ElevatedButton(text='Meu desenpenho',width=350,icon=ft.icons.CLEAR_ALL, icon_color=ft.colors.GREEN ,url='www.google.com',style= estilo03)
    button_submit5: ElevatedButton = ElevatedButton(text='Minhas ocorrências', width=350,icon=ft.icons.GRADIENT,icon_color= ft.colors.GREEN,url='www.google.com',style= estilo03)
    button_limpar: ElevatedButton = ElevatedButton(text=' limpar', width=110, style=estilo02,icon= ft.icons.DELETE,on_click= apagar)
    

    def validate(e: ControlEvent) -> None:

        if all([text_username.value,text_password.value, Checkbox_signup.value]):
            button_submit.disabled = False

      
            if text_password.value == senha1:
                button_submit.disabled = False

            if text_username.value == login1:
                button_submit.disabled = False

            else:
                button_submit.disabled = True

        page.update()
        

    def submit(e: ControlEvent) -> None:

        #tela 2
        page.clean()
        page.add(
             Row(
            controls=[
                Column(
                    [   
                       esp,
                       titulo2,
                       esp,
                       button_submit4,
                       esp,
                       button_submit5,
                       
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),esp,img2,esp,img3
           
    )

    Checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    #tela 1
    page.add(
        Row(
    controls=[
        Column(
            [   titulo,
                text_username,
                text_password,
                Checkbox_signup,
                button_submit,
                button_limpar,
                button_submit3
                
               
            ]
         )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    ),esp,img2,img3
     
    )
    
 
if __name__ == '__main__':
    ft.app(target=main, assets_dir= 'assets')
