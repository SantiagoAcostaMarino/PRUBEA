# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:51:21 2022

@author: Sanmars
"""



def carga_de_datos (nombre_archivo:str) -> dict: #1
    avistamientos = {}
    archivo = open(nombre_archivo,"r", encoding="utf-8")
    archivo.readline()
    
    linea = archivo.readline()
    while (len(linea) >0):
        datos = linea.strip("\n").split(",")
        avistamiento = {}
        avistamiento["datatime"]= datos[0]
        avistamiento["city"]= datos[1]
        avistamiento["state"]= datos[2]
        avistamiento["shape"]= datos[4]
        avistamiento["duration"]= float(datos[5])
        avistamiento["comments"]= datos[6]
        avistamiento["date posted"]= datos[7]
        avistamiento["latitude"]= float(datos[8])
        avistamiento["longitude"]= float(datos[9])
        if datos[3] not in avistamientos:
            avistamientos[datos[3]]=[avistamiento]
        else:
            avistamientos[datos[3]].append(avistamiento)
        linea=archivo.readline()
    archivo.close()
    return avistamientos

def avistamientos_en_fecha (avistamientos:dict, fecha:str) ->list:
    lista = []
    for pais in avistamientos:
        for avistamiento in avistamientos[pais]:
            if fecha in avistamiento["datatime"]:
                lista.append(avistamiento)
    return lista


def avistamientos_por_ciudad(avistamientos:dict) -> dict: #3
    ciudades = {}
    for pais in avistamientos:
        for ciudad in avistamientos[pais]:
            if ciudad["city"] not in ciudades:
                nombre_ciudad = []
            else:
                nombre_ciudad = ciudades[ciudad["city"]]
            ciudades[ciudad["city"]]=nombre_ciudad
            nombre_ciudad.append(ciudad)
    return ciudades

def avistamientos_mas_de_x_segundos (avistamientos:dict,segundos:float) -> dict:#4
    avistamiento_x_segundos = avistamientos
    for pais in avistamientos:
        for ciudad in avistamientos[pais]:
            if ciudad["duration"] < segundos:
                avistamientos[pais].remove(ciudad)    
    return avistamiento_x_segundos

def avistamientos_por_rango_de_fechas (avistamientos:dict, inicio:str, final:str) -> str: #5
    lista = []
    for pais in avistamientos:
        for avistamiento in avistamientos[pais]:
            if avistamiento["datatime"] >= inicio and avistamiento["datatime"] <= final:
                lista.append(avistamiento)
    return lista 

from math import radians, cos, sin, asin, sqrt
def distancia_entre_dos_puntos(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    dif_lon = lon2 - lon1
    dif_lat = lat2 - lat1
    a = sin(dif_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2)**2
    c = 2 * asin(sqrt(a))
    return c * 6371

def avistamientos_en_radio_determinado (avistamientos:dict, lat:float,lon:float, radio:float) -> list: #6
    respuesta = []
    for pais in avistamientos:
        for avistamiento in avistamientos[pais]:
            if distancia_entre_dos_puntos(lat, lon, avistamiento["latitude"], avistamiento["longitude"]) < radio:
                respuesta.append(avistamiento)
    return respuesta 
        
def minimo_x_avistamientos_en_mes(avistamientos:dict, cantidad:int,fecha:str) -> bool: #7
    cantidad_fecha = 0
    respuesta = False
    for pais in avistamientos:
        for avistamiento in avistamientos[pais]:
            if fecha in avistamiento["datatime"]:
                cantidad_fecha+=1
    if cantidad_fecha >= cantidad:
        respuesta = True
    return respuesta

def dar_avistamiento_mas_corto_y_largo_por_pais (avistamientos:dict,pais:str) -> dict: #8
    respuesta = {}
    respuesta["corto"] = 0
    respuesta ["largo"] = 0
    for avistamiento in avistamientos[pais]:
        if respuesta["corto"] == 0:
            corto = avistamiento["duration"]
            respuesta["corto"] = avistamiento
        if respuesta["largo"] == 0:
            respuesta["largo"] = avistamiento
            largo = avistamiento["duration"]
        elif largo < avistamiento["duration"]:
            largo = avistamiento["duration"]
            respuesta["largo"] = avistamiento
        elif avistamiento["duration"]< corto:
            corto = avistamiento["duration"]
            respuesta["corto"] = avistamiento           
    return respuesta

def avistamientos_por_forma (avistamientos:dict) -> dict:#9.1
    avistamientos_forma = {}
    for pais in avistamientos:
        for ciudad in avistamientos[pais]:
            if ciudad["shape"] not in avistamientos_forma:
                forma = []
            else:
                forma = avistamientos_forma[ciudad["shape"]]
            avistamientos_forma[ciudad["shape"]]=forma
            forma.append(ciudad)
    return avistamientos_forma

def contar_avistamiento_por_forma (avistamientos:dict) -> dict:#9

    n_avistamientos_forma = {}
    avistamientos_forma = avistamientos_por_forma (avistamientos)
    for forma in avistamientos_forma:
        n_avistamientos_forma[forma] = len(avistamientos_forma[forma])
    return n_avistamientos_forma

def pais_con_mas_avistamientos_de_x_segundos (avistamientos:dict,segundos:float)->dict: #10
    pais_mas_de_x_segundos = {}
    pais_mas_de_x_segundos["pais"] =""
    pais_mas_de_x_segundos["avistamientos"] = 0
    mas_de_x_segundos = avistamientos_mas_de_x_segundos(avistamientos, segundos)
    for pais in mas_de_x_segundos:
        if len(mas_de_x_segundos[pais])> pais_mas_de_x_segundos["avistamientos"]:
            pais_mas_de_x_segundos["pais"] = pais
            pais_mas_de_x_segundos["avistamientos"] = len(mas_de_x_segundos[pais])
    return pais_mas_de_x_segundos
            
def avistamientos_que_contengan_cadena_en_comentarios (avistamientos:dict,cadena:str) -> list: #11
    lista = []
    for pais in avistamientos:
        for avistamiento in avistamientos[pais]:
            if cadena in avistamiento["comments"]:
                lista.append(avistamiento)
    return lista 
    


    




    
                
        
                
    
    



        
        
       
            
            
        