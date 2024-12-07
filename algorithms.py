import random

def bogo_sort(_list):
    if len(_list) <= 1:
        return _list  #tek elemanlı ya da boş liste zaten sıralıdır (yani sanırım)

    _result = _list

    while _result != sorted(_result):
        random.shuffle(_result)  #istenen liste elde edilene kadar karıştır

    return _result


def bubble_sort(_list):
    n = len(_list)
    for i in range(n):
        swapped = False
        # Daha önceden sıralanmış kısmı tekrar kontrol etmeyin
        for j in range(n - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
                swapped = True
        # Eğer hiç değişim yapılmadıysa, liste zaten sıralıdır
        if not swapped:
            break
    return _list


def selection_sort(_list):
    n = len(_list)
    for i in range(n):
        # i. sıradaki eleman için en küçük elemanı bul
        min_index = i
        for j in range(i + 1, n):
            if _list[j] < _list[min_index]:
                min_index = j
        # Sadece gerekliyse elemanları değiştir
        if min_index != i:
            _list[i], _list[min_index] = _list[min_index], _list[i]
    return _list


def merge_sort(_list):
    if len(_list) <= 1:
        return _list

    #listenin ortasını bul
    mid = len(_list) // 2

    #listenin sol ve sağ yarılarını ayır
    left_half = merge_sort(_list[:mid])
    right_half = merge_sort(_list[mid:])

    #iki yarıyı birleştir
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    #sol ve sağ yarıları karşılaştırarak sıralı birleştirme yap
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    #eğer sol yarıda kalan elemanlar varsa onları ekle
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    #eğer sağ yarıda kalan elemanlar varsa onları ekle
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def quick_sort(_list):
    if len(_list) <= 1:
        return _list

    pivot = _list[-1]  #pivot olarak son elemanı seçiyoruz
    left = []  #pivot'tan küçük elemanlar
    right = []  #pivot'tan büyük elemanlar

    #listenin tüm elemanlarını pivot ile karşılaştır
    for element in _list[:-1]:  #son eleman pivot olduğu için onu atlıyoruz
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    #pivot ile birlikte sol ve sağ listeleri birleştirerek döner
    return quick_sort(left) + [pivot] + quick_sort(right)


def heap_sort(_list):
    n = len(_list)

    # max-heap oluşturma
    for i in range(n // 2 - 1, -1, -1):
        heapify(_list, n, i)

    # sıralama işlemi
    for i in range(n - 1, 0, -1):
        # en üstteki (max) elemanı son eleman ile değiştir
        _list[i], _list[0] = _list[0], _list[i]
        # kalan elemanlarla heap'i yeniden düzenle
        heapify(_list, i, 0)

    return _list

def heapify(_list, n, i):
    largest = i  # en büyük elemanın başlangıç indeksini al
    left = 2 * i + 1  # sol çocuk
    right = 2 * i + 2  # sağ çocuk

    # eğer sol çocuk mevcutsa ve daha büyükse, en büyük olarak güncelle
    if left < n and _list[left] > _list[largest]:
        largest = left

    # eğer sağ çocuk mevcutsa ve daha büyükse, en büyük olarak güncelle
    if right < n and _list[right] > _list[largest]:
        largest = right

    # en büyük eleman, mevcut düğüm değilse, yer değiştir
    if largest != i:
        _list[i], _list[largest] = _list[largest], _list[i]
        # alt ağaç için heapify çağır
        heapify(_list, n, largest)


def radix_sort(_list):
    # en büyük sayıyı bul
    max_num = max(_list)

    # basamağın yerini belirtmek için bir yerel değişken oluştur
    exp = 1

    # en büyük sayının basamağı kadar döngü oluştur
    while max_num // exp > 0:
        counting_sort_for_radix(_list, exp)
        exp *= 10  # bir sonraki basamağa geç

    return _list

def counting_sort_for_radix(_list, exp):
    n = len(_list)
    output = [0] * n  # sıralanmış listeyi tutacak
    count = [0] * 10  # 0-9 arasındaki sayılar için sayaç

    # mevcut sayılara göre sayaçları doldur
    for i in range(n):
        index = (_list[i] // exp) % 10  # şu anki basamağı al
        count[index] += 1  # sayacı artır

    # sayaçları birikimli hale getir
    for i in range(1, 10):
        count[i] += count[i - 1]

    # sıralanmış listeyi oluştur
    for i in range(n - 1, -1, -1):
        index = (_list[i] // exp) % 10  # şu anki basamağı al
        output[count[index] - 1] = _list[i]  # sıralı listeyi doldur
        count[index] -= 1  # sayacı azalt

    # sıralı listeyi orijinal listeye kopyala
    for i in range(n):
        _list[i] = output[i]


def shell_sort(_list):
    n = len(_list)
    gap = n // 2  # başlangıç aralığı

    # gap büyüklüğünü azaltarak döngü oluştur
    while gap > 0:
        # bu iç döngü insertion sort gibi çalışır
        for i in range(gap, n):
            temp = _list[i]  # geçici olarak mevcut elemanı sakla
            j = i

            # aralıklı karşılaştırmalar yap
            while j >= gap and _list[j - gap] > temp:
                _list[j] = _list[j - gap]  # elemanları kaydır
                j -= gap

            _list[j] = temp  # geçici elemanı doğru yere yerleştir

        gap //= 2  # aralığı azalt

    return _list


def counting_sort(_list):
    max_val = max(_list)  # maksimum değeri bul
    count = [0] * (max_val + 1)  # sayım dizisini başlat
    output = [0] * len(_list)  # sıralanmış listeyi tutacak

    # mevcut sayılara göre sayaçları doldur
    for num in _list:
        count[num] += 1

    # birikimli sayım yap
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # sıralı listeyi oluştur
    for i in range(len(_list) - 1, -1, -1):
        output[count[_list[i]] - 1] = _list[i]
        count[_list[i]] -= 1  # sayacı azalt

    # sıralı listeyi orijinal listeye kopyala
    for i in range(len(_list)):
        _list[i] = output[i]

    return _list