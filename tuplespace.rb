
require 'rinda/tuplespace'

puts "Begin"

T_URI = "druby://localhost:8000"

puts "Start service"

DRb.start_service(T_URI,Rinda::TupleSpace.new)

puts "Thread join"

DRb.thread.join

puts "End service"
