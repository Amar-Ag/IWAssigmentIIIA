def tof(disks, source, middle, target):
    if disks == 1:
        print('Move disk 1 from tower {} to tower {}.'.format(source, target))
        return

    tof(disks - 1, source, target, middle)
    print('Move disk {} from tower {} to tower {}.'.format(disks, source, target))
    tof(disks - 1, middle, source, target)


disks = int(input('Enter number of disks: '))
tof(disks, 'A', 'B', 'C')