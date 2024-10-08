"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # Limpieza de monto_del_credito
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.strip(" ")
        .str.replace("[,$]|(\.00$)", "", regex=True)
        .astype(float)
    )

    # Limpieza de fecha_de_beneficio
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).fillna(
        pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
    )

    # Cambio de tipo de dato de comuna_ciudadano
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Eliminación de duplicados y valores nulos
    df = df.drop_duplicates().dropna()

    return df

#
clean_data()
