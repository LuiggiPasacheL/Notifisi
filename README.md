
<h1 align="center">
Notifisi
</h1>

## Descripción

Notifisi es una aplicación de escritorio que informa cada día si se han publicado nuevas noticias de la página web de la facultad de ingeniería de informática de la UNMSM.

## Instalación

Puedes clonar este repositorio o descargar el [ejecutable](https://github.com/LuiggiPasacheL/Notifisi/releases/tag/v1.0).

Es recomendable añadir un acceso directo al ejecutable a los programas de inicio.

En windows: ```C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```


## Compilación

- Instalar dependencias

    ```ps1
    pip install -r requirements.txt
    ```

- Compilar

    Windows:

    ```ps1
    pyinstaller --windowed --add-data "assets/logo.png;assets" --onefile --icon ./assets/logo.png --name Notifisi main.py
    ```
    Linux:

    ```sh
    pyinstaller --windowed --add-data "assets/logo.png:assets" --onefile --icon ./assets/logo.png --name Notifisi main.py
    ```

- Buscar ejecutable en la carpeta dist generada
## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
