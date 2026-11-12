import json
# # with open("orders.json","w") as f:
# #     json.dump("salom",f)

# # 1m 

# with open("orders.json",encoding="utf-8") as f:
#     data=json.load(f) #1-shart
#     umumiy_sumlar=[]
#     for order in data:
#         narsalar=order["items"]
#         sumlar=[]

#         for narsa in narsalar:
#             summa=narsa["price"]*narsa["quantity"]
#             sumlar.append(summa)
            

            
    

#         print(f"{order['order_id']} ni umumiy summasi: {sum(sumlar)} ")
#          #2-shart
#         umumiy_sumlar.append(sum(sumlar))
#     maxi=max(umumiy_sumlar)
#     for order in data:
#         narsalar=order["items"]
#         sumlar=[]
        
#         for narsa in narsalar:
#             summa=narsa["price"]*narsa["quantity"]
#             sumlar.append(summa)
#         if sum(sumlar)== maxi:
#             print(f"bu odam: {order['customer_name']}") #3-sahrt

# with open("menu.json",encoding="utf-8") as f:
#     data=json.load(f)
#     # print(data) #1-shart

#     # 2-shart
#     # for taom in data:
#     #     if taom["category"]=="Pizza":
#     #         print(taom) 

#     # 3-shart
#     qimmati=sorted(data, key=lambda x: x["price"])
#     print(f"eng arzoni: {qimmati[0]}")
#     print(f"eng qimmati: {qimmati[-1]}")
        
# # 3-m

# with open("tickets.json") as f:
#     data=json.load(f)
    # print(data)
    # ------ 2-shart--------

    # for reys in data:
    #     if reys["from"]=="Tashkent":
    #         print(reys)

    # 3-shart
    # tartiblangan=sorted(data, key=lambda x: x["price"],reverse=True)
    # print(tartiblangan[0])
    # print(tartiblangan[-1])

    # # 4-shart
    # natija =sum(reys["seats"] for reys in data)
    # print(natija)

# 4-m

# with open("weather.json",encoding="utf-8") as f:
#     data=json.load(f)
#     # print(data)

    # issiq=max(data, key=lambda x: x["temperature"])
    # sovuq=min(data, key=lambda x: x["temperature"])

    # print(sovuq)
    # print(issiq)        

# 3-shart
    # summa=sum(shahar["temperature"] for shahar in data)
    # ortacha=summa/len(data)

    # print(ortacha)

# 5-m

# with open("students_vazifa.json",encoding="utf-8") as f:
#     data=json.load(f)
    # print(data)

# 2-shart

    # for student in data:
    #     if "Python" in student["courses"]:


    #         print(student["name"])

# 3-shart
    # new={}
    # for student in data:
    #     for kurs in student["courses"]:
    #         if kurs not in new:
    #             new[kurs]=1
    #         else:
    #             new[kurs]+=1
    # print(new)


print("yangi")




    




















