Secret Message Encoder in Images

  This Python script allows you to hide a secret message inside an image using OpenCV. The message is encoded into the pixel values of the image and can only be     accessed with the correct passcode.

Features:

  Encodes a secret message into an image.
  
  Uses RGB pixel values to store message characters.
  
  Requires a passcode for authentication.
  
  Saves the encoded image as a new file.
  
  Provides an option to open the encrypted image after authentication.

Requirements

  Python 3.x
  
  OpenCV (cv2)
  
  OS module (os)

Installation:

  Ensure you have Python installed, then install OpenCV:
  
  pip install opencv-python

Usage:

  Place the image you want to encode a message in the same directory as the script and rename it to original.jpg (or modify the script to use a different         
  filename).

Run the script:

  python script.py

  Enter your secret message and set a passcode when prompted.
  
  The script will encode the message and save a new image as encryptedImg.png.
  
  To verify, enter the passcode and choose whether to open the encrypted image.

Notes:

  The image must be large enough to store the entire message.
  
  The encoded image may look slightly altered due to pixel modifications.
  
  The message is stored in RGB channels cyclically.
  
  Unauthorized access is restricted via a passcode mechanism.

Example:

🔐 Enter secret message: Hello, World!
🔑 Set a passcode: 1234
✅ Secret message successfully hidden in 'encryptedImg.png'
🔑 Enter passcode for authentication: 1234
✅ Authorization successful!
🖼️ Do you want to open the encrypted image? (yes/no): yes
📂 Image opened.

License:

  This project is open-source and free to use.
