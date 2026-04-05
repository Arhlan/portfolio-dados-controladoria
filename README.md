# 🛠️ Automações e Inteligência de Dados: Área Fiscal & Controladoria

Repositório dedicado a soluções tecnológicas que otimizam a rotina fiscal e transformam dados brutos em decisões estratégicas.

---

## 📊 1. Business Intelligence & Controladoria: Análise Comercial
Este projeto apresenta uma solução de ponta a ponta, unindo extração em nuvem, tratamento automatizado e visualização estratégica.

### 🖼️ Visualização do Dashboard
![Dashboard Comercial](COLE_O_LINK_GERADO_AQUI)

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

**Desenvolvido por Arhlan Gurgel** *Fiscal & Controladoria | Data Enthusiast*
