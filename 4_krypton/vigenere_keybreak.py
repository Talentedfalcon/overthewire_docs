import sys
import numpy as np

def find_key_len(cipher):
    coincidences=np.zeros(len(cipher),dtype=int)

    shift=0
    for i in cipher:
        shift+=1
        j=0
        # for i in range(shift):
        #     print(" ",end="")
        while(j+shift<len(cipher)):
            # print(cipher[j],end="")
            if(cipher[j]==cipher[j+shift]):
                coincidences[shift-1]+=1
            j+=1
        # print(f" {coincidences[shift-1]}")

    #Cleaning up coincidences such that only fairly large numbers remain
    maximum=np.max(coincidences)
    last_non_zero_index=0
    threshold=maximum-maximum/3. #try changing the threshold value to get better estimates
    # print(f"Maximum Coincidences per shift: {maximum}")
    # print(f"Chosen Threshold: {threshold}")
    # print(coincidences)
    for i in range(len(coincidences)):
        if float(coincidences[i])<threshold:
            coincidences[i]=0
        else:
            last_non_zero_index=i

    coincidences=coincidences[:last_non_zero_index+1] #Remove all trailing zeros to reduce array size
    # print(coincidences)

    probable_key_lens=np.array([],dtype=int)
    for i in range(len(coincidences)):
        if(coincidences[i]==0):
            continue
        else:
            probable_key_lens=np.append(probable_key_lens,0)
            for j in range(i+1,len(coincidences)):
                probable_key_lens[-1]+=1
                if coincidences[j]!=0:
                    # print(f"from {i}-{j} estimated key length: {probable_key_lens[len(probable_key_lens)-1]}")
                    break
            if(probable_key_lens[-1]<=1):
                probable_key_lens=probable_key_lens[:-1]

    if(len(probable_key_lens)==0):
        print("Unable to find key length (cyphertext not long enough)")
        return None
    
    # print(probable_key_lens)
    count=np.bincount(probable_key_lens)
    key_len=np.argmax(count) #Getting the mode
    return key_len

def get_key(cipher,key_len):
    #english letter frequency. According to https://www.dcode.fr/frequency-analysis
    english_frequency={
        'A':0.082,'B':0.015,'C':0.028,'D':0.043,
        'E':0.127,'F':0.022,'G':0.020,'H':0.061,
        'I':0.070,'J':0.002,'K':0.008,'L':0.040,
        'M':0.024,'N':0.067,'O':0.075,'P':0.019,
        'Q':0.001,'R':0.060,'S':0.063,'T':0.091,
        'U':0.028,'V':0.010,'W':0.024,'X':0.002,
        'Y':0.020,'Z':0.001
    }

    key=''

    #Dividing into key_len segments where each segment corresponds to each letter of the key
    for i in range(key_len):
        subset=np.unique(np.array(list(cipher[i::key_len])),return_counts=True)

        #Calculating the frequency of the segment
        subset_frequency=np.zeros((len(english_frequency.keys())))
        sum_subset=sum(subset[1])
        for j in range(len(subset[1])):
            # print(subset[0][j][0],end=" ")
            subset_frequency[ord(subset[0][j][0])-65]=float(subset[1][j]/sum_subset)
        # print()
        # print(subset_frequency)

        english_frequency_values=np.array(list(english_frequency.values()))

        max_shift={'shift':0,'value':0}
        for shift in range(0,len(english_frequency.keys())):
            #shifting the segment frequency to the left
            temp_frequency=np.roll(subset_frequency,shift=-shift)
            #theoretically maximum dot_product value only occurs when the original frequency vector and the extracted frequency vector are aligned
            #so if they are aligned then all we need to do is find the letter shift between them to extract the segment's letter
            dot_product=sum(temp_frequency*english_frequency_values)
            if(max_shift['value']<dot_product):
                max_shift['shift']=shift
                max_shift['value']=dot_product
        key+=list(english_frequency.keys())[max_shift['shift']]

    return key

cipher=''
for arg in sys.argv[1:]:
    with open(arg,"r") as file:
        cipher+="".join(file.read().strip().upper().split(" "))

key_len=find_key_len(cipher)
print(f"Estimated key length: {key_len}")

if key_len:
    key=get_key(cipher,key_len)
    print(f"Key is: {key}")