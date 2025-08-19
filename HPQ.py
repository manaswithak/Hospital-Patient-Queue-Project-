import heapq
from collections import deque

# Priority Queue for emergency patients (min-heap based on severity)
# Format: (priority, patient_name)
emergency_queue = []

# Normal Queue for regular patients
regular_queue = deque()

# Add patient
def add_patient():
    name = input("Enter patient name: ")
    patient_type = input("Emergency or Regular (E/R): ").lower()

    if patient_type == "e":
        priority = int(input("Enter severity (1 = most critical, higher = less critical): "))
        heapq.heappush(emergency_queue, (priority, name))
        print(f"🚨 Emergency patient {name} added with priority {priority}.")
    else:
        regular_queue.append(name)
        print(f"🩺 Regular patient {name} added to the queue.")

# Serve next patient
def serve_patient():
    if emergency_queue:
        priority, name = heapq.heappop(emergency_queue)
        print(f"➡️ Serving EMERGENCY patient: {name} (Priority {priority})")
    elif regular_queue:
        name = regular_queue.popleft()
        print(f"➡️ Serving REGULAR patient: {name}")
    else:
        print("✅ No patients in queue.")

# View all patients
def view_queue():
    print("\n--- Current Queue ---")
    if emergency_queue:
        print("🚨 Emergency Patients (by priority):")
        for priority, name in sorted(emergency_queue):
            print(f"   {name} (Priority {priority})")
    else:
        print("🚨 No emergency patients.")

    if regular_queue:
        print("🩺 Regular Patients:")
        for name in regular_queue:
            print(f"   {name}")
    else:
        print("🩺 No regular patients.")

# Estimate wait time
def estimate_wait():
    total_patients = len(emergency_queue) + len(regular_queue)
    avg_time = 10  # assume 10 minutes per patient
    print(f"⏳ Estimated wait time: {total_patients * avg_time} minutes for new patient.")

# Main program
def main():
    while True:
        print("\n==== Hospital Patient Queue ====")
        print("1. Add Patient")
        print("2. Serve Next Patient")
        print("3. View Queue")
        print("4. Estimate Wait Time")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            serve_patient()
        elif choice == "3":
            view_queue()
        elif choice == "4":
            estimate_wait()
        elif choice == "5":
            print("👋 Exiting system. Stay healthy!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
