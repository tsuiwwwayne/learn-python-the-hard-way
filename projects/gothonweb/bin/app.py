# Learn Python the Hard Way
# Exercise 50 - My First Website

import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s." % (form.greet, form.name)
        return render.index(greeting = greeting)

    # def GO_BACK(self):
    #     return render.hello_form()

if __name__ == "__main__":
    app.run()
