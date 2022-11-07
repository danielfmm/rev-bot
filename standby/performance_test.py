from playwright.sync_api import sync_playwright
from pushbullet import Pushbullet
import re
import json
import time

#################################

with open('profile.json') as profile_json:
    profile = json.load(profile_json)
    profile_json.close()
#################################
######## WEBSITE CONFIGS ########
#################################
URL_login = r"https://www.rev.com/account/auth/login"
URL_main = r"https://www.rev.com/workspace/mywork"
URL_find_work_sub = r"https://www.rev.com/workspace/findwork/Subtitle"
URL_find_work_grading = r"https://www.rev.com/workspace/findwork/subtitlegrade"
acc_email = profile['acc_email']
acc_pass = profile['acc_pass']
######## BUTTONS ID #############
refresh_job = '#title-and-refresh-line>div'
collapse = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div[1]/div/div/div/div'
pay_max_sort = '//*[@id="find-work-root"]/div/div[2]/div/div[2]/div/div/div[3]/div/span/span'
job_price_on_claim = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div[3]/span'
claim_button = '.project-claim-btn'
claimed_job_price = 'div.pay-info-container>div:nth-child(3)'
current_project = "text=Continue Current Project"
################################
######### FUNCTIONS ############
################################


def print_request_sent(request):
  print("Request sent: " + request.url)


def timestamp():
    return time.strftime('%H:%M:%S')


def send_push():
    # Envia aviso pelo pushbullet instalado no celular
    api_key = "o.gWJiOosLWRj38MOrRzlcKY3cxnjblvdM"
    pb = Pushbullet(api_key)
    pb.push_note('NOVA TRADUCAO!', 'Veja o valor no rev')


def login(page):
    print('Fazendo login...')
    page.goto(URL_login)
    page.fill('id=Email', acc_email)
    page.click('id=next-btn')
    page.fill('id=Password', acc_pass)
    page.click('id=login-btn')
    print('Login efetuado.')


def confirm_claim(page):
    is_on = False
    page.goto(URL_find_work_sub)

    try:
        page.click(current_project)
        is_on = True
    except:
        pass

    return is_on



excluded_resource_types = ["stylesheet", "image", "font"]
def block_aggressively(route):
    if (route.request.resource_type in excluded_resource_types):
        route.abort()
    else:
        route.continue_()



def main():
    with sync_playwright() as p:
        print('=========/REVBOT-Webkit=/========')
        browser = p.webkit.launch()
        page = browser.new_page()
        page.route("**/*", block_aggressively)
        start_time = time.time()
        page.goto(URL_main)
        login(page)
        page.goto(URL_find_work_sub)

        # page.click(popup)
        page.click(pay_max_sort)
        print(f'Tempo de execução: {(time.time() - start_time)}')


        # while True:
        #     try:
        #         page.on("request", print_request_sent())
                # if page.inner_text('//*[@id="title-and-refresh-line"]/div/h5') != 'Waiting for new jobs...':
                #     # page.on("request", print_request_sent)
                #     # assert page.title() != "Rev - Find Work"
                #     print('Projeto encontrado.')
                #     page.click(refresh_job)
                #     page.click(collapse)
                #     page.click(claim_button)
                #     print("Achou! Clicando em Claim...")
                #     assert confirm_claim(page)
                #     send_push()
                #     print("Trabalho confirmado!")
                #     print("Finalizando...")
                #     break
                # else:
                #     print(f'\r{timestamp()} ainda não', end="\r")
                #     time.sleep(0.02)
                #
            # except:
                # print("Monitorando...")
                # time.sleep(0.02)
                # pass

        input("...")
        browser.close()


for n in range(5):
    main()
from playwright.sync_api import sync_playwright
from pushbullet import Pushbullet
import re
import json
import time

#################################

with open('profile.json') as profile_json:
    profile = json.load(profile_json)
    profile_json.close()
#################################
######## WEBSITE CONFIGS ########
#################################
URL_login = r"https://www.rev.com/account/auth/login"
URL_main = r"https://www.rev.com/workspace/mywork"
URL_find_work_sub = r"https://www.rev.com/workspace/findwork/Subtitle"
URL_find_work_grading = r"https://www.rev.com/workspace/findwork/subtitlegrade"
acc_email = profile['acc_email']
acc_pass = profile['acc_pass']
######## BUTTONS ID #############
refresh_job = '#title-and-refresh-line>div'
collapse = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div[1]/div/div/div/div'
pay_max_sort = '//*[@id="find-work-root"]/div/div[2]/div/div[2]/div/div/div[3]/div/span/span'
job_price_on_claim = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div[3]/span'
claim_button = '.project-claim-btn'
claimed_job_price = 'div.pay-info-container>div:nth-child(3)'
current_project = "text=Continue Current Project"
################################
######### FUNCTIONS ############
################################


def print_request_sent(request):
  print("Request sent: " + request.url)


def timestamp():
    return time.strftime('%H:%M:%S')


def send_push():
    # Envia aviso pelo pushbullet instalado no celular
    api_key = "o.gWJiOosLWRj38MOrRzlcKY3cxnjblvdM"
    pb = Pushbullet(api_key)
    pb.push_note('NOVA TRADUCAO!', 'Veja o valor no rev')


def login(page):
    print('Fazendo login...')
    page.goto(URL_login)
    page.fill('id=Email', acc_email)
    page.click('id=next-btn')
    page.fill('id=Password', acc_pass)
    page.click('id=login-btn')
    print('Login efetuado.')


def confirm_claim(page):
    is_on = False
    page.goto(URL_find_work_sub)

    try:
        page.click(current_project)
        is_on = True
    except:
        pass

    return is_on



excluded_resource_types = ["stylesheet", "image", "font"]
def block_aggressively(route):
    if (route.request.resource_type in excluded_resource_types):
        route.abort()
    else:
        route.continue_()



def main():
    with sync_playwright() as p:
        print('=========/REVBOT-Webkit=/========')
        browser = p.webkit.launch()
        page = browser.new_page()
        page.route("**/*", block_aggressively)
        start_time = time.time()
        page.goto(URL_main)
        login(page)
        page.goto(URL_find_work_sub)

        # page.click(popup)
        page.click(pay_max_sort)
        print(f'Tempo de execução: {(time.time() - start_time)}')


        # while True:
        #     try:
        #         page.on("request", print_request_sent())
                # if page.inner_text('//*[@id="title-and-refresh-line"]/div/h5') != 'Waiting for new jobs...':
                #     # page.on("request", print_request_sent)
                #     # assert page.title() != "Rev - Find Work"
                #     print('Projeto encontrado.')
                #     page.click(refresh_job)
                #     page.click(collapse)
                #     page.click(claim_button)
                #     print("Achou! Clicando em Claim...")
                #     assert confirm_claim(page)
                #     send_push()
                #     print("Trabalho confirmado!")
                #     print("Finalizando...")
                #     break
                # else:
                #     print(f'\r{timestamp()} ainda não', end="\r")
                #     time.sleep(0.02)
                #
            # except:
                # print("Monitorando...")
                # time.sleep(0.02)
                # pass

        input("...")
        browser.close()


main()
