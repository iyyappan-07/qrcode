import pyqrcode as pq

url="https://instagram.com/broken_heart__vj07?igshid=Mzc0YWU1OWY="
k=pq.create(url)
k.svg('qr.svg',scale=10)