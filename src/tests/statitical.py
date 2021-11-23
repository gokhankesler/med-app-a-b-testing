from scipy import stats

class Hypotesis:
    def __init__(self, p1, p2, n, m):
        self.p1 = p1
        self.p2 = p2
        self.n = n
        self.m = m
        self.p_hat = (self.m * self.p1 + self.n * self.p2) / (self.m  + self.n)

    def single_sided_hypotesis(self, alpha):
         return (self.p1 - self.p2) / ((self.p_hat * (1-self.p_hat)*((1/self.n)+(1/self.m)))**0.5)

    def two_sided_hypotesis(self, alpha):
        return 2 * (self.p1 - self.p2) / ((self.p_hat * (1-self.p_hat)*((1/self.n)+(1/self.m)))**0.5)


    def get_power(self, cl):
        alpha = 1 - cl
        qu = stats.norm.ppf(1 - alpha/2) # 0.025 / 0.025
        diff = abs(self.p2 - self.p1)
        bp = (self.p1 + self.p2) / 2
        v1 = self.p1 * (1 - self.p1)
        v2 = self.p2 * (1 - self.p2)
        bv = bp * (1 - bp)
        power_part_one = stats.norm.cdf((self.n**0.5 * diff - qu * (2 * bv)**0.5)/ (v1 + v2)**0.5)
        power_part_two = 1 - stats.norm.cdf((self.n**0.5 * diff + qu * (2 * bv)**0.5)/ (v1 + v2)**0.5)
        
        power = power_part_one + power_part_two
        return(power)