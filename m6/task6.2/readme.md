1. Created virtual machines connection according to INET---HOST---nat---VM1---internal---VM2
                                                                           ---internal---VM3:
                                                         ![Linux](Images/1.png "VB")                                                            
2. Installed and configured DHCP server on VM1:          ![Linux](Images/2.png "dsmasq")
                                                         ![Linux](Images/3.png "dsmasq.conf")
                                                         ![Linux](Images/4.png "dsmasq.conf")
                                                         ![Linux](Images/5.png "dhclient.conf")
                                                         ![Linux](Images/6.png "interfaces")
3. Checked VM2 and VM3 for obtaining network addresses from DHCP server:														 
														 ![Linux](Images/7.png "VBox") 
4. Installed and configured DNS server on VM1:           ![Linux](Images/8.png "iptables") 
                                                         ![Linux](Images/9.png "iptables") 
                                                         ![Linux](Images/10.png "resolv.conf") 
                                                         ![Linux](Images/11.png "dnsmasq.conf") 
                                                         ![Linux](Images/12.png "dnsmasq.conf") 
                                                         ![Linux](Images/13.png "status_dnsmasq") 
5. Checked VM2 and VM3 for gaining access to DNS server: ![Linux](Images/14.png "ping_google.com") 
