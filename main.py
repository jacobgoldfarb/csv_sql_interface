from query_interface import run_query_from_prompt, run_query

def main():
    # run_query("select * from addresses")
    # run_query("select first_name from users")
    run_query_from_prompt()
    
if __name__ == "__main__":
    main()
