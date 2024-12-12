from neo4j import GraphDatabase

def init_driver(uri, username, password):
    driver =  GraphDatabase.driver(uri, auth=(username, password))
    driver.verify_connectivity()
    return driver