import cv2
import os

# Function to check if the image exists
def load_image(image_path):
    if not os.path.exists(image_path):
        print(f"❌ Error: File '{image_path}' not found. Check the path!")
        exit()
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Unable to read the image. It may be corrupt or an unsupported format.")
        exit()
    return img

# Function to encode the message into the image
def encode_message(image_path, output_path):
    img = load_image(image_path)
    h, w, _ = img.shape  # Get image dimensions

    msg = input("🔐 Enter secret message: ")
    password = input("🔑 Set a passcode: ")

    d = {chr(i): i for i in range(255)}  # Character to ASCII mapping
    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        if n >= h:  # Move to the next column when reaching image height
            n = 0
            m += 1
            if m >= w:  # Stop if the image width is exceeded
                print("❌ Error: Image too small to encode the message.")
                exit()
        z = (z + 1) % 3  # Cycle through RGB channels

    cv2.imwrite(output_path, img)  # Save encrypted image
    print(f"✅ Secret message successfully hidden in '{output_path}'")

    return password  # Return password for verification

# Function to verify the password and ask whether to open the image
def verify_and_open_image(image_path, correct_password):
    pas = input("🔑 Enter passcode for authentication: ")
    
    if pas != correct_password:
        print("❌ YOU ARE NOT AUTHORIZED!")
        return

    print("✅ Authorization successful!")

    choice = input("🖼️ Do you want to open the encrypted image? (yes/no): ").strip().lower()
    if choice == "yes":
        os.system(f"start {image_path}")  # Open the encrypted image on Windows
        print("📂 Image opened.")
    else:
        print("❌ Image not opened.")

# Main execution
if __name__ == "__main__":
    image_path = r"original.jpg"
    output_path = r"encryptedImg.png"

    password = encode_message(image_path, output_path)
    verify_and_open_image(output_path, password)


