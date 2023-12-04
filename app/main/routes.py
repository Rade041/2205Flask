from flask import Blueprint, render_template
from app.models import User, Articles, Jobs, Courses
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, request, url_for, redirect
from app import db
from flask_login import login_required, current_user
from app.main.forms import ArticlesForm, JobForm, CoursesForm


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index(cat=None):
    return render_template('index.html',  title='Home')

@main.route('/aboutUs')
def aboutUs(cat=None):
    return render_template('aboutUs.html',  title='About Us')


@main.route('/product')
def product(cat=None):
    return render_template('product.html',  title='product')


@main.route('/privacyPolicy')
def privacyPolicy(cat=None):
    return render_template('privacyPolicy.html',  title='privacyPolicy')

    
@main.route('/terms')
def terms(cat=None):
    return render_template('terms.html',  title='Terms and Conditions')

    
@main.route('/pricing')
def pricing(cat=None):
    return render_template('pricing.html',  title='pricing')


@main.route ('/corporate_sponsor')
def corporate_sponsor(cat=None):
    return render_template('corporate_sponsor.html', title='corporate Sponsor')


@main.route('/faq')
def faq(cat=None):
    return render_template('faq.html',  title='faq')
    
@main.route('/blog')
def blog(cat=None):
    return render_template('blog.html',  title='blog')

@main.route('/create_article/<id>', methods=['GET', 'POST'])
def create_article(id):

    if current_user.is_authenticated:
        form = ArticlesForm()

        if request.method == 'POST':
            print(id)
            if id == '-1':
                article = Articles(
                    title=form.title.data, 
                    body=form.body.data, 
                    author_name=form.author_name.data
                    )
                db.session.add(article)
            else :
                article = Articles.query.filter_by(id=id).first()

                article.title = form.title.data
                article.author_name = form.author_name.data
                article.body = form.body.data

            db.session.commit()

            return redirect(url_for('main.articles'))
        else :

            if id != '-1':
                article = Articles.query.filter_by(id=id).first()

                form.title.data = article.title
                form.author_name.data = article.author_name
                form.body.data = article.body
            return render_template('create_article.html', form=form)
    else:
        return(redirect(url_for('auth.login')))


@main.route('/articles')
def articles():
    if current_user.is_authenticated:
        articles = Articles.query.all()
        
        return render_template('article_list.html', articles=articles)
    else:
        return(redirect(url_for('auth.login')))

@main.route('/create_jobs/<id>', methods=['GET', 'POST'])
def create_jobs(id):

    if current_user.is_authenticated:
        form = JobForm()

        if request.method == 'POST':
            
            if id == '-1':
                job = Jobs (
                    job_title = form.job_title.data,
                    salary = form.salary.data,
                    description = form.description.data,
                    location = form.location.data,
                    industry = form.industry.data,
                    sector = form.sector.data
                    )
                db.session.add(job)
            else :
                job = Jobs.query.filter_by(id=id).first()

                job.job_title = form.job_title.data
                job.salary = form.salary.data
                job.description = form.description.data
                job.location = form.location.data
                job.industry = form.industry.data
                job.sector = form.sector.data

            db.session.commit()

            return redirect(url_for('main.jobs'))
        else :

            if id != '-1':
                job = Jobs.query.filter_by(id=id).first()

                form.job_title.data = job.job_title
                form.salary.data = job.salary
                form.description.data = job.description
                form.location.data = job.location
                form.industry.data = job.industry
                form.sector.data = job.sector
            return render_template('create_jobs.html', form=form)
    else:
        return(redirect(url_for('auth.login')))

@main.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if current_user.is_authenticated:
        job_listings = Jobs.query.all()

        return render_template('jobs.html', title='Jobs', job_listings=job_listings)
    else:
        return(redirect(url_for('auth.login')))
    


@main.route('/create_course/<id>', methods=['GET', 'POST'])
def create_course(id):

    if current_user.is_authenticated:
        form = CoursesForm()

        if request.method == 'POST':
            
            if id == '-1':
                course = courses (
                    course_title = form.course_title.data,
                    leader = form.course_leader.data,
                    start_date = form.start_date.data,
                    end_date = form.end_date.data,
                    venue_name_address = form.venue_name_address.data,
                    contact_phone = form.contact_phone.data,
			        contact_email = form.contact_email.data,
			        description = form.description.data 
                    )
                db.session.add(course)
            else :
                course = courses.query.filter_by(id=id).first()

                course.title = form.course_title.data
                course.leader = form.leader.data
                course.start_date = form.start_date.data
                course.end_date = form.end_date.data
                course.name_address = form.name_address.data
                course.phone = form.phone.data
                course.contact_email = form.contact_email.data
                course.description = form.description.data	

            db.session.commit()

            return redirect(url_for('main.course_list'))
        else :

            if id != '-1':
                course = courses.query.filter_by(id=id).first()

                form.course_title.data = course.course_title
                form.leader.data = course.leader
                form.start_date.data = course.start_date
                form.end_date.data = course.end_date
                form.contact_phone.data = course.contact_phone
                form.contact_email.data = course.contact_email
            return render_template('create_course.html', form=form)
    else:
        return(redirect(url_for('auth.login')))

@main.route('/course', methods=['GET', 'POST'])
def courses():
    if current_user.is_authenticated:
        course_list = Courses.query.all()

        return render_template('course_list.html', title='Courses', course_list=course_list)
    else:
        return(redirect(url_for('auth.login')))
