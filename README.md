# DeathNote 
A tool on commandline used to kill process on time. 

<p>
  <img src="https://dingo.care2.com/pictures/petition_images/petition/188/907194-1490205999-wide.jpg" width=300/>
</p>

## Requirement
- Python 2.7+ or Python 3.5+
- pip or pip3

## Installation

```sh
pip install deathnote
```


## Usage
```
Usage:
  deathnote <hour> <minute> --pid <pid>
```

## Examples

```sh
date
# => Sun Jan 14 23:34:58 DST 2018

deathnote 23 42 --pid 9646 &
# => PID 9646 shall be killed at 23:42:47 on 2018-01-14.
```

If you add alias to bashrc, zshrc etc. as below, this will be used more conveniently.
```sh
alias dn="deathnote"
dn 12 34 --pid 5678
```
