📌 Project Description – Hospital Patient Queue

The Hospital Patient Queue System is designed to manage patients efficiently in a hospital setting by differentiating between emergency (critical) and regular cases. It ensures that critical patients receive immediate attention while still maintaining order for regular patients.

✅ Why Use It?

Hospitals often face situations where patients arrive with varying levels of urgency.

This system helps prioritize critical patients without completely ignoring regular ones.

It reduces confusion, speeds up emergency response, and ensures fair patient handling.

🌟 Advantages

Priority Handling – Critical patients are always treated first.

Fairness – Regular patients are managed in proper order (FIFO).

Efficiency – Reduces waiting time mismanagement and improves hospital workflow.

Scalability – Can be expanded to include different departments or triage levels.

📍 Where It Can Be Used

Emergency rooms (ER) to handle accident or trauma patients.

Outpatient departments (OPD) where patients queue for general consultation.


#OUTPUT

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 1
Enter patient name: John
Emergency or Regular (E/R): R
🩺 Regular patient John added to the queue.

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 1
Enter patient name: Alice
Emergency or Regular (E/R): E
Enter severity (1 = most critical, higher = less critical): 2
🚨 Emergency patient Alice added with priority 2.

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 1
Enter patient name: Bob
Emergency or Regular (E/R): E
Enter severity (1 = most critical, higher = less critical): 1
🚨 Emergency patient Bob added with priority 1.

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 3

--- Current Queue ---
🚨 Emergency Patients (by priority):
   Bob (Priority 1)
   Alice (Priority 2)
🩺 Regular Patients:
   John

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 2
➡️ Serving EMERGENCY patient: Bob (Priority 1)

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 4
⏳ Estimated wait time: 20 minutes for new patient.

==== Hospital Patient Queue ====
1. Add Patient
2. Serve Next Patient
3. View Queue
4. Estimate Wait Time
5. Exit
Enter your choice: 5
👋 Exiting system. Stay healthy!


Clinics and small hospitals to maintain simple yet effective patient flow.

🎯 Usefulness

The system is useful for ensuring that patients in need of urgent care are prioritized while maintaining a smooth queue for all others. It improves patient satisfaction, supports better hospital management, and can be integrated with digital hospital management systems.
