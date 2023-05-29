
<h1 align="center">Notifisi</h1>

## Descripción

Notifisi es una aplicación de escritorio (icono del sistema) que informa en cada inicio de sesión, si se han publicado nuevas noticias de la página web de la facultad de ingeniería de informática de la UNMSM.
Adicionalmente se puede cambiar la configuración del sistema para que funcione con otras facultades.

## Uso

Puedes clonar este repositorio o descargar el [ejecutable](https://github.com/LuiggiPasacheL/Notifisi/releases/tag/v1.0).
O también puedes utilizar el ejecutable ```Notifisi.bat``` que se encuentra en la raíz del repositorio, para utilizarlo es necesario seguir los pasos de [compilación](#compilación) hasta [Instalar dependencias](#instalar-dependencias).
Es recomendable añadir un acceso directo al ejecutable, .bat o .exe, a los programas de inicio.
En windows: ```C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```

## Requerimientos

- Python 3.10+
- Pip 22.2+

## Compilación

### Crear entorno virtual
    ```ps1
    python -m venv venv
    ```

### Ingresar al entorno virtual

    Windows:

    ```ps1
    . .\venv\Scripts\activate
    ```
    
    Linux:

    ```sh
    source venv/bin/activate
    ```

### Instalar dependencias

    ```ps1
    pip install -r requirements.txt
    ```

### Compilar

    Windows:

    ```ps1
    pyinstaller --windowed --add-data "assets/logo.png;assets" --onefile --icon ./assets/logo.png --name Notifisi main.py
    ```
    Linux:

    ```sh
    pyinstaller --windowed --add-data "assets/logo.png:assets" --onefile --icon ./assets/logo.png --name Notifisi main.py
    ```

- Buscar ejecutable en la carpeta dist generada

- **NOTA**: Pyinstaller puede dar [falso positivo para virus en windows](https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg).


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
