class Sol:
    def count_prime_bits(self,L,R):
        primes=[2,3,5,7,11,13,17,19]
        res=0
        for i in range(L,R+1):
            if bin(i).count('1') in primes:
                res+=1
        return res

if __name__ == '__main__':
    p=Sol()
    print(p.count_prime_bits(10,15))
