from flask import Flask, request, render_template

app = Flask(__name__)

# Sample list of tasks (can be replaced with database integration)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    user_message = request.form['user_message']
    response_message = generate_response(user_message)
    return response_message

def generate_response(user_message):
    global tasks
    # Split user message into words
    words = user_message.lower().split()
    
    # Check if the user's message contains a greeting
    greetings = ['hi', 'hello', 'hey', 'whatsapp']
    if any(word in greetings for word in words):
        response = "Hi there! How can I assist you today?"
    # Check if the user's message contains a goodbye
    elif 'bye' in words or 'goodbye' in words:
        response = "Goodbye! Have a great day."
    # Check if the user wants to add a task
    elif 'add' in words:
        # Find the index of 'add' and get the task description
        index_add = words.index('add')
        task_description = ' '.join(words[index_add + 1:])
        tasks.append(task_description)
        response = f'Added "{task_description}" to your tasks.'
    # Check if the user wants to delete a task
    elif 'delete' in words:
        # Find the index of 'delete' and get the task description
        index_delete = words.index('delete')
        task_description = ' '.join(words[index_delete + 1:])
        if task_description in tasks:
            tasks.remove(task_description)
            response = f'Deleted "{task_description}" from your tasks.'
        else:
            response = f'Task "{task_description}" not found in your tasks.'
    # If the user wants to list tasks
    elif 'list' in words and 'tasks' in words:
        if tasks:
            response = 'Your tasks:\n'
            for i, task in enumerate(tasks, start=1):
                response += f'{i}. {task}\n'
        else:
            response = 'You have no tasks.'
    # If the user's message does not match any command
    else:
        response = "I'm sorry, I didn't understand that. Please try again."

    return f'<div class="chat-message user">You: {user_message}</div><div class="chat-message chatbot">Chatbot: {response}</div>'

if __name__ == '__main__':
    app.run(debug=True)
