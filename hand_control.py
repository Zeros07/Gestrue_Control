import cv2
import mediapipe as mp
import pyautogui
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# State buat mencegah spam gesture
last_action_time = 0
action_cooldown = 1.2  # detik cooldown tiap gesture

def distance(a, b):
    return math.hypot(b.x - a.x, b.y - a.y)

def get_finger_state(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_pip = [6, 10, 14, 18]

    fingers = []
    for tip, pip in zip(finger_tips, finger_pip):
        fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y else 0)

    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]
    fingers.insert(0, 1 if thumb_tip.x < thumb_ip.x else 0)

    return fingers  # contoh: [1, 1, 0, 0, 0]

def perform_action(fingers, hand_landmarks):
    global last_action_time
    current_time = time.time()
    if current_time - last_action_time < action_cooldown:
        return  # cooldown biar ga spam

    print("Detected Fingers:", fingers)

    # PLAY / PAUSE - semua jari terbuka
    if fingers == [1, 1, 1, 1, 1]:
        print("▶️ Play/Pause")
        pyautogui.press('playpause')
        last_action_time = current_time

    # NEXT - telunjuk dan jari tengah terbuka
    elif fingers == [0, 1, 1, 0, 0]:
        print("⏭ Next Track")
        pyautogui.press('nexttrack')
        last_action_time = current_time

    # PREVIOUS - hanya jari telunjuk terbuka
    elif fingers == [0, 1, 0, 0, 0]:
        print("⏮ Previous Track")
        pyautogui.press('prevtrack')
        last_action_time = current_time

    # VOLUME - pakai jarak antara ibu jari dan telunjuk
    thumb = hand_landmarks.landmark[4]
    index = hand_landmarks.landmark[8]
    dist = distance(thumb, index)

    if dist > 0.2:
        print("🔊 Volume Up")
        pyautogui.press("volumeup")
        last_action_time = current_time
    elif dist < 0.05:
        print("🔉 Volume Down")
        pyautogui.press("volumedown")
        last_action_time = current_time

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    print("🎵 Gesture Control aktif — Tekan 'q' untuk keluar.")
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kamera tidak terdeteksi.")
            break

        # Konversi ke RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Balik lagi ke BGR buat OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                fingers = get_finger_state(hand_landmarks)
                perform_action(fingers, hand_landmarks)

                # Gambarin tangan di frame
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        cv2.imshow('Gesture Control', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
