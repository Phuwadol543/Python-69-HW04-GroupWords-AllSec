def group_by_signature(words: list) -> list:
    answer = set()
    result = []

    for i in range(len(words)):
        if i in answer or words[i] == '':
            continue
        
        data1 = {}
        for char in words[i]:
            if char in data1:
                data1[char] += 1
            else:
                data1[char] = 1
            # print(data1)
            
        group = []
        
        for j in range(i,(len(words))):
            if j in answer or words[j] == '':
                continue
            data2 = {}
            for char in words[j]:
                if char in data2:
                    data2[char] += 1
                else:
                    data2[char] = 1 
            if data1 == data2:
                group.append(words[j])
                answer.add(j)
                    # print(answer)
        result.append(group)
    return (result)        
        
if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
