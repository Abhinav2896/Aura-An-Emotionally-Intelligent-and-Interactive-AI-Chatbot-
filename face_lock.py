import face_recognition
import cv2
import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def start_face_lock():
    speak("Starting face lock")
    known_image = face_recognition.load_image_file("face_data/user.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]
        faces = face_recognition.face_encodings(rgb_frame)

        for face_encoding in faces:
            match = face_recognition.compare_faces([known_encoding], face_encoding)
            if match[0]:
                speak("Face recognized. Access granted.")
                cap.release()
                return True
        cv2.imshow('Face Lock - Press q to quit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    speak("Access denied.")
    return False

def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def unlock_by_voice():
    speak("Say the unlock phrase.")
    command = input("Say password (simulate voice command): ")
    if "unlock aura" in command.lower():
        speak("Voice recognized. Unlocked.")
    else:
        speak("Wrong voice command.")