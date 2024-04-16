# Síntese de Bases de Dados

Este repositório contém scripts e arquivos relacionados à síntese de bases de dados, uma técnica importante no campo da ciência de dados e da privacidade de dados. A síntese de bases de dados envolve a criação de conjuntos de dados artificiais que preservam as características estatísticas e estruturais dos dados originais, mas sem conter informações sensíveis ou identificáveis. Isso é essencial para proteger a privacidade dos dados, especialmente em cenários em que os dados originais contêm informações pessoais ou confidenciais.

## Arquivos no Ambiente

### generating_fake_datasets.py

Este arquivo contém o script para gerar um conjuntos de dados falsos. Ele pode ser usado para criar conjuntos de dados sintéticos que se assemelham aos dados reais, mas sem conter informações reais. Isso é útil para testar algoritmos, modelos ou sistemas sem expor dados reais a riscos de segurança ou privacidade.

### synthesis.py

O arquivo synthesis.py contém funções e métodos relacionados à síntese de bases de dados. Ele fornece funcionalidades para criar e manipular dados sintéticos, como gerar amostras sintéticas, preservar a distribuição estatística dos dados originais e avaliar a qualidade dos dados sintéticos.

### getting_hashes.py

O script getting_hashes.py é responsável por calcular hashes de dados. Hashes são valores únicos gerados a partir dos dados originais e podem ser usados para verificar a integridade dos dados e identificar duplicatas. Este script pode ser útil para garantir a consistência dos dados antes e depois da síntese.

### runner.sh

O arquivo runner.sh é o shell script responsável por ordenar as execuções dos arquivos anteriores. 

## Importância da Síntese de Bases de Dados

A síntese de bases de dados desempenha um papel crucial em várias áreas, incluindo:

- Privacidade de dados: Ao substituir dados reais por dados sintéticos, é possível compartilhar conjuntos de dados para análise sem comprometer a privacidade das pessoas envolvidas.
- Testes e Desenvolvimento: Conjuntos de dados sintéticos podem ser usados para testar algoritmos, modelos e sistemas em ambientes controlados, sem o risco de expor informações confidenciais.
- Pesquisa Reproduzível: Ao disponibilizar dados sintéticos, os pesquisadores podem reproduzir resultados e validar metodologias sem depender do acesso a conjuntos de dados reais sensíveis.

A síntese de bases de dados é uma prática fundamental para garantir a segurança e privacidade dos dados, bem como promover a transparência e a reprodutibilidade na ciência de dados e pesquisa.

