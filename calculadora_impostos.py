class CalculadoraImpostosNFS:
    def __init__(self):
        # Alíquotas base de retenção federal na fonte
        self.aliquota_csll = 0.03
        self.aliquota_pis_cofins = 0.0165
        
        # Alíquotas de IRRF dependem do tomador
        self.aliquota_irrf_privada = 0.015
        self.aliquota_irrf_publica = 0.012
        
        # ISS (devido pelo prestador via guia à parte)
        self.aliquota_iss = 0.03

    def calcular(self, valor_bruto, tipo_entidade="privada"):
        # 1. Determina a alíquota de IR de acordo com o tomador
        if tipo_entidade.lower() == "publica":
            irrf_aliquota = self.aliquota_irrf_publica
        else:
            irrf_aliquota = self.aliquota_irrf_privada
            
        # 2. Calcula as retenções na fonte (o cliente desconta do que tem a pagar)
        csll = valor_bruto * self.aliquota_csll
        pis_cofins = valor_bruto * self.aliquota_pis_cofins
        irrf = valor_bruto * irrf_aliquota

        # 3. Aplica a Regra de Dispensa: se o DARF gerado for < R$ 10,00, a retenção é dispensada.
        if csll < 10.00:
            csll = 0.0
        if pis_cofins < 10.00:
            pis_cofins = 0.0
        if irrf < 10.00:
            irrf = 0.0

        # 4. Totaliza as retenções e o líquido que cai na conta
        total_retido = csll + pis_cofins + irrf
        valor_liquido = valor_bruto - total_retido

        # 5. Calcula o ISS que o emissor vai pagar posteriormente
        iss_devido = valor_bruto * self.aliquota_iss

        # Retorna o dicionário com os dados sumarizados
        return {
            "Valor Bruto": valor_bruto,
            "Tipo Entidade": tipo_entidade.capitalize(),
            "Retencoes": {
                "CSLL (3%)": csll,
                "PIS/COFINS (1,65%)": pis_cofins,
                f"IRRF ({irrf_aliquota*100:.1f}%)".replace('.', ','): irrf
            },
            "Total Retido": total_retido,
            "Valor Liquido": valor_liquido,
            "ISS Devido (3%)": iss_devido
        }

def formatar_moeda(valor):
    # Formatação BR
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def exibir_demonstrativo(dados):
    print("=" * 60)
    print(f" DEMONSTRATIVO DA NOTA FISCAL - Entidade {dados['Tipo Entidade']} ".center(60))
    print("=" * 60)
    print(f"{'Valor Bruto Inicial (NF):':<25} {formatar_moeda(dados['Valor Bruto']):>34}")
    print("-" * 60)
    print(" RETENÇÕES FEDERAIS NA FONTE ".center(60))
    print("-" * 60)
    
    # Imprimi os impostos separadamente, como solicitado
    for nome_imposto, valor in dados["Retencoes"].items():
        print(f" -> {nome_imposto:<22} {formatar_moeda(valor):>34}")
        
    print("-" * 60)
    print(f"{'Total Descontado na Fonte:':<25} {formatar_moeda(dados['Total Retido']):>34}")
    print(f"{'VALOR LÍQUIDO A RECEBER:':<25} {formatar_moeda(dados['Valor Liquido']):>34}")
    print("=" * 60)
    # ISS em destaque como aviso (obrigação do prestador)
    print(f" * AVISO: É sua obrigação recolher o ISS Municipal no ")
    print(f"   valor de {formatar_moeda(dados['ISS Devido (3%)'])}. Isso não desconta do Líquido pago pelo cliente.")
    print("=" * 60)
    print("\n")

def main():
    calculadora = CalculadoraImpostosNFS()

    print("\n>>> INICIANDO TESTES DO NOVO CÁLCULO DE IMPOSTOS <<<\n")

    # TESTE 1: Entidade Privada
    print("Testando Nota de R$ 5.000 para cliente PRIVADO...")
    resultado_1 = calculadora.calcular(5000.00, tipo_entidade="privada")
    exibir_demonstrativo(resultado_1)

    # TESTE 2: Entidade Pública
    print("Testando Nota de R$ 5.000 para cliente PÚBLICO...")
    resultado_2 = calculadora.calcular(5000.00, tipo_entidade="publica")
    exibir_demonstrativo(resultado_2)

    # TESTE 3: Regra de Dispensa
    print("Testando Nota de R$ 100 para observar Regra de Dispensa (< R$ 10)...")
    resultado_3 = calculadora.calcular(100.00, tipo_entidade="privada")
    exibir_demonstrativo(resultado_3)

if __name__ == "__main__":
    main()
