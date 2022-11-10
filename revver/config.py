import functions

profile = functions.importar_profile()
#################################
######## WEBSITE CONFIGS ########
#################################
URL_login = r"https://www.rev.com/account/auth/login"
URL_main = r"https://www.rev.com/workspace/mywork"
URL_find_work_sub = r"https://www.rev.com/workspace/findwork/Subtitle"
URL_find_work_grading = r"https://www.rev.com/workspace/findwork/subtitlegrade"
acc_email = profile['acc_email']
acc_pass = profile['acc_pass']
price_limit = profile['price_limit']
price_check = profile['price_check']
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
