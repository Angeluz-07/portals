# Unit of work
def get_actors(tx, movie): # (1)
    result = tx.run("""
        MATCH (p:Person)-[:ACTED_IN]->(:Movie {title: $title})
        RETURN p
    """, title=movie)

    # Access the `p` value from each record
    return [ record["p"] for record in result ]

def get_actors_single(tx, movie):
    result = tx.run("""
        MATCH (p:Person)-[:ACTED_IN]->(:Movie {title: $title})
        RETURN p
    """, title=movie)

    return result.single()

def get_actors_from_movie(driver, movie="Nixon"):
    actors = None
    # Open a Session
    with driver.session() as session:
        # Run the unit of work within a Read Transaction
        actors = session.execute_read(get_actors_single, movie=movie) # (2)
        actors = list(actors)

        session.close()
    return actors