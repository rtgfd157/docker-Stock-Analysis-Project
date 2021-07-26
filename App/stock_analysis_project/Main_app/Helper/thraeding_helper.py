from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading
import time as t
import concurrent.futures
lock= threading.Lock()

def start_thraeding(number_of_threading, splitted_list_of_querysets, function_to_be_threaded ):

    futures = [] # misions list for threading

    with ThreadPoolExecutor(max_workers=number_of_threading) as executor:
        
        for qs in splitted_list_of_querysets:
            #executor.submit(make, dt )
            futures.append(executor.submit(function_to_be_threaded, qs))

        #while futures:
        for future in concurrent.futures.as_completed(futures):
                futures.remove(future)


    t.sleep(2)
    print("---- finished threading")