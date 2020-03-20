#  file eco_client
require 'socket'



ClientSocket = TCPSocket.open('127.0.0.1',8080)

puts 'Insert code in python: \n'

msg = gets 

ClientSocket.puts(msg)

response = ClientSocket.recvfrom(1024) 
puts response
