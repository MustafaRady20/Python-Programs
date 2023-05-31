# QR stands for Quick Response, used to encode and decode data into a machine-readable form
# It contains a grid of black squares on a white background, which can be read by any imaging device such as a camera, 
# and processed to extract the required data from the patterns that are present in the horizontal components of the image


import pyqrcode

link="https://github.com/MustafaRady20"

url = pyqrcode.create(link)


url.svg("myGitHub.svg",scale=8)