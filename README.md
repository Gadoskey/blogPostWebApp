**Gadoski Web Blog**

***Author***
Yusuf Mustapha Opeyemi [mustopha.yusufope@gmail.com]

***Overview***
Gadoski Blog is a simple and dynamic web application designed for users to engage with and manage content. Built with Flask, this app allows users to create, update, delete and see others posts, as well as customize their profiles. It's equipped with features that facilitate user interaction and content management, aiming to provide a smooth and enjoyable experience.

***Features***
Post Creation: Users can create and publish posts with rich content.
Profile Customization: Personalize profiles with profile pictures and bios.
Updating Posts: Modify or update existing posts as needed.
Deleting Posts: Remove posts that are no longer relevant or needed.
Email Update: Change your email address associated with your account.
Username Update: Modify your username if needed.
Password Reset: Reset your password securely if you forget it.
Announcements: View important updates and announcements from the app.

**Installation**

***Prerequisites***
Python 3.x
Flask
SQLAlchemy
[Other dependencies listed in requirements.txt]

***Clone the Repository***
*git clone https://github.com/yourusername/gadoski-blog.git*
*cd gadoski-blog*

**Set Up a Virtual Environment**
*python -m venv venv*
*source venv/bin/activate  # On Windows use `venv\Scripts\activate`*

***Install Dependencies***
*pip install -r requirements.txt*

***Configuration***
1. Database Setup: Run the following commands to set up the database and apply migrations:
*flask db upgrade*
2. Environment Variables: Create a .env file in the root directory and add the following:
*SECRET_KEY=your_secret_key_here*
*DATABASE_URL=your_database_url_here*

**Running the Application**

***Start the development server with:***
*flask run*

Visit http://127.0.0.1:8000 in your web browser to view the app.

***Usage***
Home Page: Browse recent posts and updates from the community.
Profile Page: Update your bio, manage your posts, and view your interaction history.
Creating Posts: Share your thoughts and content with the community.
Updating Posts: Edit existing posts to keep them current and relevant.
Deleting Posts: Remove posts that are outdated or no longer needed.
Interacting with Posts: Like and comment on posts to engage with other users.
Account Settings: Update your email, username, and reset your password if necessary.

***Contribution***
I welcome contributions to improve Gadoski Web Blog! To contribute:

1. Fork the Repository
2. Create a Branch: git checkout -b feature/YourFeature
3. Make Your Changes: Implement your feature or fix a bug.
4. Commit Your Changes: git commit -am 'Add new feature or fix'
5. Push to the Branch: git push origin feature/YourFeature
6. Open a Pull Request: Describe your changes and request a review.

***Acknowledgments***
Corey Schafer: For the explanatory videos
Flask: For the powerful and flexible web framework.
SQLAlchemy: For seamless database integration.
Bootstrap: For responsive and stylish UI components.

***Contact***
For any questions or further information, feel free to reach out to:

Yusuf Mustapha Opeyemi: *mustopha.yusufope@gmail.com*
