# SKAII119-TASKS
SKILLRACE  ARTIFICIAL INTELLIGENCE  DOMAIN TASKS

TASK1A-CONSTRUCT A CHATBOT 

 AI-driven task management chatbot! Simplify task organization with natural language commands. It utilizes Flask for backend development and HTML for frontend interaction. Users can interact with the chatbot through a web interface, where they can add, list, and delete tasks using natural language commands. The chatbot interprets user messages and responds accordingly, providing a user-friendly and efficient way to manage daily tasks. This project demonstrates the integration of machine learning techniques with web development to create practical AI solutions for everyday tasks.
For instance, if a user types "add", followed by the task description, the chatbot adds the task to the task list. Similarly, if the user requests to list tasks by typing "list tasks", the chatbot displays the existing tasks. Additionally, users can delete tasks by specifying "delete" followed by the task description.

TASK1B-WORD PREDICTION | PREDICT THE UPCOMING WORD 

This code utilizes artificial intelligence (AI) techniques to predict the next word in a sequence based on user input. It first preprocesses a text corpus from Shakespeare's "Hamlet" using NLTK, tokenizing and filtering out non-alphanumeric tokens. Then, it creates n-grams from the text data to capture contextual information. The create_ngrams function constructs n-grams (sequences of n words) and stores them in a dictionary. The predict_next_word function takes a context (the last two words entered by the user) and predicts the most likely next word based on the context and the n-grams generated earlier.
During execution, the user provides input, and the program predicts the next word based on the context of the input. For example, if the user types "I am going to", the program might predict "be" as the next word. This prediction is made by analyzing the frequency of occurrence of words following the given context in the training data. The program combines principles of natural language processing (NLP), data processing, and probabilistic modeling to generate accurate predictions.

TASK2-FACE RECOGNIZATION 

This task implements a basic facial recognition system using OpenCV, demonstrating how biometric technology can be applied to identify or verify a person’s identity in real-time. The program captures video from the default camera and utilizes a pre-trained Haar Cascade classifier, specifically the haarcascade_frontalface_default.xml file, which contains data for detecting frontal faces.This application of facial recognition technology, commonly used in security and law enforcement, in a straightforward and accessible manner.

TASK3-Automated Attendance System
This task demonstrates an AI-powered attendance tracking system using facial recognition. It utilizes OpenCV for real-time face detection and OpenPyXL for recording attendance in an Excel spreadsheet. The program captures video, detects faces using the haarcascade_frontalface_default.xml classifier, and records the user's ID and attendance status in attendance.xlsx. Users are prompted to enter their ID, and the system logs their presence upon detecting their face. The process continues until the 'Esc' key is pressed, saving the attendance data and closing all resources. This system provides a practical, contactless solution for automated attendance tracking.



