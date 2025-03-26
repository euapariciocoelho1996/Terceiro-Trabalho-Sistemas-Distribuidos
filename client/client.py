import requests
from tkinter import filedialog, ttk
from PIL import ImageTk, Image
import tkinter as tk
import os

class ClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Upload Client")
        self.master.geometry("800x600")  # Aumentei o tamanho da janela
        self.master.configure(bg="#2C3E50")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Arial", 12), padding=10, background="#1ABC9C", foreground="white")
        self.style.configure("TLabel", font=("Arial", 12), background="#2C3E50", foreground="white")
        
        self.frame = ttk.Frame(master, padding=20, style="TFrame")
        self.frame.pack(expand=True, pady=20)

        self.upload_button = ttk.Button(self.frame, text="\U0001F4E4 Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.image_label = ttk.Label(self.frame, text="Selecionar Imagem")
        self.image_label.pack(pady=5)

        self.image_frame = ttk.Frame(self.frame, padding=20)
        self.image_frame.pack(pady=10)

        self.original_label = ttk.Label(self.image_frame, text="Imagem Original")
        self.original_label.grid(row=0, column=0, padx=20, pady=5)

        self.modified_label = ttk.Label(self.image_frame, text="Imagem com Filtro")
        self.modified_label.grid(row=0, column=1, padx=20, pady=5)

        self.original_image_label = ttk.Label(self.image_frame)
        self.original_image_label.grid(row=1, column=0, padx=20)

        self.modified_image_label = ttk.Label(self.image_frame)
        self.modified_image_label.grid(row=1, column=1, padx=20)

        self.image_selected = False

        if not os.path.exists('client_images'):
            os.makedirs('client_images')

    def upload_image(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            local_original_path = os.path.join('client_images', os.path.basename(filepath))
            Image.open(filepath).save(local_original_path)  # Copia a imagem para a pasta local

            self.show_image(local_original_path)
            self.apply_and_save_filter(local_original_path)
            self.send_image_to_server(local_original_path)

    def show_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300))  # Aumentei o tamanho da exibição
        img = ImageTk.PhotoImage(img)

        if not self.image_selected:
            self.image_label.config(text="")
            self.image_selected = True

        self.original_image_label.config(image=img)
        self.original_image_label.image = img

    def apply_and_save_filter(self, image_path):
        img = Image.open(image_path)
        smaller_size = (img.width // 5, img.height // 5)
        img = img.resize(smaller_size, Image.NEAREST)
        img = img.resize((img.width * 5, img.height * 5), Image.NEAREST)
        img = img.convert("L")

        filtered_image_path = os.path.join('client_images', f"filtered_{os.path.basename(image_path)}")
        img.save(filtered_image_path)
        self.show_modified_image(filtered_image_path)

    def show_modified_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300))  # Aumentei o tamanho da exibição
        img = ImageTk.PhotoImage(img)

        self.modified_image_label.config(image=img)
        self.modified_image_label.image = img

    def send_image_to_server(self, image_path):
        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = requests.post('http://192.168.1.15:5000/upload', files=files)
            if response.status_code == 200:
                print("Image successfully uploaded to the server.")
            else:
                print("Failed to upload image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()