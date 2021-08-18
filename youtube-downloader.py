from pytube import YouTube


def get_link_list():
    links = []
    while True:
        link = input('Enter the link of the Youtube video you want to download.. ')
        if link == '':
            break
        links.append(link)
    links = list(set(links))    # removing duplicate links
    return links


def get_path():
    file_path = input('Enter the path where you want to save the download.. ')
    if file_path == '':
        file_path = '/home/maxo/Storage/Music/'
    return file_path


def extract_audio():
    if 'n' in input('Do you want to extract the audio? ').lower():
        return False
    else:
        return True


def get_name(link):
    video = YouTube(link)
    name = list(video.title)
    name.remove('.')
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
    os.rename(f'{path_to_file}{name}.mp4', f'{path_to_file}{name}.mp3')


def main():
    links = get_link_list()
    path = get_path()
    extract = extract_audio()
    length = len(links)
    current = 0
    if extract:
        print('Downloading audio..')
        for link in links:
            video_name = get_name(link)
            download(extract, link, path)
            convert_mp4_to_mp3(path, video_name)
            current += 1
            print(f'Progress: {current}/{length}')
    else:
        print('Downloading video..')
        for link in links:
            download(extract, link, path)
            current += 1
            print(f'Progress: {current}/{length}')
    print('Done!')


if __name__ == '__main__':
    main()
