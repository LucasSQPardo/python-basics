import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
def streaming_f():
    path =  './assets/teste.mp4'
    video = ffmpeg_streaming.input(path)
    hsl_f(video)
    dash_f(video)
    return

def dash_f(video):
   #region [Representacao por qualidade]
    _144p  = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
    _240p  = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
    _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    _1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
    _2k    = Representation(Size(2560, 1440), Bitrate(6144 * 1024, 320 * 1024))
    _4k    = Representation(Size(3840, 2160), Bitrate(17408 * 1024, 320 * 1024))
    #endregion
    dash = video.dash(Formats.h264())
    dash.representations(_144p, _240p, _360p, _480p, _720p, _1080p, _2k, _4k)
    dash.output()
    return



def hsl_f(video):
    #region [Representacao por qualidade]
    _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    #endregion
    hls = video.hls(Formats.h264())
    hls.representations(_360p, _480p, _720p)
    hls.output()

    return


def main() -> int:
    streaming_f()  
    return 0

if __name__ == '__main__':
    main()

