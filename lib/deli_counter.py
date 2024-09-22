# Function to display the current line
def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        # Join the names without commas between them
        line_status += " ".join([f"{i+1}. {name}" for i, name in enumerate(queue)])
        print(line_status)

# Function to take a number and add a person to the line
def take_a_number(queue, name):
    queue.append(name)
    print(f"Welcome, {name}. You are number {len(queue)} in line.")

# Function to serve the next person in line
def now_serving(queue):
    if len(queue) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {queue.pop(0)}.")
