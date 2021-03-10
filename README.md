# bootstrap confidence intervals

### Quick note on Bootstrapping

More than often, when estimating standard errors (SE) and confidence intervals (CI) of certain parameters (e.g means, medians, correlation coefficients, kinetic parameters)
we make the assumption that the underlying distribution of the sample we are trying to measure is normally distributed. What if our samples do not come from a normal distribution? 

Bootstrap is a resampling technique that allows to overcome the need to assume normality when estimating SE and CI of a given sample statistics.
The idea behind the bootstrap is to use our sample (an estimate of the real distribution) to draw hundreds of subsamples, mimicking what we would do in real life (if we had the chance).
The resulting bootstrap distribution functions as an estimate of the real sample distribution and we use it to obtain better estimates of our parameters. The procedure is simple:

- We draw N subsamples from our original sample allowing replacement (typically more than 1000) to create new pseudo samples of the original data – we call them bootstrap samples. By allowing replacement, some data points will be duplicated while other will be omitted; 
- We then compute and store the mean of the desire sample statistics θ (e.g mean, median, correlation coefficient) of each bootstrap sample; 
- By the end we have created a new dataset containing a distribution of means of the sample statistics that we are investigating. Since N is large, this distribution will be normally distributed and centered around mean of our estimate (central limit theorem).

The resampling distribution is approximately similar to the real distribution (statistical inference) which by consequence implies that the variance of the resampling statistics will be a good estimator of the real variance, and we can use it to investigate the variability of the original data (SE and CI).
So instead of estimating our statistic only once using the sample we have obtained, we can do it many times by resampling the original sample. The rationale is based on the law of large numbers, which states that with enough data the empirical distribution will be a good approximation of the true distribution. It does not provide any information about the true value of the parameter (the mean value of the paramter will be the same), but it provides a better strategy to show how the parameter estimation might vary.

Why this is not cheating? <br>
The bootstrap is based on a principle that is very common in statistic inference: If the real distribution is unknown, our sample distribution - an estimate of that distribution - is the best guide to understand it. 
Essentially, we consider that our sample provides a good illustration of the all the possible samples that we would get from the real data distribution in case we had the time and the money to perform our study countless times. Thus, resampling our estimate from the real distribution is a reasonable strategy to understand what we could expect if we had the means to repeat our study thousands of times.
