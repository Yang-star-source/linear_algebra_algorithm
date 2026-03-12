# Matrix Factorization

LU , PLU , LDU , PLDU factorization will be used but since PLU and PLDU is more general than  LU and LDU , then do the PLU and PLDU enough.

## PLDU factorization
In PLDU factorization, we cannot do $U_{new} = U_{orig} / D$ even we do it in practice.

Practically , we use $DU_{new} = U_{orig}$

Then $U_{new} = D^{-1}U_{orig}$

We knew for a diagonal matrix D , $D^{-1} = \frac{1}{D}$

