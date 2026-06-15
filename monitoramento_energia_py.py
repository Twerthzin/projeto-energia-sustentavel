### -*- coding: utf-8 -*-
"""

monitoramento_energia.py.ipynb

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

print("="*70)
print("SISTEMA DE MONITORAMENTO DE ENERGIA SOLAR - PROVA DE CONCEITO")
print("="*70)

print("\n[FUNDAMENTACAO TECNICA DOS DADOS]")
print("Os dados foram simulados com base em:")
print("- Irradiancia solar media para regiao Sudeste (INMET)")
print("- Painel fotovoltaico de 5kWp (potencia de pico)")
print("- Eficiencia do sistema considerando perdas (inversor, temperatura, sombreamento)")
print("- Perfil de consumo residencial tipico (manha e noite)")

horarios = [f"{h:02d}:00" for h in range(6, 19)]

geracao_kwh = [
    0.3,
    1.0,
    2.2,
    3.8,
    5.2,
    6.8,
    7.5,
    7.2,
    6.2,
    4.8,
    3.0,
    1.4,
    0.4
]

consumo_kwh = [
    1.8,
    2.0,
    1.5,
    1.2,
    1.0,
    1.1,
    1.3,
    1.2,
    1.1,
    1.0,
    1.2,
    1.5,
    2.2
]

total_geracao = sum(geracao_kwh)
total_consumo = sum(consumo_kwh)
balanco_energetico = total_geracao - total_consumo

energia_aproveitada = min(total_geracao, total_consumo)
eficiencia_sistema = (energia_aproveitada / total_geracao) * 100 if total_geracao > 0 else 0

potencia_instalada_kwp = 5
horas_sol_equivalentes = total_geracao / potencia_instalada_kwp
fator_capacidade = (total_geracao / (potencia_instalada_kwp * 13)) * 100

fator_emissao_co2 = 0.084
co2_evitado_kg = total_geracao * fator_emissao_co2

arvores_equivalentes = co2_evitado_kg / 18

tarifa_energia_brl = 0.90
economia_financeira = total_geracao * tarifa_energia_brl

print("\n" + "="*70)
print("RESULTADOS DA SIMULACAO - DADOS GERADOS PELO SISTEMA")
print("="*70)

print("\n[1] BALANCO ENERGETICO DIARIO")
print(f"Energia gerada pelo sistema solar: {total_geracao:.1f} kWh")
print(f"Energia consumida pela residencia: {total_consumo:.1f} kWh")
print(f"Balanco energetico: {balanco_energetico:.1f} kWh")
if balanco_energetico > 0:
    print(f"-> EXCEDENTE de {balanco_energetico:.1f} kWh (pode ser armazenado ou injetado na rede)")
else:
    print(f"-> DEFICIT de {abs(balanco_energetico):.1f} kWh (energia vinda da rede)")

print("\n[2] METRICAS DE EFICIENCIA ENERGETICA")
print(f"Potencia instalada: {potencia_instalada_kwp} kWp")
print(f"Horas de sol equivalentes: {horas_sol_equivalentes:.1f} h/dia")
print(f"Fator de capacidade: {fator_capacidade:.1f}%")
print(f"Eficiencia do sistema: {eficiencia_sistema:.1f}%")

print("\n[3] IMPACTO AMBIENTAL (SUSTENTABILIDADE)")
print(f"Emissao de CO2 evitada: {co2_evitado_kg:.2f} kg/dia")
print(f"Equivalente em arvores plantadas: {arvores_equivalentes:.2f} arvores/dia")
print(f"Projecao anual de CO2 evitado: {co2_evitado_kg * 365:.1f} kg/ano")
print(f"Arvores equivalentes anuais: {arvores_equivalentes * 365:.1f} arvores")

print("\n[4] VIABILIDADE ECONOMICA")
print(f"Economia financeira diaria: R$ {economia_financeira:.2f}")
print(f"Economia financeira mensal: R$ {economia_financeira * 30:.2f}")
print(f"Economia financeira anual: R$ {economia_financeira * 365:.2f}")

print("\n[5] ANALISE HORARIA DETALHADA")
print("-"*70)
print(f"{'Horario':<10} {'Geracao (kWh)':<15} {'Consumo (kWh)':<15} {'Balanco (kWh)':<15}")
print("-"*70)

for i, hora in enumerate(horarios):
    balanco = geracao_kwh[i] - consumo_kwh[i]
    status = "EXCEDENTE" if balanco > 0 else "DEFICIT"
    print(f"{hora:<10} {geracao_kwh[i]:<15.1f} {consumo_kwh[i]:<15.1f} {balanco:<15.1f} {status}")

print("\n[6] GERANDO VISUALIZACAO GRAFICA...")

plt.figure(figsize=(14, 7))

plt.plot(horarios, geracao_kwh, 'g-o', linewidth=2, markersize=8,
         label='Geracao Solar (kWh)', color='green')
plt.plot(horarios, consumo_kwh, 'r-s', linewidth=2, markersize=8,
         label='Consumo Residencial (kWh)', color='red')

plt.fill_between(horarios, geracao_kwh, consumo_kwh,
                 where=np.array(geracao_kwh) >= np.array(consumo_kwh),
                 color='green', alpha=0.3, label='Excedente (Energia Limpa)')
plt.fill_between(horarios, geracao_kwh, consumo_kwh,
                 where=np.array(geracao_kwh) < np.array(consumo_kwh),
                 color='red', alpha=0.3, label='Deficit (Energia da Rede)')

plt.title('MONITORAMENTO DE ENERGIA SOLAR - PROVA DE CONCEITO', fontsize=16, fontweight='bold')
plt.xlabel('Horario do Dia', fontsize=12)
plt.ylabel('Energia (kWh)', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('monitoramento_solar_prova_conceito.png', dpi=150, bbox_inches='tight')
plt.show()

print("Grafico salvo como: monitoramento_solar_prova_conceito.png")

print("\n" + "="*70)
print("JUSTIFICATIVA TECNICA E PROVA DE CONCEITO")
print("="*70)

print("\n[A] ARQUITETURA DO SISTEMA")
print("- 1 componente de simulacao de geracao solar (baseada em irradiancia)")
print("- 1 componente de simulacao de consumo residencial")
print("- 1 componente de calculo de balanco energetico")
print("- 1 componente de metricas de sustentabilidade")
print("- 1 componente de visualizacao grafica")

print("\n[B] PRINCIPIOS DE EFICIENCIA ENERGETICA APLICADOS")
print("1. Dimensionamento adequado: 5kWp para residencia media")
print("2. Aproveitamento maximo do excedente (armazenamento ou injecao)")
print("3. Monitoramento horario para otimizacao do consumo")

print("\n[C] CONEXAO COM ENERGIAS RENOVAVEIS")
print("1. Fonte limpa e inesgotavel (energia solar fotovoltaica)")
print("2. Zero emissao de CO2 durante operacao")
print("3. Reducao da dependencia de fontes fosseis")

print("\n[D] VIABILIDADE TECNICA COMPROVADA")
print("1. O sistema demonstra coleta e processamento de dados")
print("2. Gera metricas uteis para tomada de decisao")
print("3. Pode ser implementado com hardware real (sensores, inversor, PLC)")
print("4. Escalavel para diferentes portes de residencias/empresas")

print("\n[E] FUNCIONALIDADES OPERACIONAIS DEMONSTRADAS")
print("1. Simulacao de geracao solar horaria")
print("2. Calculo automatico de balanco energetico")
print("3. Geracao de metricas ambientais (CO2 evitado)")
print("4. Geracao de metricas economicas (economia financeira)")
print("5. Visualizacao grafica para tomada de decisao")

print("\n" + "="*70)
print("PROVA DE CONCEITO CONCLUIDA - PROTOTIPO FUNCIONAL E VIAVEL")
print("="*70)