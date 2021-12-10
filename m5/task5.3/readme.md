1. Processes in linux from birth to death are in ready, running, waiting states.
   Current process output with "pstree":                ![Linux](Images/1.png "pstree")    
2. The "proc" file system provides the user with a link to the information of the kernel processes at the moment.
   The processor information:                           ![Linux](Images/2.png "lscpu") 
3. The process output with "ps":                        ![Linux](Images/3.png "ps") 
4. Kernel and other processes:                          ![Linux](Images/4.png "ps") 
                                                        ![Linux](Images/5.png "ps-N")
                                                        ![Linux](Images/6.png "pstree")
                                                        ![Linux](Images/7.png "pstree_2")   														
5. The "S" column describes the state of the process:                                             
   - D - process pending completion;                                                            
   - R - running;                                                                                
   - S - sleeping;                                                                                
   - T - stopped;                                                                                
   - t - stopped by debugger;                                                                   
   - Z - zombie,                                                                                  
   - < - with negative "nice" value. A negative value of "nice" increases the process priority;    
   - N - with positive nice value.  A positive "nice" value decreases the process priority.
   Outputs information about the processes with the "top" utillite:	
                  	                                ![Linux](Images/8.jpg "top")
                                                        ![Linux](Images/9.png "top-p")
                                                        ![Linux](Images/10.png "top-p")   																												
6. Displayed the processes for a certain user:          ![Linux](Images/11.png "ps-fu")   
														![Linux](Images/12.png "ps-fu") 														
7. Displayed the processes for a certain user with "top" utillite:
                                                        ![Linux](Images/13.png "top-u")
8. Interactive "htop", "atop", "top V n 15":		![Linux](Images/14.png "htop")
                                                        ![Linux](Images/15.png "atop")
														![Linux](Images/16.png "topVn")
9. Sort "top" by time "Shift+T", by memory "Shift+M":   ![Linux](Images/17.png "time")
														![Linux](Images/18.png "memory")														
10. Changed process priority:                           ![Linux](Images/19.png "renice15")
                                                        ![Linux](Images/20.png "renice-15")
														![Linux](Images/21.png "renice0")														
11. Used the "kill" command:                            ![Linux](Images/22.png "kill-l")
                                                        ![Linux](Images/23.png "kill_19")
														![Linux](Images/24.png "top-p")
														![Linux](Images/25.png "top")														
12. Manage background processes:
    - jobs - displays a list of processes;
    - bg - continues executing the process in the background;
    - fg - takes the process out of the background mode;
    - nohup - allows the process to continue running in the background when it logs out of the system.                                                    
	                                                    ![Linux](Images/26.png "jobs")
														![Linux](Images/27.png "fg")
														![Linux](Images/28.png "bg")														
13. Checked the implementability of the most frequently used OPENSSH commands in the MS Windows OS:                                               
                                                        ![Linux](Images/29.png "ssh-keygen")
                                                        ![Linux](Images/30.png "ifconfig")
														![Linux](Images/31.png "ssh")
														![Linux](Images/32.png "scp.exe")																
14. Implement basic SSH settings to increase the security of the client-server connection:
                                                        ![Linux](Images/33.png "bak")
                                                        ![Linux](Images/34.png "PermitRootLogin_no")
														![Linux](Images/35.png "port2021")
														![Linux](Images/36.png "ListenAdress_my")															
15. Implemented three keys for encryption in SSH (rsa, dsa, ecdsa):
                                                        ![Linux](Images/37.png "rsa")
														![Linux](Images/38.png "dsa_ecdsa")
														![Linux](Images/39.png "ls")	
16. Implemented port forwarding for the SSH client from the host machine to the guest Linux VM behind NAT:
                                                        ![Linux](Images/40.png "NAT")														
17. Intercepted traffic with wireshark while authorizing the remote client:  
                                                        ![Linux](Images/41.png "wireshark")
                                                        ![Linux](Images/42.png "wireshark")
                                                        ![Linux](Images/43.png "wireshark")
														![Linux](Images/44.png "wireshark")
                                                        ![Linux](Images/45.png "wireshark")
