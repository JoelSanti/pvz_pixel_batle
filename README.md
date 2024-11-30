# 🌻 Plantas vs Zombies - Pixel Battle 🌿

¡Bienvenido a **Plantas vs Zombies - Pixel Battle**! Este es un clon del popular juego Plantas vs Zombies, desarrollado en Python 3.12.7 utilizando la biblioteca Pygame.

## 📋 Descripción

En este juego, los jugadores deben defender su jardín de oleadas de zombies plantando diferentes tipos de plantas. Cada planta tiene habilidades únicas que ayudan a detener a los zombies antes de que lleguen a la casa.

## 🚀 Instalación

Sigue estos pasos para instalar y ejecutar el juego en tu máquina local:

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/JoelSanti/pvz_pixel_batle.git
    cd pvz_pixel_batle
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):

    Un entorno virtual es una herramienta que permite mantener las dependencias requeridas por diferentes proyectos en espacios aislados. Esto es especialmente útil para evitar conflictos entre versiones de bibliotecas y mantener un entorno limpio para cada proyecto.

    **Pasos para crear y activar un entorno virtual:**

    1. **Crear el entorno virtual**:
        ```bash
        python3 -m venv venv
        ```
        Este comando crea un directorio llamado `venv` que contiene una copia del intérprete de Python y una instalación de pip.

    2. **Activar el entorno virtual**:
        - En Linux/Mac:
            ```bash
            source venv/bin/activate
            ```
        - En Windows:
            ```bash
            venv\Scripts\activate
            ```
        Al activar el entorno virtual, el intérprete de Python y pip del entorno virtual se utilizarán en lugar de los globales.

    3. **Desactivar el entorno virtual** (cuando termines de trabajar):
        ```bash
        deactivate
        ```
        Este comando desactiva el entorno virtual y vuelve a usar el intérprete de Python global.

3. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta el juego**:
    ```bash
    python src/main.py
    ```

## 📂 Estructura del Proyecto

```plaintext
pvz_pixel_battle/  
├── 📁 assets/              # Archivos de imágenes y música  
├── 📁 src/                 # Código fuente del juego  
│   ├── 📁 characters/      # Clases de personajes  
│   │   └── 📁 utilities/   # Utilidades de personajes  
│   ├── 📁 components/      # Componentes de la interfaz de usuario  
│   ├── 📁 pages/           # Páginas del juego  
│   └── 📄 main.py          # Archivo principal del juego  
├── 📄 requirements.txt     # Dependencias del proyecto  
└── 📄 README.md            # Documentación principal del proyecto  
```

## 🎮 Controles del Juego

- **Clic Izquierdo**: Interactuar con los elementos del menú y recoger soles.

## 🛠️ Tecnologías Utilizadas

- **Python 3.12.7**
- **Pygame**

¡Gracias por jugar y disfrutar de **Plantas vs Zombies - Pixel Battle**! 🌼🧟‍♂️