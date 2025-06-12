import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    altura, largura, _ = frame.shape
    cx = int(largura / 2)
    cy = int(altura / 2)
    centro_pixel = hsv_frame[cy, cx]
    h, s, v = int(centro_pixel[0]), int(centro_pixel[1]), int(centro_pixel[2])

    cor = "Indefinida"

    # Baseado em valores típicos para Hue, Saturação e Brilho
    if v < 40:
        cor = "PRETO"
        
    elif s < 30 and v > 180:
        cor = "BRANCO"
    elif s < 60 and 40 < v < 180:
        cor = "CINZA"
    elif 5 < h < 22 and s > 100 and v < 150:
        cor = "MARROM"
        
    elif h < 5 or h >= 170:
        cor = "VERMELHO"
    elif h < 22:
        cor = "LARANJA"
    elif h < 33:
        cor = "AMARELO"
    elif h < 78 and v < 100:
        cor = "VERDE ESCURO"
    elif h < 78:
        cor = "VERDE"
    elif h < 102:
        cor = "AZUL"
    elif h < 131:
        cor = "AZUL ESCURO"
    elif h < 145:
        cor = "ROXO"
    elif h < 168 and v < 160:
        cor = "ROSA ESCURO"
    elif h < 168:
        cor = "ROSA"
    else:
        cor = "VERMELHO"

    centro_pixel_bgr = frame[cy, cx]
    b, g, r = int(centro_pixel_bgr[0]), int(centro_pixel_bgr[1]), int(centro_pixel_bgr[2])

    cv2.putText(frame, cor, (10, 70), 0, 1.5, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    chave = cv2.waitKey(1)
    if chave == 27:
        break

cap.release()
cv2.destroyAllWindows()
