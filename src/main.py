import math

class LogisticPRNG:
    def __init__(self, iters, r_offset):
        self.iters = iters % 110 + 10
        self.r_offset = math.fmod(r_offset, 0.01)

    def gen_prng(self):
        """A pseudo-random number generator utilizing the
        logistic map function's chaotic regions."""

        # We'll start our logistic map at r = 3.95, since this will give
        # us essentially the full range from 0 to 1 for our PRNG
        # Our PRNG will be biased towards >0.9 and <0.1.. but, oh well.
        # I can try and even it out later, maybe by only taking samples between
        # a p range of 0.4-0.6 and just scaling them.

        # The iteration count is seeded, as well as r_offset, which change with each random
        # new number. We'll be using modulo on iters to get it within the range of 1-10
        # to reduce lag, essentially. Most randomness will come from increasing r
        # by miniscule steps.

        # We'll also be using fmod to ensure that r_offset stays within the range of
        # 0 to 0.01, since r will be calculated essentially as just (r_offset + 3.99)
        # and we don't ever want it to be above

        # If we get floating-point rounding errors, good! More pseudo-randomness for us.

        self.iters = max(10, self.iters % 110)
        self.r_offset = math.fmod(self.r_offset, 0.01)
        r = self.r_offset + 3.95
        p = 0.1

        for _ in range(self.iters):
            p = self.logistic_map(r, p)

        self.iters = round(p * 100) + 10
        self.r_offset += 0.0000001

        return p

    def logistic_map(self, r, p):
        """The logistic map equation. Models population growth
        and has a chaotic region at r >~ 3.6 that can be used
        to generate (mediocre) random numbers"""
        return r * p * (1 - p)

if __name__ == "__main__":
    rng = LogisticPRNG(35, 0.0012615)
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(10000):
        n = rng.gen_prng()
        integer = math.floor(n * 10)
        count[integer] += 1
    print(count)
