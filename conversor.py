import json
import re
import os

entrada = """
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Criação de Quincy: Vollständig*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ De início, se trata de uma evolução dos quincys que não possui as desvantagens que o *Quincy: Letzt Stil* tem, que é considerada obsoleta. Aqui poderão em determinado momento optar por escolher uma Quincy: Vollständig apresentada em Bleach ou criar a sua própria conforme os requisitos abaixo.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Quincy: Vollständig permite manter seus poderes e usa-lo repetidamente, podendo ativar e reativar várias vezes durante um dia.

*O2 •* A Quincy: Vollständig só é possível devido ao Leiden Hant que serve como um catalisador. Podendo ser um emblema ou um cinto entre outros objetos e formas.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Um Quincy: Vollständig fornece habilidades únicas mas também fornece aumento das habilidades únicas de acordo com o usuário, isto varia conforme o quincy.*_

❐➮ *Quincy: Vollständig :* O método padrão para um Quincy ativar Quincy: Vollständig está usando seu Leiden Hant como um catalisador, no qual o emblema brilhará com uma grande quantidade de energia espiritual. No entanto, vários Quincy podem usar dispositivos alternativos, como um cinto que serve como substituto da luva, ativá-lo revirando o olho esquerdo e etc. Além disso, o Quincy: Vollständig pode ser ativado sozinho quando o usuário está cercado por altas concentrações de Reishi e não possui controle total sobre ele. 
➮ *Requisitos:* Desconhecido por enquanto.

❐➮ *Domínio de reish completo*: Quincy: Vollständig permite ao usuário absorver uma grande quantidade de Reishi na ponta de sua Arma Espiritual para usar em um ataque poderoso. Nesta forma, a capacidade de um Quincy para absorção de Reishi aumenta drasticamente. Eles podem absorver as árvores, areia, pedras e até os prédios do Hueco Mundo ou Sociedade das almas, e formas de vida espiritual. Aumenta em +2x status gerais com exceção do reiatsu.

❐➮ *Voo*: Os usuários do Vollständig podem usar as asas reishi geradas pela técnica para vôos em alta velocidade. Essas asas aumentam a velocidade enquanto fora de contato com o chão em +2x. 

❐➮ *Arma espiritual*: Com seu Quincy: Vollständig ativado, um Quincy pode produzir uma Arma Espiritual, feita inteiramente de Reishi, a partir da luva em seu pulso. Eles podem usar essa arma para ataques corpo a corpo e para disparar flechas. 

❐➮ *Schrift aprimorado*: a capacidade concedida pelo Schrift de um Sternritter é bastante ampliada. Seu poder e alcance são aumentados para o triplo, e um Quincy ganha acesso a novas técnicas que eles não podem usar normalmente.

❐➮ *Consciência espiritual aprimorada*: um Quincy usando Quincy: Vollständig pode sentir o reiatsu em um nível muito maior, permitindo que eles superem qualquer habilidade que oculte a presença de alguém se for mais poderoso ou tiver poder igual do oponente em questão.

❐➮ *Extras*: Quincy: Vollständig não é uma técnica natural; O Quincy precisa treinar para alcançá-lo. Quincy: Vollständig assume uma variedade de formas, mas geralmente dá ao usuário uma aparência de anjo, com construções de reishi em forma de asa e um Quincy Zeichen em forma de estrela para um halo, conhecido como Heiligenschein (光 輪 (ハ イ リ ゲ ンIgャ イ ン), Hairigenshain ; alemão e japonês para " Halo "). No entanto, nem todos Quincy: Vollständig conceder essas construções específicas. É possível que se sofrerem uma lesão fatal no estado inicial de Quincy: Vollständig , poderá adentrar em uma segunda forma. Seus corpos se transformam drasticamente diferentes de suas formas anteriores, e os ferimentos fatais e as partes perdidas são regenerados mas isto é para poucos casos. Esta característica se aplica apenas para alguns Quincys, os mais podersos da Wandenreich.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Gintō*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Gintō (銀 筒, Tubos de Prata ) como o nome sugere, Gintō são pequenos tubos de prata, com aproximadamente 5 centímetros de tamanho. Ao condensar o Reiryoku em um estado líquido, Quincy pode armazená-lo dentro dos tubos. Apesar de ser considerado ferramentas antiquados, eles permitem ao Quincy para executar técnicas especiais poderoso o suficiente para subjugar Hollows, embora a sua eficácia depende do usuário. Esses vários ataques são desencadeados quando o Reiryoku líquido armazenado é liberado. Como Kidō, alguns deles são ativados chamando vários comandos.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋

┈── _Técnicas Ginto_

❐➮ *Heizen (聖 噬 [ハ イ ゼ ン], Haizen; alemão para "Aquecimento", japonês para "Mordida Sagrada"):* Heizen instantaneamente arranca e purga tudo o que está no espaço feito pelos quatro Gintō arremessados. Esta técnica cria um feixe de energia retangular e transparente a partir dos tubos de prata que cortam o oponente. É extremamente eficaz, mesmo contra o Menos Grande. O dano de ataque dessa técnica é de 140% baseado no reiatsu do usuário.
➮ Encantamento de utilização: "Sinta a ira da batalha e aceite este cálice sagrado!"
➮ Itens necessários: 4 Gintos.

❐➮ *Gritz (五 架 縛 [グ リ ツ], Gurittsu; japonês para "Five Rack Ties"):* Um filme de Reishi emitido por um Gintō lançado cerca o inimigo. Esta técnica forma uma cruz pentagonal Quincy do tamanho de um homem, que envolve seu alvo prendendo tal. A defesa do ginto pode ir ate 90% do reiatsu do usuário.
➮ Encantamento de utilização: "Uma haste de prata atinge o leito de pedra de cinco dedos!"
➮ Itens necessários: 1 Ginto por contenção.

❐➮ *Wolke (緑 杯 [ヴ ォ ル コ ル], Vorukōru ; alemão para "Nuvem", japonês para "Copa Verde"):* O praticante usa um Ginto para criar uma grande explosão, que amortece o impacto de uma queda com o Reiryoku contido dentro do Ginto.
➮ Encantamento de utilização: "Incline a taça para o oeste!"
➮ Itens necessários: 1 Ginto.

❐➮ *Sprenger (破 芒 陣 [シ ュ プ レ ン ガ], Shupurenga; alemão para "Explosão", japonês para "Breaking Caespitose Formation"):* Esta técnica usa cinco Seele Schneider para criar um selo em forma de pentágono que, quando ativado, cria uma explosão massiva dentro de suas fronteiras. Quando um objeto ou pessoa fica no meio do pentágono, a colocação da quinta Seele Schneider pode prendê-los ao envolver e amarrar suas pernas ao solo com um Reishi denso. Os Seele Schneider funcionam como acumuladores, reunindo a quantidade necessária de Reishi para criar a explosão. O líquido dentro de um Ginto atua como o gatilho. O dano de ataque dessa técnica é depende da quantidade de reishi no local, se feita em um lugar com pouco reishi como o mundo humano, o dano máximo é de 100% do reiatsu do usuário, ja se feita em um lugar com reishi abundante como hueco mundo, o dano chega ate 250% do total de reiatsu do usuário. Além de necessitar de 1 turno preparando a técnica em combate. Pode ser usado apenas 1 vez por combate. 
➮ Encantamento: Não possui.
> ➮ Itens necessários: 5 Seele Schneider e 1 Ginto.

❐➮ *Geldschrank (, Gerutoshuranku; Alemão para "Seguro", Japonês para "Formação de Destruição de Caixa de Trava") 封庫滅陣*: Esta técnica envolve disparar um único Seele Schneider no alvo pretendido, que então para no ar, cercando o oponente com uma barreira de alta densidade de Reishi. Cortes minúsculos criados pelo Seele Schneider fazem com que o Reishi flua para fora do corpo do alvo, e o usuário então joga um Gintō no Seele Schneider , fazendo com que a barreira imploda antes de criar uma enorme explosão. Ignora 20% da resistência do alvo e causa dano de 150% do reiatsu do usuário. Usado uma vez por combate.
> ➮ Itens necessários: 1 Seele Schneider e 1 Ginto.

❐➮ *Sistema de aprendizagem e criação:* Para o quincy aprender basta realizar uma cena filler treinando a técnica e possuir os gintos para a execução dela. A eficiência dos gintos depende do usuário, ou seja quanto mais forte o usuário mais forte será o ginto. É possível criar feitiços próprios mas somente para aqueles que obter destaque em eventos e missões.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── 𝙂𝙊𝙏𝙀𝙄 13 • 十三隊 ─ _"𝘼 𝙇𝙖𝙢𝙞𝙣𝙖 𝘾𝙚𝙡𝙚𝙨𝙩𝙞𝙖𝙡 𝙙𝙖 𝘼𝙡𝙢𝙖"_
_“𝙉𝙤𝙨 𝙨𝙤𝙢𝙤𝙨 𝙖 𝙢𝙪𝙧𝙖𝙡𝙝𝙖 𝙚𝙣𝙩𝙧𝙚 𝙖 𝙤𝙧𝙙𝙚𝙢 𝙚 𝙤 𝙘𝙖𝙤𝙨.”_
━━━━━━━━━━━━━━━━━━━━━━━━
➻ O Gotei 13 é o brɑço militɑr dɑ Soul Society, formɑdo por treze divisões, cɑdɑ umɑ liderɑdɑ por um cɑpitα̃o com forçɑ dignɑ de moldɑr erɑs. Mɑis do que um exército, o Gotei representɑ o equilíbrio entre os mundos, zelɑndo pelɑs ɑlmɑs e pelɑ reencɑrnɑçα̃o. Seus membros sα̃o treinɑdos nɑ ɑrte do Zɑnjutsu (espɑdɑ), Kido (mɑgiɑ espirituɑl), Shunpo (movimentɑçα̃o veloz) e Hɑkudɑ (combɑte corporɑl), formɑndo guerreiros completos. Mesmo em tempos de pɑz, suɑs Zɑnpɑkutō vibrɑm em expectɑtivɑ. Cɑdɑ divisα̃o possui suɑ especiɑlidɑde e ideologiɑ, mɑs em guerrɑ... todɑs se tornɑm lα̂minɑs de um mesmo corte divino. O Gotei 13 serve como uma força militar com suas principais responsabilidades estão listadas logo abaixo.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •*  A defesa da Seireitei, o centro da Soul Society.

*O2 •* O desdobramento de membros da Divisão em território inimigo para operações de combate.

*O3 •* A implantação de forças militares como medidas defensivas no mundo humano.

*O4 •* Guiar as almas para a Soul Society.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*A seguir veja os cargos do gotei 13.*_

❐➮ *Shinigamis comuns:*
❶ • Ja começa neste cargo.
❷ • Ser um shinigami ativo.
❸ • Pode ser promovido, de acordo com a sua evolução e desempenho. Caso o atual capitão(adm) deseje pode torna-lo um oficial.

❐➮ *Oficiais:*
❶ • Ser no mínimo nível 8.
❷ • Ser um Shinigami ativo.
❸ • Possuir pelo menos shikai.
❹ • Pode ser escolhido por recomendação de um determinado capitão.
❺ • Pode ser promovido, de acordo com a sua evolução e desempenho. Caso o atual 3° em comando venha à morrer, um oficial destaque poderá tomar seu lugar.

❐➮ *Tenente:*
❶ • Ser nível 30 ou superior.
❷ • Ser um Shinigami ativo.
❸ • Possuir no mínimo Shikai.
❹ • Deve ter sido 3° oficial, antes do tenente anterior "perder" seu posto.
❺ • Possuir Reiatsu nível Tenente.
❻ • Pode ser escolhido por recomendação de um determinado capitão.

❐➮ *Capitão:*
❶ • Nível mínimo desconhecido.
❷ • Ser um Shinigami ativo.
❸ • Possuir Shikai e Bankai.
❹ • Ser tenente, ou pelo menos ter passado por esta patente, exceção apenas para a décima primeira divisão que basta desafiar o atual capitão para um combate ate a morte para assumir seu lugar não importa o cargo do desafiante.
❺ • Possuir Reiatsu nível Acima de Tenente/Capitão.

❐➮ *Capitão-Comandante:* 
❶ • Nível mínimo desconhecido.
❷ • Deve ter evoluído de forma completa, ou seja, passando de cargo em cargo oficial de um determinado esquadrão. Destacando-se sempre como o mais forte ou pegando algum destaque minimamente em eventos.
❸ • Ser um Shinigami Puro.
❹ • Possuir Shikai e Bankai completa.
❺ • Possuir Reiatsu nível Comandante Geral.
❻ • Necessário ser um player muito ativo, ausências podem levar à substituição.
❼ • O mais forte dentre todos os 13 capitães do
Sereitei.

❐➮ *Caso já possua todos os requisitos necessários para obter um determinado cargo, basta simplesmente notificar algum dos adm's. Deste modo, uma avaliação será feita, para obter uma confirmação detalhada e assim seder-lhe o cargo desejado.*

❐➮ _Informações Extras:_
> ➮ 𝙎𝙞𝙢𝙗𝙤𝙡𝙤: 𖥅
> 𝙇𝙞𝙙𝙚𝙧𝙖𝙣𝙘𝙖 𝙎𝙪𝙥𝙧𝙚𝙢𝙖: 𝘾𝙖𝙥𝙞𝙩𝙖𝙤-𝘾𝙤𝙢𝙖𝙣𝙙𝙖𝙣𝙩𝙚 (𝙎𝙤𝙪𝙩𝙖𝙞𝙘𝙝ō)
> 𝙎𝙚𝙙𝙚: 𝙎𝙚𝙞𝙧𝙚𝙞𝙩𝙚𝙞, 𝙎𝙤𝙪𝙡 𝙎𝙤𝙘𝙞𝙚𝙩𝙮
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Shinigami*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Shinigamis são almas que originam-se do gotei treze, e são enviados ao mundo humano para manter o equilíbrio entre os mundos, purificando e matando hollows que praticam o mal no mundo dos vivos, além de enviar os plus(almas humanas) do mundo humano para o mundo espiritual ou para o inferno caso este último tenha feito muitos pecados ruins, atrocidades imperdoáveis enquanto ainda era vivo. Possuem um alto nível de reiryoku e passam por uma selação além de um árduo treinamento. Como almas, seu corpo é feito de reishi e é invisível para seres sem poderes espirituais significativos, ou seja, consciência espiritual, como os humanos. Quando almas de alto nível de reiryoku treinam seus corpos, podem tornar-se shinigamis.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Shinigamis recebem salários assim como trabalhadores do mundo humano.

*O2 •* Recebem recompensas pela purificação de hollows, geralmente as que constam nas missões. 

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Habilidades gerais dos shinigamis.*_

❐➮ *Konsō (魂葬, "funeral de alma")*: É a técnica que os shinigami usam para enviar um plus(alma) para um dos planos não-terrenos, seja Soul Society (se seus pecados forem perdoáveis) ou o inferno (caso a pessoa tenha cometido atrocidades imperdoáveis enquanto viva, como assassinatos etc.) ao tocar a testa do espírito com a base da empunhadura de sua zampakutō.
➮ *Requisitos:* Ja possui inicialmente.

❐➮ *Sublimação*: Quando um hollow é morto por uma zanpakutō, os crimes cometidos após sua transformação são imediatamente perdoados (não os cometidos em vida) e a alma é purificada. Com isso, o efeito konsō ocorre, guiando a alma para a Soul Society ou para o Inferno.
➮ *Requisitos:* Ja possui inicialmente.

❐➮ *Forma evoluída*: Uma zanpakutō completa possui a habilidade de revelar sua verdadeira forma através da liberação de shikai, onde mostra sua verdadeira natureza. O poder máximo de uma zanpakutō, porém, só é demonstrado em seu estado de liberação final. Este estado é chamado de bankai (antigamente, shinuchi) em Soul Society.
➮ *Requisitos:* Favor ler o sistema de zampakutō.

❐➮ *Transferência de poder*: Um shinigami pode usar esta técnica não-nomeada para inserir metade de seu poder em um indivíduo. A transferência pode ser feita rapidamente quando a zanpakutō atravessa o peito da pessoa que terá seu poder aumentado. Se o procedimento falhar, o indivíduo ao qual o poder foi transferido morre, e mesmo com um nível alto de reiryoku, um ser humano tem chances baixas de sobrevivência. Transfere apenas 50% do Reiatsu limitado a 1 vez por shinigami.
➮ *Requisitos:* Possuir nível 15 para poder fazer isto.

❐➮ *Shunpo (瞬 歩, Flash Steps)*: É uma técnica de movimento que permite ao usuário se mover mais rápido do que o olho pode seguir. O ponto focal que determina a base dessa técnica é a velocidade. Como a velocidade é o principal fator da técnica, o método é melhor caracterizado pela rapidez com que pode chegar do ponto A ao ponto B na menor quantidade de etapas. Treinamento e habilidade são o que determina o quão rápido um usuário de Shunpo pode se mover; Os usuários de pouca habilidade na técnica ou aqueles que não o usaram por um longo período de tempo obviamente estarão fora de prática, fazendo com que sejam consideravelmente mais lentos, o que exige o uso de mais etapas para mover a mesma distância e tornar-se sinuoso um curto período de tempo. Essa técnica aumenta em 2x o atributo velocidade do usuário, por exemplo se você possui 100 pode se mover a 200.
➮ *Requisitos:* Possui no nivel 8, para aprender basta realizar uma cena de filler de 30 linhas aprendendo. Constante melhora.

❐➮ *Kidō (鬼道, caminho espiritual)*: Kidō é uma das formas de combate shinigami, usando o reiryoku, palavras e gestos manuais ou não se pode efetuar eles. Existe diversos tipos de kidō para uso dos shinigamis, o do tipo ofensivo chamado hadō, o do tipo de proteção ou contenção chamado bakudō e o do tipo auxiliar sem nome ate o momento, usado como método de cura. Mais informações sobre kidō basta ver no site ou pedir a administração para que tire suas dúvidas.
➮ *Requisitos:* Liberado a partir do nível 2.

❐➮ *Senkaimon (穿 界 門, World Penetration Gate; Viz "Tunnel World Gate"):* é o portal dimensional que os Shinigami usam para entrar e sair da Soul Society. 
➮ Requisitos: Uso livre para qualquer shinigami ir para o mundo humano e retornar. Ja para ir ao hueco mundo é necessário permissão da central 46(Adms).
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Crıαçα̃o de Zαnpαkutõ*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ A Criação de Zanpakutõ é um benefício da qual todos os players recém chegados podem utilizar para criar a principal arma que vai lhes auxiliar em todo o decorrer de sua história dentro deste RPG, caso escolha ser um shinigami. Para isso ser feito sem nenhum problema, os players devem seguir uma lista de regras e observações anexadas abaixo, que devem ser lidas com atenção e seguidas perfeitamente. Algumas delas retiradas da obra e outras para o melhor funcionamento e equilíbrio do RPG.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Todos os Asauchi são forjados exclusivamente por Ōetsu Nimaiya. Desde o nascimento da Soul Society, nunca houve um Shinigami que despertou seu próprio Zanpakutō sem empunhar um Asauchi que Nimaiya forjou.

*O2 •* Por serem parte da alma de seus donos, um Zanpakutō não pode ser substituído, embora se regenere lentamente se for quebrado enquanto em estado shikai.

*O3 •* A única coisa que pode curar um Zanpakutō quebrado é a força de vontade de seu próprio usuário, Reiatsu, e o tempo necessário para infundir o Zanpakutō com esse Reiatsu. Isso se refere apenas ao Shikai de alguém e só pode ser feito se o punho do Zanpakutō permanecer intacto. A destruição de um Shikai e a destruição de um Bankai têm significados bastante diferentes, pois um Bankai destruído nunca pode ser restaurado à sua forma original.

*O4 •* Todo Zanpakutō tem seu próprio nome, que o usuário deve aprender.

*O5 •* Zanpakutō tem uma forma verdadeira. Esta verdadeira forma reside dentro de seus Shinigami. Um Zanpakutō tem uma mente e um corpo, que controlam seus poderes. Shinigami pode crescer mais poderoso se comunicando com eles.

*O6 •* Independentemente da forma (ou tamanho) de um Zanpakutō, é sempre praticamente fácil para o seu dono exercer, porque faz parte da alma do seu dono. 

*O7 •* Nenhum Zanpakutō existente possui um Shikai e um Bankai que usam habilidades não relacionadas.

*O8 •* Um Zanpakutō não pode ter habilidades elementares de mais de um elemento.

*O9 •* Todo Zanpakutõ com poderes elevados, aqueles considerados extravagantes, extremos ou apelativos devem conter uma "Fraqueza". Uma regra, requisitos ou qualquer outra coisa que equilibre suas ações, afim de não o tornar alvo de críticas e denúncias e manter a ordem no RPG.

*1O •* Todos os Zanpakutõ's Criados devem conter uma descrição completa de suas capacidades, desde nome até habilidades. Qualquer falta de explicação será considerada nula.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _Todos os Zanpakutō têm dois níveis de lançamento, além da forma selada. O primeiro é *Shikai* e o segundo é *Bankai*._

❐➮ *Forma Selada:*
Muitos Zanpakutō parecem katana comuns, com pequenas variações entre eles, como seria de esperar entre espadas diferentes. Suas variações são comumente: Katana, Wakizashi, Nodachi e Tantō. Nessa forma selada, como o próprio nome sugere, uma Zanpakutõ não manifesta quaisquer habilidades especiais com a única exceção de suas gerais próprias, como a purificação.
➮ *Requisitos:* Todos possuem inicialmente. 

❐➮ *Shikai (解 解, Versão Inicial):* É a primeira atualização disponível para um Zanpakutō. Para ativá-lo, os Shinigami precisam aprender o nome de seus Zanpakutō. Isso não é tão fácil quanto escolher um nome, pois o espírito vivo do Zanpakutō já tem seu próprio nome. A lâmina muda de forma e ganha habilidades especiais cantando um Kaigo (号 号, Liberar Chamada) ou liberar encantamento. É crucial memorizar cada frase, pois todo Zanpakutō tem um encantamento diferente. Os comandos variam entre os usuários e variam de um simples verbo imperativo a um pequeno poema. Eles geralmente se relacionam com a habilidade de assinatura do Zanpakutō ou sugerem a natureza de seu espírito.
➮ *Requisitos:* Requer nível 10, reiatsu nível oficial e uma cena aprendendo o nome da shikai pela primeira vez para algum adm avaliar. Vale-se citar que a quantidade de linhas fica a critério do player.

❐➮ *Bankai (解 解, Versão Final):* É a segunda e última forma atualizada de um Zanpakutō. Para alcançar Bankai, é preciso ser capaz de materializar e subjugar seu espírito Zanpakutō. Materialização significa o oposto de ser arrastado para o mundo interior do Zanpakutō: o usuário precisa convocar o espírito do Zanpakutō para o mundo físico. Geralmente, leva 10 anos ou mais para ser alcançado, além da experiência necessária para dominá-lo. Apesar do espírito de Zanpakutō ser subjugado para seus Shinigami aprenderem Bankai, os Zanpakutō também se tornam mais fortes e aprendem Bankai exatamente no momento em que seus Shinigami aprendem. Mesmo que Bankai seja o estágio final de um Zanpakutō, isso não significa que o crescimento dos Shinigami termina aí. As Bankais geralmente são armas gigantescas e monstruosas, mas também podem se manifestar em formas mais compactas e simples.
➮ *Requisitos:* Desconhecido.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Sistema de Kidō*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Kidō (鬼道 "caminho demônio" ou "caminho 
espiritual", às vezes traduzido como Artes Demoníacas; nomeadamente "Poder dos Ceifadores de Almas", "Magias") é uma forma de combate Shinigami que se baseia em feitiços avançados que são produzidos com Reiryoku forte e se dividem em duas categorias: Hadou para ataques diretos, e Bakudō como apoio de batalha é uma das técnicas no Zankensoki, o grupo de Shinigami habilidades de combate primários.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋

┈── _*A seguir veja tudo sobre os kidos no rpg.*_

❐➮ Kidou Mecânicas.
➮ Cada feitiço mágico é classificado numa escala de 1 a 99, sendo este último o mais potente e mais difícil de executar. A escala é uma medida de dificuldade. Para usar Kidō, um Shinigami deve recitar o encantamento específico para o feitiço, que muitas vezes é longa e exige alguns segundos para falar. O poder de um feitiço depende do poder do usuário, como até mesmo uma magia de baixo nível pode ser totalmente devastadora quando utilizada por um Shinigami de alta classe. 

┈── _*Kidou Classificação.*_

❐➮ Existem três tipos principais de Kido: Magias de ligação(Bakudou), Magias de destruição(Hadou), e Magias de cura(Kaido).

❐➮Bakudō (缚道, lit. "Caminho da ligação"): Magias complementares que podem imobilizar um inimigo ou ter um efeito além de um ataque direto. Eles podem parecer sutil, mas essas magias podem dar a seus usuários uma vantagem tática quando utilizado corretamente. Trata-se de uma ampla categoria de feitiços defensivos que bloqueiam/repelem ataques inimigos ou os congelam no lugar. Esta classe de magias incluem barreiras Kidō & Selamentos.

❐➮ Barreiras: Focada energia espiritual formado em uma forma sólida de energia. Esta energia pode assumir diversas formas ou cores, tal como determinado pelo utilizador. A força de uma barreira é dependente da potência do reiatsu do utilizador. Barreiras fracas são facilmente quebrável enquanto os fortes podem durar séculos. Certas barreiras podem ser colocados de antemão e ativado mais tarde, enquanto outros exigem certos artefatos e tempo para ativar.

❐➮ Selos: São um pouco semelhante a barreiras, mas são muito mais poderosos e requerem uma preparação maior para criar. Selos só são possíveis de usar por ser de potência suficiente espiritual, que são destinadas a manter os artefatos mais poderosos e/ou perigoso ou seres. São geralmente difíceis de quebrar.

❐➮ Hadou (破道, lit. "Caminho da destruição".): 
Magias ofensivas que infligem danos diretos ao inimigo. A sua eficácia varia de acordo com o usuário. Diz-se que a eficácia dos feitiços mais bem classificados são além da imaginação.

❐➮ Kaidō (回道, também conhecido como Magias de cura): Estas magias não têm nomes conhecidos, números ou encantamentos para lançar, e simplesmente curam o alvo. À medida que o usuário mantém suas mãos acima das feridas do paciente, suas palmas das mãos iluminam com a energia espiritual verde para facilitar a cicatrização.

┈── _*Classes de Encantamento.*_

❐➮ Eishōhaki (咏唱破弃, "Abandono Encantamento"): uma classe de encantamento Kidō, onde o praticante Kidō renuncia usando um encantamento falado em tudo. Enquanto diminui o tempo necessário para liberar o Kidō, que enfraquece em -50% drasticamente o feitiço/kidō. Embora ninguém versado em Kidō pode usar esta técnica, é mais eficaz quando feito por um profissional qualificado, caso contrário, o feitiço pode falhar completamente(ou seja, ; o feitiço explode no rosto do usuário). Os especialistas mais qualificados são capazes de usar essa técnica para efeito surpreendente. 

❐➮ Kōjutsu Eishō (後述詠唱, "Encantamento falados-Depois"): Uma classe de encantamento Kidou, onde o encantamento é recitado após o início da magia, a fim de ligá-lo. Até agora, apenas Hachigen Ushōda tem sido visto usando esta técnica, a fim de reforçar a natureza de sua Ryūbi não Jomon durante sua luta contra Baraggan Louisenbairn. Kidou é comumente visto utilizado em casos de ataques de surpresa, ao invés de completa investida, sendo mais eficaz quando o adversário não o vê chegando. Kidou também é utilizável apenas com o nome da magia, encantamento e número respectivo por especialistas e mestres nesta arte.

┈── _*Sistema(RPG)*_

❐➮ Como explicado no exposto acima, a classificação dos Kidous é baseado numa escala de 1 à 99. A escala é uma medida de dificuldade, sendo o número 1 mais fácil, enquanto o 99 é o mais poderoso e difícil de ser executado.

❐➮ Aprendizagem de Kidous baseia-se obviamente em seu número. Cada kidou deverá ser treinado de acordo com o seu nível, sendo necessário uma determinada quantidade de linhas. Em termos simples, Kidous de N° 1 à 40 deverão possuir de 10 à 50 linhas, individualmente em cada cena de treinamento. Kidous acima de 40 deverão possuir de 50 à 70 linhas em cada cena de treinamento, individualmente.
Obs: A quantidade de linhas com base no exposto acima ficará a critério do player. No entanto, vale-se ressaltar que, não deve ser utilizado o mínimo de linhas para Kidous de escala média ou superior. Para manter uma certa lógica e equilíbrio entre os Shinigamis, cada kidou será disponível para treinamento, de acordo com o nível do determinado Shinigami.

❐➮ Nível 1 à 26.
➮ Kidou, escala de 1 à 26.
> Dano, Defesa e Velocidade: Definidos pela reiatsu.
> Gasto: 50 para kidō 1 aos 10. 200 para kidō 11 aos 26. Limite de 3 kidō por combate.

❐➮ Nível 27 à 40.
➮ Kidou escala de 27 à 40
> Dano, Defesa e Velocidade: Definidos pela reiatsu.
> Gasto: 300 para kidō 27 aos 30. 500 para kidō 31 aos 40. Limite de 3 kidō por combate.

❐➮ Nível 41 à 70.
➮ Kidou escala de 40 à 88.
> Dano, Defesa e Velocidade: Definidos pela reiatsu.
> Gasto: 1.000 para kidō 41 aos 60. 3.000 para kidō 61 aos 80. Limite de 3 kidō por combate.


❐➮ Nível Capitão: Tem total liberdade para aprender Kidous de 1 à 88, sem a necessidade do respectivo nível.
❐➮ Nível Comandante Geral: Tem total liberdade para aprender Kidous de 1 à 99 +2 Kidos proibidos, sem a necessidade do respectivo nível.

❐➮ Kidous sem numeração: Existe alguns Kidous que não possuem uma numeração de identificação. Neste caso, deve-se sempre levar o caso para algum adm, para assim obter uma análise mais completa, decidindo se terá permissão de aprendizagem ou não. Vale-se ressaltar que, a maioria desses kidous são de alto nível.
❐➮ Kidous Proibidos: Este tipo de kidou é totalmente proibido, não somente o treinamento, como também a insistência de aprendizagem. Somente em casos extremos, envolvendo o bem estar da Soul Society, ou de suas determinadas áreas de proteção, será permitido o uso deste tipo de kidou.
➮Obs: Vale-se ressaltar que, cada kidou deverá ser treinado de acordo com o seu nível, ou seja, um kidou N° 31 deverá ser treinado por alguém no nível 31 ou superior. Deste modo será mantido um equilíbrio de poder e aprendizagem.

❐➮ Bônus - Criação: Em eventos ou missões será possível obter a chance de criar/ganhar seu próprio feitiço/kidō porém apenas aqueles com destaque em missões pode ter uma chance destas.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── 𝙓𝘾𝙐𝙏𝙄𝙊𝙉 • 執行 ─ _"𝘼𝙨 𝘾𝙤𝙧𝙧𝙚𝙣𝙩𝙚𝙨 𝙙𝙤 𝙋𝙤𝙙𝙚𝙧 𝙋𝙚𝙧𝙙𝙞𝙙𝙤"_
_“𝙊 𝙥𝙤𝙙𝙚𝙧 𝙦𝙪𝙚 𝙛𝙤𝙞 𝙩𝙞𝙧𝙖𝙙𝙤... 𝙥𝙤𝙙𝙚 𝙨𝙚𝙧 𝙧𝙚𝙚𝙨𝙘𝙧𝙞𝙩𝙤.”_
━━━━━━━━━━━━━━━━━━━━━━━━
➻  Xcution é umɑ orgɑnizɑçα̃o compostɑ por humɑnos com hɑbilidɑdes especiɑis chɑmɑdɑs Fullbring, que mɑnipulɑm ɑ ɑlmɑ dos objetos. Cɑdɑ membro teve contɑto com energiɑ espirituɑl em ɑlgum ponto de suɑs vidɑs — normɑlmente ɑntes mesmo de nɑscer — por isso desenvolverɑm poderes únicos. Ao contrάrio dɑs outrɑs fɑcções, ɑ Xcution ɑtuɑ nɑs sombrɑs do mundo humɑno, sem exércitos, mɑs com estrɑtégiɑs ɑfiɑdɑs e tɑlentos singulɑres. Seu objetivo? Restɑurɑr o que foi perdido. Redefinir o conceito de poder. Subverter os pɑpéis. E no processo... queimɑr tudo o que veio ɑntes.
﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* A X-Cution funciona como uma sociedade secreta exclusiva para Fullbring.

*O2 •* Para entrar em contato com tal organização é necessário contatar o líder ou um dos membros em eventos ou missões.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Mais abaixo se encontra informações sobre o grupo e dos requisitos para se tornar um membro.*_

❐➮ *Informações do grupo:* O grupo tem o principal foco em ajudar fullbrings, em faze-los trabalhar em equipe e evoluir para benefício do grupo, ao contrário das outras raças a X-Cution não é a organização dos fullbring, e sim um grupo, oque significa que pode haver outros grupos diferentes desconhecidos.

❐➮ *Lider:*
❶ • Nível necessário desconhecido.
❷ • Reiatsu equivalente a um capitão. 
❸ • Obter destaque em missões e eventos.
❹ • Possuir objeto vetor em forma final.
❺ • Permissão da Staff(Adm's).

❐➮ *Braço direito:*
❶ • Nível necessário desconhecido.
❷ • Reiatsu equivalente a um tenente.
❸ • Bringer Light formidável.
❹ • Possuir Objeto Vetor Completo.
❺ • Permissão da Staff(Adm's).

❐➮ *Membros comum do grupo:*
❶ • Nível superior ao 5.
❷ • Possuir reiatsu comum ou melhorada.
❸ • Permissão da Staff(Adm's).

❐➮ *Caso já possua todos os requisitos necessários para obter um determinado cargo, basta simplesmente notificar algum dos adm's. Deste modo, uma avaliação será feita, para obter uma confirmação detalhada e assim seder-lhe o cargo desejado.*

┈── _*Informações adicionais*_

❐➮ Informações Extras:
> 𝙎𝙞𝙢𝙗𝙤𝙡𝙤: ❖
> 𝙇𝙞𝙙𝙚𝙧𝙖𝙣𝙘𝙖 𝙎𝙪𝙥𝙧𝙚𝙢𝙖: 𝙆ū𝙜𝙤 𝙂𝙞𝙣𝙟ō
> 𝙎𝙚𝙙𝙚: 𝙉𝙖𝙧𝙪𝙠𝙞 𝘾𝙞𝙩𝙮 (𝙎𝙪𝙗𝙢𝙪𝙣𝙙𝙤 𝙃𝙪𝙢𝙖𝙣𝙤)
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Fullbringer*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Espiritualmente conscientes, Fullbringers não são uma raça específica, são humanos com poderes especiais, estes poderes consiste em manipular as almas em toda a matéria física, como por exemplo um poste ou uma cadeira. Seus poderes originam-se de hollows, logo são formados por uma reiryoku hollow. Cada Fullbringer tem um pai/mãe que sobreviveu a um ataque hollow, com isto resquícios do poder hollow permaneceram nos corpos de seus pais/mães, e assim que nascem seus pais transmitem o resquícios de poder hollow dando origem aoa Fullbringers.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Fullbringers usam seu poder com/no corpo físico, devido a isto devem treinar bastante para forjar sua resistência afim de usar o Fullbringer bem. 

*O2 •* Quando mortos, suas habilidades são levadas consigo, para a vida após a morte.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Mais abaixo se encontram as habilidade Fullbringer.*_

❐➮ *Fullbringer (完現術者 (フルブリンガー):* Esta habilidade permite a tais manipular as almas contidas na matéria. Tudo, ate mesmo objetos rudimentares como postes, possuem uma alma, por menor que ela seja. Ao usar esta habilidade para "puxar" a alma, os Fullbringers manipulam o movimento do objeto ou ate mesmo alteram suas características físicas. Todos os Fullbringers nascem com esta habilidade, mas a idade em que percebem que o possui varia de Fullbringer para Fullbringer. 
➮ *Requisitos:* Inicialmente ja começa com tal habilidade. Constante melhora.

❐➮ *Consciência Espiritual:* Os fullbrings são capazes de ver e interagir com seres espirituais normalmente. 
➮ *Requisitos:* Ja possui inicialmente.

❐➮ *Bringer Light (完 現 光, - Full Manifestation Light ):* Ao usar a habilidade de extrair a alma na terra/solo sob seus pés ou ate aproveitando o ar em torno deles, acabam por aumentar a sua elasticidade, aumentando a capacidade de salto com isto. Tais movimentos possuem uma luz verde chamada "Luz de Bringer", que é a preliminar dos movimentos de alta velocidade. Essa técnica aumenta a velocidade do usuário em 2x o atributo destreza do usuário, por exemplo se você possui 100 vai para 200. Gasto: 200 Reiatsu inicialmente.
➮ *Requisitos:* Possuir nivel 8, basta realizar uma cena de 30 linhas aprendendo a técnica. 

❐➮ *Afinidade material (材料親和性 - Zairyō shinwa-sei):* Todo fullbringer possui algo material que ele pode criar um apego, o apego material que o fullbringer em questão possui é oque permite que ele consiga manipular a alma de tal coisa e desta forma ganhar uma habilidade. Por isso é importante o fullbringer manter seu apego ao material bem forte, pois com muito treinamento e apego pode chegar a evoluir a ponto de enfrentar inimigos ferozes.
➮ *Requisitos:* Ler o sistema de afinidade.

❐➮ *Objeto Vetor (ベクトルオブジェクト - Bekutoruobujekuto):* Um item que o fullbring possui um apego, pode ser um pingente ou video game ate mesmo alguma parte do corpo da pessoa como os braços.
➮ *Requisitos:* Já começa com 1 objeto.

❐➮ *Transferência de energia*: É possível que outros Fullbringers transfiram suas habilidades para outro Fullbringer devido a natureza hollow em comum. Fazendo isto podem se livrar de seus poderes, oque os torna humanos comuns quando compartilham completamente suas habilidades. Um Fullbringer pode roubar o Fullbring de uma outra pessoa para usa-lo pra si próprio se atacar o Fullbring de forma desprevenida. É necessário uma interação longa ou combates consideráveis entre os Fullbrings para tal transferência, de modo que caso o ladrão não saiba inteiramente como funciona o fullbring do outro, poderá acabar selando os próprios poderes por um tempo. Um fullbring consegue suportar apenas +4 Fullbrings consigo.
➮ *Requisitos:* Desconhecidos por enquanto.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Criação de Objeto Vetor e Afinidade Material*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Este Role-Playing Game, ou RPG, é um gênero de jogos onde os jogadores criam um personagem e um mundo fictício. Nestes jogos não há ganhadores ou perdedores, estimula a criatividade e raciocínio lógico. A Criação de objeto vetor é um benefício da qual todos os players recém chegados podem utilizar para criar a principal arma que vai lhes auxiliar em todo o decorrer de sua história dentro deste RPG, caso escolha ser um fullbringer. Para isso ser feito sem nenhum problema, os players devem seguir uma lista de regras e observações anexadas abaixo, que devem ser lidas com atenção e seguidas perfeitamente. Algumas delas retiradas da obra e outras para o melhor funcionamento e equilíbrio do RPG.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Os Objetos Vetores podem ser qualquer coisa material. Exemplos como um par de botas, um amuleto, um video game, o próprio braço do fullbringer, e por ai vai.

*O2 •* A afinidade que o Fullbringer tem com seu objeto determina o grau de poder que pode extrair e usar para benefício próprio. 

*03 •* Um fullbringe pode conceder poderes ao objeto além de mudar sua forma também. 

*04 •* Fullbrings podem ser definidos por alguns tipos, como os que encobrem seus usuários com seu poder, são chamados de Clad-Type.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Mais abaixo se encontra informações de como criar seu objeto vetor e aumentar sua afinidade material.*_

❐➮ *Afinidade material (材料親和性 - Zairyō shinwa-sei):* Quando tem um objeto que possui uma grande afinidade ou ate mesmo é uma preferência sem igual a outro, um Fullbringer pode conceder poderes a este objeto mas também pode mudar sua forma física, a afinidade pode ser definida pelo amor ou carinho pelo objeto. Este poder é despertado através de uma forte emoção associada ao objeto, como orgulho. Com esta afinidade, ao usa-la o Fullbringer retira a alma do objeto e o impulsiona com o seu próprio, transformando-o no processo. Uma vez que o Fullbringer tenha percebido completamente esse poder, suas habilidades não mudam e não podem mudar com o crescimento. Mas para usar suas habilidades ao máximo devem progredir ate um determinado nível. 

❐➮ *Objeto Vetor (ベクトルオブジェクト, Bekutoruobujekuto) - Forma Base:* Quando o fullbring extrai a alma do objeto que possui afinidade ele consegue fazer o objeto assumir uma forma base, como por exemplo um pingente assumir a forma de uma espada. Mas é apenas isto, apenas a forma materializada do fullbring sem nenhuma habilidade do objeto sendo possível ser usada.
➮ *Requisitos:* Ja começa com esta habilidade. 

❐➮ *Objeto Vetor (ベクトルオブジェクト, Bekutoruobujekuto) - Forma incompleta:* E ao decorrer do processo de evolução, o Fullbring atinge estágios diferentes de sua forma base e final além de poder serem considerados "incompletos". Nesta forma o fullbring consegue usar o objeto vetor transformado e também ganha sua habilidade única e especial do fullbring.
➮ *Requisitos:* Libera a partir do nível 7, necessário possuir uma reiatsu equivalente a de um oficial e realizar uma cena liberando esta forma.

❐➮ *Objeto Vetor (ベクトルオブジェクト, Bekutoruobujekuto) - Forma final:* Quando o potencial do Fullbring é totalmente percebido e progride para sua forma final, ele libera uma explosão de energia que pode causar danos ao corpo do usuário e devido a isto é necessário outro Fullbringer para supervisionar o processo e impedir a explosão suprimindo ela ou que tal explosão prejudique seu usuário.
➮ *Requisitos:* Requer nível desconhecido. Reiatsu equivalente ao nível tenente ou capitão além de uma cena atingindo tal forma pela primeira vez.

❐➮ *Aceleração:* Uma forma de promoção/crescimento do Fullbring é sua exposição ao Hueco Mundo, oque simboliza a natureza hollow. O poder do Fullbring depende bastante do objeto usado como foco. Objetos materiais possuem memórias em suas almas quando o seu possuidor vivência vários eventos, de modo que Fullbringers com uma grande quantidade de experiência de batalha antes de despertar seu poder possuem Fullbrings mais fortes. Aqueles que por algum motivo entre no hueco mundo e lute por algumas vezes acabará podendo ganhar +1 habilidade para seu fullbring na próxima forma que evoluir, por exemplo se estiver na forma base, na forma incompleta terá 2 habilidades invés de 1. Caso esteja na forma final permite o fullbring desenvolver uma nova forma com a habilidade extra. A aceleração faz o Fullbring quando usado na forma final, aumenta o status do usuário em 2x.
➮ *Requisitos:* Desconhecido por enquanto.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Criação de Resurrección*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Resurrección (帰 刃 (レ ス レ ク シ オ)), Resurekushion; espanhol para "Ressurreição", japonês para "Lâmina Retornante") devolve a essência das habilidades ofensivas ocas de um arrancar a seus corpos humanóides. Arrancar normalmente selam os núcleos de suas habilidades na forma de uma espada, que é totalmente diferente do que os Shinigami usam. Quando liberam os selos de suas armas, liberam seu verdadeiro poder e sua verdadeira forma. 

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* O único momento em que eles podem retornar à forma humana é quando eles selam novamente seus poderes na forma de espada. 

*O2 •* Mudar sua forma sem selar seus poderes em uma espada é o mesmo que queimar um braço, e se eles descartarem parte de sua forma liberada, enquanto nela, nunca mais poderão voltar ao normal. 

*O3 •* A Resurrección mais conhecida dá ao usuário do Arrancar uma aparência de animal, mas esse nem sempre é o caso. 

*O4 •* Enquanto a maioria dos Shinigami zampakutou não lançados, toma a forma de uma katana ou wakizashi, há um alcance significativamente mais amplo para o Arrancar. Exemplos típicos incluem uma grande variedade de armas brancas, como sai, machados ou armas de formato exclusivo como apêndices orgânicos ou um ser consciente. 

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*A seguir veja as etapas que uma Resurrección possui e seus requisitos.*_

❐➮ *Habilidade Natural:* Ao atingir a forma arrancar, alguns desenvolvem habilidades naturais que possuem ligação com seu poder principal na forma liberada. Como exemplo uma barreira de desaceleração de movimentos para um arrancar com aspecto da velhice do tempo, e por aí vai. O arrancar terá apenas 2 habilidades em seu estado padrão, ligada a sua ressurreição onde a primeira habilidade será desbloqueada no nível 20 enquanto a segunda será liberada no nível 25
➮ *Requisitos:* Possuir nível acima do 20. Reiatsu equivalente a um oficial ou ou tenente. 

❐➮ *Primeira Etapa:* A liberação da primeira etapa Arrancar aumenta drasticamente a viabilidade de combate e o poder do Arrancar em questão, e permite que eles tenham acesso total a todas as suas habilidades. O formulário pós-lançamento geralmente reflete em vários graus a aparência do Arrancar como um puro oco. Uma ressurreição restaura um Arrancar à sua forma "verdadeira", resultando em vários aumentos significativamente na velocidade, força, resistência, durabilidade e poder espiritual, além de permitir o acesso a variações mais poderosas de técnicas anteriores e habilidades completamente novas. Alguns Arrancar até ganham novas armas como parte de sua forma liberada.  
➮ *Requisitos:* Desconhecido por agora.

❐➮ *Segunda Etapa:* A mais poderosa e originária forma do arrancar que por ventura demonstra mais alterações físicas tornando o arrancar semelhante se não igual a sua forma oca pura, obtendo capacidades de feitos superiores aos de um arrancar na primeira etapa.
➮ *Requisitos:* Desconhecidos por agora.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Hierarquia e Evolução Arrancar/Hollow*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Arrancar/Hollow possui cargos entre si e evoluções, no rpg, todos iniciam como um adjucha, este sistema tem como base informar as classes, cargos e evoluções dos arrancar/hollows no rpg.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* Apesar de todos serem adjucha, são inicialmente equivalentes a nível de um shinigami comum, quincy comum e etc. 

*02 •* Vários hollows/arrancar podem ter seus buracos hollows em outros locais além do peito.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Logo abaixo veja as evoluções que um arrancar/hollow possui.*_

❐➮ *Adjucha:* Todos iniciam nessa forma e permanecem nela até atingir o nível 15, onde conseguem quebrar sua máscara para evoluir para um arrancar.

❐➮ *Arrancars:* É a forma que o adjucha obtém ao quebrar sua máscara, se assemelhando a forma dos humanos e shinigamis. É dito que esta forma é a mais complexa de se atingir.

❐➮ *Vasto Lorde:* Informações para atingir tal nível, desconhecidas por enquanto.

┈── _*Logo abaixo veja os cargos que um arrancar pode chegar a possuir.*_

❐➮ *Exéquias:* Grupo de extermínio semelhante ao Onmitsu Kidou dos Shinigamis. Acatam as ordens dos Espadas. Para fazer parte deles, basta possuir forma arrancar e requisitar os adms para aquisição do cargo.

❐➮ *Espadas:* São a elite dos Arrancars, enumerados inicialmente de 1 a 10 em ordem decrescente de poder (sendo que o de número 1 é o mais forte de todos). Quando um Número prova ser forte o bastante, ele entra para os Espadas, e o Espada abaixo do nível deste é rebaixado, tornando-se um Privarón Espada. Quando o espada número 10 libera sua Ressuréction, torna-se o espada número 0 e a contagem torna-se de 0 a 9. Para saber mais informações dos Espada basta ler o sistema deles.

❐➮ *Privarón Espada:* São os Espadas que foram substituídos por outros mais fortes, perdendo sua numeração antiga e recebendo uma numeração de 3 dígitos, iniciando no 100.

❐➮ *Números:* São os Arrancars mais fracos, enumerados de 11 à 99, sendo que seus números muitas vezes não existem.

❐➮ *Escudos:* São Números livres, que não foram escolhidos por um Espada. 

❐➮ *Fraccíons:* Tem como objetivo servir um Espada até a morte dele. Para ser um fraccion basta ser escolhido pelo Espada, não importa seu nível e poder atual.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── *Arrancars - Hollows Adjucha*
━━━━━━━━━━━━━━━━━━━━━━━━
➻ Arrancar (破面 (アランカル), "Máscara Quebrada") Arrancar é o nome dado aos Hollows que retiraram suas máscaras. Quando um Hollow atinge determinado nível de poder e consciência, adquirindo no processo uma Zanpakutō. Eles não utilizam Shikai e muito menos Bankai, mas uma técnica de liberação chamada de Resurrección, a qual eles ganham aparência semelhante a de quando eram Hollows (podendo ser realizado por qualquer Hollow, seja comum ou até mesmo Vasto Lorde, mas o processo é irreversível). Arrancars se diferem de outros Hollows pela retirada parcial de suas máscaras. A maioria dos Arrancars tendem a ter forma humana, mas mantém alguns de seus traços hollow como o buraco em seus corpos e os restos de suas antigas máscaras ainda presas em seus rostos, embora nem sempre adquiram forma totalmente humana, o que aparenta depender do nível de evolução do hollow, tornando os Vastos Lordes e Adjuchas mais propensos a readquirir forma humana, ao contrário de um Gillian.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋

*01 •* O player ja começa com seu personagem na forma Adjucha mas consegue algumas habilidades padrão dos hollows aqui.

﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋

┈── _*Vejam a seguir algumas das habilidades gerais dos hollows e arrancar.*_

❐➮ *Bala* _*(虚 弾 (バ ラ), bara, espanhol para "Projétil", japonês para "Projétil de Hollow")*:_ É uma técnica ofensiva exclusiva de Arrancar. Enquanto semelhante em função de um Cero, um Bala não é tão poderoso, mas, graças à sua composição, sua velocidade é de ate 20 vezes mais rápida, permitindo que ele seja disparado rapidamente. Além disso, possui força mais compulsiva do que um Cero típico faz. A velocidade e o poder globais de um Bala variam de acordo com o Arrancar utilizador. A velocidade da bala inicialmente equivalente a 20% a mais do atributo velocidade, já seu potencial de dano inicialmente é de 10% do atributo reiatsu. Esses valores aumentam a cada nível ultrapassado, a cada nível aumenta em +10% a velocidade e +5% o dano baseado no atributo reiatsu, chegando no máximo de +120% de velocidade e 50% o atributo reiatsu.
➮ *Requisitos:* Liberado a partir do nível 15 e ser arrancar, para aprender basta realizar uma cena de 20 linhas aprendendo a técnica. 

❐➮ *Sonído* _*(響 転 (ソニード), Sonīdo, espanhol para "Som", japonês para "Cerimônia de som")*:_ Uma técnica de movimento de alta velocidade do Arrancar. Embora um pouco parecido com Hohō no que diz respeito à função e velocidade, Sonído parece ser mais instintivo, aparentemente não requer conhecimento prévio. Produz um som diferente; Ao invés do shunpo shing do Shinigami, que suaviza ou às vezes silencioso, ele faz um barulho explosivo ou estático. Essa técnica aumenta inicialmente a velocidade do usuário em 2x o atributo velocidade do usuário, por exemplo se você possui 100 pode se mover a 200. Gasto: 200 Reiatsu inicialmente.
➮ *Requisitos:* Liberado a partir do nível 8 ser adjucha, para aprender basta realizar uma cena filler de 30 linhas usando a técnica pela primeira vez.

❐➮ *Cero* _*(虚闪(セロ), Sero; Espanhol para "Zero", Japonês para "Flash Oco")*:_ Cero é um ataque usado por Menos Grande, Arrancar e Vaizard. O praticante dispara uma poderosa explosão de energia espiritual concentrada no alvo. Enquanto na maioria dos casos ele é acionado a partir da boca, alguns Arrancar e Vaizard podem disparar Cero de suas mãos, dedos e outras partes de seus corpos. A área de energia, a força, a velocidade e a explosão do Cero é dependente da força, poder espiritual, e, por vezes, a habilidade do utilizador (isto é, quanto mais forte o utilizador, mais forte é o ataque). O tempo de carregamento e disparo para Cero varia muito, de cobrar relativamente rápido para queima-lo para disparar instantaneamente um sem muita carga. O cero pode ter um dano equivalente ate mesmo a 100% do atributo reiatsu, inicialmente o dano do cero é de 50% do atributo reiatsu, a velocidade do cero chega a 100% do atributo reiatsu, inicialmente é de 50%. A cada nível ultrapassado ganha +10% ate chegar no máximo permitido. Gasto: 300 por cero.
➮ *Requisitos:* Liberado a partir do nível 1, para aprender basta realizar uma cena filler de 20 linhas.

❐➮ *Gran Rey Cero* _*(王虚の閃光 (グラン・レイ・セロ), guran rei sero; Espanhol para "Grande Zero Rei", Japonês para "Flash Hollow Real")*:_ Para executar esta variação potente do Cero, o Arrancar primeiro desenha o sangue do apêndice Cero de geração utilizando a sua Zanpakutō, em seguida, carrega o Cero ao misturar o sangue com ele. O resultado é um Cero com uma potência muito maior de ataque e velocidade, bem como uma alteração de cor única para o Espada. O gran rey cero tem um dano equivalente a 200% do atributo reiatsu e sua velocidade equivale a 100% do reiatsu do usuário. 
➮ *Requisitos:*  Liberado apenas ao se tornar um Espada.

❐➮ *Cero Oscuras* _*セ 虚 閃 (セロ・オキキュラス) Rōmajisero osukyurasu English/Espanhol para "Dark Zero". Japonês para "Black Hollow Flash" Cero Oscuras, sero osukyurasu.)*:_ O Cero Oscuras, ou Cero Negro, é muito mais poderoso do que um Cero médio, com um vasta alcance e poder de ataque massivo. Reunindo o poder de seu reiatsu, condensando-o em um único ponto e atira contra seu inimigo, podendo, destruir metade do domo localizado sobre Las Noches com certa facilidade. O cero oscuras tem um dano equivalente a 3x do atributo reiatsu. 
➮ *Requisitos:* Liberado apenas na primeira etapa.

❐➮ *Arrancar* _*(破面 (アランカル), "Máscara Quebrada":*_ É quando o Adjucha pode quebrar sua máscara, desta forma obtendo acesso a uma forma mais humanoide e uma Zanpakutõ no processo. Aqueles que realizam este processo obtem uma quantia significativa em seus atributos, a quantia é revelada apenas após o adm avaliar a cena.
➮ *Requisitos:* Possuir no mínimo o nível 15, realizar uma cena filler quebrando a máscara, possuir reiatsu equivalente a de um oficial shinigami. 

❐➮ *Resurrección* _*(帰刃(レス レクシオン), Resurekushion; Espanhol para "Ressurreição", Japonês para "Retornando Espada")*:_ Liberando o núcleo da capacidade de um Arrancar selado em sua Zanpakutō para recuperar os poderes originais de um Hollow. Eles muitas vezes assumem uma forma mais próxima de um Hollow que um ser humano após a realização de Resurrección.
➮ *Requisitos:* Favor ler o sistema de Resurrección.

❐➮ *Descorrer* _*(解空(デス コレール), Desukorēru; Japonês para "Vácuo Desligado", Espanhol para "Desenho de Retorno/Abertura")*:_ A técnica usada por Hollows, Arrancar e às vezes outros como Adjuchas, para abrir uma Garganta entre os mundo dos vivos e Hueco Mundo.
➮ *Requisitos:* Já começa com esta habilidade liberada.

❐➮ *Hierro* _*(钢皮(イエロ), Iero, Espanhol para "Ferro", Japonês para "Pele Aço"):*_ É a pele exterior de um Arrancar com alta dureza espiritual que serve como armadura. Inicialmente aumenta a resistência em +30%.
➮ *Requisitos:* Obtém tal característica ao atingir o nível 18.

❐➮ *Pesquisa* _*(探查回路(ペスキサ), Pesukisa; Espanhol para "Pesquisa", Japonês para "Circuito de Inquérito")*:_ Uma habilidade Arrancar para medir e localizar a pressão espiritual, e desta forma obter uma previsão parcial dos movimentos do inimigo. Se o inimigo tiver a velocidade inferior ao intelecto do usuário, seus movimentos serão previstos 1 vez a cada 2 turnos.
➮ *Requisitos:* Liberada no nível 15, para aprender basta realizar uma cena filler de 30 linhas.

❐➮ *Amplificação de Regeneração:* Devido ao controle de reiatsu do arrankar, tal pode usar de sua própria reiatsu para acelerar sua regeneração, quanto maior a maestria em regeneração mais rápido e maiores quantidades de células poderam ser aceleradas para amplificar a regeneração podendo até regenerar membros inteiros em segundos gerando alto custo de reiatsu, feitos como o citado agora pouco, pode ser feito apenas aos que possuir maestria nível 4. Essa habilidade pode ser usada apenas 3 vezes em batalha, como é algo natural, com o tempo o arrancar se recupera normalmente. Os que não escolherem a maestria de regeneração, podem se curar apenas de ferimentos medianos, os que escolher a maestria de regeneração podem curar ate membros perdidos no nível 4 de maestria.
➮ Requisitos: Todo hollow e arrancar começam com esta habilidade.
[24/5 04:00] Besk | L Lover: 🔮 ⃝ •── 𝙊𝙨 𝘿𝙚𝙯 𝙀𝙎𝙋𝘼𝘿𝘼 • 十刃 ─ _"𝙊𝙨 𝘿𝙚𝙯 𝙈𝙖𝙣𝙙𝙖𝙢𝙚𝙣𝙩𝙤𝙨 𝙙𝙖 𝙍𝙪𝙞𝙣𝙖"_
_“𝘼 𝙢𝙤𝙧𝙩𝙚 𝙩𝙚𝙢 𝙛𝙤𝙧𝙢𝙖𝙨. 𝙀 𝙘𝙖𝙙𝙖 𝙪𝙢𝙖 𝙙𝙚𝙡𝙖𝙨 𝙘𝙖𝙧𝙧𝙚𝙜𝙖 𝙪𝙢 𝙣𝙤𝙢𝙚.”_
━━━━━━━━━━━━━━━━━━━━━━━━
➻  Os Espɑdɑ sα̃o os ɑrrɑncɑr mɑis poderosos do Hueco Mundo — Hollows que ɑrrɑncɑrɑm suɑs mάscɑrɑs pɑrɑ ɑlcɑnçɑr um estɑdo superior. Liderɑdos por Barragan durɑnte suɑ rebeliα̃o, eles representɑm os ɑspectos dɑ morte: Desespero, Destruiçα̃o, Vingɑnçɑ, Sɑcrifício, entre outros. Cɑdɑ um cɑrregɑ umɑ numerɑçα̃o de 0 ɑ 9, refletindo seu poder espirituɑl e hierɑrquiɑ. Inumɑnos, implɑcάveis, e ɑindɑ ɑssim... trάgicos. Os Espɑdɑ nα̃o sα̃o ɑpenɑs guerreiros: sα̃o símbolos. A memóriɑ vivɑ dɑ dor, do vɑzio e dɑ eternidɑde perdidɑ.
﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
*O1 •* É proíbido para qualquer Espada executar o Gran Rey Certo dentro de Las Noches.

*O2 •* Rebaixamento: Um Espada pode ser rebaixado do grupo quando perde força. 
﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋
┈── _*Requisitos para cada espada.*_

```Requisito básico para todos os ranks de espadas:``` ter quebrado sua máscara e ter se tornado arrancar


❐➮ *10°/0° Espada:* 
❶ • Ser nível 15.
❷ • Ser o mais poderoso(maior quantidade de força e resistência).
❸ • Reiatsu Nível Oficial.
❹ • Necessário ser um player ativo, ausências podem levar á substituição.

❐➮ *9° Espada:* 
❶ • Nível acima de 15.
❷ • Reiatsu nível oficial.
❸ • Ser arrancar.
❹ • Permissão do Líder do Las Noches.

❐➮ *8° Espada:* 
❶ • Nível superior ao 25.
❷ • Reiatsu nível Oficial.
❸ • Gênio, um arrancar de inteligência digna de aplausos. 
❹ • Ser arrancar.

❐➮ *7° Espada:* 
❶ • Nível superior ao 25.
❷ • Reiatsu nível Oficial.
❸ • Possuir sonido.
❹ • Possuir Pré-Resurrección.
❺ • Permissão da Staff(Adm's).

❐➮ *6° Espada:* 
❶ • Ser nível 35.
❷ • Reiatsu Nível Tenente.
❸ • Ser arrancar.
❹ • Possuir Resurrección.
❺ • Permissão da Staff(Adm's).

❐➮ *5° Espada:* 
❶ • Ser nível 35.
❷ • Reiatsu Nível Capitão.
❸ • Ser arrancar.
❹ • Possuir Resurrección.
❺ • Permissão da Staff(Adm's).

❐➮ *4° Espada:* 
❶ • Nível mínimo desconhecido.
❷ • Reiatsu acima de capitão.
❸ • Possuir ressurreción completa.
❹ • Desconhecida

❐➮ *3° Espada:*
❶ • Nível mínimo desconhecido.
❷ • Reiatsu acima de capitão.
❸ • Desconhecida.
❹ • Possuir Resurrección completa.

❐➮ *2° Espada:* 
❶ • Nível mínimo desconhecido.
❷ • Desconhecido.
❸ • Reiatsu Acima de Capitão.
❹ • Possuir Resurrección completa.
❺ • Derrotar 1 Vasto Lorde ou Capitão sozinho.

❐➮ *1° Espada:* 
❶ • Desconhecido.
❷ • Mestre em Sonido. Mais especificamente, o possuidor do sonido mais rápido e mestre em cero.
❸ • Maior Reiatsu dentre todos os Espadas.
❹ • Possuir Resurrección completa.
❺ • Necessário ser um player muito 
ativo, ausências podem levar à substituição.

❐➮ *Caso já possua todos os requisitos necessários para obter um determinado cargo, basta simplesmente notificar algum dos adm's. Deste modo, uma avaliação será feita, para obter uma confirmação detalhada e assim seder-lhe o cargo desejado.*


❐➮ _Informações Extras:_
> 𝙎𝙞𝙢𝙗𝙤𝙡𝙤: 𝙉𝙪𝙢𝙚𝙧𝙤 𝙩𝙖𝙩𝙪𝙖𝙙𝙤 𝙣𝙤 𝙘𝙤𝙧𝙥𝙤
> 𝙇𝙞𝙙𝙚𝙧𝙖𝙣𝙘𝙖 𝙎𝙪𝙥𝙧𝙚𝙢𝙖: 𝘽𝙖𝙧𝙧𝙖𝙜𝙖𝙣
> 𝙎𝙚𝙙𝙚: 𝙇𝙖𝙨 𝙉𝙤𝙘𝙝𝙚𝙨""".strip()

padrao = re.compile(r'^\[(.*?)\] (.*?): (.*)', re.DOTALL)

mensagens = entrada.split('\n[')
mensagens = [m if m.startswith('[') else '[' + m for m in mensagens]

novos_items = []

for msg in mensagens:
    match = padrao.match(msg)
    if match:
        texto = match.group(3).strip()
        item = {
            "command": "",
            "title": "",
            "categoria": "",
            "response": texto
        }
        novos_items.append(item)

# Caminho do arquivo JSON
arquivo_json = "commands.json"

# Se o arquivo existir, carrega conteúdo atual, senão começa com lista vazia
if os.path.exists(arquivo_json):
    with open(arquivo_json, "r", encoding="utf-8") as f:
        dados_atuais = json.load(f)
else:
    dados_atuais = []

# Adiciona os novos itens na lista atual
dados_atuais.extend(novos_items)

# Salva tudo de volta no arquivo, codificação UTF-8
with open(arquivo_json, "w", encoding="utf-8") as f:
    json.dump(dados_atuais, f, ensure_ascii=False, indent=4)

print(f"{len(novos_items)} novos itens adicionados no {arquivo_json} com sucesso!")
