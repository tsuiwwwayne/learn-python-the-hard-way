# Learn Python the Hard Way
# Exercise 50 - My First Website

import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

# so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # this is used to setup the session with starting values
        session.room = map.START
        web.seeother('/game')


class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # do you need this? Page will be stuck
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # need to fix bug here
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother('/game')


if __name__ == "__main__":
    app.run()
