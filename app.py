import os

from time import strftime, sleep, localtime


def send_video():
    os.system('git commit -m "update video on repository" ')


def update_video():
    day = strftime('%a', localtime())
    hour = strftime('%H', localtime())

    if day == 'Fri':

        if hour == '24':
            os.system('git pull')
            sleep(5)
        else:
            print(hour)
            print('No updates for today')
    else:
        print('No updates for today')


def run_video():
    update_video()
    os.system('vlc -f --repeat video.mp4')


if __name__ == '__main__':
    run_video()
