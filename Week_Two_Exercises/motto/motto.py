import os

motto_filename = "motto.txt"

script_path = os.path.dirname(os.path.abspath(__file__))

motto_handle = open(script_path + "/" + motto_filename, "w")

motto_handle.write("Fiat Lux!")
motto_handle.write("\n")
motto_handle.write("Let there be light!")
motto_handle.close()
