from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
POSTS_FILE = 'posts.json'

def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = load_posts()
    return render_template('blog.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/posts')
def api_posts():
    return jsonify(load_posts())

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d')
        posts = load_posts()
        new_post = {
            'title': title,
            'date': date,
            'content': content
        }
        posts.insert(0, new_post)
        save_posts(posts)
        return redirect(url_for('blog'))
    return render_template('add_post.html')

@app.route('/delete_post/<int:index>', methods=['POST'])
def delete_post(index):
    posts = load_posts()
    if 0 <= index < len(posts):
        del posts[index]
        save_posts(posts)
    return redirect(url_for('blog'))

@app.route('/clear_posts', methods=['POST'])
def clear_posts():
    save_posts([])
    return redirect(url_for('blog'))

if __name__ == '__main__':
    app.run(debug=False)

