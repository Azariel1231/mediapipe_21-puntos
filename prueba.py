import cv2
import mediapipe as mp

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

def drawHandLandmarks(image, hand_landmarks):
    """Dibuja los puntos y conexiones de la mano"""
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(
                image, landmarks, mp_hands.HAND_CONNECTIONS
            )

while True:
    success, image = cap.read()
    if not success:
        print("No se pudo acceder a la cámara.")
        break

    # Voltear la imagen horizontalmente (efecto espejo)
    image = cv2.flip(image, 1)

    # Convertir la imagen a RGB (MediaPipe usa RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Procesar la detección
    results = hands.process(image_rgb)

    # Dibujar los puntos si se detectan manos
    drawHandLandmarks(image, results.multi_hand_landmarks)

    # Mostrar la imagen
    cv2.imshow("Controlador de medios", image)

    # Salir con la barra espaciadora
    if cv2.waitKey(1) & 0xFF == 32:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
