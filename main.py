import cv2
import customtkinter as ctk
from PIL import Image, ImageTk
from simple_facerec import SimpleFacerec
from datetime import datetime
import csv
import os

ctk.set_appearance_mode("dark")

class FaceRecognitionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Attendance System v2.1")
        self.geometry("1100x650")

        # Load Face Logic
        self.sfr = SimpleFacerec()
        self.load_images()
        self.already_marked = []

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="FaceAI v2.1", font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.pack(pady=20)

        # --- LIVE CLOCK ---
        self.time_label = ctk.CTkLabel(self.sidebar, text="00:00:00", font=ctk.CTkFont(size=18, weight="bold"), text_color="yellow")
        self.time_label.pack(pady=10)
        self.update_clock() # Start the clock

        # Registration UI
        self.name_entry = ctk.CTkEntry(self.sidebar, placeholder_text="Enter Name to Register")
        self.name_entry.pack(pady=10, padx=10)
        
        self.reg_btn = ctk.CTkButton(self.sidebar, text="Register New Face", command=self.register_face, fg_color="blue")
        self.reg_btn.pack(pady=10, padx=10)

        self.count_label = ctk.CTkLabel(self.sidebar, text="Present Today: 0")
        self.count_label.pack(pady=20)

        # Video Area
        self.video_label = ctk.CTkLabel(self, text="")
        self.video_label.pack(expand=True, fill="both", padx=20, pady=20)

        self.cap = cv2.VideoCapture(1)
        self.current_frame = None
        self.update_frame()

    def update_clock(self):
        # This function updates the clock every 1 second
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.after(1000, self.update_clock)

    def load_images(self):
        self.sfr.load_encoding_images("images/")

    def register_face(self):
        name = self.name_entry.get().strip()
        if name and self.current_frame is not None:
            cv2.imwrite(f"images/{name}.jpg", self.current_frame)
            self.name_entry.delete(0, 'end')
            self.load_images()
            print(f"Registered {name}")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame.copy()
            face_locations, face_names = self.sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)

                if name != "Unknown" and name not in self.already_marked:
                    self.log_attendance(name)

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(800, 500))
            self.video_label.configure(image=ctk_img)
            self.video_label.image = ctk_img
        
        self.after(10, self.update_frame)

    def log_attendance(self, name):
        self.already_marked.append(name)
        with open('attendance.csv', 'a', newline='') as f:
            csv.writer(f).writerow([name, datetime.now().strftime('%H:%M:%S')])
        self.count_label.configure(text=f"Present Today: {len(self.already_marked)}")

if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.mainloop()