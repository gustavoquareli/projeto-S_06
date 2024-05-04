import pandas as pd


""""Essa linha de código serve para todas as funções que infelizmente não estão vindo de data_manipulation.py"""

def columns_format(df):
    """Função para formatar os nomes das colunas"""
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.strip()
    return df



def columns_convert(df, columns, type):
    """Função para alterar o tipo das colunas"""
    for column in columns:
        df[column] = df[column].astype(type)
    return df

def study_null_values(df, column):
    """Função para estudar os valores nulos"""
    return df[df[column].isnull()]


def total_sales_columns(df, columns):
    """Função para somar as vendas"""
    df['total_sales'] = df[columns].sum(axis=1)
    return df
