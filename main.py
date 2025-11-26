from sklearn import datasets
import pandas as pd
import numpy as np
from math import sqrt
import cv2 as cv
import statistics

ORIGINAL_ESC = 255
DESTINATION_ESC = 16
STEP_ESC = DESTINATION_ESC / ORIGINAL_ESC

MENU = """_____________________________
IDENTIFICARDOR DE NUMEROS POR DNI

 - Ingrese su DNI -> """

dict_number_test = {
    0:"cero", 1:"uno", 2:"dos", 3:".tres", 4:"cuatro", 5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve"
}

datos_number_dataset = datasets.load_digits()

def euclidean_distance_matrix(A: np.ndarray, B: np.ndarray) -> float:
    assert A.shape == (8,8) and B.shape == (8,8)
    diff = A.astype(float) - B.astype(float)
    sq = diff**2
    d = sqrt(sq.sum())
    return d

def normalized_distance(A: np.ndarray, B:np.ndarray) -> float:
    d = euclidean_distance_matrix(A, B)
    max_d = 128
    return d / max_d

def process_input_image(img: str) -> list[list]:
    img_array = cv.imread(img, cv.IMREAD_GRAYSCALE)
    scale8_img = cv.resize(img_array, (8,8))
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            scale8_img[i][j] = (255 - scale8_img[i][j]) * STEP_ESC
            if scale8_img[i][j] <= 5 :
                scale8_img[i][j] = 0
            j += 1
        i += 1
    return scale8_img

def approach_pass(array, list_number_aprox: list):
    for i in range(len(datos_number_dataset["images"])):
        d = normalized_distance(array, datos_number_dataset["images"][i])
        list_number_aprox.append((round(d, 8), i))

def detection_numbers(img: str, list_number_aprox: list) -> list:
    array = process_input_image(img)
    approach_pass(array, list_number_aprox)
    list_number_aprox.sort()
    return list_number_aprox

def performance_test(img: str, numero: int):
    print(f"El número a evaluar es: {numero}\n")

    list_number_aprox = []
    list_number_aprox = detection_numbers(img, list_number_aprox)
    three_digits = []
    print(list_number_aprox)
    print("Los targets de los 3 vecinos más cercanos son: ")
    for i in range(3):
        three_digits.append(datos_number_dataset["target"][list_number_aprox[i][1]])
        print(datos_number_dataset["target"][list_number_aprox[i][1]], end=" ")
    print("\n")
    print("La etiqueta verdadera es: ")
    list_targets = []
    for i in range(len(list_number_aprox[:100])):
        list_targets.append(datos_number_dataset["target"][list_number_aprox[i][1]])
    moda = statistics.mode(list_targets)
    print(f"{moda}\n")

    print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {moda}")

def menu():
    while True:
        print(MENU, end="")
        try:
            dni = int(input())
            if dni == -1:
                break
            if len(str(dni)) != 8:
                print("El DNi ingresado no tiene 8 digitos, volver a ingresar el DNI")
                continue
        except Exception as e:
            print(e)
            print("Se ingreso de manera incorrecta el DNI")
            continue

        list_dni = [int(n) for n in str(dni)]
        for i in list_dni:
            url_img = f"./test/img/{dict_number_test[i]}.png"
            print(performance_test(url_img,i))

if __name__ == "__main__":
    menu()

