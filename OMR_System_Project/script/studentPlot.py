import matplotlib.pyplot as plt

# Student answers data
student_answers = {
    '1': 6,
    '2': 7,
    '3': 8,
    '4': 5,
    '5': 6,
    '6': 7,
    '7': 9,
    '8': 8,
    '9': 6,
    '10': 7
}

# Extract questions and student counts
questions = list(student_answers.keys())
student_counts = list(student_answers.values())

# Create a bar chart
plt.bar(questions, student_counts)

# Set chart title and labels
plt.title('Number of Students Who Answered Each Question Correctly')
plt.xlabel('Questions')
plt.ylabel('Number of Students')

plt.yticks(range(1, 11))


# Show the chart
plt.show()



