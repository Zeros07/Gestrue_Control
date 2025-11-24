# ✋ Hand Gesture Media Control (Python & MediaPipe)

Proyek ini memungkinkan Anda mengontrol pemutaran media (Play/Pause, Next/Previous Track, Volume Up/Down) pada komputer Anda menggunakan gerakan tangan yang dideteksi melalui kamera.

Proyek ini dibangun menggunakan **MediaPipe** untuk deteksi *landmark* tangan dan **PyAutoGUI** untuk simulasi penekanan tombol media.

## 🔗 Demo Aksi

[Opsional: Masukkan GIF atau tautan Video Singkat di sini yang menunjukkan script sedang berjalan]

---

## 🛠️ Teknologi yang Digunakan

* **Python:** Bahasa pemrograman utama.
* **OpenCV (`cv2`):** Untuk interaksi dengan kamera dan menampilkan *video feed*.
* **MediaPipe:** Untuk deteksi dan pelacakan tangan secara *real-time*.
* **PyAutoGUI:** Untuk simulasi penekanan tombol media (Play/Pause, Volume, dll.) pada sistem operasi.
* **Math & Time:** Untuk perhitungan jarak dan manajemen *cooldown* gesture.

---

## ⚙️ Fitur dan Gesture

| Gesture | Status Jari (Thumb, Index, Middle, Ring, Pinky) | Aksi yang Dilakukan |
| :--- | :--- | :--- |
| **Play/Pause** | Semua jari terbuka (\[1, 1, 1, 1, 1]) | `playpause` |
| **Next Track** | Telunjuk & Jari Tengah terbuka (\[0, 1, 1, 0, 0]) | `nexttrack` |
| **Previous Track** | Hanya Jari Telunjuk terbuka (\[0, 1, 0, 0, 0]) | `prevtrack` |
| **Volume Up** | Jarak Ibu Jari & Telunjuk **Jauh** (dist > 0.2) | `volumeup` |
| **Volume Down** | Jarak Ibu Jari & Telunjuk **Dekat** (dist < 0.05) | `volumedown` |

*(Terdapat cooldown 1.2 detik setelah setiap aksi untuk mencegah spam input.)*

---

## 🚀 Setup dan Instalasi

Proyek ini memerlukan Python 3.x dan beberapa *library* pihak ketiga.

### 1. Kebutuhan (Prerequisites)

* Python 3.x terinstal.
* Kamera web terpasang dan berfungsi.

### 2. Instalasi Library

Buka Terminal atau Command Prompt dan instal semua *dependency* yang dibutuhkan:

```bash
pip install opencv-python mediapipe pyautogui