import pandas as pd
import numpy as np
from numpy import random



def produit(n, m ):
    if n*m > 0 :
        print('positive')
    else:
        print ('negative')

def addivite(n):
    somme = 0
    for i in range (0,n+1):
        somme = somme + i
    print(somme)

def sommetab(df):
    somme = 0
    for i in range (0, len(df)):
        for j in range (0, df.shape[1]):
            somme = somme + df[i,j]
    return(somme)

def FacProduct(df, df2):
    res = 0
    for i in range (0, len(df)):
        for j in range (0, df.shape[1]):
            res = res + df[i,j] * df2[i,j]
    return(res)

def avg(df):
    avg = sommetab(df) / (len(df)*df.shape[1])
    print ("la moyenne est de", avg)
    for i in range (0, len(df)):
        for j in range (0, df.shape[1]):
            if df[i,j] > avg:
                print (df[i,j])

def bubble_sort(df):
    n = len(df)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if df[j] > df[j + 1]:
                df[j], df[j + 1] = df[j + 1], df[j]
                already_sorted = False
        if already_sorted:
            break
    return df

def factorielle(n):
    fact = 1
    if (n==0):
        return (fact)
    else:
        for i in range (1,n+1):
            fact = fact * i
        return (fact)

def multiply_matrix(A,B):
    if  A.shape[1] == B.shape[0]:
        result = np.zeros((len(A),len(B[0])))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return (result)   
    else:
        return "Sorry, cannot multiply the data frames"

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def limit(limite):
    k=1
    somme = 0
    while somme < limite :
        somme = somme + 1/k
        k = k + 1
    return k




df = random.randint(5, size=(4, 2))
df2= random.randint(5, size=(2, 3))

list = [8, 2, 6, 4, 5]

l = 5

limite = limit(l)

print(limite)



