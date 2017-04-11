#coding=utf-8

stack = []

def push():
    stack.append(raw_input(' Enter new string').strip())


def pop():
    if(len(stack) == 0):
        print 'Can not pop from an empty stack'
    else:
        print 'Removed [', repr(stack.pop()), ']'


def viewStack():
    print stack

CMDs = {'u': push, 'o': pop, 'v': viewStack}


def showMenu():
    pr = '''
    push
    pop
    view
    quit

    enter choice:
    '''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\n Your picked: [%s]' % choice

            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showMenu()