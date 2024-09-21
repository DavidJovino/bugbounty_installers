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
        "Gau": {"check": lambda: is_go_tool_installed("gau"), "install": lambda: install_go_program("Gau", "github.com/lc/gau")},
        "Httpx": {"check": lambda: is_go_tool_installed("httpx"), "install": lambda: install_go_program("Httpx", "github.com/projectdiscovery/httpx/cmd/httpx")},
        "Jaeles": {"check": lambda: is_go_tool_installed("jaeles"), "install": lambda: install_go_program("Jaeles", "github.com/jaeles-project/jaeles")},
        "SQLMap": {"check": lambda: is_apt_package_installed("sqlmap"), "install": lambda: install_apt_program("sqlmap")},
        "Subfinder": {"check": lambda: is_go_tool_installed("subfinder"), "install": lambda: install_go_program("Subfinder", "github.com/projectdiscovery/subfinder/cmd/subfinder")},
        "DNSgen": {"check": lambda: is_pip_package_installed("dnsgen"), "install": lambda: install_pip_program("dnsgen")},
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
    manage_all_tools()

if __name__ == "__main__":
    main()
