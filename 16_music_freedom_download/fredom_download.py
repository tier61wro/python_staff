# script for downloading mp3 files with fredom_music
# url example: https://audio.rferl.org/RU/2018/06/09/20180609-190500-RU081-program_hq.mp3?download=1
import urllib3
from typing import Dict
import datetime
from time import sleep


def create_url(p_date):
    (y, m, d) = (str(p_date)).split('-')
    url = f'https://audio.rferl.org/RU/{y}/{m}/{d}/{y}{m}{d}-190500-RU081-program.mp3?download=1'
    #print(url)
    return url


def download_file(url, p_date):
    file_name = f'freedom_music_{str(p_date).replace("-","_")}.mp3'
    print(file_name)
    print(url)
    with urllib3.PoolManager() as http:
        r = http.request('GET', url)
        with open(file_name, 'wb') as fout:
            fout.write(r.data)


def main() -> Dict[str, str]:
    beginning_date = datetime.date(2016, 12, 31)
    programs_number = 40 #  how much files we want download
    for i in range(20, programs_number + 1):
        program_date = beginning_date + datetime.timedelta(days=7*i)
        print(f'downloading={i} file for date {program_date}')
        url = create_url(program_date)
        download_file(url, program_date)
        sleep(1)


if __name__ == '__main__':
    main()
