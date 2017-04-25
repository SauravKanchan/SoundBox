# a=[]
# for i in range(90):a.append(0)
# response=a[:]
# ans=a[:]
# print("Enter your response: ")
# while True:
#     a=(input().split())
#     for i in range(1,len(a),2):
#         response[int(a[i-1][1:])-1]=(a[i])
#     if a==[]:break
#
# print("Enter your ans: ")
# while True:
#     a=(input().split())
#     for i in range(1,len(a),2):
#         ans[int(a[i-1][1:])-1]=(a[i])
#     if a==[]:break
#
# total=0
# phy=0
# chem=0
# maths=0
# for i in range(90):
#     if response[i]=='-':continue
#     if response[i]==ans[i]:total+=4
#     else:total-=1
#     if i<30:
#         if response[i] == ans[i]:
#             chem += 4
#         else:
#             chem -= 1
#     if 30<=i<60:
#         if response[i] == ans[i]:
#             maths += 4
#         else:
#             maths -= 1
#     if 60<=i:
#         if response[i] == ans[i]:
#             phy += 4
#         else:
#             phy -= 1
# print(total)
# print("Physics: ",phy)
# print("Chemistry: ",chem)
# print("Maths: ",maths)
# print("total: phy+mahts+chem",phy+maths+chem)
# '''
# Enter your response:
# Q1	1	Q31	4	Q61	3
# Q2	2	Q32	-	Q62	1
# Q3	4	Q33	1	Q63	3
# Q4	2	Q34	-	Q64	4
# Q5	3	Q35	3	Q65	1
# Q6	3	Q36	3	Q66	4
# Q7	4	Q37	-	Q67	1
# Q8	3	Q38	4	Q68	4
# Q9	2	Q39	2	Q69	2
# Q10	3	Q40	4	Q70	2
# Q11	-	Q41	-	Q71	3
# Q12	-	Q42	2	Q72	4
# Q13	2	Q43	3	Q73	2
# Q14	-	Q44	1	Q74	2
# Q15	-	Q45	4	Q75	1
# Q16	4	Q46	-	Q76	2
# Q17	1	Q47	-	Q77	4
# Q18	1	Q48	1	Q78	4
# Q19	3	Q49	3	Q79	1
# Q20	4	Q50	3	Q80	4
# Q21	2	Q51	3	Q81	2
# Q22	-	Q52	2	Q82	-
# Q23	2	Q53	2	Q83	4
# Q24	-	Q54	1	Q84	4
# Q25	1	Q55	4	Q85	1
# Q26	1	Q56	2	Q86	3
# Q27	1	Q57	3	Q87	3
# Q28	2	Q58	3	Q88	1
# Q29	3	Q59	-	Q89	3
# Q30	4	Q60	2	Q90	2
#
# Enter your ans:
# Q1	1	Q31	4	Q61	2
# Q2	2	Q32	4	Q62	1
# Q3	4	Q33	2	Q63	3
# Q4	4	Q34	3	Q64	2
# Q5	2	Q35	3	Q65	2
# Q6	4	Q36	3	Q66	4
# Q7	2	Q37	4	Q67	1
# Q8	3	Q38	1	Q68	1
# Q9	3	Q39	3	Q69	3
# Q10	2	Q40	3	Q70	2
# Q11	2	Q41	4	Q71	3
# Q12	2	Q42	2	Q72	4
# Q13	3	Q43	4	Q73	3
# Q14	2	Q44	1	Q74	1
# Q15	2	Q45	4	Q75	1
# Q16	4	Q46	2	Q76	2
# Q17	1	Q47	3	Q77	4
# Q18	3	Q48	4	Q78	4
# Q19	3	Q49	4	Q79	4
# Q20	1	Q50	4	Q80	4
# Q21	4	Q51	2	Q81	3
# Q22	3	Q52	3	Q82	2
# Q23	4	Q53	4	Q83	4
# Q24	1	Q54	2	Q84	4
# Q25	1	Q55	4	Q85	4
# Q26	1	Q56	4	Q86	3
# Q27	1	Q57	2	Q87	2
# Q28	2	Q58	1	Q88	1
# Q29	2	Q59	1	Q89	3
# Q30	1	Q60	3	Q90	4
# '''