# PyMatch - Output auxiliary tool

pyMatch is designed to help you generate formatted and valid outputs, in a simple way. 
He uses Regex to collate and validate data, and then you can use the captured groups to generate a formatted output as well want to.

## Screenshots

![](http://i58.tinypic.com/20md8h.png) 

![](http://i57.tinypic.com/11177lw.jpg)



## Installation


You can download the latest tarball by clicking [here](https://github.com/rfunix/PyMatch/tarball/master) or latest zipball by clicking  [here](https://github.com/rfunix/PyMatch/zipball/master).

Preferably, you can download PyMatch by cloning the [Git](https://github.com/rfunix/PyMatch) repository:

```
git clone https://github.com/rfunix/PyMatch.git PyMatch-dev
```

PyMatch works out of the box with [Python](http://www.python.org/download/) version '''2.6.x''' and '''2.7.x''' on any platform.

## Usage

To get the list of basic options and information about the project:

```bash
python pymatch.py -h
```

Examples of use:
    
    To use the groups obtained in the use Regex -g (Group number).
    
    python pymatch.py -f "teste.txt" -p "^(011)(\d{4,5})(\d{4})$" -g "((1))(2)-(3)"

