def soluion(participant, completion): # 
        answer = ''     
        i = 0
        completion.sort()
        participant.sort()
        while i < len(completion):
                if completion[i] in participant:
                        participant.remove(completion[i])
                i += 1
        answer = participant[0]
        return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

result = soluion(participant, completion)
print(result)