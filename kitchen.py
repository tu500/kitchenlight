import time
import curses

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet.task import LoopingCall

try:
    f = open("test","w")
except:
    pass


APP_URL = '/app'

def renderForm(buttonText='Ok', parameters=None, text='', description='', url=None):
    if not parameters:
        pars = {}
    else:
        pars = parameters

    urlstring = ''
    if url:
        urlstring += ' action="%s"' % (url,)

    s = ''
    if text:
        s += '<h3>%s</h3>' % (text,)
    if description:
        s += '<p>%s</p>' % (description,)
    s =  '<form method="post"%s>' % (urlstring,)

    for k, v in pars.iteritems():
        s += '<input type="hidden" name="%s" value="%s">' % (str(k), str(v))
    s += '<input type="submit" name="submit" value="%s">' % (buttonText,)
    s += '</form>'

    return s



class App():
    name = ""
    description = ""

    paused = False
    started = False
    stopped = False

    interval = 0.1
    keyToEvent = {}
    actions = []


    def __init__(self):
        self.inittime = time.time()
        self.lasttime = self.inittime
        self.runtime = 0.0
        self.frametime = 0.0


    def loop(self):
        if self.paused or self.stopped:
            return

        if not self.started:
            self.onStart()
            self.started = True

        curtime = time.time()
        passedTime = curtime - self.lasttime
        self.lasttime = curtime
        self.frametime += passedTime
        self.runtime += passedTime

        if self.frametime >= self.interval:
            self.update(self.frametime)
            self.frametime = 0.0


    def pause(self):
        self.paused = True
    def unPause(self):
        if not self.paused:
            return
        self.lasttime = time.time()
        self.paused = False

    def stop(self):
        self.stopped = True
        self.cleanup()

    def keypress(self, k):
        try:
            self.event(self.keyToEvent[k])
        except KeyError:
            pass


    def getPage(self, request):
        s = '<html><body> <h1><a href="/">Hauptseite</a></h1> <h1>%s</h1>' % (self.name,);
        for action in self.actions:
            s += renderForm(action[0], action[1])
        s += '</html></body>';
        return s

    def webEvent(self, request):
        try:
            self.event(request.args['action'][0])
            return self.getPage(request)
        except KeyError:
            return self.getPage(request)


    def onStart(self):
        pass
    def update(self, frametime):
        pass
    def event(self, e):
        pass
    def cleanup(self):
        pass



class WebInterface(Resource):
    isLeaf = True

    def __init__(self, manager):
        Resource.__init__(self)
        self.manager = manager

    def render_GET(self, request):
        if request.path.startswith(APP_URL):
            return self.manager.getAppPage(request)
        return self.manager.getMainPage(request)

    def render_POST(self, request):
        if request.path.startswith(APP_URL):
            return self.manager.appWebEvent(request)
        return self.manager.mainWebEvent(request)


class Manager():
    nextApp = None

    def __init__(self, scr, defaultApp, apps):
        self.apps = apps
        self.scr = scr
        self.scr.keypad(1)
        self.scr.nodelay(1)
        self.currentApp = defaultApp()

    def run(self):
        lc = LoopingCall(self.loop)
        lc.start(0.01)

        resource = WebInterface(self)
        factory = Site(resource)
        reactor.listenTCP(8880, factory)
        reactor.run()

    def loop(self):
        if self.nextApp:
            self.setApp()
        self.processInput()
        self.currentApp.loop()

    def processInput(self):
        c = self.scr.getch()
        while c != -1:
            if not self.processKey(c):
                self.currentApp.keypress(c)
            c = self.scr.getch()

    def processKey(self, k):
        if k == ord('c'):
            self.changeApp(a)
            return True
        return False


    def getAppPage(self, request):
        return self.currentApp.getPage(request)

    def appWebEvent(self, request):
        return self.currentApp.webEvent(request)

    def getMainPage(self, request):
        s = '<html><body> <h1><a href="%s">Aktuelle App</a></h1> <h1>Andere App starten</h1>' % (APP_URL,);
        for index, app in enumerate(self.apps):
            s += renderForm('Ausfuehren',
                    parameters={ 'index': index, 'action': 'startapp' },
                    text=app.name,
                    description=app.description)
        s += '</html></body>';
        return s

    def mainWebEvent(self, request):
        try:
            if request.args['action'][0] == 'startapp':
                self.changeApp(self.apps[int(request.args['index'][0])])
                return "Successful"
            return self.getMainPage(request)
        except KeyError:
            return self.getMainPage(request)


    def setApp(self):
        self.currentApp.stop()
        self.currentApp = self.nextApp()
        self.nextApp = None

    def changeApp(self, nextApp):
        self.nextApp = nextApp



class a(App):
    name = "Testname"
    description = "desc"
    keyToEvent = { ord('r'): 'r', ord('a'): 'a' }
    actions = [
            ('tet', { 'action': 'thor' }),
            ('te2', { 'action': 'r' }),
            ]
    def onStart(self):
        f.write("\nstarted")
        f.flush()
    def update(self, frametime):
        f.write("\nupdate" + str(self.runtime) + str(frametime))
        f.flush()
    def event(self, e):
        f.write("\nevent" + e)
        f.flush()
    def cleanup(self):
        f.write("\ncleanup")
        f.flush()


def main(scr):
    c = Manager(scr, a, [a])
    c.run()


if __name__ == '__main__':
    curses.wrapper(main)
