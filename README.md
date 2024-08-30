# socialhosts

A simple Python script to hide social media



## Prerequisites

- Python 3.x
- Git (for cloning the repository)
- Sudo privileges (for modifying the hosts file)
- It works on Linux and might work on MacOS X

## Instructions

### Installation
Clone the repository:
```sh
git clone https://github.com/xalava/socialhosts.git
```
Install the blocking list
```sh
sudo python socialhosts.py install
```
You can then manually edit the list to your needs. 


### Usage
To block access to the sites:
```sh
sudo python socialhosts.py lock
```

To unblock access to the sites:
```sh
sudo python socialhosts.py unlock
```
You might have to reboot the system, or at least some DNS service, in order for it to take effect.


### Tips

You can create an alias in your `.bashrc` or `.profile` file:
```sh
alias sm="sudo python LOCATION/socialhosts.py"
```
where PATH is the location of your cloned folder. 

## Contributing

Contributions are welcome. Particularly to the `blocked_sites.txt` with the idea to keep it lean and customizable.