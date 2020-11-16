f1=open('text1.txt',encoding='ISO-8859-1')
f2=open('text2.txt',encoding='ISO-8859-1')
c=0
l2=f2.readlines()
l1=f1.readlines()
result={}
for i in range(len(l1)):
    if l1[i] in l2:
        c+=1
result['relevant_len']=len(l1)
result['retrieved_len']=len(l2)
result['non_relevant_len']=94858-len(l1)
result['not_retrieved_len']=94858-len(l2)
result['true_positive']=c
result['false_positive']=result['retrieved_len']-c
result['false_negative']=result['relevant_len']-c
result['true_negative']=result['non_relevant_len']-result['false_positive']
result['precision']=(result['true_positive'])/(result['false_positive']+result['true_positive'])
result['recall']=result['true_positive']/(result['true_positive']+result['false_negative'])
result['f1-score']=(2*result['precision']*result['recall'])/(result['precision']+result['recall'])
result['accuracy']=(result['true_positive']+result['true_negative'])/(result['true_positive']+result['true_negative']+result['false_positive']+result['false_negative'])
print(result)
