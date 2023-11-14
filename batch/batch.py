from db import create_server_connection
from db import create_db_connection
from db import execute_query

# Set your database connection details
host_name ='server54.web-hosting.com'
user_name = "ryanqvkl_gaia"
user_password = "G!n4&J4$m!ne2008"
db_name = "ryanqvkl_gaia"

# Create a connection to the MySQL server
server_connection = create_server_connection(host_name, user_name, user_password)

# Create a connection to the MySQL database
db_connection = create_db_connection(host_name, user_name, user_password, db_name)

# Example query
query = "CREATE TABLE your_table_name;"

# Execute the query
execute_query(db_connection, query)

# Close the connections
# server_connection.close()
# db_connection.close()