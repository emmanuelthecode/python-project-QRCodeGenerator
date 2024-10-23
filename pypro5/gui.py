from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

# Initialize the main window
app = Tk()

# Global variable to store the QR code image
qr_image_label = None

def create_qr():
    """
    This function is triggered when the 'Create QR Code' button is clicked.
    It retrieves the data entered by the user (name and link), generates a QR code,
    saves it as a PNG file, and displays it in the window.
    """
    global qr_image_label

    # Get the link name and link from the input fields
    file_name_entry = name_input.get()
    link_entry = url_input.get()

    # Generate the filename and create the QR code
    qr_file = file_name_entry + ".png"
    qr_code = pyqrcode.create(link_entry)
    qr_code.png(qr_file, scale=8)

    # Load the generated QR code image
    qr_image = ImageTk.PhotoImage(Image.open(qr_file))

    # Display the QR code image in the window
    if qr_image_label is None:
        qr_image_label = Label(app, image=qr_image)
        display_area.create_window(200, 450, window=qr_image_label)
    else:
        qr_image_label.config(image=qr_image)

    # Keep a reference to prevent garbage collection
    qr_image_label.image = qr_image

# Create a canvas for the layout
display_area = Canvas(app, width=400, height=600)
display_area.pack()

# Add a title label
app_title = Label(app, text="QR Code Creator", 
                  fg="darkblue", 
                  font=("Helvetica", 30))
display_area.create_window(200, 50, window=app_title)

# Labels for the user inputs
label_name = Label(app, text="File Name")
label_link = Label(app, text="URL")

# Position the labels on the canvas
display_area.create_window(200, 100, window=label_name)
display_area.create_window(200, 160, window=label_link)

# Entry fields for name and link input
name_input = Entry(app)
url_input = Entry(app)

# Place the input fields on the canvas
display_area.create_window(200, 130, window=name_input)
display_area.create_window(200, 180, window=url_input)

# Button to generate the QR code
create_button = Button(text="Generate QR Code", command=create_qr)
display_area.create_window(200, 230, window=create_button)

# Start the Tkinter main loop
app.mainloop()
