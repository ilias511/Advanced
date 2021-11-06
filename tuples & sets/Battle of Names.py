number = int(input())

set_odd = set()
set_even = set()


for name in range(1,number+1):
    summary = 0
    person = input()
    for ch in person:
        summary+=ord(ch)
    final_summary = int(summary/name)
    if final_summary%2==0:
        set_even.add(final_summary)
    else:
        set_odd.add(final_summary)

if sum(set_odd)==sum(set_even):
    union = set_odd.union(set_even)
    a = ', '.join(str(s) for s in union)
    print(a)
elif sum(set_odd)>sum(set_even):
    different = set_odd.difference(set_even)
    a = ', '.join(str(s) for s in different)
    print(a)
else:
    symmetric = set_even.symmetric_difference(set_odd)
    a = ', '.join(str(s) for s in symmetric)
    print(a)