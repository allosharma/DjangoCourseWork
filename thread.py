import threading
import time

class threadClass(threading.Thread):
    def __init__(self, person_name):
        self.person_name = person_name
        threading.Thread.__init__(self)

    def run(self):
        print(f"Thread Name: {threading.current_thread().name}, Thread ID: {threading.get_ident()}")
        time.sleep(2)
        print(f"Person Name: {self.person_name}")

def doSomething(name, age, gender):
    print(f"Thread Name: {threading.current_thread().name}, Thread ID: {threading.get_ident()}")
    time.sleep(2)
    print(f"Person Details: Name: {name}, Age: {age}, gender:{gender}")

startTime = time.time()

if __name__ == "__main__":
    # print("Main program finished")
    # Creating a thread using threading.Thread
    # thread1 = threading.Thread(target=doSomething, args=["Alice", 25, "F"]) #remember that we are not executing the function here, just passing the reference. If we execute it here, it will run in the main thread and not in the new threads.
    # thread2 = threading.Thread(target=doSomething, args=["Bob", 30, "M"])
    # thread3 = threading.Thread(target=doSomething, args=["Charlie", 35, "M"])
    # thread1.start()  # Start the thread
    # thread2.start()
    # thread3.start()
    # thread1.join()   # Wait for the thread to finish, if not used main program will finish before thread finishes
    # thread2.join()
    # thread3.join()

    # Above we had 3 threads and we had to write 9 lines of code to create and start them.
    # We can use a loop to create multiple threads and start them.
    person = {
        "Alice": (25, "F"),
        "Bob": (30, "M"),
        "Charlie": (35, "M"),
        "David": (28, "M"),
        "Eve": (22, "F")
    }
    threads = [] #list to keep track of all threads
    for name, details in person.items():
        thread = threading.Thread(target=doSomething, args=[name, details[0], details[1]])
        thread.start()
        threads.append(thread) #add thread to the list

    for thread in threads: # iterate through the list of threads
        thread.join()  # Wait for the thread to finish, if not used main program will finish before thread finishes
    
    # Instead of thread.start() and thread.join() we can use thread.run() which will start the thread and wait for it to finish before moving to the next line of code.
    # But this will not run the threads concurrently, it will run them sequentially on a single thread.

    # Creating a thread by extending the threading.Thread class
    t1 = threadClass("Alice")
    t1.start()
    t2 = threadClass("Bob")
    t2.start()
    t1.join()
    t2.join()

    print(f"Total time taken: {time.time() - startTime:.2f} seconds")