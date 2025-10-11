from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os



def upload_image():
    global img_path, img
    img_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((400, 400))  
        tk_img = ImageTk.PhotoImage(img)
        canvas.image = tk_img
        canvas.create_image(200, 200, image=tk_img)
        messagebox.showinfo("Success", "Image uploaded successfully!")


def add_watermark():
    if not img_path:
        messagebox.showwarning("Warning", "Please upload an image first!")
        return
    
    text = watermark_entry.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter watermark text!")
        return
    
    # Open the original image again (full size)
    image = Image.open(img_path).convert("RGBA")
    watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark_layer)
    
    # Define watermark style
    font_size = int(min(image.size) / 15)
    font = ImageFont.truetype("arial.ttf", font_size)
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        text_width, text_height = draw.textsize(text, font=font)


    
    # Position (bottom right corner)
    # it looks better with a margin than sticking to the edge bc looked weird before like 
    # half way off the image
    x = image.size[0] - text_width - int(image.size[0] * 0.02)  # 2% margin
    y = image.size[1] - text_height - int(image.size[1] * 0.02)  # 2% margin

    
    # Add semi-transparent text
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    
    # Combine original + watermark layers
    watermarked = Image.alpha_composite(image, watermark_layer)
    watermarked = watermarked.convert("RGB")  
    
    # Save result
    save_path = os.path.splitext(img_path)[0] + "_watermarked.jpg"
    watermarked.save(save_path)
    messagebox.showinfo("Done!", f"Watermark added!\nSaved as:\n{save_path}")


# UI SETUP

window = Tk()
window.title("Watermark Adder")
window.config(padx=20, pady=20, bg="#f0f0f0")

canvas = Canvas(width=400, height=400, bg="#ddd", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3, pady=10)

upload_btn = Button(text="📁 Upload Image", command=upload_image, width=20)
upload_btn.grid(row=1, column=0, pady=5)

Label(text="Watermark Text:", bg="#f0f0f0").grid(row=2, column=0)
watermark_entry = Entry(width=30)
watermark_entry.grid(row=2, column=1)

add_btn = Button(text="💧 Add Watermark", command=add_watermark, width=20)
add_btn.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()
