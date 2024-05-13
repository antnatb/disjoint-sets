import test

if __name__ == "__main__":
    test.compare_all_running_times(1, 1000, 10)
    test.compare_all_running_times(10, 1000, 10)
    test.compare_all_running_times(100, 1000, 10)
    test.compare_wlist_vs_forest(1, 2000, 10)
    test.compare_wlist_vs_forest(10, 1000, 10)
    test.compare_wlist_vs_forest(100, 500, 10)
