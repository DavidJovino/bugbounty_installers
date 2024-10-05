# Ferramenta de Instalação Automática de Ferramentas para Bug Bounty

This README is available in other languages:
- [English](README_EN.md)

Esta ferramenta automatiza a instalação de várias ferramentas utilizadas em _bug bounty_ e _pentesting_. O script verifica se as ferramentas já estão instaladas no sistema e, caso não estejam, faz a instalação automaticamente, incluindo as dependências necessárias.

## Ferramentas Instaladas

As ferramentas instaladas estão organizadas nas seguintes categorias:

### 1. Ferramentas de Reconhecimento (Reconnaissance)

- **Amass**: Ferramenta poderosa para reconhecimento de subdomínios e mapeamento de redes.
- **Assetfinder**: Ferramenta para encontrar subdomínios associados a um domínio usando várias fontes online.
- **Subfinder**: Ferramenta de enumeração de subdomínios com suporte para uma variedade de fontes.
- **Chaos**: Ferramenta para enumeração de domínios a partir do serviço Chaos da ProjectDiscovery.
- **Hakrawler**: Um web crawler simples, usado para descoberta de endpoints ocultos em sites.
- **Httpx**: Verificador rápido e configurável de URLs, suporta captura de cabeçalhos, validação de status HTTP e muito mais.
- **Gau**: Gathers URLs arquivadas do Wayback Machine, Common Crawl, entre outros, para análise de segurança.
- **Waybackurls**: Coleta URLs arquivadas pelo Wayback Machine para realizar testes em conteúdo antigo.
- **DNSgen**: Gera variações de subdomínios a partir de um domínio, útil para descoberta de subdomínios por mutação.
- **GetJS**: Ferramenta para extrair links de arquivos JavaScript e identificar possíveis endpoints interessantes.
- **Hakrevdns**: Ferramenta para realização de _reverse DNS lookup_, permitindo a descoberta de hosts a partir de endereços IP.
- **Haktldextract**: Ferramenta para extração de TLDs (domínios de topo) e SLDs (domínios de segundo nível) de URLs.
- **Cariddi**: Web crawler rápido com suporte para detecção de vulnerabilidades e exfiltração de dados de URLs.
- **Naabu**: Scanner rápido de portas que usa o pacote `libpcap-dev` para realizar varreduras.

### 2. Ferramentas de Fuzzing

- **Ffuf**: Ferramenta de fuzzing rápida, excelente para encontrar diretórios ocultos e arquivos em aplicações web.
- **Bhedak**: Ferramenta de automação para fuzzing, útil para a descoberta de vulnerabilidades de segurança.
- **Qsreplace**: Utilitário para substituição de parâmetros de query string em URLs, muito útil em testes de fuzzing.
- **Dalfox**: Ferramenta para descoberta de vulnerabilidades XSS em aplicações web, ideal para testes de segurança.

### 3. Ferramentas de Detecção de Vulnerabilidades

- **Dalfox**: Ferramenta para descoberta de vulnerabilidades XSS em aplicações web.
- **Jaeles**: Framework de automação para testes de segurança com suporte a personalização de ataques.
- **SQLMap**: Ferramenta poderosa para automação de testes de injeção SQL e exploração de falhas relacionadas.
- **Airixss**: Scanner de XSS que testa automaticamente aplicações em busca de vulnerabilidades de Cross-Site Scripting.
- **Shuffledns**: Ferramenta rápida para resolução de subdomínios que utiliza várias fontes e resolvers.

### 4. Ferramentas de Notificação e Automação

- **Notify**: Ferramenta para notificações personalizadas, ideal para integrar com ferramentas de segurança e receber alertas.
- **Rush**: Ferramenta para execução paralela de comandos com controle de limite de recursos, ideal para automação em larga escala.

### 5. Outras Ferramentas Úteis

- **Anew**: Utilitário para manipulação de listas, adiciona entradas novas sem duplicá-las.
- **Freq**: Ferramenta de análise de frequências de respostas HTTP, útil para identificar padrões anômalos em grandes conjuntos de respostas.
- **Gowitness**: Tira capturas de tela de páginas da web, coleta informações e gera relatórios.
- **Goop**: Utilitário para parsing de arquivos Go.mod, útil para gerenciar dependências em projetos Go.
- **Haklistgen**: Gera listas de palavras personalizadas para ataques de força bruta com base em várias técnicas.
- **Unfur**: Utilitário para análise de URLs e extração de componentes úteis.
- **Page-fetch**: Utilitário para coleta de conteúdo de páginas da web, útil para análise posterior.
- **Cf-check**: Verifica se um endereço IP está protegido por Cloudflare.
- **Hednsextractor**: Ferramenta para extração de informações DNS de cabeçalhos HTTP.

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
git clone https://github.com/DavidJovino/bugbounty_installers.git
cd bugbounty_installers
```

2. Executando o script de instalação

Execute o script `install_tools.py` para instalar automaticamente as ferramentas:

```bash
python3 install_tools.py
```

3. Configurando variáveis de ambiente para o Go

Se você ainda não configurou o ambiente para o Go, o script automaticamente adiciona as seguintes variáveis de ambiente no seu arquivo de configuração do shell (`~/.bashrc` ou `~/.zshrc`):

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

Para algumas ferramentas, o script também instala automaticamente as dependências necessárias. Por exemplo, para o **Naabu**, o script garante que o pacote `libpcap-dev` esteja instalado.

### Uso

Depois de executar o script de instalação, as ferramentas estarão disponíveis no seu sistema. Você pode utilizá-las diretamente no terminal, por exemplo:

```bash
amass enum -d example.com
subfinder -d example.com
naabu -host example.com
```

Como Funciona

 1. O script verifica se as ferramentas já estão instaladas no sistema.
 2. Se uma ferramenta não estiver instalada, o script faz o download e a instala automaticamente.
 3. O script também instala qualquer dependência necessária (como `libpcap-dev` para o Naabu).
 4. As ferramentas Go são instaladas no diretório `$GOPATH/bin`.

Adicionando Novas Ferramentas

Se você deseja adicionar novas ferramentas à lista de instalação automática, edite o dicionário `tools` no arquivo `install_tools.py` da seguinte maneira:

```python
tools = {
    "NovaFerramenta": {"check": lambda: is_go_tool_installed("novaferramenta"), "install": lambda: install_go_program("NovaFerramenta", "github.com/exemplo/novaferramenta")},
}
```
Basta adicionar a nova ferramenta conforme o exemplo acima, especificando como verificar a instalação e como proceder para instalá-la.
Contribuindo

Contribuições são bem-vindas! Se você quiser adicionar novas funcionalidades ou corrigir bugs, por favor, siga as etapas abaixo:

  1. Faça um *fork* deste repositório.
  2. Crie um *branch* para sua funcionalidade (`git checkout -b minha-funcionalidade`).
  3. Faça o *commit* das suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
  4. Envie o *branch* para o seu repositório (`git push origin minha-funcionalidade`).
  5. Abra um *pull request*.



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
