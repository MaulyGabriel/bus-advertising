import os

from time import strftime, sleep, localtime


class Advertising:

    def __init__(self):

        self.upgrade = strftime('%a', localtime())
        self.hour = strftime('%H', localtime())

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
        self.update_video()
        os.system('vlc -f --repeat video.mp4')


if __name__ == '__main__':
    a = Advertising()
    a.run_video()
