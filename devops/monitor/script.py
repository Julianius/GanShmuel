import socket
import time

<<<<<<< HEAD
def monitor():
=======
def script():
>>>>>>> 628b9e15eed277c9cf1aa5c21c849d3e63168fb0
   open("open_ports.txt", 'w').close()
   f = open("open_ports.txt", "a")

   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8080)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8081)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8082)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8083)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8084)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8085)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()


   a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   location = ("18.157.175.199", 8086)
   result_of_check = a_socket.connect_ex(location)
   if result_of_check == 0:
      f.write("1\n")
   else:
      f.write("0\n")

   a_socket.close()

<<<<<<< HEAD
   f.close()

def loop():
   while True:
      monitor()
      time.sleep(5)

loop()
=======
   f.close()
>>>>>>> 628b9e15eed277c9cf1aa5c21c849d3e63168fb0
