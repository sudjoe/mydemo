def myfun(a,b,c,name,data,add):
    '''

    :param a: for integer value
    :return: None
    '''
    print"myfuction",a,b,c
    print"myfuction", name,data,add



def myfun2(*s,**ss):
    '''

    :param a: for integer value
    :return: None
    '''
    print"myfuction",s
    print"myfuction", ss




if __name__ == '__main__':
    myfun(1, 3, 4, name=1, data=2, add=34)
    myfun2(1, 3, 4, name=1, data=2, add=34)




