#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 21:17:26 2018

@author: felipe
"""

import pandas as pd
from analise.model.stat import *

df = pd.read_csv('dados/serie.csv')
# Recupera somente os dados de cada ano

woman, men = get_men_and_woman(df)

gen_boxplot(woman, 'Mulher')
gen_boxplot(men, 'Homem')