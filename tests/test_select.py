from query_plan import run_query

class TestSelect:
    def test_identity(self):
        run_query("select * from users")
    
TestSelect().test_identity