from scipy import stats

def beta_binomial_credible_interval(prior_mu, prior_M, obs_N, obs_k, percent_interval=(0.1, 0.9)):
    post_alpha = obs_k + prior_mu * prior_M
    post_beta = obs_N - obs_k + prior_M * (1 - prior_mu)
    confidence_low = stats.beta.ppf(percent_interval[0], post_alpha, post_beta)
    confidence_high = stats.beta.ppf(percent_interval[1], post_alpha, post_beta)
    return confidence_low, confidence_high


