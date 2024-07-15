queue = []

def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        output = "The line is currently: " + " ".join(f"{position}. {person}" for position, person in enumerate(queue, start=1))
        print(output)

def take_a_number(queue, person, print_line_status=False):
    queue.append(person)
    print(f"Welcome, {person}. You are number {len(queue)} in line.")
    if print_line_status:
        line(queue)

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        # person = queue.pop(0)
        print(f'Currently serving {queue.pop(0)}.')
