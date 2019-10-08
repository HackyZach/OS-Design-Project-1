require 'rinda/rinda'

URI = "druby://localhost:5005"
DRb.start_service
ts = Rinda::TupleSpaceProxy.new(DRbObject.new(nil, URI))

puts ts.take(["bob",String,String])
puts ts.take([String,"distsys", String])
