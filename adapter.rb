require 'rinda/rinda'
require 'xmlrpc/server'

URI = "druby://localhost:5005"
DRb.start_service
ts = Rinda::TupleSpaceProxy.new(DRbObject.new(nil, URI))

server = XMLRPC::Server.new(5000)

server.add_handler '_out' do |t|
  ts.write(t)
end

server.add_handler '_in' do |t|
  ts.take(t)
end

server.add_handler '_rd' do |t|
  ts.read(t)
end

puts "Starting Server..."

server.serve
