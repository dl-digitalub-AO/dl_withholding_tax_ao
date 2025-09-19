# Retenção na Fonte Angola (dl_withholding_tax_ao)

Este módulo adiciona a funcionalidade de Retenção na Fonte para Angola ao Odoo 15.

## Funcionalidades

*   Configuração de diferentes tipos de retenção na fonte.
*   Aplicação de retenção nas linhas da fatura.
*   Cálculo automático do valor da retenção e do líquido a pagar.
*   Exibição dos valores de retenção no formulário da fatura e nos relatórios em PDF.

## Instalação

1.  Copie a pasta `dl_withholding_tax_ao` para a sua pasta de addons do Odoo.
2.  Reinicie o serviço do Odoo.
3.  Ative o modo de programador.
4.  Vá a "Aplicações", clique em "Atualizar Lista de Aplicações".
5.  Procure por "Retenção na Fonte Angola" e clique em "Instalar".

## Utilização

1.  **Configurar as taxas de retenção:**
    *   Vá a `Contabilidade > Configuração > Retenção na Fonte`.
    *   Crie ou edite as taxas de retenção conforme necessário. O módulo já vem com algumas taxas pré-configuradas.

2.  **Aplicar retenção numa fatura:**
    *   Ao criar uma fatura de fornecedor, numa das linhas da fatura, no campo "Retenção", selecione a taxa de retenção a aplicar.
    *   O valor da retenção e o líquido a pagar serão calculados e exibidos automaticamente no rodapé da fatura após guardar.
