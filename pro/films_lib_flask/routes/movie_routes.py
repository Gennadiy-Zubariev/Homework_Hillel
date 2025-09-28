from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from models import Media
from db_config import db
from forms import MediaForm, ReviewForm
from omdb_api import search_media

media_bp = Blueprint('media', __name__)

@media_bp.route('/add/<string:media_type>', methods=['GET', 'POST'])
def add_media(media_type):
    form = MediaForm()
    form.type.data = media_type
    if form.validate_on_submit():
        title = form.title.data
        print(f"Adding {media_type} with title: {title}")  # Дебаг
        media_data = search_media(title, media_type)
        print(f"search_media returned: {media_data}")  # Дебаг
        with current_app.app_context():
            new_media = Media(
                title=title,
                type=media_type,
                watched=False,
                description=None,
                poster_url=None
            )
            if media_data:
                new_media.title = media_data['title']
                new_media.description = media_data.get('description', None)
                new_media.poster_url = media_data.get('poster_url', None)
                print(f"Setting description: {new_media.description}")  # Дебаг
                flash(f"{media_type.capitalize()} додано з описом та постером!", 'success')
            else:
                flash('Опис або постер не знайдено. Додано тільки з назвою.', 'warning')
            db.session.add(new_media)
            try:
                db.session.commit()
                print(f"Saved to DB: title={new_media.title}, description={new_media.description}")  # Дебаг
            except Exception as e:
                db.session.rollback()
                print(f"DB Commit Error: {str(e)}")  # Дебаг
                flash('Помилка при збереженні в базу даних!', 'danger')
                return redirect(url_for('main.index'))
        return redirect(url_for('main.index'))
    return render_template('add_media.html', form=form, media_type=media_type)

@media_bp.route('/toggle_watched/<int:media_id>', methods=['POST'])
def toggle_watched(media_id):
    with current_app.app_context():
        media = Media.query.get_or_404(media_id)
        print(f"Before update: media_id={media_id}, watched={media.watched}, impressions={media.impressions!r}")  # Дебаг
        media.watched = request.form.get('watched') == 'on'
        print(f"Received: watched={request.form.get('watched')}")  # Дебаг
        try:
            db.session.commit()
            print(f"After update: media_id={media_id}, watched={media.watched}, impressions={media.impressions!r}")  # Дебаг
        except Exception as e:
            db.session.rollback()
            print(f"DB Commit Error: {str(e)}")  # Дебаг
            flash('Помилка при оновленні статусу!', 'danger')
            return redirect(url_for('main.index'))
        flash('Статус оновлено!', 'success')
    return redirect(url_for('main.index'))

@media_bp.route('/save_impressions/<int:media_id>', methods=['POST'])
def save_impressions(media_id):
    with current_app.app_context():
        media = Media.query.get_or_404(media_id)
        print(f"Saving impressions for media_id={media_id}, watched={media.watched}, current impressions={media.impressions!r}")  # Дебаг
        if media.watched:
            impressions = request.form.get('impressions', '').strip()
            media.impressions = impressions
            print(f"Saved impressions: {impressions!r}")  # Дебаг
            try:
                db.session.commit()
                print(f"After saving impressions: media_id={media_id}, impressions={media.impressions!r}")  # Дебаг
                flash('Враження збережено!', 'success')
            except Exception as e:
                db.session.rollback()
                print(f"DB Commit Error: {str(e)}")  # Дебаг
                flash('Помилка при збереженні вражень!', 'danger')
        else:
            flash('Враження можна зберігати лише для переглянутих медіа!', 'warning')
    return redirect(url_for('main.index'))

@media_bp.route('/edit_review/<int:media_id>', methods=['GET', 'POST'])
def edit_review(media_id):
    with current_app.app_context():
        media = Media.query.get_or_404(media_id)
        form = ReviewForm(impressions=media.impressions)
        if form.validate_on_submit():
            media.impressions = form.impressions.data.strip()
            try:
                db.session.commit()
                print(f"Updated impressions: {media.impressions!r}")  # Дебаг
                flash('Враження оновлено!', 'success')
            except Exception as e:
                db.session.rollback()
                print(f"DB Commit Error: {str(e)}")  # Дебаг
                flash('Помилка при оновленні вражень!', 'danger')
            return redirect(url_for('main.index'))
    return render_template('edit_review.html', form=form, media=media)

@media_bp.route('/delete/<int:media_id>')
def delete_media(media_id):
    with current_app.app_context():
        media = Media.query.get_or_404(media_id)
        try:
            db.session.delete(media)
            db.session.commit()
            flash('Медіа видалено!', 'success')
        except Exception as e:
            db.session.rollback()
            print(f"DB Commit Error: {str(e)}")  # Дебаг
            flash('Помилка при видаленні медіа!', 'danger')
    return redirect(url_for('main.index'))