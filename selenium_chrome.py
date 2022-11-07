from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pushbullet import Pushbullet

from time import localtime as tempo
import random
import time
import sys
import os


def empty_method():
    pass


def save_source(page_source):
    with open('page_source/{0}_page.html'.format(snap_timestamp()), 'w') as f:
        f.write(page_source)
        f.close()


def log_print(content):
    with open('logs/{0}.txt'.format(time.strftime('%d-%m-%y')), 'a', encoding="utf-8") as logging:
        print(content)
        logging.write(content)
        logging.close()


def timestamp():
    return time.strftime('%H:%M:%S')


def snap_timestamp():
    return time.strftime('%d-%m-%y__%H-%M-%S')


def print_flush(content):
    print(f"\r{content}", end='\r')


def send_push(totalpay):
    api_key = "o.gWJiOosLWRj38MOrRzlcKY3cxnjblvdM"
    pb = Pushbullet(api_key)
    pb.push_note('NEW JOB!',
                 'Valor: {0}.'.format(totalpay))


class RmBot:

    def __init__(self, rdriver):
        self.USER = (By.ID, "Email")
        self.PASS = (By.ID, "Password")
        self.NEXT = (By.ID, "next-btn")
        self.SUBMIT = (By.ID, "login-btn")
        self.UPDATE = (By.CLASS_NAME, "projects-banner")
        self.COLLAPSE = (By.XPATH, '//*[@id="find-work-root"]/div/div[2]/div/div[3]/div[1]/div/div/div/div')
        self.PAY_MAX_SORT = (By.XPATH, '//*[@id="find-work-root"]/div/div[2]/div/div[2]/div/div/div[1]/div')
        self.CLAIM_BTN = (By.CLASS_NAME, "project-claim-btn")
        self.PAY = (By.CSS_SELECTOR, "div[class='table-cell column narrow']")

        self.CURRENT_PROJECT_BTN = (By.CLASS_NAME, "my-work-btn")
        self.POPUP = (By.ID, "pushActionRefuse")
        self.CONT_MAX = random.randint(1000, 5000)  # 3800
        # self.CONT_MAX = 50
        self.TITLE = 'Rev - Find Work'
        self.MINIM_PAY = 50.0
        self.ANCHOR_TIME = time.time()
        self.PAY_DECREASING = False
        self.PAY_DECREASING_MIN = 20.0
        self.PAY_DECREASING_CHECK_POINT = time.time()
        self.HORA, self.MINUTO = 0, 0
        self.TROCAR = False
    

    def login(self):
        log_print("\r[{0}] (FIREFOX PID: {1}) Efetuando login...".format(timestamp(), os.getpid()))
        driver.find_element(*self.USER).send_keys(acc_email)
        driver.find_element(*self.NEXT).click()
        time.sleep(4)
        try:
            driver.find_element(*self.PASS).send_keys(*acc_pass)
            driver.find_element(*self.SUBMIT).click()
            log_print("\r[{0}] (FIREFOX PID: {1}) Login efetuado!".format(timestamp(), os.getpid()))
            

        except NameError:
            log_print(">>> Ocorreu um erro <<<")
            log_print(NameError)

        # input('Pressione para continuer...')

        driver.get('https://www.rev.com/workspace/findwork/Subtitle')

        time.sleep(5)
        driver.find_element(*self.POPUP).click()
        time.sleep(5)
        driver.find_element(*self.PAY_MAX_SORT).click()

    
    def pay_decrease_check_time(self):
        if time.time() > (self.PAY_DECREASING_CHECK_POINT + 1800): #1800 => meia-hora
            self.PAY_DECREASING_CHECK_POINT = time.time()
            payment_min_tmp = self.MINIM_PAY - 2.5
            if payment_min_tmp >= self.PAY_DECREASING_MIN and payment_min_tmp > -0.1:
                self.MINIM_PAY = payment_min_tmp
                # log_print(f"\n[{timestamp()}] Limite de valor reduzido para {self.MINIM_PAY}")
            else:
                self.PAY_DECREASING = False
    
    
    def trocar_limite(self):
        if self.TROCAR and self.HORA == int(tempo().tm_hour) and self.MINUTO == int(tempo().tm_min):
            self.MINIM_PAY = 0.0
            self.PAY_DECREASING = False
        

    def recarregar(self):
        if self.CONT_MAX == 0:
            driver.refresh()
            time.sleep(0.02)
            self.CONT_MAX = random.randint(1000, 50000)

    def animate(self):
        print_flush('\r[{0}] MONITORANDO! (PID:  {1}) (VALUE: {2}) ({3})'.format(timestamp(), os.getpid(), self.MINIM_PAY, "Y" if self.PAY_DECREASING else "N"))


    def job_exists(self):
        its_real = False
        log_print('\r[{0}] (FIREFOX PID: {1}) Conferindo se o projeto foi pego'.format(timestamp(), os.getpid()))
        try:
            driver.get('https://www.rev.com/workspace/findwork/Subtitle')
            driver.find_element(*self.CURRENT_PROJECT_BTN).click()
            its_real = True

        except:
            driver.get('https://www.rev.com/workspace/findwork/Subtitle')
            log_print('\r[{0}] (FIREFOX PID: {1}) A tentativa falhou.'.format(timestamp(), os.getpid()))

        return its_real


    def monitorar(self, start_time):
        print(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
        while True:

            self.recarregar()
            ## self.trocar_limite()
            self.pay_decrease_check_time() if self.PAY_DECREASING else empty_method()
            ## self.ver_status()
            try:
                assert driver.title != self.TITLE
                driver.find_element(*self.UPDATE).click()
                log_print('\r[{0}] (FIREFOX PID: {1}) Atualizando... {2}'.format(timestamp(), os.getpid(), self.CONT_MAX))
                driver.find_element(*self.COLLAPSE).click()
                current_pay = driver.find_element(*self.PAY).text
                log_print('\r[{1}] (FIREFOX PID: {2}) Valor: {0}'.format(current_pay, timestamp(), os.getpid()))
                if float(current_pay.replace('$', '')) > self.MINIM_PAY:
                    driver.find_element(*self.CLAIM_BTN).submit()
                    time.sleep(10)
                    assert self.job_exists()
                    log_print('\r[{0}] (FIREFOX PID: {1}) PEGOU!'.format(timestamp(), os.getpid()))
                    send_push(current_pay)
                    break
                else:
                    self.CONT_MAX -= 1
                    if current_pay:
                        log_print(
                            '\r[{0}] (FIREFOX PID: {2}) Valor do projeto menor que o definido: {1}'.format(timestamp(),
                                                                                                          current_pay,
                                                                                                          os.getpid()))
                    else:
                        log_print('\r[{0}] (FIREFOX PID: {1}) O problema é na captação do valor'.format(timestamp(),
                                                                                                       os.getpid()))
                    time.sleep(15)
                    #driver.refresh()
                    #time.sleep(10)
                    try:
                        driver.find_element(*self.UPDATE).click()
                        driver.find_element(*self.COLLAPSE).click()
                        log_print('\r[{0}] (FIREFOX PID: {1}) Novo projeto, atualizando!'.format(timestamp(), os.getpid()))

                    except:
                        pass
                        #driver.refresh()

            except:
                self.CONT_MAX -= 1
                self.animate()
                time.sleep(0.05)



# # # # # # # # # # # # # # # # #
# log_print(custom_fig.renderText('RMBOT'))
# log_print('###############################')
# log_print('##   FIREFOX LIGHT VERSION   ##')
# log_print('###############################')
# log_print("## Inicializando...          ##")
log_print("\r[{0}] (FIREFOX PID: {1}) Inicializando...".format(timestamp(), os.getpid()))

# # # # # # # # # # # # # # # # #
#          CONFIGS              #
# # # # # # # # # # # # # # # # #
URL = "https://www.rev.com/account/auth/login"
acc_email = "robertolmayer2@gmail.com"
acc_pass = "eurev3vc"
# # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # #
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument("--mute-audio")

###################################################
###################################################


#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
start_time = time.time()
driver.get(URL)

driver.implicitly_wait(1)
# # # # # # # # # # # # # # # # #
job_seeker = RmBot(driver)
job_seeker.login()
job_seeker.monitorar(start_time)
input('\r[{0}] (FIREFOX PID: {1}) RMBOT FINALIZADO.'.format(timestamp(), os.getpid()))
driver.quit()
