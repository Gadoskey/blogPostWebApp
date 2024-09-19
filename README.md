# **Gadoski Web Blog**

## **Author**

Yusuf Mustapha Opeyemi [mustopha.yusufope@gmail.com]

## ***Overview***

Gadoski Blog is a simple and dynamic web application designed for users to engage with and manage content. Built with Flask, this app allows users to create, update, delete and see others posts, as well as customize their profiles. It's equipped with features that facilitate user interaction and content management, aiming to provide a smooth and enjoyable experience.

## ***Features***

1. Post Creation: Users can create and publish posts with rich content.
2. Profile Customization: Personalize profiles with profile pictures and bios.
3. Updating Posts: Modify or update existing posts as needed.
4. Deleting Posts: Remove posts that are no longer relevant or needed.
5. Email Update: Change your email address associated with your account.
6. Username Update: Modify your username if needed.
7. Password Reset: Reset your password securely if you forget it.
8. Announcements: View important updates and announcements from the app.


## ***Technologies Used***

1. Flask: A lightweight Python web framework that powers the server-side of the application, managing routes, requests, and responses.
2. SQLAlchemy: A powerful Object Relational Mapper (ORM) used for interacting with the database, allowing seamless integration between Python code and SQL queries.
3. Jinja2: A templating engine used within Flask to render dynamic HTML content, enabling separation of logic and presentation.
4. HTML: Provides the structure for the web pages of the application.
5. CSS and Bootstrap: Used to style the application, ensuring responsiveness and a visually appealing layout across various screen sizes.
6. SQLite: Handles the database layer, storing and managing user data, posts, and other persistent information.
7. WTForms: A form-handling library used to easily manage form creation, validation, and rendering in the web app.
8. Flask-Mail: For handling email functionalities, including sending confirmation emails, password reset requests, and other notifications.

# **Installation**

## ***Prerequisites***

1. Python 3.x
2. Flask
3. SQLAlchemy
4. Other dependencies listed in `requirements.txt`

## ***Clone the Repository***

`git clone https://yourtoken@github.com/Gadoskey/blogPostWebApp.git`

## ***Navigate to the project directory***

`cd blogPostWebApp`

## ***Set Up a Virtual Environment***

`python -m venv venv`

`source venv/bin/activate`  # On Windows use `venv/Scripts/activate`

## ***Install Dependencies***

`pip install -r requirements.txt`

## ***Configuration***
1. Database Setup: Run the following commands to set up the database and apply migrations:

`flask db upgrade`

2. Environment Variables: Create a `.env` file in the root directory and add the following:

`SECRET_KEY=your_secret_key_here`

`DATABASE_URL=your_database_url_here`

# **Running the Application**

## ***Start the development server with:***

`flask run.py`

`Visit http://127.0.0.1:8000 in your web browser to view the app.`

## ***Usage***

1. Home Page: Browse recent posts and updates from the community.
2. Profile Page: Update your bio, manage your posts, and view your interaction history.
3. Creating Posts: Share your thoughts and content with the community.
4. Updating Posts: Edit existing posts to keep them current and relevant.
5. Deleting Posts: Remove posts that are outdated or no longer needed.
6. Interacting with Posts: Like and comment on posts to engage with other users.
7. Account Settings: Update your email, username, and reset your password if necessary.

## ***Contribution***

I welcome contributions to improve Gadoski Web Blog! To contribute:

1. Fork the Repository
2. Create a Branch: git checkout -b feature/YourFeature
3. Make Your Changes: Implement your feature or fix a bug.
4. Commit Your Changes: git commit -m 'Add new feature or fix'
5. Push to the Branch: git push origin feature/YourFeature
6. Open a Pull Request: Describe your changes and request a review.

## ***Acknowledgments***

1. Corey Schafer: For the explanatory videos
2. Flask: For the powerful and flexible web framework.
3. SQLAlchemy: For seamless database integration.
4. Bootstrap: For responsive and stylish UI components.

## ***Contact***

For any questions or further information, feel free to mail me @ *mustopha.yusufope@gmail.com*