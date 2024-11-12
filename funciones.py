import itertools
import pandas as pd

def contar_dato_col(df, columna):
    """
    Cuenta los tipos de datos en una columna específica de un DataFrame.
    
    Parámetros:
    df (pd.DataFrame): El DataFrame de entrada.
    columna (str): El nombre de la columna para contar los tipos de datos.
    
    Retorna:
    pd.Series: Una serie con los conteos de tipos de datos en la columna especificada.
    """
    # Contar los tipos de datos en la columna especificada y convertir los tipos a cadenas
    conteos_tipos = df[columna].apply(lambda x: type(x)).value_counts()
    
    return conteos_tipos

# Función para aplanar listas y poder contar valores
def flatten_and_count(column):
    flattened_list = list(itertools.chain(*df[column].values))
    return pd.Series(flattened_list).value_counts()

def contar_dato_df(df):
    """
    Cuenta los tipos de datos por columna en un DataFrame.
    
    Parámetros:
    df (pd.DataFrame): El DataFrame de entrada.
    
    Retorna:
    pd.DataFrame: Un DataFrame con los conteos de tipos de datos por columna.
    """
    # Diccionario para almacenar los resultados
    conteos_tipos = {}

    # Iterar sobre cada columna del DataFrame
    for col in df.columns:
        # Contar los tipos de datos en cada columna y convertir los tipos a cadenas
        conteos = df[col].apply(lambda x: str(type(x))).value_counts()
        # Almacenar el resultado en el diccionario
        conteos_tipos[col] = conteos

    # Convertir el diccionario en un DataFrame para mejor visualización
    df_conteos_tipos = pd.DataFrame(conteos_tipos).fillna(0)
    
    return df_conteos_tipos
