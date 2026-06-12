from backend.core.query_guard import (
    validate_query
)


def execute(
    self,
    query,
    parameters=None
):

    validate_query(query)

    with self.driver.session() as session:

        return session.run(
            query,
            parameters or {}
        )
