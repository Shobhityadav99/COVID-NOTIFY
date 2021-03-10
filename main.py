from plyer import notification

def notifyMe(title,message):
    notification.notify(
        title=title,
        message =message,
        app_icon="F:\PythonProjects\COVID NOTIFY\icon.ico",
        timeout=10
    )

if __name__ == '__main__':
    notifyMe("Shobhit","What is this")