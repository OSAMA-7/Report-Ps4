try:
    import requests
except:
    print('[-] pip install requests')
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=colorama)
except:
    print('[-] pip install colorama')
import re
def banner():
    Bb = Fore.LIGHTYELLOW_EX
    print(Bb + """
        __  __ ____   _____  ____  _   _ 
        |  \/  |___ \ / ____|/ __ \| \ | |
        | \  / | __) | |  __| |  | |  \| |
        | |\/| ||__ <| | |_ | |  | | . ` |
        | |  | |___) | |__| | |__| | |\  |
        |_|  |_|____/ \_____|\____/|_| \_|
    """, Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )",
          Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @_m3gon)              \n",
          Fore.LIGHTYELLOW_EX + "                ( Report Ps4 )\n\n" + Fore.RESET)
banner()
npsso = input('[?] Enter npsso : ')
def get_id_token_your_account():
    url_id_token = 'https://ca.account.sony.com/api/v1/oauth/token'
    headers_id_token = {
        'Host': 'ca.account.sony.com',
        'Connection': 'close',
        'Content-Length': '258',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'X-Referer-Info': 'https://my.account.sony.com/central/signin/?duid=0000000700090100153820defd7fc4430a400e2ffeba6699455315f5c9eb70a53d86f94fe793c2c7&response_type=code&client_id=e4a62faf-4b87-4fea-8565-caaabb3ac918&access_type=offline&state=94b02275bf11e90ebc875e40034a4a22eb309deb3badb29380c15574a0bdb052&service_entity=urn%3Aservice-entity%3Apsn&ui=pr&smcid=web%3Apdc&redirect_uri=https%3A%2F%2Fweb.np.playstation.com%2Fapi%2Fsession%2Fv1%2Fsession%3Fredirect_uri%3Dhttps%253A%252F%252Fio.playstation.com%252Fcentral%252Fauth%252Flogin%253Flocale%253Dar_SA%2526postSignInURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Far-sa%25252Fsupport%25252Faccount%25252F%2526cancelURL%253Dhttps%25253A%25252F%25252Fwww.playstation.com%25252Far-sa%25252Fsupport%25252Faccount%25252F%26x-psn-app-ver%3D%2540sie-ppr-web-session%252Fsession%252Fv5.5.0&auth_ver=v3&error=login_required&error_code=4165&error_description=User+is+not+authenticated&no_captcha=false&cid=efcc7a0e-12e2-48e3-b09b-296cf1d9befa',
        'X-CorrelationId': 'efcc7a0e-12e2-48e3-b09b-296cf1d9befa',
        'X-Origin-ClientId': 'e4a62faf-4b87-4fea-8565-caaabb3ac918',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DUID': '0000000700090100153820defd7fc4430a400e2ffeba6699455315f5c9eb70a53d86f94fe793c2c7',
        'Accept': '*/*',
        'Origin': 'https://my.account.sony.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://my.account.sony.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'npsso={npsso}'
    }
    data_id_token = 'grant_type=sso_cookie&scope=openid%3Aage%20openid%3Acontent_ctrl%20kamaji%3Aget_privacy_settings%20kamaji%3Aget_account_hash%20openid%3Auser_id%20openid%3Actry_code%20openid%3Alang&client_id=8c52bc6a-4ad1-43fb-bd63-4465cf818937&client_secret=bKC6jEYJ6CCXdxzr'
    try:
        req_id_token = requests.post(url_id_token, data=data_id_token, headers=headers_id_token).text
        access_id0 = re.findall('"access_token":"(.*?)"', req_id_token)
        access_id = "".join(access_id0)
        def get_id_your_account():
            url_id_account = 'https://commerce.api.np.km.playstation.net/commerce/api/v1/users/me/account/id'
            headers_id_account = {
                'Host': 'commerce.api.np.km.playstation.net',
                'Connection': 'close',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                'sec-ch-ua-mobile': '?0',
                'Authorization': f'Bearer {access_id}',
                'Accept': '*/*',
                'Origin': 'https://my.account.sony.com',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://my.account.sony.com/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9'
            }
            try:
                req_id_account = requests.get(url_id_account, headers=headers_id_account).text
                accountId0 = re.findall('"accountId":"(.*?)"', req_id_account)
                accountId = "".join(accountId0)
                def get_username_your_account():
                    url_get_username = f'https://io.playstation.com/central/auth/user/details?token={accountId}'
                    headers_get_username = {
                        'Host': 'io.playstation.com',
                        'Connection': 'close',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'sec-ch-ua-mobile': '?0',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                        'Origin': 'https://www.playstation.com',
                        'Sec-Fetch-Site': 'same-site',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Dest': 'empty',
                        'Referer': 'https://www.playstation.com/',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.9'
                    }
                    try:
                        req_get_username = requests.get(url_get_username, headers=headers_get_username).text
                        hundle0 = re.findall('"handle":"(.*?)"', req_get_username)
                        hundle = "".join(hundle0)
                        originalId0 = re.findall('"originalId":"(.*?)"', req_get_username)
                        originalId = "".join(originalId0)
                        legalCountry0 = re.findall('"legalCountry":"(.*?)"', req_get_username)
                        legalCountry = "".join(legalCountry0)
                        locale0 = re.findall('"locale":"(.*?)"', req_get_username)
                        locale = "".join(locale0)
                        dob0 = re.findall('"dob":"(.*?)"', req_get_username)
                        dob = "".join(dob0)
                        print('=====================================')
                        print('[+] Info Your Account :')
                        print(f'[+] Username New : {hundle}')
                        print(f'[+] Username of your old account : {originalId}')
                        print(f'[+] Country : {legalCountry}')
                        print(f'[+] Account birth date : {dob}')
                        print('=====================================')
                        username_target = input('[?] Enter Username Target : ')
                        while True:
                            def get_token_report():
                                url_token_report = 'https://ca.account.sony.com/api/v1/oauth/authorize?service_entity=urn%3Aservice-entity%3Apsn&response_type=token&redirect_uri=https%3A%2F%2Fonlinesafetyreport.playstation.com%2Fcc%2Fweb%2Frelease%2Fimplicit_complete.html%3Fflow%253Dstandard%2526platform%253Dweb%2526theme%253Dpc%2526parent_app%253Dbh%2526parent_origin%253Dhttps%25253A%25252F%25252Fmy.playstation.com%2526locale%253Dar-AE%2526authConfig%253Dcentral%2526targets%253D%25257B%252522items%252522%25253A%25255B%25257B%252522type%252522%25253A%252522OnlineId%252522%25252C%252522onlineId%252522%25253A%252522NAZ__COD%252522%25257D%25252C%25257B%252522type%252522%25253A%252522AboutMe%252522%25252C%252522onlineId%252522%25253A%252522NAZ__COD%252522%25257D%25255D%25257D&client_id=09d63ae3-ea6f-46b3-a35e-f6fd90577148&scope=capone%3Areport_submission%2Ckamaji%3Aactivity_feed_get_news_feed%2Ckamaji%3Acommunities%2Ckamaji%3Aget_account_hash%2Ckamaji%3Aurl_preview%2Ckamaji%3Amusic_views%2Ckamaji%3Augc%3Adistributor%2Cuser%3Aaccount.profile.get%2Cuser%3Aaccount.identityMapper%2Copenid%3Aiss%2Copenid%3Aaud%2Copenid%3Aiat%2Copenid%3Aexp%2Copenid%3Aacct_id_str%2Copenid%3Aonline_id%2Copenid%3Actry_code%2Copenid%3Alang%2Copenid%3Acomm_domain%2Copenid%3Anonce%2CgamingLoungeGroups%3Auser.mobile.get%2CgamingLoungeGroups%3Auser.web.get%2CgameMediaService%3Aconsole.gamingLounge.get%2CgamingLoungeGroups%3Auser.mobile.set%2CgamingLoungeGroups%3Auser.web.set&prompt=none&nonce=3ba9f849cf8418e4d4bfa203c8e0f0df&state=9658ea609af6ffe22876c915228af3c4'
                                headers_id_report = {
                                    'Host': 'ca.account.sony.com',
                                    'Connection': 'close',
                                    'Pragma': 'no-cache',
                                    'Cache-Control': 'no-cache',
                                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                                    'sec-ch-ua-mobile': '?0',
                                    'Upgrade-Insecure-Requests': '1',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                    'Sec-Fetch-Site': 'cross-site',
                                    'Sec-Fetch-Mode': 'navigate',
                                    'Sec-Fetch-Dest': 'iframe',
                                    'Referer': 'https://onlinesafetyreport.playstation.com/',
                                    'Accept-Encoding': 'gzip, deflate',
                                    'Accept-Language': 'en-US,en;q=0.9',
                                    'Cookie': f'npsso={npsso}'
                                }
                                try:
                                    req_id_report = requests.get(url_token_report, headers=headers_id_report).url
                                    token_report0 = req_id_report.split('access_token=')[1]
                                    token_report = token_report0.split('&')[0]
                                    def get_id_your_account_report():
                                        url_id_your_account = 'https://accounts.idmapper.api.playstation.com/api/v2/accounts/map/onlineId2accountId'
                                        headers_id_your_account = {
                                            'Host': 'accounts.idmapper.api.playstation.com',
                                            'Connection': 'close',
                                            'Content-Length': '12',
                                            'Pragma': 'no-cache',
                                            'Cache-Control': 'no-cache',
                                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                                            'Accept': '*/*',
                                            'Authorization': f'Bearer {token_report}',
                                            'sec-ch-ua-mobile': '?0',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                            'Content-Type': 'application/json; charset=UTF-8',
                                            'Origin': 'https://onlinesafetyreport.playstation.com',
                                            'Sec-Fetch-Site': 'same-site',
                                            'Sec-Fetch-Mode': 'cors',
                                            'Sec-Fetch-Dest': 'empty',
                                            'Referer': 'https://onlinesafetyreport.playstation.com/',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'en-US,en;q=0.9'
                                        }
                                        data_id_your_account = [f"{hundle}"]
                                        try:
                                            req_id_your_account = requests.post(url_id_your_account, json=data_id_your_account, headers=headers_id_your_account).text
                                            accountId_my = re.findall('"accountId":"(.*?)"', req_id_your_account)
                                            accountId_my = "".join(accountId_my)
                                            def get_info_account_target():
                                                url_info = 'https://accounts.idmapper.api.playstation.com/api/v2/accounts/map/onlineId2accountId'
                                                headers_info = {
                                                    'Host': 'accounts.idmapper.api.playstation.com',
                                                    'Connection': 'close',
                                                    'Content-Length': '12',
                                                    'Pragma': 'no-cache',
                                                    'Cache-Control': 'no-cache',
                                                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                                                    'Accept': '*/*',
                                                    'Authorization': f'Bearer {token_report}',
                                                    'sec-ch-ua-mobile': '?0',
                                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                                    'Content-Type': 'application/json; charset=UTF-8',
                                                    'Origin': 'https://onlinesafetyreport.playstation.com',
                                                    'Sec-Fetch-Site': 'same-site',
                                                    'Sec-Fetch-Mode': 'cors',
                                                    'Sec-Fetch-Dest': 'empty',
                                                    'Referer': 'https://onlinesafetyreport.playstation.com/',
                                                    'Accept-Encoding': 'gzip, deflate',
                                                    'Accept-Language': 'en-US,en;q=0.9'
                                                }
                                                data_info = [f"{username_target}"]
                                                try:
                                                    req_info = requests.post(url_info, json=data_info, headers=headers_info).text
                                                    accountId_target0 = re.findall('"accountId":"(.*?)"', req_info)
                                                    accountId_target = "".join(accountId_target0)
                                                    onlineId0 = re.findall('"onlineId":"(.*?)"', req_info)
                                                    onlineId = "".join(onlineId0)
                                                    def send_report():
                                                        done = 0
                                                        error = 0
                                                        url_send_report = 'https://gr-reporting.api.playstation.com/capone/reportCollector/api/v2/submit'
                                                        headers_send_report = {
                                                            'Host': 'gr-reporting.api.playstation.com',
                                                            'Connection': 'close',
                                                            'Content-Length': '494',
                                                            'Pragma': 'no-cache',
                                                            'Cache-Control': 'no-cache',
                                                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                                                            'Accept': '*/*',
                                                            'Authorization': f'Bearer {token_report}',
                                                            'Accept-Language': 'ar,en,ja,fr,es,de,it,nl,pt,ru,ko,zh-TW,zh-CN,fi,sv,da,no,pl,pt-BR,en-GB,tr,es-MX,fr-CA,cs,hu,el,ro,th,vi,id',
                                                            'sec-ch-ua-mobile': '?0',
                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                                            'Content-Type': 'application/json; charset=UTF-8',
                                                            'Origin': 'https://onlinesafetyreport.playstation.com',
                                                            'Sec-Fetch-Site': 'same-site',
                                                            'Sec-Fetch-Mode': 'cors',
                                                            'Sec-Fetch-Dest': 'empty',
                                                            'Referer': 'https://onlinesafetyreport.playstation.com/',
                                                            'Accept-Encoding': 'gzip, deflate'
                                                        }
                                                        data_send_report = {"platformId": '3', "sourceId": '28',
                                                                            "reportReasonId": '17',
                                                                            "reportLanguageCode": "ar",
                                                                            "reporterLanguageCode": "ar",
                                                                            "reporterAccountId": f"{accountId_my}",
                                                                            "reportTime": '1619171441944',
                                                                            "reporterDescription": "يستخدم لغة مسيه",
                                                                            "version": "2.0",
                                                                            "reporterCountryCode": f"{legalCountry}",
                                                                            "reporter": f"{hundle}",
                                                                            "item": {"creationDate": '1619171441944',
                                                                                     "ownerAccountId": f"{accountId_target}",
                                                                                     "owner": f"{onlineId}",
                                                                                     "ownerCountryCode": "sa",
                                                                                     "sourceItemId": f"{onlineId}",
                                                                                     "mimeType": "text/plain",
                                                                                     "extraInfo": {
                                                                                         "onlineId": f"{onlineId}"}}}
                                                        req_send_report = requests.post(url_send_report, json=data_send_report, headers=headers_send_report).text
                                                        if ('griefReportId') in req_send_report:
                                                            print('[+] Done Report')
                                                        else:
                                                            print('[-] Error Report')
                                                    send_report()
                                                except:
                                                    print('[-] Error Get Id Target')
                                            get_info_account_target()
                                        except Exception as xxxx:
                                            print('[-] Error Get Id My Account')
                                    get_id_your_account_report()
                                except:
                                    print('[-] Error Get Token Report')
                            get_token_report()
                    except:
                        print('[-] Error Get Info My Account')
                get_username_your_account()
            except:
                print('[-] Error Get Id My Account Malh Faedh')
        get_id_your_account()
    except:
        print('[-] Error In Get Token Your Account')
get_id_token_your_account()
