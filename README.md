# Ferramenta de Instalação Automática de Ferramentas para Bug Bounty

Esta ferramenta automatiza a instalação de várias ferramentas utilizadas em _bug bounty_ e _pentesting_. O script verifica se as ferramentas já estão instaladas no sistema e, caso não estejam, faz a instalação automaticamente, incluindo as dependências necessárias.

## Ferramentas Instaladas

A ferramenta atualmente suporta a instalação das seguintes ferramentas:

- **Amass**: Reconhecimento de subdomínios.
- **Anew**: Ferramenta para manipulação de listas.
- **Assetfinder**: Descoberta de subdomínios.
- **Gau**: Gathers URLs do arquivo _Wayback Machine_.
- **Httpx**: Ferramenta de verificação de URLs.
- **Jaeles**: Framework de testes de segurança.
- **SQLMap**: Ferramenta de injeção SQL.
- **Subfinder**: Ferramenta para enumeração de subdomínios.
- **DNSgen**: Gera mutações de subdomínios.
- **Naabu**: Verificador de portas com suporte a `libpcap-dev`.

## Requisitos

Antes de executar o script, certifique-se de ter as seguintes dependências instaladas:

- **Python 3**: O script utiliza Python para executar alguns comandos.
- **Git**: Necessário para clonar repositórios das ferramentas.
- **Go**: Algumas ferramentas precisam ser instaladas via `go install`.
- **Apt**: O script utiliza `apt` para instalar algumas dependências e ferramentas.

## Instalação

### 1. Clonando o repositório

Primeiro, clone este repositório para o seu sistema:

```bash
git clone https://github.com/seuusuario/suarepositorio.git
cd suarepositorio
```

2. Executando o script de instalação

Execute o script install_tools.py para instalar automaticamente as ferramentas:

```bash
python3 install_tools.py
```

3. Configurando variáveis de ambiente para o Go

Se você ainda não configurou o ambiente para o Go, o script automaticamente adiciona as seguintes variáveis de ambiente no seu arquivo de configuração do shell (~/.bashrc ou ~/.zshrc):

```bash
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```

Após a execução do script, execute o comando abaixo para carregar as novas variáveis de ambiente:

```bash
source ~/.bashrc
# ou se estiver usando Zsh
source ~/.zshrc
```

4. Ferramentas que exigem dependências

Para algumas ferramentas, o script também instala automaticamente as dependências necessárias. Por exemplo, para o Naabu, o script garante que o pacote libpcap-dev esteja instalado.
Uso

Depois de executar o script de instalação, as ferramentas estarão disponíveis no seu sistema. Você pode utilizá-las diretamente no terminal, por exemplo:

```bash
amass enum -d example.com
subfinder -d example.com
naabu -host example.com
```

Como Funciona

 1. O script verifica se as ferramentas já estão instaladas no sistema.
 2. Se uma ferramenta não estiver instalada, o script faz o download e a instala automaticamente.
 3. O script também instala qualquer dependência necessária (como libpcap-dev para o Naabu).
 4. As ferramentas Go são instaladas no diretório $GOPATH/bin.

Adicionando Novas Ferramentas

Se você deseja adicionar novas ferramentas à lista de instalação automática, edite o dicionário tools no arquivo install_tools.py da seguinte maneira:

```python
tools = {
    "NovaFerramenta": {"check": lambda: is_go_tool_installed("novaferramenta"), "install": lambda: install_go_program("NovaFerramenta", "github.com/exemplo/novaferramenta")},
}
```
Basta adicionar a nova ferramenta conforme o exemplo acima, especificando como verificar a instalação e como proceder para instalá-la.
Contribuindo

Contribuições são bem-vindas! Se você quiser adicionar novas funcionalidades ou corrigir bugs, por favor, siga as etapas abaixo:

  1. Faça um fork deste repositório.
  2. Crie um branch para sua funcionalidade (git checkout -b minha-funcionalidade).
  3. Faça o commit das suas mudanças (git commit -m 'Adiciona nova funcionalidade').
  4. Envie o branch para o seu repositório (git push origin minha-funcionalidade).
  5. Abra um pull request.



Falta programar a integracao:

Anti-burl
Filter-resolved
Findomain
Gargs
gf
github-search
GoSpider
Hudson Rock Free Cybercrime Intelligence Toolset
Html-tool
Jsubfinder
Kxss
Knoxss
LinkFinder
log4j-scan
metabigor
MassDNS
ParamSpider
SecretFinder
Shodan
subjs
unew
urldedupe
Wingman
tojson
X8
commix
xray
XSStrike
