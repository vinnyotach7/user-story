from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Category, Comment, Upvote, Downvote
from .forms import UpdateProfile, CommentForm, PitchForm
from .. import db, photos
import markdown2

# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the best pitching website'
    pitches = Pitch.get_all_pitches()
    categories = Category.get_categories()
    return render_template('index.html', title=title, pitches=pitches, categories=categories)

#categories section


@main.route('/pickup/pitches')
def pick_up():
    pitches = Pitch.get_all_pitches()
    title = 'Pitch your pickup lines'
    return render_template('pickup.html', title=title, pitches=pitches)


@main.route('/interview/pitches')
def interview_pitch():
    pitches = Pitch.get_all_pitches()
    title = 'Interview Pitches'
    return render_template('interview.html', title=title, pitches=pitches)


@main.route('/promotion/pitches')
def promotion_pitch():
    pitches = Pitch.get_all_pitches()
    title = 'Promotion Pitches'
    return render_template('promotion.html', title=title, pitches=pitches)


@main.route('/product/pitches')
def product_pitch():
    pitches = Pitch.get_all_pitches()
    title = 'Product Pitches'
    return render_template('product.html', title=title, pitches=pitches)
#end of categories section


@main.route('/pitch/new/', methods=['GET', 'POST'])
@login_required
def new_pitch():

    form = PitchForm()
    if category is None:
        abort(404)

    if form.validate_on_submit():
        pitch = form.content.data, form.category_id.data
        # category_id = form.category_id.data
        new_pitch = Pitch(pitch=pitch)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form=form, category=category)


@main.route('/category/<int:id>')
def category(id):

    category = PitchCategory.query.get(id)
    category_name = PitchCategory.query.get(category_name)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
    return render_template('category.html', category=category, pitches=pitches_in_category)


@main.route('/pitch/comments/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            pitch_id=id, comment=form.comment.data, username=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('new_comment.html', comment_form=form)


@main.route('/comments/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment, extras=[
                                    "code-friendly", "fenced-code-blocks"])
    return render_template('new_comment.html', review=review, format_comment=format_comment)


@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that shows the comments of a particular pitch
    '''
    comments = Comment.get_comments(id)

    return render_template('view_comments.html', comments=comments, id=id)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
