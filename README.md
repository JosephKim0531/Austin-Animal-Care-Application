# Austin-Animal-Care-Application
In the Austin Animal Care project, an application was developed using the Model, View, Controller architecture. Dash was used to develop the web application's layout as well as additional controller logic that contained callback functions. Python and PyMongo were employed to create CRUD functionality that served as the "glue" between the web application's interface and the MongoDB database. MongoDB was used as the NoSQL database that stored the Austin Animal Care data as documents. In order to create programs that are maintainable, readable, and adaptable, the application was built modularly and repetitive logic was separated into functions. In creating a module for the CRUD logic, the code could be reused for a different web application that required connecting to a MongoDB database. 
The web application was developed modularly and in an iterative fashion. First, the model portion or the database, was set up which required loading data from a CSV file. In addition, user authentication and authorization was set up from the database layer. Next the controller portion or the CRUD functionality was developed and database connection logic was also included in the CRUD module. Finally, the layout of the view portion or the application's web layout was developed using the Dash framework. In addition to the layout, the Dash framework to create dynamic web pages was employed with callback functions. Although this project was my first time creating CRUD methods for a database, I approached the design and implmentation for the database and dashboard requirements in a similar fashion as my previous projects, iteratively. When creating a web application that contains and requires data manipulation and projection, I will utilize the Dash framework as it contains a rich set of libraries for said applications. In addition, I will make sure to create a separate module to handle the CRUD logic from the database. 
The work done in this project is important to many companies that have large datasets as it allows the company to access and analyze the data efficiently and effectively. The web application developed abstracts the lower level details of connecting to and using a database. This allows the company to focus on their goals and provide services/products to the best of their ability. 
