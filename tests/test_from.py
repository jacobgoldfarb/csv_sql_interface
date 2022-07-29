from query_plan import run_query

class TestFrom:
    def test_from_single_source(self):
        run_query("from users")

TestFrom().test_from_single_source
