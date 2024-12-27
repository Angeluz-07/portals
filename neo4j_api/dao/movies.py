# Define the Unit of Work
def get_movies(tx, sort, order, limit, skip, user_id):
    # Define the cypher statement
    cypher = """
        MATCH (m:Movie)
        WHERE m.`{0}` IS NOT NULL
        RETURN m {{ .* }} AS movie
        ORDER BY m.`{0}` {1}
        SKIP $skip
        LIMIT $limit
    """.format(sort, order)

    # Run the statement within the transaction passed as the first argument
    result = tx.run(cypher, limit=limit, skip=skip, user_id=user_id)

    """
    Make sure that you extract the results within the unit of work. Once the 
    transaction function ends, any results that have not been consumed will be lost.
    """

    # Extract a list of Movies from the Result
    return [row.value("movie") for row in result]


def get_all( driver, sort="title", order="ASC", limit=6, skip=0, user_id=None):
    with driver.session() as session:
        return session.execute_read(get_movies, sort, order, limit, skip, user_id)