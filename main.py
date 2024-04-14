from playwright.async_api import async_playwright
import asyncio
import random
import os
import time
from colorama import Fore

"""
by playboisanz
"""

def mask_pw(pw):
    return '•' * len(pw)

async def isRobuxGet(cnt):
    f = open("info.txt" , "r" , encoding="UTF-8")
    re = f.read()

    rbx_id = re.split(":")[0]
    rbx_pw = re.split(":")[1]


    be = 0
    af = 0
    async with async_playwright() as RBX:
        browser = await RBX.chromium.launch(headless=False)
        bot = await browser.new_page()
        await bot.goto("https://www.roblox.com/login")
        await bot.type("#login-username",rbx_id)
        await bot.type("#login-password",rbx_pw)
        await bot.click("#login-button")
        await asyncio.sleep(3)
        print("Login Success")
        await asyncio.sleep(3)
        path = 'xpath=//*[@id="nav-robux-amount"]'
        rand_second = random.randint(2,9)
        handle = await bot.query_selector(path)
        value = await handle.inner_text()
        print("현재 로벅스 수 : {}".format(value))
        be = value
        print(f"{Fore.RED} [!] 최소 2초 최대 9초 까지 시간이 걸릴수 있습니다.{Fore.RESET}")
        result = int(value) + int(cnt)
        print(result)

        for _ in range(rand_second):
            await bot.reload()
        x = 'span[id^=nav-robux-amount]'
        await bot.evaluate(f"() => document.querySelector('{x}').innerHTML = ' '")
        await asyncio.sleep(0.3)
        af = str(result)
        await bot.evaluate(f"() => document.querySelector('{x}').innerHTML = '{str(result)}'")
        
            
        
        await asyncio.sleep(5)
        await bot.close()
        os.system("cls")
        print(f""" {Fore.YELLOW}
        ┌─  Roblox Account Info ───────────────────────────────────────────────┐
        │  • Account id : {rbx_id}                                             │
        │  • Account pw : {mask_pw(rbx_pw)}                                    │
        │  • Before Robux : {be}                                               │
        │  • After Robux : {af}                                                │
        └──────────────────────────────────────────────────────────────────────┘
        {Fore.RESET}""")

        await asyncio.sleep(1)
        return input("종료는 아무키나 누르시면 종료 됩니다.")
        
        
def main():
    if os.path.isfile("info.txt"):
       # os.system("playwright install")
        fe_ = open("info.txt" , "r" , encoding="UTF-8")
        re_ = fe_.read()

    
        count = re_.split(":")[2]
        #count = input("로벅스를 받을 갯수를 입력 해 주세요 >> ")
        time.sleep(3)
        os.system("cls")
        asyncio.run(isRobuxGet(count))
    else:
        print("파일이 존재 하지 않습니다!")
        return input("info.txt 형식으로 파일을 생성 해 주세요.")

if __name__ == "__main__":
    main()    
