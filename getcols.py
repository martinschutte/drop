from sqlalchemy import create_engine

connection = create_engine('mysql://msa:zFcmVW!P5bBF2rmo97@37.77.193.36:3306/49winters').connect()

result = connection.execute("select * from products")

log = open("result.txt", "w")

connection.close()
