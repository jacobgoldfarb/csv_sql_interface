from query_interface import run_query

class TestWhere:
    def test_in_lowercase(self):
        query = "select * from users where id in (1,3)"
        expected = [
            ['id', 'first_name', 'last_name', 'user_name'],
            ['1', 'Jacob', 'Goldfarb', 'jacobjr23'],
            ['3', 'Christina', 'Lim', 'clim']
        ]
        actual = run_query(query)
        assert(expected == actual)
    
    def test_in_uppercase(self):
        query = "select * from users where id IN (1,3)"
        expected = [
            ['id', 'first_name', 'last_name', 'user_name'],
            ['1', 'Jacob', 'Goldfarb', 'jacobjr23'],
            ['3', 'Christina', 'Lim', 'clim']
        ]
        actual = run_query(query)
        assert(expected == actual)
        
    def test_in_no_brackets_fails(self):
        query = "select * from users where id in 1,3"
        try:
            actual = run_query(query)
        except SyntaxError:
            pass
        else:
            raise AssertionError("Expected test to fail but it passed.")
    
    
if __name__ == "__main__":
    tests = TestWhere()
    for function_name in dir(tests):
        if "test_in_uppercase" in function_name:
            test = getattr(tests, function_name)
            print(f"Running {function_name}...")
            test()