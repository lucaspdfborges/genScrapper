from bot import cbaBot

def main():
    myBot = cbaBot('cba_arduino', 'a1b2c3')
    localBrowser = myBot.signIn()
    myBot.getAcessos(localBrowser)
    myBot.closeBrowser()

if __name__ == "__main__":
    # execute only if run as a script
    main()
