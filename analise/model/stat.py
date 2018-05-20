# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def get_men_and_woman(df: pd.DataFrame):
    """Função para realizar separação do dataset masculino e feminino
    :param: df: Dataframe contendo todos os dados recuperados do CSV
    :rtype: tuple(list, list)
    """
    
    woman = []
    men = []
    for city in range(df.shape[0]):
        if city % 2 == 0:
            men.append(df.iloc[city])
        else:
            woman.append(df.iloc[city])
       
    return woman, men


def gen_boxplot(list_data: list, class_type):
    """Função para gerar gráficos boxplot dos dados
    :param: list_data: Lista contendo os dados masculino/feminino
    :param: class_type: Indica o tipo que está sendo plotado
    """

    fig, axs = plt.subplots(6, 2, figsize=(15, 15))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.5)
    x = 0; y = 0       
         
    for city in list_data:
        plt.suptitle('Analfabetismo funcional - {} - de 1992 até 2006'
                 .format(class_type))
        
        axs[x, y].boxplot(list(city.iloc[2:]))
        axs[x, y].set_title(city.iloc[0])
    
        y += 1          
        if y == 2:
            x += 1
            y = 0
        if x == 6:
            break
        

def general_stat(df: pd.DataFrame):
    """Função para levantamento de dados como Média, Mediana, Desvio padrão
    e coeficiente de variação
    :param: df
    """
    
    pass    
    