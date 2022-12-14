from query_interface import run_query

class TestFrom:
    def test_from_single_source(self):
        expected = [
            ['id', 'first_name', 'last_name', 'user_name'],
            ['1', 'Jacob', 'Goldfarb', 'jacobjr23'],
            ['2', 'Alex', 'Lars', 'abenlars'],
            ['3', 'Christina', 'Lim', 'clim']
        ]
        actual = run_query("select * from users")
        assert(actual == expected)

    def test_from_multiple_sources(self):
        run_query("select * from users, addresses")

if __name__ == "__main__":
    tests = TestFrom()
    for function_name in dir(tests):
        if "test" in function_name:
            test = getattr(tests, function_name)
            print(f"Running {function_name}...")
            test()
