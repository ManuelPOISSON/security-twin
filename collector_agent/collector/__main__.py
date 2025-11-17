import multiprocessing

from collector import collector

multiprocessing.freeze_support()
collector.main()