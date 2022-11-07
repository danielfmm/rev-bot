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

def send_push(total):
    # Envia aviso pelo pushbullet instalado no celular
    api_key = "o.gWJiOosLWRj38MOrRzlcKY3cxnjblvdM"
    pb = Pushbullet(api_key)
    pb.push_note('NOVA TRADUCAO!', 'Valor: $%d' % total)


def timestamp():
    return time.strftime('%H:%M:%S')


def printin(text):
    print("\r|{0}| Limite de valor {2} | {1}".format(
        timestamp(),
        text,
        'ativado: $%d' % price_limit if price_check else 'desativado'),
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


def unclaim_current_job():
    page.click(unclaim_project_details)
    page.click(unclaim_personal_reasons)
    page.click(unclaim_confirm)


def confirm_claim(page):
    is_on = False
    page.goto(URL_find_work_sub)

    try:
        page.click(current_project)
        is_on = True
    except:
        pass

    return is_on


def get_project_price(page):
    page.goto(URL_main)
    page.click(first_project_details)
    current_price = float(page.inner_text(job_price).replace('$',''))
    return current_price


async def is_on_price(page):
    output = False
    current_price_vs = get_project_price(page)
    if current_price_vs >= price_limit:
        output = True
        printc('Preço dentro do confirmado!')
        printc('Enviando notificação para o celular...')
        send_push(current_price_vs)
    else:
        printc('Valor mínimo é de {0} e o projeto paga {1}.'.format(price_limit, current_price_vs))
        printc('O projeto será devolvido e o REVBOT voltará a monitorar.')
        #await unclaim_current_job()
        printc('Pronto! Retornando ao monitoramento...')

    return output


with sync_playwright() as p:
    print('==================================')
    print('=========/REVBOT-Chromium/========')
    print('==================================')
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL_main)

    if page.title() == "Sign In - Rev":
        login(page)
    else:
        printc("Não precisou fazer login.")

    while confirm_claim(page):
         printc('Existe um projeto ativo na conta.')
         inputc('Pressione qualquer tecla quando entregar o trabalho...')

    page.goto(URL_find_work_sub)
    # page.click(popup)
    page.click(pay_max_sort)

    while True:
        try:
            assert page.title() != "Rev - Find Work"
            printc('Projeto encontrado.')
            page.click(refresh_job)
            printc('Atualizou.')
            page.click(collapse)
            #printc('Expandiu.')
            # page.screenshot(path="claiming.png")
            current_price = float(page.inner_text(job_price_on_claim).replace('$', ''))
            #print(current_price)
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
                #send_push(get_project_price(page))
        except:
            printin("Monitorando...")
            time.sleep(0.002)

    browser.close()
