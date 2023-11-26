import flet as ft
import minecraft_launcher_lib
import os
import subprocess
from time import sleep
from flet import (
    Image,
    Row,
    Container,
    Column,
    Stack,
    ElevatedButton,
    ButtonStyle,
    RoundedRectangleBorder,
    TextField,
    Dropdown,
    dropdown,
    ProgressBar,
    Text
)


user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"


def inicio_mine(e):
    ejecuta_mine(mine_user)

# Insalación de Minecraft
def install_minecraft():
    minecraft_launcher_lib.install.install_minecraft_version(
        minecraft_version, minecraft_directory)
    print(f'Instalada la version {minecraft_version}')


# Instalar Forge
def install_forge():
    forfe = minecraft_launcher_lib.forge.find_forge_version(minecraft_version)
    print(forfe)
    minecraft_launcher_lib.forge.install_forge_version(
        forfe, minecraft_directory)
    print(f'Instalado Forge {forfe}')

# Ver todas las versiones que tengo instaladas


def ejecuta_mine(mine_user):
    forts = minecraft_launcher_lib.utils.get_installed_versions(
        minecraft_directory)
    for fort in forts:
        print(fort['id'])

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',

        "jvmArguments": ["-Xmx2G", "-Xms2G"],  # The jvmArguments
        "launcherVersion": "0.0.1",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        minecraft_version, minecraft_directory, options)
    subprocess.run(minecraft_command)






# ------------------------------------- Interfaz de la app ---------------------------------
def main(page: ft.Page):
    global mine_user,btn,minecraft_version
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = 'Launcher'
    page.window_width = 450
    page.window_height = 650
    page.window_resizable = False
    page.padding = 0


    logo = Image('logo.png', height=50)
    spases = Container(width=50, height=400)
    spases1 = Container(width=1, height=5)
    bg = Image('bg.jpg')
    conte_logo = Container(logo, padding=10)
    mine_user = TextField(
        height=30,
        width=200,
        text_size=15,
        bgcolor='#ffffff',
        border=12,
        color='#000000',
        content_padding=5,
        focused_border_color='#000000',
        cursor_color='#660366',
        )
    
    minecraft_version = Dropdown(
        options=[
            dropdown.Option("1.16.5")
        ],
        width=200,
        height=30,
        color='#000000',
        focused_bgcolor='#ffffff',
        content_padding=5,
        focused_border_color='#000000',
        filled=True,
        bgcolor='#ffffff'
    )

    btn = ElevatedButton(
        'Play',
        color='#ffffff',
        bgcolor='#660366',
        height=30,
        width=200,
        style=ButtonStyle(shape={'': RoundedRectangleBorder(radius=2)})
        )
    
    pb = ProgressBar(width=350, bgcolor='#1b1b1b', color='#660366')
    porciento= Text('90%')

    barra_de_progreso = Row([
        pb,
        porciento
    ])

    def column_with_horiz_alignment(align: ft.CrossAxisAlignment):
        return Column(
            [
                Container(
                    Column([conte_logo,spases,mine_user,spases1,minecraft_version,spases1,btn,barra_de_progreso],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                           horizontal_alignment=align,
                           ),
                ),
            ]
        )

    page.add(Stack([
        bg,
        Row(
            [
                column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    ]),

    )

    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(0.1)
        page.update()


ft.app(target=main, assets_dir="assets")