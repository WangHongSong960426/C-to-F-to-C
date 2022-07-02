x = input('你是要華氏轉攝氏,還是攝氏轉華氏? ')
if x == '華氏轉攝氏' :
    f = input('請問現在的華氏溫度? ')
    f = float(f)
    c = (f - 32) * 5 / 9
    print('攝氏溫度為: ', c)
if x == '攝氏轉華氏' :
    c = input('請問現在的攝氏溫度? ')
    c = float(c)
    f = c * 9 / 5 + 32
    print('華氏溫度為: ', f)