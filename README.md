# piedra-papel-tijera
Juego de Piedra Papel o Tijera utilizando Flet

## 🧭 **DERROTERO: DESARROLLO DE UNA APP CON FLET**

### Proyecto: “🪨📄✂️ Piedra, Papel o Tijera”

---

### 🕐 **Bloque 1: Preparación del entorno y GitHub**

#### 🎯 Objetivo:

Configurar el entorno de trabajo profesional con Git y Python, usando ramas personales.

#### 📋 Actividades:

2. **Clonar el repo en el computador**

   ```bash
   cd ~/Documents/GitHub
   git clone https://github.com/opraupe0017/piedra-papel-tijera.git
   cd piedra-papel-tijera
   ```

3. **Cada estudiante: crear su propia rama**

   ```bash
   git checkout -b dev-[nombre_estudiante]
   ```

4. **Abrir en VS Code y abrir la carpeta del proyecto**

5. **Crear entorno virtual**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # En Windows
   ```

6. **Instalar Flet**

   ```bash
   pip install flet[all]
   ```

7. **Comprobar instalación**

   ```bash
   python -m flet --version
   ```

#### 💡 Pauta pedagógica:

Hacer un *commit inicial* para confirmar su rama:

```bash
git add .
git commit -m "Configuración inicial del proyecto"
git push origin dev-[nombre_estudiante]
```

---

### 🕑 **Bloque 2: Crear el proyecto Flet**

#### 🎯 Objetivo:

Generar la estructura base del proyecto y entender la arquitectura Flet.

#### 📋 Actividades:

1. **Crear proyecto base**

   ```bash
   flet create .
   ```

3. **Abrir y limpiar el archivo `main.py`.**

4. Implementar el juego.

5. Guardar cambios y hacer **commit:**

   ```bash
   git add main.py
   git commit -m "Implementación de la interfaz inicial con Flet"
   git push origin dev-[nombre_estudiante]
   ```

---

### 🕒 **Bloque 3: Comprender cómo interactúan la UI y la lógica**

#### 🎯 Objetivo:

Comprender cómo interactúan la UI y la lógica.

#### 📋 Actividades:

1. Estudiar el flujo del código:

   * `page` representa la interfaz.
   * `ElevatedButton` dispara `on_click`.
   * `jugar(jugador)` compara las elecciones.

2. **Ejecutar la app:**

   ```bash
   flet run main.py
   ```

4. **Explorar posibles mejoras:**

   * Cambiar emojis.
   * Modificar mensajes.
   * Agregar colores (`Text.color`, `Button.color`).

#### 💡 Pauta pedagógica:

Personalice la interfaz y suba su versión:

```bash
git commit -m "Agregado color personalizado y emojis nuevos"
git push
```

---
