head = '\U0000259B'
head1 = '\U00002580'
top = '\U00002582'
lower = '\U00002584'
quart = '\U00002586'
L = '\U00002599'
head2 = '\U0000258D'
block = '\U00002588'
line = '\U0000258C'
knight = '\U0000259C'
lower2 = '\U00002582'
space4 = '       '
space3 = '     '
space2 = '    '
space1 = '   '
# s = ' ' + top + '\n' + 3 * block + '\n' +  head + 2 * head1 + '\n' + head + 2 * head1
s = space4 + ' ' + top + '\n' + space4 + 3 * block + '\n' + space4 + L +  2 * lower + '\n' + space4 + block + lower + '\n' + space3 + lower +  5 * block + head1 + line + '\n' + knight + 2 * lower2  + 2 * quart + 5 * block + '\n'
#s += space3 + 2 * block + '' + 3 * block + '\n'
s += space3 + head + 2 * head1 + head + '\n'
s += space3 + 2 * head1 + ' ' + 2 * head1

part1 = space4 + ' ' + top + '\n' + space4 + 3 * block + '\n' + space4 + L +  2 * lower + '\n'
part2 = space4 + block + lower + '\n' + space3 + lower +  5 * block + head1 + line + '\n' + knight + 2 * lower2  + 2 * quart + 5 * block + '\n'
part3_1 = space3 + head + 2 * head1 + head + '\n' + space3 + 2 * head1 + ' ' + 2 * head1
part3_2 = space2 + head + 4 * head1 + head + '\n' + space2 + 2 * head1 + '   ' + 2 * head1
lines = 10 * ['']
lines[0] = space4 + ' ' + top
lines[1] = space4 + 3 * block
lines[2] = space4 + L +  2 * lower
lines[3] = space4 + block + lower
lines[4] = space3 + lower +  5 * block + head1 + line
lines[5] = knight + 2 * lower2  + 2 * quart + 5 * block
lines[6] = space3 + head + 2 * head1 + head
lines[7] = space3 + 2 * head1 + ' ' + 2 * head1
lines[8] = space2 + head + 4 * head1 + head
lines[9] = space2 + 2 * head1 + '   ' + 2 * head1
s = ""
for i in range(10):
	if i == 6 or i == 7:
		continue
	s += lines[i] + '\n'
print(s)

cactus = '\U0001F335'
print(cactus + '\n' + cactus)
