from sklearn import datasets
import pandas as pd
import numpy as np
from math import sqrt
import cv2 as cv

ORIGINAL_ESC = 255
DESTINATION_ESC = 16
STEP_ESC = DESTINATION_ESC / ORIGINAL_ESC

MENU = """_____________________________
IDENTIFICARDOR DE NUMEROS POR DNI

 - Ingrese su DNI -> """

dict_number_test = {

}

datos_number_dataset = datasets.load_digits()
print(dir(datos_number_dataset))

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

def approach_pass(array, list_number_aprox: list) -> None:
    for i in range(len(datos_number_dataset["images"])):
        d = normalized_distance(array, datos_number_dataset["images"][i])
        if d < 0.30:
            print(d)
            list_number_aprox.append((round(d, 8), i))

def detection_numbers(img: str, list_number_aprox: list) -> list:
    array = process_input_image(img)
    approach_pass(array, list_number_aprox)
    list_number_aprox.sort()
    return list_number_aprox

def performance_test(img: str) -> int:
    list_number_aprox = []
    list_number_aprox = detection_numbers(img, list_number_aprox)

    print(list_number_aprox)
    for i in range(3):
        print(datos_number_dataset["images"][list_number_aprox[i][1]])
        print("El numero se aproxima a ->", datos_number_dataset["target"][list_number_aprox[i][1]])
        print("___________________________")

url_img = "./test/img/nueve_test.png"
performance_test(url_img)

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
        for numb in list_dni:
            print(numb)

        

if __name__ == "__main__":
    menu()