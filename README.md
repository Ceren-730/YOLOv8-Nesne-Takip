# 🚀 YOLOv8 & ByteTrack ile Gerçek Zamanlı Nesne Takibi

Bu proje, görüntü işleme ve yapay zeka tekniklerini kullanarak web kamerası üzerinden nesne tespiti ve kesintisiz nesne takibi gerçekleştirir.

## 🧠 Teknik Özellikler
* **Nesne Tespiti:** YOLOv8 (Ultralytics) mimarisi ile yüksek doğruluklu analiz.
* **Nesne Takibi:** `ByteTrack` algoritması kullanılarak nesnelere benzersiz ID'ler atanmış ve hareket takibi stabilize edilmiştir.
* **Donanım Erişimi:** OpenCV DirectShow entegrasyonu ile optimize edilmiş kamera akışı.

## 🛠 Kullanılan Teknolojiler
* **Python 3.9**
* **OpenCV** (Görüntü İşleme)
* **Ultralytics** (YOLOv8 & Tracking)

## 🚀 Kurulum
Projenin çalışması için gerekli kütüphaneleri şu komutla yükleyebilirsiniz:
```bash
pip install ultralytics opencv-python
