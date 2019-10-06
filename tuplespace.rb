
require 'rinda/tuplespace'

puts "Begin"

URI = "druby://localhost:5005"

puts "Start service"

DRb.start_service(URI,Rinda::TupleSpace.new)

puts "Thread join"

DRb.thread.join

puts "End service"
