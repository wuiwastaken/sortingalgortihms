import random as rand
from Workspace.algorithms import *
import time
import tracemalloc

from fontTools.merge.util import current_time

#istenen bilgileri alma
desired_length = int(input("enter the length of the list (n): "))
desired_algorithm = str(input("enter the algorithm that you want to sort with (type 'help' for list): "))

#istenen listeyi oluşturma ve karıştırma
list_unsorted = []
list_sorted = []

counter = 0
while counter < desired_length:    #listeye elemanları ekleme
    list_unsorted.append(counter)
    counter += 1

rand.shuffle(list_unsorted)    #listeyi karşıtırma

#eldeki rastgele listeyi yazdır
print("unsorted list is: ", list_unsorted)

#bellek ve süre sayaçlarını başlat
start_time = time.time()
tracemalloc.start()

#girilen algoritma türünü işleme
if desired_algorithm == "bogo":
    list_sorted = bogo_sort(list_unsorted)
elif desired_algorithm == "bubble":
    list_sorted = bubble_sort(list_unsorted)
elif desired_algorithm == "selection":
    list_sorted = selection_sort(list_unsorted)
elif desired_algorithm == "merge":
    list_sorted = merge_sort(list_unsorted)
elif desired_algorithm == "quick":
    list_sorted = quick_sort(list_unsorted)
elif desired_algorithm == "heap":
    list_sorted = heap_sort(list_unsorted)
elif desired_algorithm == "radix":
    list_sorted = radix_sort(list_unsorted)
elif desired_algorithm == "shell":
    list_sorted = shell_sort(list_unsorted)
elif desired_algorithm == "counting":
    list_sorted = counting_sort(list_unsorted)
elif desired_algorithm == "help":   #"help" yazılırsa algoritma listesini çıkar
    print("bogo, \nbubble, \nselection, \nmerge, \nquick, \nheap, \nradix, \nshell, \ncounting")
else:
    print("enter a valid algorithm type (consider typing 'help' for a list of algorithms)")   #bilinmeyen algoritma türü girilirse hata ver

#sayaçların bitişi
end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

#sonuçların çıktısı
print(f"sorted list is: {list_sorted}")
print(f"{desired_algorithm} sort took {end_time - start_time:.5f} seconds")
print(f"current memory usage: {current_memory / 1024:.2f} KB, peak memory usage: {peak_memory / 1024:.2f} KB")
