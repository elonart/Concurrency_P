from multiprocessing import Process, Pipe

class CustomClass:
    pass

def work(connention):
    while True:
        instance = connention.recv()
        if instance:
            print("CHLD: {}".format(instance))
        else:
            return

def main():
    parent_conn, child_conn = Pipe()
    child = Process(target=work, args=(child_conn,))
    for item in (42, "khai", {"huy" : 4}, CustomClass(), None):
        print("PRNT: send {}:".format(item))
        parent_conn.send(item)

    child.start()
    child.join()

if __name__ == "__main__":
    main()