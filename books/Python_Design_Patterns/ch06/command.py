#coding:utf-8
import abc
import os

history = []

class Command(object):
    '''커맨드 인터페이스'''

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        '''커맨드를 실행하기 위한 메서드'''
        pass

    @abc.abstractmethod
    def undo(self):
        '''커맨드 실행을 취소하기 위한 메서드'''
        pass


class LsCommand(Command):
    '''유닉스 명령어 ls를 흉내내는 실제 커맨드'''

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        '''리시버로의 호출을 델리게이트하는 커맨드'''
        self.receiver.show_current_dir()

    def undo(self):
        '''ls 커맨드는 취소할 수 없다.'''
        pass


class LsReceiver(object):
    def show_current_dir(self):
        '''리시버는 어떻게 커맨드를 실행해야 하는지 알고 있다'''

        cur_dir = './'

        filenames = []
        for filename in os.listdir(cur_dir):
            if os.path.isfile(os.path.join(cur_dir, filename)):
                filenames.append(filename)

        print 'Content of dir: ', ' '.join(os.path.join(filenames))


class TouchCommand(Command):
    '''유닉스 명령어 touch를 흉내내는 실제 명령어 동작'''
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.create_file()

    def undo(self):
        self.receiver.delete_file()


class TouchReceiver(object):
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        '''유닉스 touch 명령어의 실제 구현'''
        with file(self.filename, 'a'):
            os.utime(self.filename, None)

    def delete_file(self):
        '''유닉스 명령어 touch 실행 취소. 여기선 간단히 파일을 삭제한다.'''
        os.remove(self.filename)


class RmCommand(Command):
    '''유닉스 명령어 rm를 흉내내는 실제 명령어 동작'''
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_file()

    def undo(self):
        self.receiver.undo()


class RmReceiver(object):
    def __init__(self, filename):
        self.filename = filename
        self.backup_name = None

    def delete_file(self):
        '''백업을 만드는 식으로 파일을 삭제하고 실행 취소 메소드에 저장한다.'''
        self.backup_name = '.' + self.filename
        os.rename(self.filename, self.backup_name)

    def undo(self):
        '''삭제한 파일을 되살린다.'''
        original_name = self.backup_name[1:]
        os.rename(self.backup_name, original_name)
        self.backup_name = None


class Invoker(object):
    def __init__(self, create_file_commands, delete_file_commands):
        self.create_file_commands = create_file_commands
        self.delete_file_commands = delete_file_commands
        self.history = []

    def create_file(self):
        print 'Creating file...'

        for command in self.create_file_commands:
            command.execute()
            self.history.append(command)

        print 'File created.\n'

    def delete_file(self):
        print 'Deleting file...'
        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)
        print 'File deleted.\n'

    def undo_all(self):
        print 'Undo all...'
        for command in reversed(self.history):
            command.undo()

        print 'Undo all finished.'


if __name__ == '__main__':
    # 클라이언트
    # 현재 디렉토리 파일을 표시한다.
    ls_receiver = LsReceiver()
    ls_command = LsCommand(ls_receiver)

    # 파일 생성
    touch_receiver = TouchReceiver('test_file')
    touch_command = TouchCommand(touch_receiver)

    # 생성한 파일 삭제
    rm_receiver = RmReceiver('test_file')
    rm_command = RmCommand(rm_receiver)

    create_file_commands = [ls_command, touch_command, ls_command]
    delete_file_commands = [ls_command, rm_command, ls_command]

    invoker = Invoker(create_file_commands, delete_file_commands)

    invoker.create_file()
    invoker.delete_file()
    invoker.undo_all()