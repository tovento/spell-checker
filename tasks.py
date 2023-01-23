from invoke import task

@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)
