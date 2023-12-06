import pandas as pd
from tkinter import *

# create a dataframe of recommended master's courses and their prerequisites
rec_courses = pd.DataFrame({
    'name': ['Master of Science in Computer Science', 'Master of Business Administration', 'Master of Arts in Education'],
    'university': ['Stanford University', 'Harvard Business School', 'Columbia University'],
    'prerequisites': [
        {'Bachelor of Science in Computer Science': 3.5, 'Bachelor of Science in Mathematics': 3.0},
        {'Bachelor of Business Administration': 3.7, 'Bachelor of Arts in Economics': 3.5},
        {'Bachelor of Arts in Education': 3.2, 'Bachelor of Science in Psychology': 3.0}
    ]
})

# function to recommend master's courses based on bachelor's courses and grade scores
# function to recommend master's courses based on bachelor's courses and grade scores
def recommend_courses():
    bachelor_courses = bachelor_courses_entry.get().split(',')
    grade_scores = dict(course.split(':') for course in grade_scores_entry.get().split(','))
    rec_text = ''
    for i, row in rec_courses.iterrows():
        if all(course in row['prerequisites'] and float(grade_scores[course]) >= row['prerequisites'][course] for course in bachelor_courses):
            rec_text += f"{row['name']} at {row['university']}\n"
        elif all(course in row['prerequisites'] and float(grade_scores[course]) >= row['prerequisites'][course] - 0.3 for course in bachelor_courses):
            rec_text += f"{row['name']} at {row['university']} (qualified)\n"
    recommendations.delete('1.0', END)
    qualified.delete('1.0', END)
    recommendations.insert('1.0', rec_text)
    qualified.insert('1.0', rec_text)


# GUI setup
root = Tk()
root.title("Master's Course Recommender")

# bachelor's courses label and entry
bachelor_courses_label = Label(root, text="Enter Bachelor's Courses:")
bachelor_courses_label.pack()
bachelor_courses_entry = Entry(root)
bachelor_courses_entry.pack()

# grade scores label and entry
grade_scores_label = Label(root, text="Enter Grade Scores (in format 'course1:score1,course2:score2,...'):")
grade_scores_label.pack()
grade_scores_entry = Entry(root)
grade_scores_entry.pack()

# recommend button
recommend_button = Button(root, text="Recommend Master's Courses", command=recommend_courses)
recommend_button.pack()

# recommendations label and text widget
recommendations_label = Label(root, text="Recommended Master's Courses:")
recommendations_label.pack()
recommendations = Text(root, height=3, width=50)
recommendations.pack()

# qualified courses and universities label and text widget
qualified_label = Label(root, text="Qualified Courses and Universities:")
qualified_label.pack()
qualified = Text(root, height=3, width=50)
qualified.pack()

root.mainloop()
