import time

from db import TarantoolSql


def main():
    store = TarantoolSql()
    print("-----------------------")
    print("  insert")
    print(store.insert_msg(1, 2, "msg-1"))
    print(store.insert_msg(1, 3, "msg-2"))
    print(store.insert_msg(3, 4, "msg-3"))
    print(store.insert_msg(3, 5, "msg-4"))
    print(store.insert_msg(4, 2, "msg-5"))
    print(store.insert_msg(4, 3, "msg-6"))
    print(store.insert_msg(5, 2, "msg-7"))
    print(store.insert_msg(6, 3, "msg-8"))

    print("\n-----------------------")
    print("  select all")
    z = store.select_all()
    for a in z:
        print(a)

    print("\n-----------------------")
    print("  select from user 3")
    z = store.get_from(3)
    for row in z:
        print(row)

    print("\n-----------------------")
    print("  select msg to user 2")
    z = store.get_to(2)
    for row in z:
        print(row)

    print("\n-----------------------")
    print("  delete id=3..6")
    for i in range(3, 7):
        res = store.del_msg_id(i)
        print(res)

    print("\n-----------------------")
    print("  select all")
    z = store.select_all()
    for a in z:
        print(a)


if __name__ == "__main__":
    time.sleep(4)
    main()
