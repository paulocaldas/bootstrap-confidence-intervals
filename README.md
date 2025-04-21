# Bootstrap Confidence Intervals

Often, when estimating standard errors (SE) and confidence intervals (CI) for certain parameters (e.g., means, medians, correlation coefficients, kinetic parameters), we assume that the underlying distribution of the sample we are measuring is normally distributed. But what if our samples do not come from a normal distribution?

The **bootstrap** is a resampling technique that helps overcome the need to assume normality when estimating SE and CI for a given sample statistic. The idea behind bootstrapping is to use our sample (which is an estimate of the real distribution) to draw hundreds of subsamples, mimicking what we would do in real life (if we had the chance). The resulting bootstrap distribution functions as an estimate of the real sample distribution, and we use it to obtain better estimates of our parameters. The procedure is simple:

- We draw N subsamples from our original sample with replacement (typically more than 1,000) to create new pseudo-samples of the original data—called bootstrap samples. By allowing replacement, some data points will be duplicated, while others will be omitted.
- We then compute and store the mean of the desired sample statistic θ (e.g., mean, median, correlation coefficient) for each bootstrap sample.
- At the end, we have a new dataset containing a distribution of means for the sample statistics we are investigating. Since N is large, this distribution will be approximately normally distributed and centered around the mean of our estimate (central limit theorem).

The resampling distribution is approximately similar to the real distribution (statistical inference), which, by consequence, implies that the variance of the resampling statistics will be a good estimator of the real variance. This allows us to investigate the variability of the original data (SE and CI). Instead of estimating our statistic only once using the sample we have obtained, we can do it many times by resampling the original sample. The rationale is based on the law of large numbers, which states that with enough data, the empirical distribution will be a good approximation of the true distribution. It does not provide any information about the true value of the parameter (the mean value of the parameter will be the same), but it offers a better strategy to show how the parameter estimation might vary.

### Why Is This Not Cheating?

The bootstrap is based on a principle that is very common in statistical inference: if the real distribution is unknown, our sample distribution—an estimate of that distribution—is the best guide to understanding it. Essentially, we consider that our sample provides a good illustration of all the possible samples that we would get from the real data distribution if we had the time and resources to perform our study countless times. Thus, resampling from our estimate of the real distribution is a reasonable strategy to understand what we could expect if we had the means to repeat our study thousands of times.

