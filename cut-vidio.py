import cv2

""" input nama vidio """
vidio_src = input('Path vidio: ')
vid = cv2.VideoCapture(vidio_src)

""" cek kondisi vidio """
if not vid.isOpened():
    print('Vidio tidak bisa dibuka. Pastikan path yg diberikan sudah benar')
    exit()

""" set durasi awal & akhir vidio yg akan dipotong """
duration_str = int(input('Durasi awal vidio dalam detik (int): '))
duration_end = int(input('Panjang durasi vidio dalam detik (int): '))

""" mengambil data penting pada vidio original """
frame_w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

""" menghitung durasi vidio """
time_str = int(duration_str * fps)
time_end = int(duration_end * fps) + time_str

""" setup data vidio yang akan dibuat """
src_out = 'cut.mp4'
fourcc = cv2.VideoWriter.fourcc(*'mp4v')
color_vid = True
vid_out = cv2.VideoWriter(src_out, fourcc, fps, frameSize=(frame_w, frame_h), isColor=color_vid)

count_frame = 0
while True:
    ret, frame = vid.read()

    """ kondisi ketika frame atau durasi mencapai akhir vidio """
    if not ret or count_frame > time_end:
        break

    """ kondisi ketika frame atau durasi awal mulai vidio """
    if count_frame >= time_str:
        vid_out.write(frame)
    count_frame += 1

vid.release()
vid_out.release()
cv2.destroyAllWindows()

print('Done ' + src_out)