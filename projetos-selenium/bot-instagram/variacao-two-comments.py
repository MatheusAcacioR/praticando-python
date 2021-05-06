from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import urllib

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Matheus\AppData\Local\Programs\Python\Python39\chromedriver.exe')

    @staticmethod
    def writeLikeAHuman(comment, ondeDigitar):
        for letra in comment:
            ondeDigitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)
    

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(5)
        inputUsername = driver.find_element_by_xpath("//input[@name='username']")
        inputPassword = driver.find_element_by_xpath("//input[@name='password']")
        inputUsername.click()
        inputUsername.clear()
        inputUsername.send_keys(self.username)
        time.sleep(3)
        inputPassword.click()
        inputPassword.clear()
        inputPassword.send_keys(self.password)
        time.sleep(3)
        inputPassword.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get("https://www.instagram.com/p/CL10qZ2lQBf/")
        time.sleep(3)
        "COLOCAR AQUI O ARRAY COM OS NOMES"
        nomes = ["@mamae_daalana", "@janelaranjinha" "@britoana2020" "@angelicapanda22", "@arllyaneingreddy",
"@drilsanttos", "@cinthialinhares29", "@krismarun", "@liacunha19", "@estela.a.machado", 
"@elisanemichels", "@faahhalmeiida", "@gizellecaldeiragoesalquimim", "@gg_carla", 
"@jacquelinecorreia17", "@jessica_raiiane","@josianequirino", "@mamaeq_oraecanta", "@karolayne_rodrygues",
"@lilianesilva768", "@liziane.oleiro", "@lucia.ribeiro.186", "@lucienecavallini2", "@maraavp", 
"@maariana_b", "@marizanunes65", "@solangecapponi", "@roberta.aires1", "@paty_pessoa", "@nezzilda", 
"@nath_andrade25", "@nararaquelalmeida", "@monikinha_ferreira85", "@thatianapaiva", "@thayna1lisboa", 
"@thaispereira2247", "@vivianadesouzaa", "@janinha241625", "@pedagogaana2022", "@angelica25silva_", 
"@adrianasanttos22", "@crismarungoncalves", "@elianaalpha", "@estelinhaebrunao", "@elisa_huzar", 
"@gizellecaldeira2019", "@jess_raianee", "@lilianekirschbauer", "@limalizianede", "@pitinharibeiro", 
"@maraaparecida_gomesvilar", "@marizanunes87", "@beta_nathaliaandrade", "@kriandoedekorando", 
"@patymends", "@thayna20lisboa", "@maedojoaoracer", "@florzinha.angel", "@mae_da_lalinha", 
"@lilianeferreira101", "@lilinha887", "@ma_apgomes1977", "@raquel_almeidac", "@eu_nezzilda", 
"@patiih_vargas", "@dani_misael_alana","@adlizen_"]
        cont = 0
        # tudo que ficara dentro do for
        while cont < 32:
            inputComment = driver.find_element_by_xpath("//textarea[@class='Ypffh']")
            inputComment.click()
            time.sleep(random.randint(2, 5))
            newInputComment = driver.find_element_by_xpath("//textarea[@class='Ypffh focus-visible']")
            newInputComment.clear()
            'comentar o nome da pessoa'
            self.writeLikeAHuman(f'{nomes[0]} {nomes[1]}', newInputComment)
            # newInputComment.send_keys(user)
            time.sleep(3)
            'clicar no botao send'
            sendButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]").click()
            'esperar 10 segundos e repetir o processo'
            time.sleep(random.randint(2, 5))
            nomes.pop(0)
            nomes.pop(0)
            cont += 1
            if len(nomes) == 1:
                self.writeLikeAHuman(f'{user[0]}', newInputComment)
                time.sleep(3)
                'clicar no botao send'
                sendButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]").click()
                'esperar 10 segundos e repetir o processo'
                time.sleep(random.randint(2, 5))
                nomes.pop(0)

matheusBot = Instagram('m4th3us.jsx', 'Warm4chine')
matheusBot.login()