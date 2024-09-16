import os
import secrets
from PIL import Image
from flaskblog import mail
from flask import url_for, current_app
from flask_mail import Message

"""def save_image(image):

    Save the user's image to the static/images path and 
    resize the image to 125x125 with rounded corners.
    try:
        # Generate a random filename to avoid conflicts
        random_hex = secrets.token_hex(8)
        _, file_extension = os.path.splitext(image.filename)
        
        # Ensure the file extension is in a safe format
        file_extension = file_extension.lower()
        allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
        if file_extension not in allowed_extensions:
            raise ValueError("Unsupported file type")

        # Construct the new filename and path
        image_filename = random_hex + file_extension
        image_path = os.path.join(current_app.root_path, 'static/images', image_filename)
        
        # Open and process the image
        with Image.open(image) as img:
            # Define the size and resize the image
            image_size = (125, 125)
            img.thumbnail(image_size)

            # Create a rounded mask
            mask = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

            # Apply the mask to the image
            img.putalpha(mask)
            img = ImageOps.fit(img, image_size, centering=(0.5, 0.5))
            img.save(image_path, format=img.format, quality=85)  # Optional: adjust quality for optimization
        
        return image_filename

    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error saving image: {e}")
        return None"""

def save_image(image):
  
  """save the user's image to the static/images path and 
  resize the image to 125 125 incase of very large images"""
  
  random_hex = secrets.token_hex(8)
  _, file_extension = os.path.splitext(image.filename)
  image_filename = random_hex + file_extension
  image_path = os.path.join(current_app.root_path, 'static/images', image_filename)
  image_size = (175, 175)
  computed_image = Image.open(image)
  computed_image.thumbnail(image_size)
  computed_image.save(image_path, quality=85)
  return image_filename
  
"""def delete_old_images(user):

  Deletes all images in the user's image directory except the current profile image
  when they update their profile picture

  user_images_path = os.path.join(app.root_path, 'static/images')
  for filename in os.listdir(user_images_path):
      file_path = os.path.join(user_images_path, filename)
      if filename != user.profile_image and os.path.isfile(file_path):
          os.remove(file_path)"""

def sendPasswordReset(user):
    token = user.get_reset_token()  # This should return a string token
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''\
Hello,

Please use the link below to reset your password:

{url_for('users.passwordReset', token=token, _external=True)}

If you did not request a password reset, please ignore this message.
'''
    try:
        mail.send(msg)
    except Exception as e:
        # Log or handle the exception
        print(f"Error sending email: {e}")