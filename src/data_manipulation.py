import pandas as pd

"""importando bibliotecas"""


def columns_format(df):
    """Função para formatar os nomes das colunas"""
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.strip()
    return df


def columns_convert(df, column, type):
    """Função para alterar o tipo das colunas"""

    df[column] = df[column].astype(type)
    return df
