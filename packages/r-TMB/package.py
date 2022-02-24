# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RTmb(RPackage):
    """Template Model Builder: A General Random Effect Tool Inspired by 'ADMB'

    With this tool, a user should be able to quickly implement complex random
    effect models through simple C++ templates. The package combines 'CppAD'
    (C++ automatic differentiation), 'Eigen' (templated matrix-vector library)
    and 'CHOLMOD' (sparse matrix routines available from R) to obtain an
    efficient implementation of the applied Laplace approximation with exact
    derivatives. Key features are: Automatic sparseness detection, parallelism
    through 'BLAS' and parallel user templates."""

    cran = "TMB"

    version('1.7.22', sha256='c24125e1a37ed2b3c2554133183465cb6f3c0021cd4d4609c61336f59c3bd384')

    depends_on('r@3.0.0:', type=('build', 'run'))
    depends_on('r-matrix')
    depends_on('r-rcppeigen')
