import time

index = 0
contador = 0
"""nomes = ["@mamae_daalana", "@janelaranjinha", "@britoana2020", "@angelicapanda22", "@arllyaneingreddy", "@drilsanttos", 
"@cinthialinhares29", "@krismarun"]
"""

"""for name in nomes:
    print(f'{index} - {name}')
    index += 1
    time.sleep(1)"""


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

while contador < 32:
    print(f'{nomes[0]} {nomes[1]}')
    nomes.pop(0)
    nomes.pop(0)
    contador += 1
    if len(nomes) == 1:
        print(nomes[0])
        nomes.pop(0)