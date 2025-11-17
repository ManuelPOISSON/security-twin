import multiprocessing

import collector.collector

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    multiprocessing.freeze_support()
    collector.collector.main()