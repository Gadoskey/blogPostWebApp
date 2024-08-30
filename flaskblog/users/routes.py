from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flaskblog.models import User, Post
from flaskblog import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.users.forms import RegistrationForm, LogInForm, UpdateForm, RequestPasswordReset, PasswordReset
from flaskblog.users.utils import save_image, sendPasswordReset
from flaskblog.posts.forms import  PostForm



users = Blueprint('users', __name__)


@users.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    """flash works just like alert. it enables us to display a one time message to the user
    flash accepts a second argument which indicates if the message is a success error or so
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashedPassword)
        db.session.add(user)
        db.session.commit()
        flash("Account Created Successfully! Welcome on Board, {}".format(form.username.data), 'success')
        return redirect(url_for('users.signIn'))
    return render_template('signUp.html', title = 'Sign Up', form = form)

@users.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))  
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_password.data)
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('main.homepage'))
        else:
            flash("Invalid Email or Password!", 'danger')
    return render_template('signIn.html', title = 'Sign In', form = form)

@users.route('/sign-out')
def signOut():
    logout_user()
    return redirect(url_for('main.homepage'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_image(form.picture.data)
             # Update the user's profile image
            current_user.profile_image = picture_file
            db.session.commit()  # Commit the changes before deleting old images
            # Delete the old images
            #delete_old_images(current_user) stop deleting for now.other users have their pp deleted when a new user uploades a pp
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account Updated!", 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    userImage = url_for('static', filename='images/' + current_user.profile_image)
    return render_template('account.html', title = 'Account', userImage = userImage, form=form)
  
@users.route('/user/<string:username>')
def userPosts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('userPosts.html', posts = posts, user=user)
  
@users.route('/reset_password', methods=['GET', 'POST'])
def requestPasswordReset():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))

    form = RequestPasswordReset()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.get_reset_token(1800)
            sendPasswordReset(user)
            flash("An email has been sent to you! Follow the instructions to reset your password.", 'info')
        else:
            flash("If an account with that email exists, a reset link has been sent.", 'info')
        return redirect(url_for('users.signIn'))

    return render_template('requestPasswordReset.html', title='Reset Password', form=form)



@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def passwordReset(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash("Invalid or Expired Token!", 'warning')
        return redirect(url_for('users.requestPasswordReset'))
    form = PasswordReset()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashedPassword
        db.session.commit()
        flash("Your Password Has Been Updated! Welcome Back on Board, {}".format(user.username), 'success')
        return redirect(url_for('users.signIn'))
    return render_template('passwordReset.html', title='Reset Password', form=form)
