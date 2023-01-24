from invoke import task

@task
def pylint(ctx):
    ctx.run("pylint src", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)
