import os
import secrets
from PIL import Image
from flaskblog import mail
from flask import url_for, current_app
from flask_mail import Message

def save_image(image):
  """
  save the user's image to the static/images path and 
  resize the image to 125 125 incase of very large images
  """
  random_hex = secrets.token_hex(8)
  _, file_extension = os.path.splitext(image.filename)
  image_filename = random_hex + file_extension
  image_path = os.path.join(current_app.root_path, 'static/images', image_filename)
  image_size = (125, 125)
  computed_image = Image.open(image)
  computed_image.thumbnail(image_size)
  computed_image.save(image_path)
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