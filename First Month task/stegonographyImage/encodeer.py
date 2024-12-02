import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

root = tk.Tk()
root.title("Steganography Image encoder")
root.geometry("600x500")


img = Image.open("stegonographyImage/imageInsert.webp")
img = img.resize((200, 200), Image.Resampling.LANCZOS)

photo = ImageTk.PhotoImage(img)

lableImage = tk.Label(root, image=photo)
lableImage.image = photo
lableImage.grid(row=0, column=0, padx=5, pady=10)


img2 = Image.open("stegonographyImage/Untitled.jpeg")
img2 = img2.resize((200, 200), Image.Resampling.LANCZOS)

photo2 = ImageTk.PhotoImage(img2)

lableImage2 = tk.Label(root, image=photo2)
lableImage2.image = photo
lableImage2.grid(row=0, column=1, padx=150, pady=10)


file_path = ""
# mage_path = "input_image.png"  # Input image path
message = "Kamlesh ki jay"  # Message to encode
output_path = "output_image.png"  # Output image path


def insert_image():
    # Open file dialog to select an image
    global file_path
    file_path2 = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    file_path = file_path2
    if file_path2:
        # Load the selected image using PIL
        img = Image.open(file_path2)
        # Resize the image
        img = img.resize((200, 200), Image.Resampling.LANCZOS)

        # Convert the image to Tkinter-compatible format
        photo = ImageTk.PhotoImage(img)

        # Display the image in a label
        lableImage.config(image=photo)
        lableImage.image = photo  # Keep a reference to avoid garbage collection


output = "kamlesh.png"
# photo9 = ImageTk.PhotoImage(output)


def string_to_bin(text):
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string


def encode():
    global file_path
    global message
    global output
    output2 = ""
    imagee = Image.open(file_path)
    encode_image = imagee.copy()
    binary_message = string_to_bin(message)+'1111111111111110'
    data_index = 0

    for x in range(imagee.size[0]):
        for y in range(imagee.size[1]):
            pixel = list(encode_image.getpixel((x, y)))
        for i in range(3):
            if data_index < len(binary_message):
                pixel[i] = (pixel[i] & -1) | int(binary_message[data_index])
                data_index += 1
        # encode_image.putpixel((x, y)), tuple(pixel)
        encode_image.putpixel((x, y), tuple(pixel))
        if data_index >= len(binary_message):
            break
    # encode_image.save(output2)
    # output = output2
    # print(file_path)
    # print(output)
    # if not output.endswith(".png"):  # Ensure valid file extension
    #     output += ".png"  # Append '.png' if not already present
    encode_image.save(output)
    output = ImageTk.PhotoImage(output)
    lableImage2.config(image=output)


def decode():
    pass
# output = ""  # Global output variable

# # Function to convert string to binary


# def string_to_bin(text):
#     binary_string = ''.join(format(ord(char), '08b') for char in text)
#     return binary_string


# # Function to encode the message into the image
# def encode():
#     global file_path
#     global message
#     global output

#     # Open the image file
#     imagee = Image.open(file_path)
#     encode_image = imagee.copy()

#     # Convert the message to binary and append the terminator '1111111111111110'
#     binary_message = string_to_bin(message) + '1111111111111110'
#     data_index = 0

#     # Iterate over the image pixels
#     for x in range(imagee.size[0]):
#         for y in range(imagee.size[1]):
#             # Get the pixel at (x, y)
#             pixel = list(encode_image.getpixel((x, y)))

#             # Modify the RGB values with the binary data
#             for i in range(3):  # Iterate over R, G, B values
#                 if data_index < len(binary_message):
#                     pixel[i] = (pixel[i] & ~1) | int(
#                         binary_message[data_index])  # Modify LSB
#                     data_index += 1

#             # Update the pixel in the encoded image
#             encode_image.putpixel((x, y), tuple(pixel))

#             # If we've encoded the whole message, stop
#             if data_index >= len(binary_message):
#                 break
#         if data_index >= len(binary_message):
#             break

#     # Save the encoded image to the output file
#     encode_image.save(output)

#     # Display the encoded image in the Tkinter window
#     show_encoded_image(output)

# Function to display the encoded image in the Tkinter window


def show_encoded_image():
    image_path = "kamlesh.png"
    encoded_img = Image.open(image_path)  # Open the saved image
    # Convert to Tkinter-compatible format
    photo = ImageTk.PhotoImage(encoded_img)

    # Update the label with the new image
    labelImage2.config(image=photo)
    labelImage2.image = photo  # Keep a reference to avoid garbage collection


InsertButton = tk.Button(root, text="Insert Image", command=insert_image)
InsertButton.grid(row=4, padx=5, pady=5)


buttonEncode = tk.Button(root, text="Encode", command=encode)
buttonEncode.grid(row=5, padx=5, pady=5)


buttonEncode2 = tk.Button(root, text="Decode", command=show_encoded_image)
buttonEncode2.grid(row=6, padx=5, pady=5)


root.mainloop()
