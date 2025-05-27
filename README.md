📝 Static Blog Website with Flask

![Screenshot 2025-05-27 125408](https://github.com/user-attachments/assets/7cd73672-6620-4afa-83c9-c11a75b57dbc)


This project is a simple static blog web application built using Python’s Flask framework. It allows users to view blog posts, add new ones, and manage them—all using a clean and colorful interface. Posts are stored in a JSON file, making it lightweight and easy to maintain without a database.

📁 Project Structure

The project includes the following key files:
app.py – Main Flask application that defines routes and logic
posts.json – Stores blog posts in JSON format
requirements.txt – Lists Python packages required
templates/index.html – Homepage HTML template
Additional template files like blog.html, about.html, contact.html, and add_post.html may also be included in the templates folder.

🚀 Features

View all blog posts on the blog page
Add new blog posts using a form
Delete individual posts
Clear all blog posts
Responsive and colorful UI with HTML/CSS
Posts stored in a JSON file (no database required)

📁 Folder Structure
.
├── app.py
├── posts.json
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── blog.html
│   ├── about.html
│   ├── contact.html
│   └── add_post.html
└── static/
    └── styles/
        └── main.css
        
✨ Future Improvements

User authentication (login/logout)
Markdown support for writing posts
Pagination for blog posts
Upload images with posts

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
