import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

def drawHandLandmarks(image, hand_landmarks):
    #dibuja las conexiones y puntos de la mano
    if hand_landmarks:

        for landmarks in hand_landmarks:
            
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

while True:
    success, image = cap.read()
    if not success:
        print("No se pudo acceder a la cámara.")
        break

    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #detectar los puntos/manos
    results = hands.process(image_rgb)

    #resultados
    #hand_landmarks = (image, results.multi_hand_landmarks)
    #drawHandLandmarks(image,hand_landmarks)
    drawHandLandmarks(image, results.multi_hand_landmarks)


    cv2.imshow("Controlador de medios", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

    
cap.release()
cv2.destroyAllWindows()
        