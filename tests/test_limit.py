from query_interface import run_query

class TestLimit:
    def test_limit_two(self):
        expected = [
            ['id', 'first_name', 'last_name', 'user_name'],
            ['1', 'Jacob', 'Goldfarb', 'jacobjr23'],
            ['2', 'Alex', 'Lars', 'abenlars'],
        ]
        actual = run_query("select * from users limit 2")
        assert(expected == actual)

if __name__ == "__main__":
    tests = TestLimit()
    for function_name in dir(tests):
        if "test" in function_name:
            test = getattr(tests, function_name)
            print(f"Running {function_name}...")
            test()