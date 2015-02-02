# Flask Rest Service for Queue

Nowadays, we have many subsystems within our web applications or mobile applications. Moreover, we have many subsystems(tasks) that takes too much time such as compression, data analytics and so on.

In such cases, we need to integrate subsystems. Thus, the most proper way is to integrate subsystems through adding message layer between the subsystems.

However, we have lots of ooportunity to use as a message queue between subsystems and we have to know the client libraries of the message queues. Therefore, we need to handle another stuff that is to learn the details of the message queue systems. 

Our project mainly has a goal to make abstraction over the message queues using the REST interface. The project aims to supports the message queues starting from RabbitMQ and Redis.
