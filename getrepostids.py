import os
import requests,user_agent,webbrowser
webbrowser.open("https://t.me/floTools")
print("""
▬▬▬.◙.▬▬▬
   ▂▄▄▓▄▄▂
◢◤ █▀▀████▄▄▄▄__◢◤
█▄▂█ █▄███▀▀▀▀▀▀▀╬
◥█████◤
══╩══╩══
 ╬═╬
 ╬═╬     BY : FLO 
 ╬═╬	telegram : @fllo3 
 ╬═╬	⚠️ ENJOI ⚠️
 ╬═╬
 ╬═╬☻/
 ╬═╬/▌
 ╬═╬//


""")
done = 0
session = input("Session > ")
cookies = {
    'store-idc': 'alisg',
    'store-country-code': 'om',
    'install_id': '7594427426378712848',
    'ttreq': '1' + os.getenv('a20cbacaf16923c58f17e684fe51ca34f880251f', ''),
    'tt-target-idc': 'alisg',
    'odin_tt': 'bd144278bdf76d5b64622b155023a6f1ffa4c647231aea65149a034aba4c1906e83b17b43bb5e98aad5282b168f27b6a214174110b4a3cb8e3e4415ac40f9c0191d32270622f4d05a7643f8f69ece4bc',
    'cmpl_token': 'AgQYAPO6_hfkTl25Wj0EYWddOPMzzxfoFv-6MWCiVjA',
    'sid_guard': 'f53871e7451b390e3f558d9c00a27d2f%7C1768715813%7C15552000%7CFri%2C+17-Jul-2026+05%3A56%3A53+GMT',
    'uid_tt': 'e22f62f762a7af5e26277caa27428473d0e4c1d5f85ced3ccede26224dc72c39',
    'uid_tt_ss': 'e22f62f762a7af5e26277caa27428473d0e4c1d5f85ced3ccede26224dc72c39',
    'sid_tt': f"{session}",
    'sessionid': f"{session}",
    'sessionid_ss': f"{session}",
    'tt_session_tlb_tag': 'sttt%7C1%7C9Thx50UbOQ4_VY2cAKJ9L_________-82jsARizKUpRDsX7fCJC5zr1LdA4Hi9i0kea0dA9ScIA%3D',
    'store-country-sign': 'MEIEDNAJFwATm4agg_1PMgQgubUSguVWcxal2sS2XqJ4-uFxYxASl7LZpnJTRc1wlHAEEEgUTMJqtj3CE7pJlF1FdKA',
    'store-country-code-src': 'uid',
    'tt-target-idc-sign': 'De6JUzkDLUOyKX10O6ZtoKwjC9McYNokshXvqQNA0JU1mIIaPZ8HL5cqTUqvctaZuGM8Q8XnfuXll1yQofSelsBHEM90i25a4L98XzNCsik_KouWZLj_3FGmk35ehJ5kJSkkNwIJptF2T8qV3ypYixhiIsXSyogNCHV73kBXrhOOUvR649hbLfH6483zbiDyKPLM86VPLjftCruFx2VfYs3AYuG1OSi8Zh_TrAkRk_ntOHinU3PqrUkL7gefO5YG07lqiyMJJbhxn5sPtt6EyyA9CAs84dyRCFbysn7iDmj_1L_fRii9ZHXeD1XNPB9JX3piNNL3_RAkAnnyM9T-tJHnSwLNdBej26EJgXFfzXh2kJEzNhLrqaCY2FPM60Lfndx0eFChgDlOWgpsY2maVggYJsQNCSQSVEs7TMttIdtVQ8MT_dWxvefGHyEOKn-z18ygqDz0JUtGjG496ypjMrOjd8Ti95XcWQmq-SX7waL0cABDIwv8uzVw0nN_wJ7W',
    'msToken': 'E5JX0OETBKYkSOp2vwpNTyGEouPSbztQOfFqQcUfZ2I_GEkjrqF8kZ8Oq1R5ingmaqzp-S-HZassXc-iiJrKphL3JTnYhbn_d9fefLI9hNOPAzzygKnN0b9jug==',
}

headers = {
    'Host': 'api16-normal-c-alisg.tiktokv.com',
    'rpc-persist-pyxis-policy-v-tnc': '1',
    'x-ss-dp': '1340',
    'sdk-version': '2',
    'x-tt-token': '03f53871e7451b390e3f558d9c00a27d2f01937573d21c72c92f64fbe7efd5e03bd282cc811ff8d045f0cbc982cc1e07d0af6060edd737966d30c32449616fbcb6ab99614f5c70e03f2670779668fcddb9ba4a2ccf42cf9c57c812e12d117b17a7be6--0a4e0a2063305238201708ba6171f62c804c16c69de5dbb92eba8203dd7cc24a73e4535b1220de85834edc5804bb8f8809d9dbf37a9e45a93dbb9fb200beeaaaac42a9d42bd71801220674696b746f6b-3.0.1',
    'passport-sdk-version': '-1',
    'x-tt-ultra-lite': '1',
    'x-vc-bdturing-sdk-version': '2.3.15.i18n',
    'x-tt-store-region': 'om',
    'x-tt-store-region-src': 'uid',
    'ttzip-tlb': '1',
    'user-agent': f'com.zhiliaoapp.musically.go/420004 {user_agent.generate_user_agent()}',
    'x-ladon': 'GvGJc3i/F9vMDFvNeubnSS3FjIj4HNM4PV1kH1psLQlLz06U',
    'x-khronos': '1768717591',
    'x-argus': 'sAVWwocxF2BOwJslEVod6GAbY+hdqJtnUyRrw6GVE1uUsp2DZ0NG5zIlOqe0VgqkEcCwVPIMcw5mQvLLQSdU60YxYrKg3fdYUf1QLfQffNjPCscojYbAeqTEvnlgK1l9GT4N5+Fn1oTKx830PmP3JtOEu9WEbdLK8PQBMxzafm2NTMbp2y4MIyJYE3px8nJ7dmAtCB4kpKZ9MSAOMx4qq5tod7vkwZ9fWbR3G2Nce0sT8mQBrWmltk9QBKwxbM1IWsWUztEGji7k8RazKOKUZV84jaP0taWTTGhrRNeWRi6zW74jkDQfjL/Rjs+VF+tjy9HJ3GqT4q8QVCGzUiVKbRRgYPmmGr7MB6Wue3K1o8PNOydlhwU2cHCVbH8BRLAy/oyHw/Wx7+d1yAg4p7USL5QmQkhqbAuT8GLOBsfG/UxZ8MxwTrwjwFfq8lNJysOVd2LfdcxXrCPsGyV2ahas29+mB9NCpg04JycZ+L+8iuPkOVCSW3cEpftIdu4VoGd7uGzOt2cCHhdC+QkEIm7eEG1g3KEyK9XpHW3lgO0qfpj/96d9+MhWrQrb+Gp7YOEtVtzNtvU1tZ9QU/i81KA5TovGu9S1ldTtxxASEhVdwBglPcs6ZeRwWKb/YUgO6WcbeEA=',
    'x-gorgon': '8404d0691000ca82fb70272350568718d031e661d96d8fec974e',
}

response1 = requests.get(
    'https://api16-normal-c-alisg.tiktokv.com/tiktok/v1/upvote/item/list?user_id=7594427572601324545&offset=0&count=9&scene=0&sec_user_id=MS4wLjABAAAA-zme5IoVKkHPHzqF9xRpNtOXE5GAmdBqyWY2Dakzp56madeFGzn91jmBCSYzmf_q&_rticket=1768717594261&manifest_version_code=420004&app_language=en&app_type=normal&iid=7594427426378712848&app_package=com.zhiliaoapp.musically.go&channel=googleplay&device_type=SM-G991U&language=en&host_abi=arm64-v8a&locale=en&resolution=1080*2400&openudid=b071bccccbd83710&update_version_code=420004&ac2=wifi&cdid=c5b566c2-1615-4009-8553-fc14e4d8e9b4&sys_region=US&os_api=35&timezone_name=Asia%2FMuscat&dpi=480&carrier_region=OM&ac=wifi&os=android&device_id=7589223035891729976&os_version=15&timezone_offset=14400&version_code=420004&app_name=musically_go&ab_version=42.0.4&version_name=42.0.4&device_brand=samsung&op_region=OM&ssmix=a&device_platform=android&build_number=42.0.4&region=US&aid=1340&ts=1768715713',
    cookies=cookies,
    headers=headers,
)



import json

response_text =response1.text


try:
    
    data = json.loads(response_text)
    
    if data.get("status_code") == 0:
        aweme_list = data.get("aweme_list", [])
        
        if not aweme_list:
            print("⚠️ لم يتم العثور على أي فيديوهات.")
        else:
            print(f"✅ تم العثور على {len(aweme_list)} فيديو:\n")
            
         
            video_ids = []
            
           
            for idx, video in enumerate(aweme_list, 1):
                aweme_id = video.get("aweme_id", "غير موجود")
                video_ids.append(aweme_id)
                
                # معلومات إضافية مفيدة
                #desc = video.get("desc", "")[:100]  # أول 100 حرف من الوصف
                #author = video.get("author", {}).get("nickname", "غير معروف")
                #create_time = video.get("create_time", 0)
                
                print(f"{idx}. 📹 ID: {aweme_id}")
                #print(f"   👤 المؤلف: {author}")
                #print(f"   📝 الوصف: {desc}")
                #print(f"   ⏰ وقت الإنشاء: {create_time}")
                print("-" * 50)
            
            # حفظ المعرفات في ملف نصي
            
            
            
            for i in range(len(video_ids)):
            	for vid in video_ids:
            		cookies = {
    'store-idc': 'alisg',
    'store-country-code': 'om',
    'install_id': '7594427426378712848',
    'ttreq': '1' + os.getenv('a20cbacaf16923c58f17e684fe51ca34f880251f', ''),
    'tt-target-idc': 'alisg',
    'odin_tt': 'bd144278bdf76d5b64622b155023a6f1ffa4c647231aea65149a034aba4c1906e83b17b43bb5e98aad5282b168f27b6a214174110b4a3cb8e3e4415ac40f9c0191d32270622f4d05a7643f8f69ece4bc',
    'cmpl_token': 'AgQYAPO6_hfkTl25Wj0EYWddOPMzzxfoFv-6MWCiVjA',
    'sid_guard': 'f53871e7451b390e3f558d9c00a27d2f%7C1768715813%7C15552000%7CFri%2C+17-Jul-2026+05%3A56%3A53+GMT',
    'uid_tt': 'e22f62f762a7af5e26277caa27428473d0e4c1d5f85ced3ccede26224dc72c39',
    'uid_tt_ss': 'e22f62f762a7af5e26277caa27428473d0e4c1d5f85ced3ccede26224dc72c39',
    'sid_tt': f"{session}",
    'sessionid': f"{session}" ,
    'sessionid_ss': f"{session}"  ,
    'tt_session_tlb_tag': 'sttt%7C1%7C9Thx50UbOQ4_VY2cAKJ9L_________-82jsARizKUpRDsX7fCJC5zr1LdA4Hi9i0kea0dA9ScIA%3D',
    'store-country-sign': 'MEIEDNAJFwATm4agg_1PMgQgubUSguVWcxal2sS2XqJ4-uFxYxASl7LZpnJTRc1wlHAEEEgUTMJqtj3CE7pJlF1FdKA',
    'store-country-code-src': 'uid',
    'tt-target-idc-sign': 'De6JUzkDLUOyKX10O6ZtoKwjC9McYNokshXvqQNA0JU1mIIaPZ8HL5cqTUqvctaZuGM8Q8XnfuXll1yQofSelsBHEM90i25a4L98XzNCsik_KouWZLj_3FGmk35ehJ5kJSkkNwIJptF2T8qV3ypYixhiIsXSyogNCHV73kBXrhOOUvR649hbLfH6483zbiDyKPLM86VPLjftCruFx2VfYs3AYuG1OSi8Zh_TrAkRk_ntOHinU3PqrUkL7gefO5YG07lqiyMJJbhxn5sPtt6EyyA9CAs84dyRCFbysn7iDmj_1L_fRii9ZHXeD1XNPB9JX3piNNL3_RAkAnnyM9T-tJHnSwLNdBej26EJgXFfzXh2kJEzNhLrqaCY2FPM60Lfndx0eFChgDlOWgpsY2maVggYJsQNCSQSVEs7TMttIdtVQ8MT_dWxvefGHyEOKn-z18ygqDz0JUtGjG496ypjMrOjd8Ti95XcWQmq-SX7waL0cABDIwv8uzVw0nN_wJ7W',
    'msToken': 'E5JX0OETBKYkSOp2vwpNTyGEouPSbztQOfFqQcUfZ2I_GEkjrqF8kZ8Oq1R5ingmaqzp-S-HZassXc-iiJrKphL3JTnYhbn_d9fefLI9hNOPAzzygKnN0b9jug==',
}

            		headers = {
    'Host': 'api16-normal-c-alisg.tiktokv.com',
    'rpc-persist-pyxis-policy-v-tnc': '1',
    'x-ss-dp': '1340',
    'x-ss-stub': '302A9249CE340123B0E15D34EDF5D28F',
    'sdk-version': '2',
    'x-tt-token': '03f53871e7451b390e3f558d9c00a27d2f01937573d21c72c92f64fbe7efd5e03bd282cc811ff8d045f0cbc982cc1e07d0af6060edd737966d30c32449616fbcb6ab99614f5c70e03f2670779668fcddb9ba4a2ccf42cf9c57c812e12d117b17a7be6--0a4e0a2063305238201708ba6171f62c804c16c69de5dbb92eba8203dd7cc24a73e4535b1220de85834edc5804bb8f8809d9dbf37a9e45a93dbb9fb200beeaaaac42a9d42bd71801220674696b746f6b-3.0.1',
    'passport-sdk-version': '-1',
    'x-tt-ultra-lite': '1',
    'x-vc-bdturing-sdk-version': '2.3.15.i18n',
    'x-tt-store-region': 'om',
    'x-tt-store-region-src': 'uid',
    'ttzip-tlb': '1',
    'user-agent': f'com.zhiliaoapp.musically.go/420004 {user_agent.generate_user_agent()}',
    #(Linux; U; Android 15; en_US; SM-G991U; Build/AP3A.240905.015.A2;tt-ok/3.12.13.44.lite-ul)',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-ladon': 'Oyl0Ct2O2i6+raDBLYFpp8xphYWj/LIb3X1Q1ghSrjmkh4pb',
    'x-khronos': '1768717588',
    'x-argus': 'xTKVZt3u9TSG3OWMxsUy2BAWjP1WzB6uzuZ1EmYv164CIp8we32inDrsXoNpLK0k/9YpOcXRjlnAmFpASpVr8nhQmDnMKGQJ6XgP6L3zwesBZBZyDZiNHVMdhLsu6ze8Bc8+firRq3/3i7VK7K41fX5sCdBB7WRONcpgeK/6VONcGE1QISEw8VZs3NB0Sy08V24U3qHgJ5gMmZOvMy+9KrqCrIsHOzgCyArHfnPbCgkAvOlbzXqHfegszU4Ii8YEaL02nSkCJqQE4sg11lQ7ddP5Uq76B4nsdlE382PCSh3sZzI9kafDCMCU8I+g2DtWnQUKelssBzN9KWkKtSYr3FgBHLf8gqoyEyI1zBkzIDSVeBxNSdtGvbjb+6HZE5PZJYuyRe0yWj15wedcgK4f45yiwIEeYbaVM+Y3oW8pkrB9CyDGzVFCuM8Xb8st3FyX/AdrdhXARC4dODFuZyAbnU+kaIkTO1svG2CEpWBs+1cQQjnJZ5yWNd09EUzyRfrzWsTOLRGlW+SXfiK06omM93SnVeUyCXdJHrtcxjoXKLjBstLE5U9jB1wJzymIVxbhK2zVnaCQUYE9lnU+eFp2FMWsp/dX7oN59zLzCHYNMdFaKuOE4qaH/4uNsJOmQAEgT0c=',
    'x-gorgon': '8404d04c1000359abced38d47813f6e353a96c95e145968c963b',
}

            		data = {
    'item_id': f"{vid}",
}

            		response = requests.post(
    'https://api16-normal-c-alisg.tiktokv.com/tiktok/v1/upvote/delete?_rticket=1768717590993&manifest_version_code=420004&app_language=en&app_type=normal&iid=7594427426378712848&app_package=com.zhiliaoapp.musically.go&channel=googleplay&device_type=SM-G991U&language=en&host_abi=arm64-v8a&locale=en&resolution=1080*2400&openudid=b071bccccbd83710&update_version_code=420004&ac2=wifi&cdid=c5b566c2-1615-4009-8553-fc14e4d8e9b4&sys_region=US&os_api=35&timezone_name=Asia%2FMuscat&dpi=480&carrier_region=OM&ac=wifi&os=android&device_id=7589223035891729976&os_version=15&timezone_offset=14400&version_code=420004&app_name=musically_go&ab_version=42.0.4&version_name=42.0.4&device_brand=samsung&op_region=OM&ssmix=a&device_platform=android&build_number=42.0.4&region=US&aid=1340&ts=1768715713',
    cookies=cookies,
    headers=headers,
    data=data,
)
            		if response.status_code ==200:
            			done += 1
            			print(f"done delet {done} ")
            			#os.system('cls' if os.name == "nt" else 'clear')
            			if done == len(video_ids):
            				print("done delet all repost if there are problem run script again ⚠️⚠️")
            				exit()


            
            print(f"   - هل هناك المزيد: {data.get('has_more', False)}")
            
    else:
        print(f"رسالة الخطأ: {data.get('status_msg', 'غير معروف')}")

except json.JSONDecodeError:
    print("❌ لم يتمكن من تحليل الـ response كـ JSON")
    print("تأكد من أن البيانات تأتي بالصيغة الصحيحة")
except Exception as e:
    print(f"❌ حدث خطأ غير متوقع: {str(e)}")
    