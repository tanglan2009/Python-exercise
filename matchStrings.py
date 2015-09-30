
#
# s1 = 'atgacatgcacaagtatgcat'
# s2 ='ggcc'
# s3 = 'atgc'
# # print s1.find(s2)
# # print s1.find(s3)
# index = s1.find(s3)
# print index



def countSubStringMatch(target, key):
    count = 0
    for i in range(1, len(target)):
        if target[i-1: i + len(key)-1 ] == key:
            count += 1
    return count

def countSubStringMatchRecursive(target, key):
    index = target.find(key)
    #print index
    if index < 0:
        return 0

    else:
        return 1 + countSubStringMatchRecursive(target[index + 1:], key)


target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
target3 = 'aaaa'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key1 = 'aa'

print countSubStringMatch(target3, key1)
print countSubStringMatchRecursive(target3, key1)