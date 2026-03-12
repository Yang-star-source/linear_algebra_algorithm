# Determinant , Eigenvalues and Eigenvectors

$$A v = \lambda v$$

where $\lambda$ is eigenvalues and $v$ is eigenvectors.

$$A v = \lambda v$$
$$A v - \lambda v = 0$$
$$(A - \lambda I)v = 0$$

Since we are more interested in $v \neq 0$ , but we could not conclude $(A - \lambda I)$ is 0. If we assume $(A - \lambda I)$ have an inverse , then

$$(A - \lambda I)v = 0$$
$$(A - \lambda I)^{-1}(A - \lambda I)v = (A - \lambda I)^{-1} 0$$
$$v = 0$$

This contradict with original assumption $(A - \lambda I)$ have an inverse.

Hence, $(A - \lambda I)$ have no inverse , determinant for $(A - \lambda I)$ is 0.

For a $n \times n$ matrix , there exist $n$ eigenvalues and $n$ eigenvectors.

This is because $det(A - \lambda I) = 0$ will makes $\lambda^n$  polynomial.

According to number theory , this exist n solutions for power n polynomial.

But be aware that there might exist imaginary parts or repeated roots issue. For a repeated roots , the matrix cant be diagonalize.

