import os
import matplotlib.pyplot as plt

# Paths
DATA_DIR = 'data'
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.txt')
ASSIGNMENTS_FILE = os.path.join(DATA_DIR, 'assignments.txt')
SUBMISSIONS_FILE = os.path.join(DATA_DIR, 'submissions.txt')

# Load students
def load_students():
    students = {}
    with open(STUDENTS_FILE, 'r') as f:
        for line in f:
            name, sid = line.strip().rsplit(' ', 1)
            students[name] = sid
    return students

# Load assignments
def load_assignments():
    assignments = {}
    with open(ASSIGNMENTS_FILE, 'r') as f:
        for line in f:
            name, points, aid = line.strip().rsplit(' ', 2)
            assignments[name] = {'points': int(points), 'id': aid}
    return assignments

# Load submissions
def load_submissions():
    submissions = {}
    with open(SUBMISSIONS_FILE, 'r') as f:
        for line in f:
            sid, aid, percent = line.strip().split()
            if aid not in submissions:
                submissions[aid] = []
            submissions[aid].append((sid, float(percent)))
    return submissions

# Option 1 - Student Grade
def student_grade(name, students, assignments, submissions):
    if name not in students:
        print("Student not found")
        return
    sid = students[name]
    total_earned = 0
    total_points = 0
    for aname, info in assignments.items():
        aid = info['id']
        points = info['points']
        for s_id, percent in submissions.get(aid, []):
            if s_id == sid:
                total_earned += (percent / 100.0) * points
                break
        total_points += points
    grade = round((total_earned / total_points) * 100)
    print(f"{grade}%")

# Option 2 - Assignment Stats
def assignment_stats(aname, assignments, submissions):
    if aname not in assignments:
        print("Assignment not found")
        return
    aid = assignments[aname]['id']
    scores = [percent for _, percent in submissions.get(aid, [])]
    if not scores:
        print("No submissions found.")
        return
    print(f"Min: {int(min(scores))}%")
    print(f"Avg: {int(sum(scores) / len(scores))}%")
    print(f"Max: {int(max(scores))}%")

# Option 3 - Histogram
def assignment_graph(aname, assignments, submissions):
    if aname not in assignments:
        print("Assignment not found")
        return
    aid = assignments[aname]['id']
    scores = [percent for _, percent in submissions.get(aid, [])]
    if not scores:
        print("No submissions found.")
        return
    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(f"Score Distribution: {aname}")
    plt.xlabel("Score (%)")
    plt.ylabel("Number of Students")
    plt.show()

# Main menu
def main():
    students = load_students()
    assignments = load_assignments()
    submissions = load_submissions()

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("\nEnter your selection: ").strip()

    if choice == '1':
        name = input("What is the student's name: ").strip()
        student_grade(name, students, assignments, submissions)
    elif choice == '2':
        name = input("What is the assignment name: ").strip()
        assignment_stats(name, assignments, submissions)
    elif choice == '3':
        name = input("What is the assignment name: ").strip()
        assignment_graph(name, assignments, submissions)
    else:
        print("Invalid selection.")

if __name__ == '__main__':
    main()
