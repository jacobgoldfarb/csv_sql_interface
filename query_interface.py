from query_plan import QueryPlan

def run_query_from_prompt():
    while True:
        queries = input().split(";")
        if len(queries) > 1:
            queries = queries[:-1]
        [run_query(query) for query in queries]

def run_query(query: str):
    try:
        query_plan = QueryPlan(query)
        output = query_plan.execute()
        print("\n".join([str(tuple) for tuple in output]))
        return output
    except SyntaxError:
        raise