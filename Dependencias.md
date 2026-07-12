# Dependencias y entorno de desarrollo

Este proyecto fue desarrollado en **Python 3** utilizando **Jupyter Notebook** como entorno de ejecución interactivo y **Visual Studio Code** como editor de código. Para implementar la simulación del problema de las jarras, la visualización gráfica y la animación, se emplearon las siguientes librerías y módulos.

---

# Librerías externas

| Librería | Función | Referencia |
|----------|----------|------------|
| **Matplotlib** | Biblioteca utilizada para la creación de gráficos, el dibujo de las jarras mediante figuras geométricas (`Polygon`, `Rectangle`) y la generación de animaciones con `FuncAnimation`. | Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55 |
| **NumPy** | Proporciona estructuras de datos eficientes y funciones para realizar operaciones numéricas, facilitando cálculos utilizados durante la animación y manipulación de datos. | Harris, C. R., et al. (2020). *Array programming with NumPy*. Nature, 585(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2 |
| **IPython** (`IPython.display`) | Permite mostrar contenido HTML, actualizar dinámicamente la salida del notebook y presentar animaciones directamente dentro de Jupyter. | Pérez, F., & Granger, B. E. (2007). *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 9(3), 21–29. https://doi.org/10.1109/MCSE.2007.53 |
| **ipywidgets** | Biblioteca utilizada para crear elementos interactivos dentro del notebook, como pantallas de introducción, botones y componentes gráficos. | Jupyter Development Team. (2024). *ipywidgets Documentation*. https://ipywidgets.readthedocs.io/ |

---

# Bibliotecas estándar de Python

Las siguientes bibliotecas forman parte de la instalación estándar de Python, por lo que no requieren instalación adicional.

| Biblioteca | Función | Referencia |
|------------|----------|------------|
| **math** | Proporciona funciones matemáticas. En este proyecto se utiliza `gcd()` para calcular el máximo común divisor y verificar la factibilidad del problema de las jarras. | Python Software Foundation. *math — Mathematical functions*. https://docs.python.org/3/library/math.html |
| **collections** | Contiene estructuras de datos especializadas. Se emplea `deque`, una cola de doble extremo utilizada para implementar eficientemente el algoritmo de búsqueda en anchura (BFS). | Python Software Foundation. *collections — Container datatypes*. https://docs.python.org/3/library/collections.html |

---

# Componentes específicos de Matplotlib

Dentro de Matplotlib se utilizaron módulos especializados para mejorar la representación gráfica de la simulación.

| Componente | Función |
|------------|----------|
| `Polygon` | Permite dibujar las paredes inclinadas de las jarras mediante polígonos personalizados. |
| `Rectangle` | Se utiliza para representar el agua contenida dentro de cada jarra. |
| `FuncAnimation` | Genera la animación cuadro por cuadro mostrando la evolución de cada estado del problema. |

---

# Entorno de desarrollo

El proyecto fue desarrollado utilizando las siguientes herramientas:

| Herramienta | Función | Referencia |
|-------------|----------|------------|
| **Python 3** | Lenguaje de programación principal empleado para desarrollar toda la lógica del proyecto. | Python Software Foundation. https://www.python.org |
| **Jupyter Notebook** | Entorno interactivo utilizado para ejecutar el código, visualizar resultados y mostrar la animación directamente en el notebook. | Project Jupyter. https://jupyter.org |
| **Visual Studio Code** | Editor de código utilizado para el desarrollo, edición y depuración del proyecto. | Microsoft. https://code.visualstudio.com |
| **Git** | Sistema de control de versiones empleado para gestionar los cambios del proyecto. | https://git-scm.com |
| **GitHub** | Plataforma utilizada para alojar el repositorio y compartir el proyecto. | https://github.com |

---

# Referencias

- Harris, C. R., et al. (2020). *Array programming with NumPy*. Nature, 585(7825), 357–362.
- Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. Computing in Science & Engineering, 9(3), 90–95.
- Pérez, F., & Granger, B. E. (2007). *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 9(3), 21–29.
- Python Software Foundation. *Python Documentation*. https://docs.python.org/3/
- Project Jupyter. https://jupyter.org
- Microsoft. *Visual Studio Code*. https://code.visualstudio.com
- Git. https://git-scm.com
- GitHub. https://github.com
