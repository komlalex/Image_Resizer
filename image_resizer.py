"""
# Install pillow if you haven't
# import pillow
# open up iamge we want to resize using python
# print current size
3specify the size we want to change it to
# save the new resized image
"""

from PIL import Image
image = Image.open("bookshelf.png")



def resize_image(width, height):
    image = Image.open("bookshelf.png")

    print(f"Current size: {image.size}")

    resized_image = image.resize((width, height))

    resized_image.save(f"komla-alex-image-resize{resized_image.size}.png")

    print(f"New size: {resized_image.size}")


width = int(input("Input new width: "))
height = int(input ("Enter height: "))

resize_image(width, height)