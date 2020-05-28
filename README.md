# powerline-shell-customized
Bert's personal customizations for powerline-shell

Add a hamburger prompt, use a more lightweight git integration that only shows the current branch name

## Usage

Install Powerline:
```
cd ~/code
git clone git@github.com:b-ryan/powerline-shell.git
cd powerline-shell
sudo python setup.py install
```

Clone repo:
```
cd ~/code
git clone git@github.com:bertrandom/powerline-shell-customized.git
```

Link config:
```
mkdir -p ~/.config/powerline-shell
ln -s ~/code/powerline-shell-customized/.config/powerline-shell/config.json config.json
```

Add contents of `.profile` to `~/.profile`
