tasks=[]



while True:
    print("\n1. View\n2. Add\n3. Update\n4. Done\n5. Exit")
    ch = input("Choice: ")

    if ch == "1":  # View
        if not tasks: print("No tasks")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif ch == "2":  # Create
        tasks.append(input("New task: ") + " (Pending)")

    elif ch == "3":  # Update
        num = int(input("Task no: "))
        if 1 <= num <= len(tasks):
            status = "(Done)" if "(Done)" in tasks[num-1] else "(Pending)"
            tasks[num-1] = input("New text: ") + " " + status

    elif ch == "4":  # Track (Done)
        num = int(input("Task no: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = tasks[num-1].replace("(Pending)", "(Done)")

    elif ch == "5": break
