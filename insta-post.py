from instagrapi import Client

# 1. Log in to your Instagram account
cl = Client()
cl.login("your_username", "your_password")

# 2. Post a photo with a caption
cl.photo_upload("path/to/image.jpg", caption="Hello Instagram from Python!")

# 3. Log out (optional)
cl.logout()
