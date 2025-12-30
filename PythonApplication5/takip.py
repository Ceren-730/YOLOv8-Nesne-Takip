import os
import cv2
from ultralytics import YOLO

def baslat():
    try:
        print("1. Model yukleniyor...")
        model = YOLO('yolov8n.pt')
        
        print("2. Kamera acilmaya calisiliyor...")
        # DirectShow kullanarak kamerayi zorla aciyoruz
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not cap.isOpened():
            raise Exception("Kamera donanimina erisilemedi!")

        print("3. Analiz basliyor... (Kapatmak icin 'q'ya basin)")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model.track(frame, persist=True, tracker="bytetrack.yaml", verbose=False)
            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8 Takip Denemesi", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"\n--- HATA BULUNDU --- \n{e}\n--------------------")
        input("Hatayi okuduysan Enter'a bas...")

if __name__ == "__main__":
    baslat()