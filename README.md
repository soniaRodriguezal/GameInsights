# GameInsights: Plataforma de Análisis y Recomendación de Videojuegos 🎮

## Índice


- [Objetivos y Motivaciones](#objetivos-y-motivaciones)
- [Estructura](#estructura)
- [Tecnologías](#tecnologías)

## Objetivos y Motivaciones

En la industria de los videojuegos, contar con una base de datos completa y precisa es esencial para comprender las tendencias del mercado, formular estrategias efectivas y ofrecer recomendaciones personalizadas a los usuarios. Este proyecto tiene como propósito principal crear una herramienta que permita a los jugadores explorar sus preferencias y descubrir nuevos títulos de manera intuitiva y personalizada.

### Visión a Largo Plazo

Entre los objetivos a largo plazo de este proyecto se incluyen la inclusión de un modelo de filtrado colaborativo: User-User para recoger recomendaciones basadas en las similitudes entre usuarios, el desarrollo de un bot que ayude a los usuarios a recibir las recomendaciones de videojuegos y la integración de descripciones de los juegos en el modelo de recomendación utilizando técnicas de procesamiento de lenguaje natural (NLP).

## Estructura 

- **Recopilación de Datos**: Obtener información de videojuegos desde diversas webs especializadas. Obtendremos detalles sobre los videojuegos disponibles, incluyendo título, año de lanzamiento, estudios desarrolladores, editores, género, puntuación, configuraciones, perspectivas de juego, número de jugadores online y offline, entre otros.

- **Limpieza y Tratamiento de Datos**: Tras la recopilación de los datos se llevará a cabo un proceso exhaustivo de limpieza y tratamiento. Esto incluye normalizar los datos extraídos para asegurar su calidad y coherencia.

- **Desarrollo de un Sistema de Recomendación**: Finalmente, crearemos un modelo de clasificación de machine learning para realizar recomendaciones personalizadas de videojuegos. Utilizaremos un modelo híbrido con técnicas de filtrado colaborativo item-item y filtrado basado en contenido para predecir juegos que puedan interesar al jugador según sus preferencias y el contenido de los videojuegos.

## Tecnologías

### Lenguajes

- **Python**: Utilizado para la extracción de datos, el tratamiento y limpieza de datos, y el desarrollo del modelo de machine learning.

### Frameworks y Librerías

- **Selenium**: Framework de automatización para el scraping de datos
- **Pandas**: Librería para la manipulación y análisis de datos en Python
- **Scikit-Learn**: Librería para el desarrollo del modelo de machine learning, proporcionando herramientas para la clasificación y predicción

### Otras Herramientas

- **Visual Studio Code**
- **Jupyter Notebooks**
- **Git**


