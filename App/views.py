from flask import Blueprint,render_template,request,jsonify
from .models import User
from .extentions import cache

blue = Blueprint('user',__name__)

@blue.route('/')
@cache.cached(timeout=600)   # 缓存有效时间：600s
def home():
    return render_template('index.html')

@blue.route('/blog/<int:id>')
def get_blog_id(id):
    return f'Blog id: {id}'

@blue.route('/book/list')
def book_list():
    page = request.args.get('page',default=1,type=int)
    return f'Response page: {page}'

@blue.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        action = request.form.get('vertify')
        if action == '发送验证码':
            return 'btn1'
        else:
            return 'btn2'

    return render_template('t.html')

@blue.route('/vertify',methods=['GET','POST'])
def vertify():

    return jsonify({'status':200})