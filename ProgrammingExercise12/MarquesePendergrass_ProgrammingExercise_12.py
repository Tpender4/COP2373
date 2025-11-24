import os
import numpy as np

# Variable for passing grade
PASSING_GRADE = 60


# function for accessing path where the grades csv is located
def get_csv_path():
    # Go up one level (to COP2373), then into ProgrammingExercise8
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, "ProgrammingExercise8", "grades.csv")

# function for loading the data that is necessary from the csv file
def load_exam_data(filename):
    # columns: First Name, Last Name, Exam1, Exam2, Exam3
    return np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        usecols=(2, 3, 4)
    )

# main program for exam statistics across all 3 exams from all 10 students
def print_statistics(exams):
    num_students, num_exams = exams.shape

    # the following is the code for each exam across the students
    print("Per-exam statistics:")
    for i in range(num_exams):
        col = exams[:, i]
        print(f"\nExam {i + 1}:")
        print(f"  Mean:  {np.mean(col):.2f}")
        print(f"  Median:{np.median(col):.2f}")
        print(f"  Std:   {np.std(col):.2f}")
        print(f"  Min:   {np.min(col):.2f}")
        print(f"  Max:   {np.max(col):.2f}")

    # the following is the code for tall the exams
    all_grades = exams.flatten()
    print("\nOverall statistics (all exams combined):")
    print(f"  Mean:  {np.mean(all_grades):.2f}")
    print(f"  Median:{np.median(all_grades):.2f}")
    print(f"  Std:   {np.std(all_grades):.2f}")
    print(f"  Min:   {np.min(all_grades):.2f}")
    print(f"  Max:   {np.max(all_grades):.2f}")

    pass_mask = exams >= PASSING_GRADE
    passes_per_exam = np.sum(pass_mask, axis=0)
    fails_per_exam = num_students - passes_per_exam

    # determines and prints whether each exam was a pass or fail
    print("\nPass/fail counts per exam (passing >= 60):")
    for i in range(num_exams):
        print(f"Exam {i + 1}: passed = {passes_per_exam[i]}, failed = {fails_per_exam[i]}")

    # total pass grades and overall pass percentage across the exams
    total_passes = np.sum(pass_mask)
    total_grades = exams.size
    overall_pass_pct = (total_passes / total_grades) * 100
    print(f"\nOverall pass percentage across all exams: {overall_pass_pct:.2f}%")

# main program for csv path and the exams and respective statistics
def main():
    csv_path = get_csv_path()
    exams = load_exam_data(csv_path)

    print("First few rows of exam data:")
    print(exams[:5])
    print()
    # statistics for exam
    print_statistics(exams)


if __name__ == "__main__":
    main()