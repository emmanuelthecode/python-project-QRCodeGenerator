from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

# Initialize the main window
root = Tk()

# Global variable to store the image label so it can be updated
image_label = None

def generate():
    """
    This function is triggered when the 'Generate QR Code' button is clicked.
    It fetches the link and link name from the entry fields, generates a QR code,
    saves it as a PNG file, and displays the generated QR code on the GUI.
    """
    global image_label

    # Get the name for the QR code image file and the link to convert
    link_name = name_entry.get()
    link = link_entry.get()

    # Construct the file name and generate the QR code
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)

    # Load the generated QR code image
    image = ImageTk.PhotoImage(Image.open(file_name))

    # Display the image on the GUI
    if image_label is None:
        # If no image label exists, create it
        image_label = Label(root, image=image)
        canvas.create_window(200, 450, window=image_label)
    else:
        # If an image label already exists, update the image
        image_label.config(image=image)
    
    # Keep a reference to the image to avoid garbage collection
    image_label.image = image

# Create a canvas to hold all GUI elements
canvas = Canvas(root, width=400, height=600)
canvas.pack()

# Add a title label to the application
app_label = Label(root, text="QR Code Generator", 
                  fg="blue", 
                  font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

# Labels for the input fields
name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")

# Place the labels on the canvas
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# Entry fields for the user to input the link name and the URL
name_entry = Entry(root)
link_entry = Entry(root)

# Place the entry fields on the canvas
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# Button to trigger QR code generation
button = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button)

# Run the main Tkinter event loop
root.mainloop()
