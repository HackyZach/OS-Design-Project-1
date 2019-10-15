Project 1 of CPSC 551

Team Members: Mircea Dumitrache
              Zachary Owen
              Bumjoong Kim

Folder structure from root of project folder
.
├── README.md
├── README.txt
├── adapter.rb
├── pythonClients
│   ├── alice.py
│   ├── arithmetic_client.py
│   ├── arithmetic_server.py
│   ├── bob.py
│   ├── chuck.py
│   └── next.py
├── rubyClients
│   ├── blog.rb
│   ├── blog2.rb
│   ├── bob.rb
│   └── chuck.rb
└── tuplespace.rb

2 directories, 14 files

 ==> adapter.rb
      - Script that implements the adapter using an XMLRPC server to listen
        to requests.
      - Is connected to tuplespace server.
      - Has four server handlers:
                  * '_out' equivalent of write
                  * '_in' equivalent of take
                  * '_rd' equivalent of read
                  * '_rd_a' used in next.py to read the next line

==> tuplespace.rb
      - Script that implements Rinda in ruby.
      - Contains the construction of the tuplespace.

==> rubyClients
      - blog.rb and blog2.rb are the ruby versions of arithmetic_client
        and arithmetic_server. They are taken from the wikipedia page
        in the project description.
      - bob.rb and chuck.rb were our test scripts for early tuple testing
        before the adapter was introduced.

==> pythonClients
      - bob.py, alice.py and chuck.py are the exact examples given in
        the book (as the project description stated)
      - arithmetic_client.py and arithmetic_server.py are the python
        equivalent(almost) of blog.rb and blog2.rb
      - next.py is the file used to read one line at a time, in order

HOW TO RUN:
      1. Open at least three terminals (recommended four)
      2. Use first terminal to run tuplespace.rb
      3. Use second terminal to run adapter.rb
      4. Use other terminals to run the test cases.
      NOTE: arithmetic_server.py will take up its own terminal until
      closed.
