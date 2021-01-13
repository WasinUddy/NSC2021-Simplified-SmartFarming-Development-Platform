import random
'''import pygame
import string

pygame.init()

screen = pygame.display.set_mode((300, 300))
intermediate = pygame.surface.Surface((300, 300))
i_a = intermediate.get_rect()
x1 = i_a[0]
x2 = x1 + i_a[2]
a, b = (255, 49, 255), (69, 21, 220)
y1 = i_a[1]
y2 = y1 + i_a[3]
h = y2 - y1
rate = (float((b[0] - a[0]) / h),
        (float(b[1] - a[1]) / h),
        (float(b[2] - a[2]) / h)
        )
for line in range(h):
    color = (min(max(a[0] + (rate[0] * line), 0), 255),
             min(max(a[1] + (rate[1] * line), 0), 255),
             min(max(a[2] + (rate[2] * line), 0), 255)
             )
    pygame.draw.line(intermediate, color, (x1, line), (x2, line))

clock = pygame.time.Clock()
quit = False
word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
u = 0
d = 3
while not quit:
    quit = pygame.event.get(pygame.QUIT)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                if u > 0:
                    u -= 1
                    d -= 1
                else:
                    pass
            if e.button == 5:
                if d < len(word):
                    u += 1
                    d += 1
                else:
                    pass

    screen.blit(intermediate, (0, 0))
    test = word[u:d]
    pygame.draw.rect(screen, (100, 100, 100), (280, 20 * u, 20, 300 - 20 * (len(word) - len(test))))
    font = pygame.font.SysFont('arial', 20)
    for w in range(len(test)):
        text = font.render(test[w], 1, (0, 0, 0))
        screen.blit(text, (0, 20 * (w + 1)))

    pygame.display.flip()
    clock.tick(60)
'''

'''mylist = ['1']
y = [len(x) for i, x in enumerate(mylist)]
prmylist[y.index(max(y))])
'''
'''
L = ['asdasddas', 'amsfeu', 'meushgo', 'mugo0', 'george is found']
pr'type here: ')
prlist.index(input()))
'''
def quick_sort(sequence, start=0):
    if start == '':
        start = 0
    number_list = [x for x in sequence if isinstance(x, int)]
    alphabets_list = [x for x in sequence if not isinstance(x, int)]
    num = [x for x in alphabets_list if x.isnumeric()]
    alphabets_list = [ele for ele in alphabets_list if ele not in num]
    number_list += [int(x) for x in num]
    special_alphabets = []
    secondary_special_alphabets = []

    for item in alphabets_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(item.lower())[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(start)[:] in str(item):
            secondary_special_alphabets.append(item)
        elif str(start)[:] in str(item.lower()):
            secondary_special_alphabets.append(item)
    alphabets_list = [ele for ele in alphabets_list if ele not in special_alphabets + secondary_special_alphabets]

    length = len(number_list)
    if length <= 1:
        return special_alphabets + secondary_special_alphabets + alphabets_list + number_list
    else:
        pivot = number_list.pop()

    special = []
    item_greater = []
    item_lower = []

    for item in number_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special.append(item)
        elif item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    if str(pivot)[:len(str(start))] == str(start)[:]:
        return [pivot] + alphabets_list + quick_sort(item_lower) + quick_sort(item_greater)

    return sorted(special_alphabets) + sorted(secondary_special_alphabets) + quick_sort(special) + alphabets_list + quick_sort(item_lower) + [pivot] + quick_sort(item_greater)


'''print(quick_sort(['text0','text1','text2','text3','text10','text20','text11']))
'''
'''s = '12abcd405'
result = ''.join([i for i in s if not i.isdigit()])
'''
list_name = ['text0','text1','text2','text3','text10','text20','text11']

#lambda x: float(x[4:]
'''def intinstr(L):
    for x in L:
        for i, c in enumerate(x):
            if c.isdigit():
                return [].append()



list_name.sort(key=intinstr)
print(list_name)
'''

l = [1,2,3,4]
w = []
for amount in l:
    w.append(50)

print(w)