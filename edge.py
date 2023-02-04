from playwright.sync_api import sync_playwright
from pushbullet import Pushbullet
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
popup = '#pushActionRefuse'
refresh_job = '#title-and-refresh-line>div'
collapse = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div[1]/div/div/div/div'
pay_max_sort = '//*[@id="find-work-root"]/div/div[2]/div/div[2]/div/div/div[3]/div/span/span'
job_price_on_claim = '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div[3]/span'
claim_button = '.project-claim-btn'
claimed_job_price = 'div.pay-info-container>div:nth-child(3)'
current_project = "text=Continue Current Project"
current_projects_order = "#current>thead>tr>th.sttable-sorted-asc"
first_project_details = '//*[@id="current"]/tbody/tr[1]/td[1]/a'
job_price = "table>tbody>tr:nth-child(4)>td.oe-summary-detail"
unclaim_project_details = 'text=Unclaim'
unclaim_personal_reasons = '//*[@id="ft_Control_2"]/div/ul/li[3]/label'
unclaim_confirm = '//*[@id="ft_Control_2"]/div/a/span'
################################
######### BOT PROFILE ##########
price_limit = profile['price_limit']
price_check = profile['price_check']
################################
######### FUNCTIONS ############
################################
limit_existence = 'ativado: $%d' % price_limit if price_limit > 0.0 else 'desativado (express)'

def send_push(total):
    # Envia aviso pelo pushbullet instalado no celular
    api_key = ""
    pb = Pushbullet(api_key)
    pb.push_note('NOVA TRADUCAO!', f'valor: {total}')


def timestamp():
    return time.strftime('%H:%M:%S')


def printin(text):
    print("\r|{0}| Limite de valor {2} | {1}".format(
        timestamp(),
        text,
        limit_existence),
        end='\r')


def printc(text):
    print("|{0}| {1}".format(timestamp(), text))


def inputc(text):
    input("|{0}| {1}".format(timestamp(), text))



def login(page):
    printc('Fazendo login...')
    page.goto(URL_login)
    page.fill('id=Email', acc_email)
    page.click('id=next-btn')
    page.fill('id=Password', acc_pass)
    page.click('id=login-btn')
    printc('Login efetuado.')


def confirm_claim(page):
    is_on = False
    page.goto(URL_find_work_sub)

    try:
        page.click(current_project)
        is_on = True
    except:
        pass

    return is_on


excluded_resource_types = ["image",
                           "font",
                           "viewport",
                           "icon",
                           "manifest",
                           "mask-icon",
                           "shortcut icon",
                           "meta"]


def block_aggressively(route):

    if route.request.resource_type in excluded_resource_types:
        route.abort()
    else:
        route.continue_()


def main():
    with sync_playwright() as p:
        print('=========/REVBOT-EDGE/========')
        browser = p.chromium.launch(channel="msedge")
        start_time = time.time()
        page = browser.new_page()
        page.route("**/*", block_aggressively)
        page.goto(URL_main)
        login(page)
        page.goto(URL_find_work_sub)
        page.click(popup)
        page.click(pay_max_sort)
        printc(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
        printc("Monitorando...")
        while True:
            try:
                assert page.title() != "Rev - Find Work"
                printc('Projeto encontrado.')
                page.click(refresh_job)
                printc('Atualizou.')
                page.click(collapse)
                # printc('Expandiu.')
                # page.screenshot(path="claiming.png")
                current_price = float(page.inner_text(job_price_on_claim).replace('$', ''))
                # print(current_price)
                # page.screenshot(path="claimed.png")
                printc(f"Conferindo se o valor de {current_price} é maior que o limite de {price_limit}.")
                if current_price > price_limit:
                    page.click(claim_button)
                    printc("Clicando em Claim...")
                    assert confirm_claim(page)
                    send_push(current_price)
                    printc("Trabalho confirmado!")
                    printc("Finalizando...")
                    break
                else:
                    time.sleep(0.1)
                    printc('Valor abaixo do limite, esperando 20 segundos para voltar a monitorar.')
                    time.sleep(20)
            except:
                time.sleep(0.04)

        browser.close()
        inputc("Aperte qualquer tecla para fechar...")


def express():
    with sync_playwright() as p:
        print('======/REVBOT-EDGE-EXPRESS/=====')
        browser = p.chromium.launch(channel="msedge")
        start_time = time.time()
        page = browser.new_page()
        page.route("**/*", block_aggressively)
        page.goto(URL_main)
        login(page)
        page.goto(URL_find_work_sub)
        page.click(popup)
        page.click(pay_max_sort)
        printc(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
        printc(f"Monitorando...")
        while True:
            try:
                assert page.title() != "Rev - Find Work"
                #printc('Projeto encontrado.')
                page.click(refresh_job)
                printc('Atualizou.')
                page.click(collapse)
                # printc('Expandiu.')
                # page.screenshot(path="claiming.png")
                # current_price = float(page.inner_text(job_price_on_claim).replace('$', ''))
                # print(current_price)
                # page.screenshot(path="claimed.png")
                # printc(f"Conferindo se o valor de {current_price} é maior que o limite de {price_limit}.")
                # if current_price > price_limit:
                page.click(claim_button)
                printc("Clicando em Claim...")
                assert confirm_claim(page)
                send_push('express')
                printc("Trabalho confirmado!")
                printc("Finalizando...")
                break
            except:
                time.sleep(0.04)

        browser.close()



main() if price_limit > 0.0 else express()
inputc("Aperte qualquer tecla para fechar...")
