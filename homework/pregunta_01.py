"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    input_path = "files/input/solicitudes_de_credito.csv"
    output_dir = "files/output"
    output_path = os.path.join(output_dir, "solicitudes_de_credito.csv")

    os.makedirs(output_dir, exist_ok=True)

    # Leer archivo
    df = pd.read_csv(input_path, sep=";", index_col=0)

    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = (
            df[col]
            .str.lower()
            .str.replace("_", " ", regex=False)
            .str.replace("-", " ", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.replace(".00", "", regex=False)
        )
        
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["fecha_de_beneficio"] = (
        pd.to_datetime(
            df["fecha_de_beneficio"],
            format="%d/%m/%Y",
            errors="coerce",
        ).combine_first(
            pd.to_datetime(
                df["fecha_de_beneficio"],
                format="%Y/%m/%d",
                errors="coerce",
            )
        )
    )

    df = df.drop_duplicates()

    df = df.dropna()

    df.to_csv(
        output_path,
        sep=";",
        index=False,
        encoding="utf-8",
    )


if __name__ == "__main__":
    pregunta_01()