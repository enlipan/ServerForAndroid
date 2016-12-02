
def getNetworkIp():
    import socket
    ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return  ip



class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print self.name


if __name__ == '__main__':
    student = Student('a',10)
    student.print_score()
