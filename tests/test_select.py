from query_interface import run_query

class TestSelect:
    def test_identity(self):
        expected = [
            ['id', 'first_name', 'last_name', 'user_name'],
            ['1', 'Jacob', 'Goldfarb', 'jacobjr23'],
            ['2', 'Alex', 'Lars', 'abenlars'],
            ['3', 'Christina', 'Lim', 'clim']
        ]
        actual = run_query("select * from users")
        assert(expected == actual)
    
    def test_single_attr(self):
        expected = [
            ['id'],
            ['1'],
            ['2'],
            ['3']
        ]
        actual = run_query("select id from users")
        assert(expected == actual)
        
    def test_multiple_attrs(self):
        expected = [
            ['first_name', 'user_name'],
            ['Jacob', 'jacobjr23'],
            ['Alex', 'abenlars'],
            ['Christina', 'clim']
        ]
        actual = run_query("select first_name, user_name from users")
        assert(expected == actual)
    
    def test_non_existing_attr_fails(self):
        try:
            run_query("select eye_color from users")
        except SyntaxError:
            pass
        else:
            raise AssertionError("Expected SyntaxError but function succeeded.")
        
    def test_no_commas_fails(self):
        try:
            run_query("select id first_name from users")
        except SyntaxError:
            pass
        else:
            raise AssertionError("Expected SyntaxError but function succeeded.")

if __name__ == "__main__":
    tests = TestSelect()
    for function_name in dir(tests):
        if "test" in function_name:
            test = getattr(tests, function_name)
            print(f"Running {function_name}...")
            test()