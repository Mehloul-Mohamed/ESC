<h1 align="center">ESC</h1>
<p align="center">Helper Utility To Assist In Escaping PyJail CTF Challenges</p>

> [!NOTE]
> The tool is still under development and is quite simplistic at the moment

## Installation
```git clone https://github.com/Mehloul-Mohamed/ESC```
## Usage

```
python3 main.py [-h] Mode ...
```

Mode can be one of:  

- `italic`: Transform Text Into Mathematical Italic Letters (Useful to avoid blacklists)  
```
usage: main.py italic [-h] Text

positional arguments:
  Text        Text To Change

options:
  -h, --help  show this help message and exit
```

- `esoteric`: Transform Text into Esoteric Python Using Boolean Tricks  
```
usage: main.py esoteric [-h] [-eval] Type Text

positional arguments:
  Type        Technique To Use
  Text        Text To Change

options:
  -h, --help  show this help message and exit
  -eval       Wrap Output In eval()
```

- `builtin`: Generate Payload To Call Function When Builtins Are Disabled  
```
usage: main.py builtin [-h] Module Function Params

positional arguments:
  Module      Module To Use
  Function    Function To Call
  Params      Arguments To The Function

options:
  -h, --help  show this help message and exit
```

- `blacklist`: Generate List Of Builtins That Don't Trigger A Specified Blacklist  
```
usage: main.py blacklist [-h] blist

positional arguments:
  blist       Blacklist String

options:
  -h, --help  show this help message and exit
```
