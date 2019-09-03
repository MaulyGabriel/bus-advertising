import os

from time import strftime, sleep, localtime


class Advertising:

    def __init__(self):

        self.upgrade = strftime('%a', localtime())
        self.hour = strftime('%H', localtime())
        self.command = 'vlc -f --repeat video.mp4'

    @staticmethod
    def send_video():
        os.system('git commit -m "update video on repository" ')

    def update_video(self):

        if self.upgrade == 'Fri':

            if self.hour == '24':
                os.system('git pull')
                sleep(5)
            else:
                print(self.hour)
                print('No updates for today')
        else:
            print('No updates for today')

    def run_video(self):
        os.system(self.command)


if __name__ == '__main__':
    a = Advertising()
    a.update_video()
