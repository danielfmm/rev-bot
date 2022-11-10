from revver import config, functions, functions_playwright
from playwright.sync_api import sync_playwright
import time


def main():
    with sync_playwright() as p:
        print('=========/REVBOT-EDGE/========')
        browser = p.chromium.launch(channel="msedge")
        start_time = time.time()
        page = browser.new_page()
        page.route("**/*", functions_playwright.block_aggressively)
        page.goto(config.URL_main)
        functions_playwright.login(page)
        page.goto(config.URL_find_work_sub)
        page.click(config.popup)
        page.click(config.pay_max_sort)
        functions.printc(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
        functions.printc("Monitorando...")
        while True:
            try:
                assert page.title() != "Rev - Find Work"
                functions.printc('Projeto encontrado.')
                page.click(config.refresh_job)
                functions.printc('Atualizou.')
                page.click(config.collapse)
                current_price = float(page.inner_text(config.job_price_on_claim).replace('$', ''))
                functions.printc(f"Conferindo se o valor de {current_price} é maior que o limite de {config.price_limit}.")
                if current_price > config.price_limit:
                    page.click(config.claim_button)
                    functions.printc("Clicando em Claim...")
                    assert functions_playwright.confirm_claim(page)
                    functions.send_push(current_price)
                    functions.printc("Trabalho confirmado!")
                    functions.printc("Finalizando...")
                    break
                else:
                    time.sleep(0.1)
                    functions.printc('Valor abaixo do limite, esperando 20 segundos para voltar a monitorar.')
                    time.sleep(20)
            except:
                time.sleep(0.04)

        browser.close()
        functions.inputc("Aperte qualquer tecla para fechar...")


def express():
    with sync_playwright() as p:
        print('======/REVBOT-EDGE-EXPRESS/=====')
        browser = p.chromium.launch(channel="msedge")
        start_time = time.time()
        page = browser.new_page()
        page.route("**/*", functions_playwright.block_aggressively)
        page.goto(config.URL_main)
        functions_playwright.login(page)
        page.goto(config.URL_find_work_sub)
        page.click(config.popup)
        page.click(config.pay_max_sort)
        functions.printc(f'Tempo de execução até monitorar: {(time.time() - start_time)}')
        functions.printc(f"Monitorando...")
        while True:
            try:
                assert page.title() != "Rev - Find Work"
                page.click(config.refresh_job)
                functions.printc('Atualizou.')
                page.click(config.collapse)
                page.click(config.claim_button)
                functions.printc("Clicando em Claim...")
                assert functions_playwright.confirm_claim(page)
                functions.send_push('express')
                functions.printc("Trabalho confirmado!")
                functions.printc("Finalizando...")
                break
            except:
                time.sleep(0.04)

        browser.close()
        functions.inputc("Aperte qualquer tecla para fechar...")


