require 'rinda/rinda'
require 'xmlrpc/client'

URI = "druby://localhost:5005"
DRb.start_service
ts = Rinda::TupleSpaceProxy.new(DRbObject.new(nil, URI))


tuple = [
  ["bob","distsys","I am studying chapter 2"],
  ["bob","distsys","The rinda exmaple's not that simple"]
]



ts.write(tuple[0])
ts.write(tuple[1])
