import os

import pytube.exceptions
from pytube import YouTube


def get_bunch_list():
    bunch_string = input('Please enter the links.. ')
    raw_bunch = bunch_string.strip().split('https://www.youtube.com')
    links = []
    for link in raw_bunch[1:]:
        link = 'https://www.youtube.com' + link.strip()
        links.append(link)
    if len(links) == 0:
        return False
    return links


def get_link_list():
    links = []
    bunch = bool('y' in input('Do you want to enter a bulk of links? '))
    if bunch:
        links = get_bunch_list()
        if not links:
            return False
        return links

    while True:
        link = input('Enter the link of the Youtube video you want to download.. ')
        if link == '':
            break
        links.append(link)

    links = list(set(links))  # removing duplicate links
    return links


def get_path():
    file_path = input('Enter the path where you want to save the download.. ')
    if file_path == '':
        return False


def extract_audio():
    if 'n' in input('Do you want to extract the audio? ').lower():
        return False
    else:
        return True


def get_name(link):
    try:
        video = YouTube(link)
    except pytube.exceptions.RegexMatchError:
        return False
    try:
        name = list(video.title)
    except pytube.exceptions.VideoUnavailable:
        return False
    while True:
        try:
            name.remove('.')
        except ValueError:
            break
    name = ''.join(name)
    return name


def download(extract: bool, url, path):
    youtube = YouTube(url)
    if extract:
        audio = youtube.streams.get_audio_only()
        audio.download(path)
    else:
        video = youtube.streams.get_highest_resolution()
        video.download(path)


def convert_mp4_to_mp3(path_to_file, name):
    try:
        os.rename(f'{path_to_file}{name}.mp4', f'{path_to_file}{name}.mp3')
    except FileNotFoundError:
        try:
            os.rename(f'{path_to_file} {name}.mp4', f'{path_to_file}{name}.mp3')
        except FileNotFoundError:
            pass


def main():
    links = get_link_list()
    if not links:
        print('Stop it, get some help')
        return False
    path = get_path()
    extract = extract_audio()
    length = len(links)
    current = 0
    failed_links = []
    if extract:
        if not path:
            path = '/home/maxo/Storage/Music/'
        print('Downloading audio..')
        for link in links:
            audio_name = get_name(link)
            if not audio_name:
                failed_links.append(link)
                continue
            download(extract, link, path)
            convert_mp4_to_mp3(path, audio_name)
            current += 1
            print(f'Progress: {current}/{length}')
    else:
        if not path:
            path = '/home/maxo/Storage/Videos'
        print('Downloading video..')
        for link in links:
            video_name = get_name(link)
            if not video_name:
                failed_links.append(link)
                continue
            download(extract, link, path)
            current += 1
            print(f'Progress: {current}/{length}')
    if len(failed_links) != 0:
        print('Could not download following objects:')
        for link in failed_links:
            if not get_name(link):
                print(f'link: {link}')
                continue
            print(f'"{get_name(link)}" (link: {link})')
    else:
        print('Done!')


if __name__ == '__main__':
    main()
