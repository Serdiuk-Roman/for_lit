from flask import Flask, jsonify, request


tasks = [
    {
        "id": 1,
        "title": "learn python",
        "description": "blablabla",
        "done": False
    },
    {
        "id": 2,
        "title": "learn flask",
        "description": "foofoofoo",
        "done": False
    }
]


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/todo/api/tasks',methods=['GET'])
def todo():
    return jsonify({"tasks": tasks})


@app.route('/todo/api/task/<int:post_id>')
def show_post(post_id):
    return jsonify({"tasks": tasks[post_id - 1]})


@app.route('/todo/api/tasks', methods=['POST'])
def add_task():
    print("656666666666")
    print(request.method)
    
    content = request.get_json()
    print(content)

    print("============")
    tasks[len(tasks)] = {
        "id": len(tasks) - 1,
        "title": content["title"],
        "description": content["description"],
        # "done": False
    }
    print(tasks)
    return jsonify({"tasks": tasks[len(tasks) - 1]})

# jsonify
