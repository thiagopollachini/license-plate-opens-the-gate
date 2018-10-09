from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

class ImageDisplay():

  @staticmethod
  def show_image(image_matrix):
    print(f'Image width: {image_matrix.shape[0]}')
    print(f'Image height: {image_matrix.shape[1]}')
    img = Image.fromarray(image_matrix, mode='L')
    img.show()

  @staticmethod
  def show_filtered_image(image_matrix):
    img = Image.fromarray(image_matrix, mode='L')
    filtered = img.filter(ImageFilter.MedianFilter())
    filtered.show()
  
