This program computes probability of k-mer sequence motif occurence in n ntd random target sequence. There's [a blog post](https://de-novo.org/2018/10/25/sequence-motif-occurrence/) describing the rationale behind it. Python 3 needs to be installed.

## Manual
```
  -h, --help              show help message and exit
  -k K [K ...]            length of query sequence (k >= 3)
  -n N [N ...]            length of random target sequence
  -p {0,1}, --plot {0,1}
                          Wheter or not to produce a plot
                          (0: no plot / 1: plot)
```

## examples
### 1. single input
```
./main -n 52 -k 7 -p 0
```

`n=52, k=7: 0.002804712821387148`

### 2. multiple inputs
```
./main -n 500 500 500 -k 3 4 7 -p 1
```

![img](https://raw.githubusercontent.com/naturale0/MotifOccur/master/Thu%20Oct%2025%2000%3A16%3A50%202018.png)
