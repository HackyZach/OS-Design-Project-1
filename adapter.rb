require 'rinda/rinda'
require 'xmlrpc/server'

# Add code to allow nil
def suppress_warnings
    previous_VERBOSE, $VERBOSE = $VERBOSE, nil
    yield
    $VERBOSE = previous_VERBOSE
end

suppress_warnings do
    XMLRPC::Config::ENABLE_NIL_PARSER = true
    XMLRPC::Config::ENABLE_NIL_CREATE = true
end
# End code to allow nil

server = XMLRPC::Server.new(5000)

ADAPTER_URI = "druby://localhost:8000"
DRb.start_service
ts = Rinda::TupleSpaceProxy.new(DRbObject.new(nil, ADAPTER_URI))

server.add_handler '_out' do |t|
  ts.write(t)
  "OK"
end

#XMLRPC::Convert.struct(i)#

server.add_handler '_in' do |t|
  t_after = []
  for i in t
    if(i.instance_of? Hash)
      i = Module.const_get(i["class"])
    end
    t_after.append(i)
  end
  ts.take(t_after)

end

server.add_handler '_rd' do |t|
  t_after = []
  for i in t
    if(i.instance_of? Hash)
      i = Module.const_get(i["class"])
    end
    t_after.append(i)
  end
  ts.read(t_after)
end

server.add_handler '_rd_a' do |t|
  t_after = []
  # puts "The _in begins here: "
  # puts "t array = ", t
  # puts "t_after array = ", t_after
  for i in t
    if(i.instance_of? Hash)
      #puts i
      i = Module.const_get(i["class"])
      #puts i
    end
    t_after.append(i)
  end
  ts_res = ts.take(t_after)
  ts.write(ts_res)
  ts_res
end

puts "Starting Server..."

server.serve
