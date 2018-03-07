def is_anagram(list1, list2):
    alist=[]
    for letter in list1:
        if letter in list2:
            alist.append(letter)
    blist=[]    
    for letters in list2:
        if letter in list1:
            blist.append(letters)
    for item in alist:
        if blist.count(item)!=1:
            return "are not"
    return "are"
def main():
    word1=input("Enter the first string:")
    list1=list(word1)
    word2=input("Enter the second string:")
    list2=list(word2)
    print(word1,"and",word2,is_anagram(word1,word2),"anagrams.")
main()