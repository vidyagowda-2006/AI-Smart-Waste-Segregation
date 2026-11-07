
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
from pathlib import Path


# ---------------- MODEL SETUP ----------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "waste_classifier.keras"

model = tf.keras.models.load_model(MODEL_PATH)

class_names = ["Glass", "Metal", "Organic", "Paper", "Plastic"]

EMAIL = "admin@gmail.com"
PASSWORD = "12345"


# ---------------- LOGIN PAGE ----------------c

def open_login_page():

    login_window = tk.Tk()
    login_window.title("Login - AI Smart Waste Segregation")
    login_window.geometry("450x420")
    login_window.configure(bg="#E8F5E9")

    def login():

        entered_email = email_entry.get().strip()
        entered_password = password_entry.get()

        if entered_email == EMAIL and entered_password == PASSWORD:
            login_window.destroy()
            open_information_page1()
        else:
            error_label.config(text="Invalid email or password!")

    def toggle_password():

        if password_entry.cget("show") == "*":
            password_entry.config(show="")
            eye_button.config(text="Hide")
        else:
            password_entry.config(show="*")
            eye_button.config(text="Show")

    tk.Label(
        login_window,
        text="WASTE SEGREGATION SYSTEM",
        font=("Arial", 17, "bold"),
        bg="#E8F5E9",
        fg="#1B5E20"
    ).pack(pady=30)

    tk.Label(
        login_window,
        text="Login to Continue",
        font=("Arial", 13),
        bg="#E8F5E9"
    ).pack(pady=10)

    tk.Label(
        login_window,
        text="Email",
        font=("Arial", 11),
        bg="#E8F5E9"
    ).pack()

    email_entry = tk.Entry(
        login_window,
        font=("Arial", 12),
        width=28
    )
    email_entry.pack(pady=8)

    tk.Label(
        login_window,
        text="Password",
        font=("Arial", 11),
        bg="#E8F5E9"
    ).pack()

    password_frame = tk.Frame(
        login_window,
        bg="#E8F5E9"
    )
    password_frame.pack(pady=8)

    password_entry = tk.Entry(
        password_frame,
        font=("Arial", 12),
        width=22,
        show="*"
    )
    password_entry.pack(side="left")

    eye_button = tk.Button(
        password_frame,
        text="Show",
        command=toggle_password
    )
    eye_button.pack(side="left", padx=5)

    tk.Button(
        login_window,
        text="LOGIN",
        font=("Arial", 12, "bold"),
        bg="#2E7D32",
        fg="white",
        width=20,
        command=login
    ).pack(pady=20)

    error_label = tk.Label(
        login_window,
        text="",
        fg="red",
        bg="#E8F5E9",
        font=("Arial", 10)
    )
    error_label.pack()

    login_window.bind(
        "<Return>",
        lambda event: login()
    )

    login_window.mainloop()


# ---------------- INFORMATION PAGE 1 ----------------

def open_information_page1():

    page = tk.Tk()
    page.title("Waste Segregation - Information")
    page.geometry("750x700")
    page.configure(bg="#E8F5E9")

    tk.Label(
        page,
        text="AI SMART WASTE SEGREGATION SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#E8F5E9",
        fg="#1B5E20"
    ).pack(pady=15)

    tk.Label(
        page,
        text="PAGE 1 - INTRODUCTION TO WASTE SEGREGATION",
        font=("Arial", 14, "bold"),
        bg="#E8F5E9"
    ).pack(pady=10)

    content_frame = tk.Frame(
        page,
        bg="#E8F5E9"
    )
    content_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=10
    )

    scrollbar = tk.Scrollbar(content_frame)
    scrollbar.pack(side="right", fill="y")

    text_area = tk.Text(
        content_frame,
        font=("Arial", 11),
        bg="#E8F5E9",
        fg="#222222",
        wrap="word",
        yscrollcommand=scrollbar.set,
        relief="flat",
        padx=10,
        pady=10
    )
    text_area.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=text_area.yview)

    content = """
WHAT IS WASTE SEGREGATION?

Waste segregation means separating different types of waste according to their materials and properties. It helps in proper disposal, recycling and reuse of waste.

WHY IS WASTE SEGREGATION IMPORTANT?

1. Reduces environmental pollution.
2. Helps in recycling useful materials.
3. Keeps our surroundings clean.
4. Reduces the amount of waste sent to landfills.
5. Supports a healthy environment.

HOW DOES AI HELP?

Artificial Intelligence (AI) helps identify different types of waste by analysing images. Our system uses a trained machine learning model to predict the category of waste.

TYPES OF WASTE

1. ORGANIC WASTE

Organic waste comes from plants and animals. It decomposes naturally and can be converted into compost.

Examples:
• Vegetable peels
• Fruit waste
• Leftover food
• Dry leaves

2. METAL WASTE

Metal waste consists of discarded objects made from metal. Many metal materials can be recycled and reused.

Examples:
• Aluminium cans
• Iron pieces
• Metal tins
• Old metal containers

3. PLASTIC WASTE

Plastic waste consists of discarded products made from plastic. It should be properly collected and recycled where possible.

Examples:
• Plastic bottles
• Plastic covers
• Food containers
• Plastic wrappers
"""

    text_area.insert("1.0", content)
    text_area.config(state="disabled")

    tk.Button(
        page,
        text="NEXT PAGE →",
        font=("Arial", 12, "bold"),
        bg="#2E7D32",
        fg="white",
        width=20,
        command=lambda: [page.destroy(), open_information_page2()]
    ).pack(pady=15)

    page.mainloop()


# ---------------- INFORMATION PAGE 2 ----------------

def open_information_page2():

    page = tk.Tk()
    page.title("Waste Segregation - Information")
    page.geometry("750x700")
    page.configure(bg="#E3F2FD")

    tk.Label(
        page,
        text="AI SMART WASTE SEGREGATION SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#E3F2FD",
        fg="#0D47A1"
    ).pack(pady=15)

    tk.Label(
        page,
        text="PAGE 2 - TYPES OF WASTE AND RECYCLING",
        font=("Arial", 14, "bold"),
        bg="#E3F2FD"
    ).pack(pady=10)

    content_frame = tk.Frame(
        page,
        bg="#E3F2FD"
    )
    content_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=10
    )

    scrollbar = tk.Scrollbar(content_frame)
    scrollbar.pack(side="right", fill="y")

    text_area = tk.Text(
        content_frame,
        font=("Arial", 11),
        bg="#E3F2FD",
        fg="#222222",
        wrap="word",
        yscrollcommand=scrollbar.set,
        relief="flat",
        padx=10,
        pady=10
    )
    text_area.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=text_area.yview)

    content = """
4. PAPER WASTE

Paper waste includes used or discarded paper products. Most clean and dry paper can be recycled into new paper products.

Examples:
• Newspapers
• Old notebooks
• Cardboard boxes
• Used office paper

5. GLASS WASTE

Glass waste consists of discarded glass products. Glass can often be recycled and made into new glass products. Broken glass must be handled carefully.

Examples:
• Glass bottles
• Glass jars
• Glass containers
• Broken glass pieces

BENEFITS OF RECYCLING

1. Saves natural resources.
2. Reduces pollution.
3. Saves energy in many manufacturing processes.
4. Reduces landfill waste.
5. Helps protect the environment.

ABOUT OUR PROJECT

The AI Smart Waste Segregation System is designed to identify waste materials using image classification.

The user selects an image of waste. The trained AI model analyses the image and predicts one of five categories:

• Glass
• Metal
• Organic
• Paper
• Plastic

The application displays the predicted category, confidence percentage and a suggested bin colour.

BIN SUGGESTION

GREEN BIN:
Suggested for Organic Waste.

BLUE BIN:
Suggested for recyclable categories in this project, including Glass, Metal, Paper and Plastic.

Note: Actual waste-bin colours and disposal rules may vary depending on local waste-management guidelines.

CONCLUSION

Proper waste segregation helps maintain a clean environment. Our project uses Artificial Intelligence to make waste identification easier and support better waste management.
"""

    text_area.insert("1.0", content)
    text_area.config(state="disabled")

    button_frame = tk.Frame(
        page,
        bg="#E3F2FD"
    )
    button_frame.pack(pady=12)

    tk.Button(
        button_frame,
        text="← BACK",
        font=("Arial", 11, "bold"),
        bg="#546E7A",
        fg="white",
        width=15,
        command=lambda: [page.destroy(), open_information_page1()]
    ).pack(side="left", padx=10)

    tk.Button(
        button_frame,
        text="CONTINUE TO APP →",
        font=("Arial", 11, "bold"),
        bg="#1565C0",
        fg="white",
        width=20,
        command=lambda: [page.destroy(), open_main_application()]
    ).pack(side="left", padx=10)

    page.mainloop()


# ---------------- ORIGINAL WASTE PREDICTION APP ----------------

def open_main_application():

    window = tk.Tk()
    window.title("AI Smart Waste Segregation System")
    window.geometry("700x750")
    window.configure(bg="#F1F8E9")

    selected_image = None

    def choose_image():

        nonlocal selected_image

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png")
            ]
        )

        if not file_path:
            return

        # IMAGE PREVIEW
        image = Image.open(file_path).convert("RGB")
        image.thumbnail((300, 300))

        selected_image = ImageTk.PhotoImage(image)
        image_label.config(
            image=selected_image,
            text=""
        )

        # ORIGINAL WORKING IMAGE PREPROCESSING
        img = tf.keras.utils.load_img(
            file_path,
            target_size=(160, 160)
        )

        img_array = tf.keras.utils.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # ORIGINAL MODEL PREDICTION
        prediction = model.predict(
            img_array,
            verbose=0
        )

        predicted_index = np.argmax(prediction[0])
        predicted_class = class_names[predicted_index]

        confidence = prediction[0][predicted_index] * 100

        prediction_label.config(
            text=f"Predicted Waste: {predicted_class}"
        )

        confidence_label.config(
            text=f"Confidence: {confidence:.2f}%"
        )

        # ORIGINAL BIN SUGGESTION LOGIC
        if predicted_class == "Organic":

            bin_label.config(
                text="Suggested Bin: GREEN BIN",
                fg="green"
            )

            bin_description.config(
                text="Suitable for organic / wet waste"
            )

        elif predicted_class in ["Paper", "Plastic", "Glass", "Metal"]:

            bin_label.config(
                text="Suggested Bin: BLUE BIN",
                fg="blue"
            )

            bin_description.config(
                text="Suitable for recyclable dry waste"
            )

        else:

            bin_label.config(
                text="Suggested Bin: GENERAL WASTE BIN",
                fg="black"
            )

            bin_description.config(
                text="Dispose according to local waste guidelines"
            )

    def clear_result():

        nonlocal selected_image

        selected_image = None

        image_label.config(
            image="",
            text="No Image Selected"
        )

        prediction_label.config(
            text="Predicted Waste: "
        )

        confidence_label.config(
            text="Confidence: "
        )

        bin_label.config(
            text="Suggested Bin: —",
            fg="black"
        )

        bin_description.config(text="")

    # MAIN HEADING
    tk.Label(
        window,
        text="AI SMART WASTE SEGREGATION SYSTEM",
        font=("Arial", 19, "bold"),
        bg="#F1F8E9",
        fg="#1B5E20"
    ).pack(pady=20)

    tk.Label(
        window,
        text="Upload a waste image to identify its category",
        font=("Arial", 12),
        bg="#F1F8E9"
    ).pack(pady=10)

    image_label = tk.Label(
        window,
        text="No Image Selected",
        bg="white",
        width=35,
        height=12
    )
    image_label.pack(pady=15)

    tk.Button(
        window,
        text="CHOOSE IMAGE",
        font=("Arial", 12, "bold"),
        bg="#2E7D32",
        fg="white",
        width=20,
        command=choose_image
    ).pack(pady=10)

    prediction_label = tk.Label(
        window,
        text="Predicted Waste: ",
        font=("Arial", 14, "bold"),
        bg="#F1F8E9"
    )
    prediction_label.pack(pady=10)

    confidence_label = tk.Label(
        window,
        text="Confidence: ",
        font=("Arial", 12),
        bg="#F1F8E9"
    )
    confidence_label.pack(pady=5)

    bin_label = tk.Label(
        window,
        text="Suggested Bin: —",
        font=("Arial", 14, "bold"),
        bg="#F1F8E9"
    )
    bin_label.pack(pady=10)

    bin_description = tk.Label(
        window,
        text="",
        font=("Arial", 11),
        bg="#F1F8E9"
    )
    bin_description.pack(pady=5)

    tk.Button(
        window,
        text="CLEAR",
        font=("Arial", 11, "bold"),
        bg="#C62828",
        fg="white",
        width=15,
        command=clear_result
    ).pack(pady=20)

    tk.Label(
        window,
        text="AI-Based Waste Classification",
        font=("Arial", 10),
        bg="#F1F8E9",
        fg="gray"
    ).pack(side="bottom", pady=10)

    window.mainloop()


# ---------------- START APPLICATION ----------------

open_login_page()
