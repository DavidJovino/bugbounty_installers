#!/usr/bin/env python3
import subprocess
import os

# Função auxiliar
def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print(f"[+] Comando executado com sucesso: {command}")
        return True
    else:
        print(f"[!] Falha ao executar: {command}")
        return False
    
# Verificar e adicionar variáveis de ambiente no .bashrc ou .zshrc
def add_go_env_vars():
    home_dir = os.path.expanduser("~")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    zshrc_path = os.path.join(home_dir, ".zshrc")
    shell_config_file = bashrc_path if os.path.exists(bashrc_path) else zshrc_path

    go_env_vars = """
    # Go environment variables
    export GOROOT=/usr/lib/go
    export GOPATH=$HOME/go
    export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    """
    # Verifica se as variáveis já estão no arquivo de configuração do shell
    with open(shell_config_file, "r") as file:
        config_content = file.read()

    if "export GOROOT=/usr/lib/go" not in config_content:
        print("[+] Adicionando variáveis de ambiente do Go no arquivo de configuração do shell.")
        with open(shell_config_file, "a") as file:
            file.write(go_env_vars)
        print(f"[+] Variáveis de ambiente adicionadas em {shell_config_file}.")
        print("[!] Por favor, execute 'source ~/.bashrc' ou 'source ~/.zshrc' para aplicar as mudanças.")
    else:
        print("[+] Variáveis de ambiente do Go já estão configuradas.")

# Verificar se o pacote Go já foi instalado
def is_go_tool_installed(tool_name):
    home_dir = os.path.expanduser("~")
    tool_path = f"{home_dir}/go/bin/{tool_name}"
    if os.path.exists(tool_path):
        print(f"[+] {tool_name} já está instalado.")
        return True
    else:
        print(f"[!] {tool_name} não está instalado.")
        return False
    
# Verificar instalações via apt
def is_apt_package_installed(package_name):
    result = subprocess.run(f"dpkg -l | grep {package_name}", shell=True, stdout=subprocess.PIPE)
    if result.stdout:
        print(f"[+] {package_name} já está instalado.")
        return True
    else:
        print(f"[!] {package_name} não está instalado.")
        return False

# Verificar instalações via pip
def is_pip_package_installed(package_name):
    result = subprocess.run(f"pip show {package_name}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"[+] {package_name} já está instalado.")
        return True
    else:
        print(f"[!] {package_name} não está instalado.")
        return False

# Funções de instalação
def install_go_program(program, repo):
    print(f"[+] Instalando {program}...")
    run_command(f"go install {repo}@latest")

def clone_and_install_git(program, repo, commands=""):
    print(f"[+] Clonando e instalando {program}...")
    home_dir = os.path.expanduser("~")
    tools_dir = f"{home_dir}/Tools/{program}"
    if not os.path.exists(tools_dir):
        run_command(f"git clone {repo} {tools_dir}")
        if commands:
            run_command(f"cd {tools_dir} && {commands}")
    else:
        print(f"[+] {program} já está instalado.")

def install_apt_program(program):
    print(f"[+] Instalando {program} via APT...")
    run_command(f"sudo apt install -y {program}")

def install_pip_program(program):
    print(f"[+] Instalando {program} via pip...")
    run_command(f"pip install {program}")

# Função principal para verificar e instalar as ferramentas automaticamente
def manage_all_tools():
    tools = {
        "Amass": {"check": lambda: is_apt_package_installed("amass"), "install": lambda: install_apt_program("amass")},
        "Anew": {"check": lambda: is_go_tool_installed("anew"), "install": lambda: install_go_program("Anew", "github.com/tomnomnom/anew")},
        "Assetfinder": {"check": lambda: is_go_tool_installed("assetfinder"), "install": lambda: install_go_program("Assetfinder", "github.com/tomnomnom/assetfinder")},
        "Airixss": {"check": lambda: is_go_tool_installed("airixss"), "install": lambda: install_go_program("Airixss", "github.com/ferreiraklet/airixss")},
        "Bhedak": {"check": lambda: is_pip_package_installed("bhedak"), "install": lambda: install_pip_program("bhedak")},
        "Cf-check": {"check": lambda: is_go_tool_installed("cf-check"), "install": lambda: install_go_program("cf-check", "github.com/dwisiswant0/cf-check")},
        "Chaos": {"check": lambda: is_go_tool_installed("chaos"), "install": lambda: install_go_program("chaos", "github.com/projectdiscovery/chaos-client/cmd/chaos")},
        "Cariddi": {"check": lambda: is_go_tool_installed("cariddi"), "install": lambda: install_go_program("cariddi", "github.com/edoardottt/cariddi/cmd/cariddi")},
        "Dalfox": {"check": lambda: is_go_tool_installed("dalfox"), "install": lambda: install_go_program("dalfox", "github.com/hahwul/dalfox/v2")},
        "Ffuf": {"check": lambda: is_go_tool_installed("ffuf"), "install": lambda: install_go_program("ffuf", "github.com/ffuf/ffuf/v2")},
        "Freq": {"check": lambda: is_go_tool_installed("freq"), "install": lambda: install_go_program("freq", "github.com/takshal/freq")},
        "Gowitness": {"check": lambda: is_go_tool_installed("gowitness"), "install": lambda: install_go_program("gowitness", "github.com/sensepost/gowitness")},
        "Goop": {"check": lambda: is_go_tool_installed("goop"), "install": lambda: install_go_program("goop", "github.com/deletescape/goop")},
        "GetJS": {"check": lambda: is_go_tool_installed("getJS"), "install": lambda: install_go_program("getJS", "github.com/003random/getJS/v2")},
        "Hakrawler": {"check": lambda: is_go_tool_installed("hakrawler"), "install": lambda: install_go_program("hakrawler", "github.com/hakluke/hakrawler")},
        "Hakrevdns": {"check": lambda: is_go_tool_installed("hakrevdns"), "install": lambda: install_go_program("hakrevdns", "github.com/hakluke/hakrevdns")},
        "Haktldextract": {"check": lambda: is_go_tool_installed("haktldextract"), "install": lambda: install_go_program("haktldextract", "github.com/hakluke/haktldextract")},
        "Haklistgen": {"check": lambda: is_go_tool_installed("haklistgen"), "install": lambda: install_go_program("haklistgen", "github.com/hakluke/haklistgen")},
        "Httpx": {"check": lambda: is_go_tool_installed("httpx"), "install": lambda: install_go_program("httpx", "github.com/projectdiscovery/httpx/cmd/httpx")},
        "Jaeles": {"check": lambda: is_go_tool_installed("jaeles"), "install": lambda: install_go_program("jaeles", "github.com/jaeles-project/jaeles")},
        "Katana": {"check": lambda: is_go_tool_installed("katana"), "install": lambda: install_go_program("katana", "github.com/projectdiscovery/katana/cmd/katana")},
        "Naabu": {"check": lambda: is_go_tool_installed("naabu"), "install": lambda: install_go_program("naabu", "github.com/projectdiscovery/naabu/v2/cmd/naabu")},
        "Notify": {"check": lambda: is_go_tool_installed("notify"), "install": lambda: install_go_program("notify", "github.com/projectdiscovery/notify/cmd/notify")},
        "Qsreplace": {"check": lambda: is_go_tool_installed("qsreplace"), "install": lambda: install_go_program("qsreplace", "github.com/tomnomnom/qsreplace")},
        "Rush": {"check": lambda: is_go_tool_installed("rush"), "install": lambda: install_go_program("rush", "github.com/shenwei356/rush")},
        "Shuffledns": {"check": lambda: is_go_tool_installed("shuffledns"), "install": lambda: install_go_program("shuffledns", "github.com/projectdiscovery/shuffledns/cmd/shuffledns")},
        "SQLMap": {"check": lambda: is_apt_package_installed("sqlmap"), "install": lambda: install_apt_program("sqlmap")},
        "Subfinder": {"check": lambda: is_go_tool_installed("subfinder"), "install": lambda: install_go_program("Subfinder", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder")},
        "Unfur": {"check": lambda: is_go_tool_installed("unfur"), "install": lambda: install_go_program("unfur", "github.com/tomnomnom/unfurl")},
        "Waybackurls": {"check": lambda: is_go_tool_installed("waybackurls"), "install": lambda: install_go_program("waybackurls", "github.com/tomnomnom/waybackurls")},
        "Gau": {"check": lambda: is_go_tool_installed("gau"), "install": lambda: install_go_program("Gau", "github.com/lc/gau")},
        "DNSgen": {"check": lambda: is_pip_package_installed("dnsgen"), "install": lambda: install_pip_program("dnsgen")},
        "Page-fetch": {"check": lambda: is_go_tool_installed("page-fetch"), "install": lambda: install_go_program("page-fetch", "github.com/detectify/page-fetch")},
        "Hednsextractor": {"check": lambda: is_go_tool_installed("hednsextractor"), "install": lambda: install_go_program("hednsextractor", "github.com/HuntDownProject/hednsextractor/cmd/hednsextractor")},
    }

    # Verificar todas as ferramentas e instalar as que não estão instaladas
    for tool_name, tool in tools.items():
        if not tool["check"]():
            print(f"[+] Instalando {tool_name}...")
            tool["install"]()
        else:
            print(f"[+] {tool_name} já está instalado.")

# Atualizando os repositorios e instalando go e as ferramentas de instalação
def main():
    run_command("sudo apt update")
    run_command("sudo apt install -y git curl wget")
    run_command("sudo apt-get install -y golang-go")
    add_go_env_vars()
    manage_all_tools()

if __name__ == "__main__":
    main()
