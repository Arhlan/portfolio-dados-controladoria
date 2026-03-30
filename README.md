# 📊 Calculadora de Validação Fiscal (NFS-e)

Este projeto é um script em **Python** desenvolvido para atuar como uma ferramenta de auditoria interna, auxiliando na dupla checagem (double-check) de impostos retidos em Notas Fiscais de Serviço frente aos valores gerados pelo ERP.

## 🎯 O Problema de Negócio
Durante o fechamento fiscal e a auditoria de notas, validar manualmente se o sistema (ex: TOTVS RM) aplicou corretamente as regras de retenção — especialmente as dispensas federais — é um processo moroso e sujeito a falha humana.

## 💡 A Solução
Para dar velocidade e segurança a essa rotina de auditoria, criei este validador que recebe o valor bruto da nota e calcula instantaneamente as retenções devidas, aplicando as regras de negócio:
* **ISS:** Cálculo da alíquota municipal (3%).
* **IRRF (1,5%):** Validação da regra de dispensa para retenções inferiores a R$ 10,00.
* **CSRF - PIS/COFINS/CSLL (4,65%):** Validação da regra de dispensa para retenções inferiores a R$ 10,00.

## 🚀 Impacto Prático
A ferramenta elimina o uso de calculadoras manuais e planilhas soltas durante a conferência individual de notas. Isso garante maior agilidade no fechamento mensal e segurança de que o *compliance* tributário está sendo respeitado antes do envio das obrigações acessórias.

## 🛠️ Tecnologias Utilizadas
* **Python** (Lógica condicional aplicada à legislação tributária)
