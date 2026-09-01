import struct, zlib

def png(size, path):
    w = h = size
    S = size / 100.0  # svg viewBox scale
    raw = b''

    def in_circle(x, y, cx, cy, r):
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r

    def wave(x, y0, x0, x1, amp=8, half=6):
        # approximate svg q6 -8 12 0 quadratic: peak 8 up at midpoint of each 12-wide segment
        if x0 <= x <= x1:
            t = ((x - x0) % (2 * half)) / half  # 0..2
            yc = y0 - amp * (1 - abs(t - 1))
            return abs(y0 - yc - (y0 - y)) if False else abs(y - yc) <= 2.5
        return False

    for py in range(h):
        raw += b'\x00'
        for px in range(w):
            x, y = px / S, py / S
            c = (10, 17, 24, 255)  # dark bg
            if in_circle(x, y, 50, 42, 22):
                # inside eye: dark fill
                c = (10, 17, 24, 255)
                d2 = (x - 50) ** 2 + (y - 42) ** 2
                # ring stroke (r 20-22)
                if 20 * 20 <= d2 <= 22 * 22:
                    c = (47, 224, 255, 255)
                # iris r=10 solid
                if in_circle(x, y, 50, 42, 10):
                    c = (47, 224, 255, 255)
            # rain streaks (approx of the two q curves)
            if 30 <= x <= 66 and abs(y - (72 - 8 * (1 - abs(((x - 30) % 12) / 6 - 1)))) <= 2.5:
                c = (77, 184, 255, 255)
            if 34 <= x <= 58 and abs(y - (84 - 8 * (1 - abs(((x - 34) % 12) / 6 - 1)))) <= 2.5:
                c = (77, 184, 255, 179)
            raw += bytes(c)

    def chunk(t, data):
        c = struct.pack('>I', len(data)) + t + data
        return c + struct.pack('>I', zlib.crc32(t + data) & 0xFFFFFFFF)

    ihdr = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
    out = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')
    open(path, 'wb').write(out)

for s in (180, 192, 512):
    png(s, f'icon-{s}.png')
print('regenerated')
