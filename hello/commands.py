# 自定义 flask 命令
import click
from hello import app, db
from hello.models import Message

@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database.')