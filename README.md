# Block-Ads-TpLink

 Block advertising on router tp link, the most important domains of publicity and malware, with tp link you can block 64 domains, if you need blocks read about free firmware (DD-WRT, OpenWrt)

----------
> It is recommended to make a backup of the configuration
## Configuration
Configure the conf.json file with the data of your tplink router

```
{
    "IpRouter": "192.168.0.2",
    "Login": {
            "User": "admin",
            "Password": "admin"
        },
    "Lan": {
            "ipStart": "192.168.0.100",
            "ipEnd": "192.168.0.199"
        },
    "FileAds": "hosts.txt"
}
```


> For now only works with python 2, soon compatible with python3

#### Run

```
python main.py
```
----
```
Then you can check the settings in the tab acces control of tp link
```
