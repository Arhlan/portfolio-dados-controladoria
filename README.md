# 🛠️ Automações e Inteligência de Dados: Área Fiscal & Controladoria

Repositório dedicado a soluções tecnológicas que otimizam a rotina fiscal e transformam dados brutos em decisões estratégicas.

---

## 📊 1. Business Intelligence & Controladoria: Análise Comercial
Este projeto apresenta uma solução de ponta a ponta, unindo extração em nuvem, tratamento automatizado e visualização estratégica.

### 🖼️ Visualização do Dashboard
![Dashboard Comercial]
<img width="1295" height="727" alt="image" src="https://github.com/user-attachments/assets/c86f0790-1618-4af1-825e-33f8b4b6674e" />
<img width="1292" height="780" alt="image" src="https://github.com/user-attachments/assets/2c5175e6-6338-4c58-a8ad-3cbca089e202" />
<img width="1279" height="774" alt="image" src="https://github.com/user-attachments/assets/89836c29-2fed-4d8b-b891-0c7c326e63f1" />
<img width="1328" height="779" alt="image" src="https://github.com/user-attachments/assets/47fe1c81-0825-4ce1-a147-0ba27a18ee60" />


### 🛠️ Arquitetura da Solução (Stack Técnica)
* **Banco de Dados:** Extração via **SQL** (PostgreSQL no Supabase).
* **Engenharia de Dados:** Script em **Python** (Antigravity) para limpeza e anonimização (LGPD).
* **Business Intelligence:** Modelagem e Dashboard no **Power BI** com medidas avançadas em **DAX**.

### 🚀 Indicadores Chave (KPIs)
* Faturamento Total & YoY (Year over Year).
* Ticket Médio por Segmento (Público vs Privado).
* Análise de Pareto (Curva ABC) de Clientes e Produtos.

---

## 🧮 2. Calculadora de Validação Fiscal (NFS-e)
Ferramenta de auditoria interna para double-check de impostos retidos frente aos valores gerados pelo ERP.

### 🎯 O Problema de Negócio
Validar manualmente as regras de retenção e dispensas federais (dispensa de R$ 10,00) no TOTVS RM é um processo moroso e sujeito a falhas.

### 💡 A Solução
Script em **Python** que aplica instantaneamente as regras de negócio:
* **ISS (3%)** | **IRRF (1,5%)** | **CSRF (4,65%)**.
* Validação automática de regras de dispensa mínima.

---

### 📈 Resultados e Impacto no Negócio
- **Mitigação de Risco Fiscal:** Eliminação de erros operacionais no cálculo de retenções (IRRF e CSRF), garantindo o cumprimento exato da legislação (como a regra de dispensa de R$ 10,00).
- **Eficiência e ROI:** Redução drástica das horas gastas com conferência manual de notas fiscais de serviços tomados, atuando como um "Double-Check" blindado antes do fechamento contábil.

### ⚙️ Como Executar a Calculadora
Este script foi desenvolvido utilizando **Programação Orientada a Objetos (POO)** para garantir escalabilidade e fácil manutenção das alíquotas.

1. Clone o repositório em sua máquina local:
   `git clone https://github.com/Arhlan/portfolio-dados-controladoria.git`
2. Certifique-se de ter o Python 3 instalado.
3. No terminal, execute o arquivo principal:
   `python calculadora_impostos.py`

   **Desenvolvido por Arhlan Gurgel** *Fiscal & Controladoria | Data Enthusiast*
