from flask import flash, redirect, url_for, render_template

from hello import app, db
from hello.models import Message
from hello.forms import HelloForm

@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)  # 实例化模型类，创建记录
        db.session.add(message)  #  添加记录到数据库会话
        db.session.commit()  # 确认提交生效
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))  # 重定向到 index 视图
    return render_template('index.html', form=form, messages=messages)  # 最终是这条返回给前端