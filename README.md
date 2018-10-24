This program computes probability of k-mer sequence motif occurence in n ntd random target sequence.

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

### multiple inputs
```
./main -n 500 500 500 -k 3 4 7 -p 1
```

![img]()