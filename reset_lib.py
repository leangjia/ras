import os

def reset_to_host_mode():
    os.system('aplay /home/pi/RaspiWiFi/Reset\ Device/button_chime.wav')
    os.system('sudo rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
    os.system('sudo rm -f /home/pi/Projects/RaspiWifi/tmp/*')
    os.system('sudo cp -r /home/pi/RaspiWiFi/Reset\ Device/static_files/dhcpd.conf /etc/dhcp/')
    os.system('sudo cp -r /home/pi/RaspiWiFi/Reset\ Device/static_files/hostapd.conf /etc/hostapd/')
    os.system('sudo cp -r /home/pi/RaspiWiFi/Reset\ Device/static_files/interfaces.aphost /etc/network/interfaces')
    os.system('sudo cp -r /home/pi/RaspiWiFi/Reset\ Device/static_files/isc-dhcp-server.aphost /etc/default/isc-dhcp-server')
    os.system('sudo rm /etc/cron.raspiwifi/apclient_bootstrapper')
    os.system('sudo cp -r /home/pi/RaspiWiFi/Reset\ Device/static_files/aphost_bootstrapper /etc/cron.raspiwifi/')
    os.system('sudo reboot')
