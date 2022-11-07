from seleniumwire import webdriver

#############################
USER =("Email")
PASS = ("Password")
NEXT = ("next-btn")
SUBMIT = ("login-btn")
UPDATE = ("projects-banner")
COLLAPSE = ('//*[@id="find-work-root"]/div/div[2]/div/div[3]/div[1]/div/div/div/div')
PAY_MAX_SORT = ('//*[@id="find-work-root"]/div/div[2]/div/div[2]/div/div/div[1]/div')
CLAIM_BTN = ("project-claim-btn")
PAY = ("div[class='table-cell column narrow']")
CURRENT_PROJECT_BTN = ("my-work-btn")
POPUP = (id, "pushActionRefuse")
# CONT_MAX = random.randint(1000, 5000)  # 3800
TITLE = 'Rev - Find Work'
#############################
exec_path = "geckodriver.exe"
URL = r"https://www.rev.com/account/auth/login"
acc_email = "robertolmayer2@gmail.com"
acc_pass = "eurev3vc"

driver = webdriver.Firefox(executable_path='exec_path')
driver.get(URL)

def login():
        print(f"\r[{timestamp()}] Efetuando login...")
        driver.find_element(USER).send_keys(acc_email)
        driver.find_element(NEXT).click()
        time.sleep(4)
        try:
            driver.find_element(PASS).send_keys(acc_pass)
            driver.find_element(SUBMIT).click()

        except NameError:
            print(">>> Ocorreu um erro <<<")
            print(NameError)

        driver.get('https://www.rev.com/workspace/findwork/Subtitle')

        time.sleep(5)
        driver.find_element(POPUP).click()
        time.sleep(5)
        driver.find_element(PAY_MAX_SORT).click()
        print("logado")
login()
driver.get("https://www.rev.com/workspace/findwork/subtitle")