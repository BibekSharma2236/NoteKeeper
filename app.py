from flask import Flask, render_template, request, redirect

app = Flask(__name__)
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    content = request.form.get('note')
    if content:
        notes.append(content)
    return redirect('/')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
