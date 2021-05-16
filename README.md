# Radios PT Home Assistant to Alexa
Play various Portuguese Radios on Your Alexas

![image](https://github.com/nunogako/Radios_PT-Home-Assistant-to-Alexa/blob/4cd9996b49c4edf3f8051422ae85648538f06110/Home%20Assistant%20R%C3%A1dios%20Alexa%20TuneIn.png)

### ADDONS necessários ###
A partir do Supervisor – Loja de Addons, instalar: 
- File Editor 

Depois a partir do HACS instalar os seguintes Addons no Frontend:
- Mini média player
- Button Card

### Texto a adicionar ao “configurations.yaml” ###
downloader:
  download_dir: www

homeassistant:
  packages: !include_dir_named packages

python_script:

### Pastas necessárias ###
Dentro da pasta config, criar as seguintes pastas:
“packages”
“python_scripts”
“www”

### Dentro da pasta “packages” ###
- Colocar o ficheiro “radio.yaml”  editar este ficheiro e alterar o nome do média player para o nome que o vosso tem no home assistant, a parte a vermelho no seguinte texto (podem usar a procura para não escapar nenhum):
entity_id: media_player.echo_dot_sala

### Dentro da pasta “python_scripts” colocar os ficheiros: ###
- “radio_details_megahits.py” e “radio_details.py”

### Dentro da pasta “www” ###
- Colocar a pasta “rádios logo” com os ficheiros incluídos
- Criar a pasta “downloads”

Depois destes procedimentos, vamos verificar a configuração do home assistant para verificar se está tudo OK e reiniciar.
Por fim, só falta criar o cartão na “Visão Geral (Lovelace)”.

### Lovelace card ###
Vamos a “Configurar Painel”
Clicamos em ”ADICIONAR CARTÃO” deslizar para baixo e escolher “MANUAL”.
Apagam o texto e colam o código do card correspondente, no exemplo, estou a colar o texto referente ao media player da sala. Também aqui, devem alterar todos os nomes “echo_dot_sala” para o nome do vosso media_player, podem alterar antes com um editor, e colar aqui já alterado.

Depois de feito, basta guardar e se tudo correu bem, já deve funcionar e podem clicar nas rádios correspondentes para ouvir na vosso player.

Para criar um card para outros media players, o procedimento é o mesmo, alterando para o nome correspondente. Esta configuração está preparada para 3 player’s diferentes: “echo_dot_sala”, “echo_dot_cozinha”, echo_dot_quarto”
