import pandas as pd
from openpyxl import Workbook
import cv2
from openpyxl.styles import Font, PatternFill
import  getAns
import matplotlib.pyplot as plt


image_filenames = ["Imges/ans1.jpeg", "Imges/ans2.jpeg", "Imges/ans3.jpeg", "Imges/ans4.jpeg",
                   "Imges/ans5.jpeg", "Imges/ans6.jpeg", "Imges/ans7.jpeg", "Imges/ans8.jpeg",
                   "Imges/ans9.jpeg", "Imges/ans10.jpeg"]

# Create a dictionary to store the answers for all ten questions
#ANSWER_KEY = {0: 1, 1: 2, 2: 3, 3: 0, 4: 4, 5: 1, 6: 2, 7: 3, 8: 0, 9: 4}
ANSWER_KEY = [1,2,2,4,3,4,1,3,4,2]



# Create a dataframe to store the results
results_df = pd.DataFrame(columns=["Student ID", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5",
                                    "Question 6", "Question 7", "Question 8", "Question 9", "Question 10", "Total Correct", "Score"])

# Loop over each student

#for student_id, image_filename in enumerate(image_filenames):
question_student_count = {}

for student_id in range(1, 11):
    # Get the image filename for the current student ID
    image_filename = image_filenames[student_id-1]  # Subtract 1 to get 0-based index
    
    # Load the image
    image = cv2.imread(image_filename)
    answers = getAns.getImage(image)
    

    # Calculate the total number of correct answers
    total_correct = sum([1 for i in range(10) if answers[i] == ANSWER_KEY[i]])
    
    for i in range(10):
        if answers[i] == ANSWER_KEY[i]:
            if i+1 not in question_student_count:
                question_student_count[i+1] = [student_id]
            else:
                question_student_count[i+1].append(student_id)
        else:
            pass

    print(total_correct)
    score = (total_correct/10)*100
    # Append the results to the dataframe
    results_df = results_df.append({"Student ID": student_id,
                                    "Question 1": answers[0],
                                    "Question 2": answers[1],
                                    "Question 3": answers[2],
                                    "Question 4": answers[3],
                                    "Question 5": answers[4],
                                    "Question 6": answers[5],
                                    "Question 7": answers[6],
                                    "Question 8": answers[7],
                                    "Question 9": answers[8],
                                    "Question 10": answers[9],
                                    "Total Correct": total_correct,
                                    "Score": score},
                                    ignore_index=True)

# Save the results to an Excel file
results_df.to_excel("student_info.xlsx", index=False)


##################################################################################################

#plot

# Extract questions and student counts
questions = list(range(1, 11))
student_counts = []

# Loop through the dictionary and extract student counts for each question
for question in questions:
    student_counts.append(len(question_student_count.get(question, [])))

# Create a bar chart
plt.bar(questions, student_counts)
plt.xlabel('Questions')
plt.ylabel('Number of Students')
plt.title('Number of Students who Answered Each Question Correctly')
plt.xticks(questions)  # Set x-axis ticks to match question numbers
plt.show()

