from app.main import main, synonymize

if __name__ == '__main__':
    x = threading.Thread(target=synonymize)
    x.start()
    app.run()