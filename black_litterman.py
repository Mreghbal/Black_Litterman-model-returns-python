######################################################################################################

import pandas as pd
import numpy as np
import numpy.linalg as nl

######################################################################################################

def black_litterman_returns(w_prior, sigma_prior, p, q,
                omega=None, delta=2.5, tau=.02):
    """

    Computes the posterior expected returns based on the original black litterman reference model:
    
    1- "w_prior" must be an N x 1 vector of weights, a perior series of weights that calculated by
       the weights of the first row divided by the sum of the weights of the first row.

    2- "sigma_prior" is an N x N variance-covariance matrix, a DataFrame that calculaated by the
       "vols.dot(vols.T) * rho" where rho is correlation matrix of returns and vols is N x 1 vector
       of annulized volatilities of returns.

    3- "q" must be an K x 1 vector of views, a series
    
    4- "p" must be a K x N matrix linking Q and the Assets, a DataFrame

    5- Omega must be a K x K matrix a DataFrame that calculated with "proportional_prior" function,
       if Omega is None, we assume it is proportional to variance of the prior.

    6- "delta" and "tau" are scalars, "delta" is risk aversion coefficient.

    7- The "proportional_prior" function returns the He-Litterman simplified Omega.

    8- The "implied_returns" function returns the implied expected returns by reverse engineering
       the weights with (N x 1) vector of returns as series and also "w" is portfolio weights
       (N x 1) as series.

    9- "N: is number of assets we have and "K" is number of our views.

    10- The Black-Litterman asset allocation model provides a methodical way of combining an
        investors subjective views of the future performance of a risky investment asset with
        the views implied by the market equilibrium. The method has seen wide acceptance amongst
        practitioners and academics.

    11- The Black-Litterman procedure can be viewed as a Bayesian shrinkage method, that shrinks
        the expected returns constructed from an investor's views on asset returns towards asset
        returns implied by the market equilibrium. 

    """

######################################################################################################

    def proportional_prior(sigma, tau, p):
        helit_omega = p.dot(tau * sigma).dot(p.T)
        return pd.DataFrame(np.diag(np.diag(helit_omega.values)), index = p.index, columns = p.index)

    def implied_returns(delta, sigma, w):
        implied_r = delta * sigma.dot(w).squeeze()
        implied_r.name = 'Implied Returns'
        return implied_r

######################################################################################################

    if omega is None:
        omega = proportional_prior(sigma_prior, tau, p)

    N = w_prior.shape[0]
    K = q.shape[0]
    pi = implied_returns(delta, sigma_prior,  w_prior)
    sigma_prior_scaled = tau * sigma_prior  
    mu_black_litterman = pi + sigma_prior_scaled.dot(p.T).dot(nl.inv(p.dot(sigma_prior_scaled).dot(p.T) + omega).dot(q - p.dot(pi).values))
    sigma_black_litterman = sigma_prior + sigma_prior_scaled - sigma_prior_scaled.dot(p.T).dot(nl.inv(p.dot(sigma_prior_scaled).dot(p.T) + omega)).dot(p).dot(sigma_prior_scaled)
    return (mu_black_litterman, sigma_black_litterman)

######################################################################################################