from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pushbullet import Pushbullet
from time import localtime as tempo
import random
import time
import json
import sys
import os


with open('profile.json') as profile_json:
    profile = json.load(profile_json)
    profile_json.close()


def empty_method():
    pass



def printc(text):
    print("|{0}| {1}".format(timestamp(), text))



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
        self.MINIM_PAY = profile['price_limit']
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
            # if (time.time() - self.ANCHOR_TIME) > 5400 and self.PAY_DECREASING and self.MINIM_PAY >= 5.0:
            #    self.ANCHOR_TIME = time.time()
            #    self.MINIM_PAY -= 0.0
            self.CONT_MAX = random.randint(1000, 5000)

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


    def monitorar(self):
        printc(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
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
                log_print('\r[{0}] (FIREFOX PID: {1}) Expandindo...'.format(timestamp(), os.getpid()))
                current_pay = driver.find_element(*self.PAY).text
                log_print('\r[{1}] (FIREFOX PID: {2}) Valor: {0}'.format(current_pay, timestamp(), os.getpid()))
                if float(current_pay.replace('$', '')) > self.MINIM_PAY:
                    driver.find_element(*self.CLAIM_BTN).submit()
                    # save_source(driver.page_source)
                    # driver.save_screenshot('screenshot\\{0}.png'.format(snap_timestamp()))
                    time.sleep(10)
                    assert self.job_exists()
                    log_print('\r[{0}] (FIREFOX PID: {1}) PEGOU!'.format(timestamp(), os.getpid()))
                    send_push(current_pay)
                    #playsound('media\\alert.wav')
                    #os.system('tools\\clean_process_firefox.bat')
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
print('################################')
print('##  FIREFOX SELENIUM LIMITED  ##')
print('################################')
log_print("\r[{0}] (FIREFOX PID: {1}) Inicializando...".format(timestamp(), os.getpid()))

# # # # # # # # # # # # # # # # #
#          CONFIGS              #
# # # # # # # # # # # # # # # # #
exec_path = "./geckodriver"
URL = r"https://www.rev.com/account/auth/login"
acc_email = profile['acc_email']
acc_pass = profile['acc_pass']
# # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # #
profile_path = r'firefox_profile'
options = Options()
options.add_argument("--headless")
options.set_preference('profile', profile_path)
options.set_preference("network.http.proxy.pipelining", True)
options.set_preference('media.volume_scale', '0.0')
options.set_preference("network.http.pipelining", True)
options.set_preference("network.http.pipelining.maxrequests", 8)
options.set_preference("content.notify.interval", 50000)
options.set_preference("content.notify.ontimer", True)
options.set_preference("content.switch.threshold", 250000)
options.set_preference("browser.cache.memory.capacity", 65536)  # Increase the cache capacity.
options.set_preference("browser.startup.homepage", "about:blank")
options.set_preference("reader.parse-on-load.enabled", False)  # Disable reader, we won't need that.
options.set_preference("browser.pocket.enabled", False)  # Duck pocket too!
options.set_preference("loop.enabled", False)
options.set_preference("browser.chrome.toolbar_style", 1) # Text on Toolbar instead of icons
options.set_preference("browser.display.show_image_placeholders", False)  # Don't show thumbnails on not loaded images.
options.set_preference("browser.display.use_document_colors", False)  # Don't show document colors.
options.set_preference("browser.display.use_document_fonts", 0)  # Don't load document fonts.
options.set_preference("browser.display.use_system_colors", True)  # Use system colors.
options.set_preference("browser.formfill.enable", False)  # Autofill on forms disabled.
options.set_preference("browser.helperApps.deleteTempFileOnExit", True)  # Delete temprorary files.
options.set_preference("browser.shell.checkDefaultBrowser", False)
options.set_preference("browser.startup.homepage", "about:blank")
options.set_preference("browser.startup.page", 0)  # blank
options.set_preference("browser.tabs.forceHide", True)  # Disable tabs, We won't need that.
options.set_preference("browser.urlbar.autoFill", False)  # Disable autofill on URL bar.
options.set_preference("browser.urlbar.autocomplete.enabled", False) # Disable autocomplete on URL bar.
options.set_preference("browser.urlbar.showPopup", False)  # Disable list of URLs when typing on URL bar.
options.set_preference("browser.urlbar.showSearch", False)  # Disable search bar.
options.set_preference("extensions.checkCompatibility", False) # Addon update disabled
options.set_preference("extensions.checkUpdateSecurity", False)
options.set_preference("extensions.update.autoUpdateEnabled", False)
options.set_preference("extensions.update.enabled", False)
options.set_preference("general.startup.browser", False)
options.set_preference("plugin.default_plugin_disabled", False)
options.set_preference("permissions.default.image", 2)  # Image load disabled again
###################################################
###################################################

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
#driver = webdriver.Firefox(executable_path=exec_path, options=option)
start_time = time.time()
driver.get(URL)
driver.implicitly_wait(1)
# # # # # # # # # # # # # # # # #
job_seeker = RmBot(driver)
job_seeker.login()
job_seeker.monitorar()
input('\r[{0}] (FIREFOX PID: {1}) RMBOT FINALIZADO.'.format(timestamp(), os.getpid()))
driver.quit()
