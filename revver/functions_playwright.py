import config
import functions

limit_existence = 'ativado: $%d' % config.price_limit if config.price_limit > 0.0 else 'desativado (express)'


def login(page):
    functions.printc('Fazendo login...')
    page.goto(config.URL_login)
    page.fill('id=Email', config.acc_email)
    page.click('id=next-btn')
    page.fill('id=Password', config.acc_pass)
    page.click('id=login-btn')
    functions.printc('Login efetuado.')


def confirm_claim(page):
    is_on = False
    page.goto(config.URL_find_work_sub)

    try:
        page.click(config.current_project)
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