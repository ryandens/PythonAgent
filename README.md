# Python Instrumentation Agent
A python instrumentation agent developed by Ryan Dens and Alice Duan. 
The agent is in the form of a WSGI middleware and was tested on a Django web application.

### Features
1. Each response now includes a unique id
2. The strings created by a single request are counted and the number is stored
3. The time each request takes is stored
4. The amount of memory each request takes is stored

An extra view is added to the application, located at '/agent_statistics'.
This displays a log of all the responses along with the data stored for 
the response's associated request (i.e. time taken, strings created, etc.)


