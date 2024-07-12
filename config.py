mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_user = "developer"
mysql_ps = "developerpassword"
mysql_database = "SpacToolChainDB"
class Config():
    """Configuration settings for the project"""

    # SQLALCHEMY_DATABASE_URI: The URI for connecting to the MySQL database.
    # It is formatted with npc credentials, host, port, and database name.
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql_user, mysql_ps, mysql_host, mysql_port,
                                                                      mysql_database)

    # SQLALCHEMY_TRACK_MODIFICATIONS: A flag to disable tracking modifications of objects
    # and emitting signals. This is set to False to improve performance.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
