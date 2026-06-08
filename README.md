# AI Attendance System v2.1

An interactive, AI-powered attendance logging application built with **Python**, **OpenCV**, and **CustomTkinter**. The system features real-time facial recognition execution, automatic attendance logging to a localized CSV layer, a live administrative clock dashboard, and on-the-fly registration for new users directly from the live video feed.

---

## 🚀 Key Features

* **Real-Time Facial Recognition:** Leverages specialized face encoding mappings to rapidly detect and recognize registered users from a live camera feed.
* **Modern administrative UI:** Styled with a sleek, native dark-mode interface built on top of CustomTkinter.
* **Live Clock Feed:** Features a synchronized, real-time status clock updated down to the second for timestamp validation.
* **On-the-Fly User Registration:** Captures the current webcam frame to instantly register and encode a new face into the local directory without requiring an application restart.
* **Automated Data Logging:** Generates and appends structured data logs to a centralized `attendance.csv` file, including full names and precise arrival timestamps.
* **Session Counters:** Dynamically updates live attendance tallies on the administrative panel sidebar.

---

## 📁 System Architecture & Directory Structure

To run the application successfully, ensure your local directory structure is organized as follows:

```text
├── images/                
│   ├── John_Doe.jpg        
│   └── Jane_Smith.jpg
├── simple_facerec.py       
├── attendance.csv          
├── main.py                 
└── README.md

```

---

## 🛠️ Tech Stack & Requirements

* **Python 3.8+**
* **OpenCV-Python (`cv2`):** Handles camera capture frames and primitive canvas operations.
* **CustomTkinter:** Powers the desktop user interface components.
* **Pillow (`PIL`):** Processes image frame color array transformations between OpenCV and Tkinter canvas widgets.
* **Face Recognition / dlib:** Generates and vectors the 128-dimension structural face encodings.

### Installation

1. Clone this repository to your local directory machine.
2. Ensure you have the required external frameworks installed via your package manager:

```bash
pip install opencv-python customtkinter Pillow face-recognition

```

*(Note: Installing `face-recognition` requires a working C++ compiler or a pre-configured `dlib` wheel matching your environment).*

---

## 💻 How To Run the Application

1. Ensure your external or integrated webcam is accessible by the operating system.
2. Initialize the application from your terminal workspace:

```bash
python main.py

```

### Administrative Operations:

* **Marking Attendance:** The application automatically runs lookups against the `images/` directory. Once a face is mapped, a green boundaries box highlights the target and records their arrival timestamp into the spreadsheet layer.
* **Registering a Guest:** Type a plain-text identifier into the sidebar input field and click **"Register New Face"**. The application immediately locks the current live frame, creates the baseline file, and triggers a dynamic database re-encoding array.

---

## 📈 Optimization Logs & Script Modifications

> ⚠️ **Developer Note for Native Implementation:**
> By default, the hardware capture line is initialized to use primary video slot index `1` (`cv2.VideoCapture(1)`). If your integrated webcam fails to activate on launch, modify line 48 inside the controller implementation block to utilize index `0`:
> ```python
> self.cap = cv2.VideoCapture(0)
> 
> ```
> 
> 

```

```
