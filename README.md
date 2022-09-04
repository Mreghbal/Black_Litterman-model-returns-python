# Black_Litterman-model-returns-python
Computes the posterior expected returns based on the original Black-Litterman reference model


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
