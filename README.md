# Pen

# Setup

```bash
# Clone the repo
# I recommend you to clone it in /opt directory
git clone https://github.com/uwumouse/pen

# Setup penta.
# It'll create a script in your .bashrc to update env variables in all of your terminals
# And will create a global command 'pen'
chmod +x ./setup.sh
./setup.sh
```

# Usage

`Pen` allows to export a text-value to ENV variable `$PEN` that is accessible in any terminal.
It is because in your `.bashrc` is a `trap` command that catches every command in any terminal and updates value with a value in `~/.pen` file.

So `Pen` ships with 2 commands:

-   `export (e)`

```bash
# Will store "value" in ~/.pen and export it to $PEN variable in shell
$ pen export value
# Alias
$ pen e value
```

-   `show (s)`

```bash
$ pen show # Shows a value from ~/.pen file
$ pen show -c # Shows a value and copies it to clipboard via xclip
# Alias
$ pen s
```

# Where it can be used?

The idea of this program came to me because when I do CTFs I need the IP of the box quite often.  
So I need to constantly copy it from the site if I need to do payload or something different.  
It would be easier for me if I could access this variable with a variable in terminal.  
But writing `export $IP=<machine-ip>` everytime I open a new window is kind of annoying, so `Pen` makes life easier by allowing to use variable I set from any terminal.
