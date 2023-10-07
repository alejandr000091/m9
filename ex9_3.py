def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else:
            result =  fibonacci(n-2) + fibonacci(n-1)
            cache[n] = result
        return result
    return fibonacci

my_fib = caching_fibonacci()
result = my_fib(10)

print(result)
    

    
        
            
        
            
        
            

        

    