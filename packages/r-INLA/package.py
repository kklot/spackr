# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RInla(RPackage):
    """INLA: approximate Bayesian inference for Latent Gaussian Models

    The integrated nested Laplace approximation (INLA) is a method for
    approximate Bayesian inference. In the last years it has established itself
    as an alternative to other methods such as Markov chain Monte Carlo because
    of its speed and ease of use via the R-INLA package. Although the INLA
    methodology focuses on models that can be expressed as latent Gaussian
    Markov random fields (GMRF), this encompasses a large family of models that
    are used in practice."""

    homepage = 'https://www.r-inla.org/download-install'
    url      = 'https://inla.r-inla-download.org/R/stable/src/contrib/INLA_21.11.22.tar.gz'
    list_url = 'https://inla.r-inla-download.org/R/stable/src/contrib/'

    version('21.11.22', sha256='f8aba0667d4266e6be7f5523f68c39544df559ac855bbd4d5d5e00d5712db96e')

    depends_on('r@3.0.0:', type=('build', 'run'))
    depends_on('r-matrix')
    depends_on('r-foreach')
    depends_on('r-parallel')
    depends_on('r-sp')
