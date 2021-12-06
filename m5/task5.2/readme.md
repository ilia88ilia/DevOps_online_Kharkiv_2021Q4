1. Added users:                                         ![Linux](Images/1.png "adduser")  
                                                        ![Linux](Images/2.png "passwd")
                                                        ![Linux](Images/3.png "group")
                                                        ![Linux](Images/4.png "user_login")                                               
2. UID (UserID), GID (GroupID), groups. Defined by the command "id":    
                                                        ![Linux](Images/5.png "UID_GID") 
3. Used "usermod". Renamed "user1" to "USER1". Used "/skel".
   The "/skel" directory contains the information that is assigned to each user when they are created: 			
                                                        ![Linux](Images/6.png "usermod")  
                                                        ![Linux](Images/7.png "rename_skel")
4. Recursive user deletion:                             ![Linux](Images/8.png "userdel")
5. Locked and unlocked "user2":                         ![Linux](Images/9.png "userlock") 	
6. Changed password to user2 using "passwd --expire:    ![Linux](Images/10.png "passs_expire")  
                                                        ![Linux](Images/11.png "pass_change")
7. 	For example drwxr-xr-x 27 ilia ilia  4096 Dec  1 18:04 .
    - d      -directory
    - rwx    -owners  (r-read, w-write, x-execute)
    - r-x    -group   (r-read, - no, x-execute) 
    - r-x    -others 	(r-read, - no, x-execute) 
	- 27     -number of objects inside the directory
	- ilia   -owners
	- ilia   -group
	                                                     ![Linux](Images/12.png "access_rights")														
8. Change the owner, access rights for the owner, groups and others. 
   Assigning access rights when creating with "umask".
   Prohibit deletion with granting full rights to all categories of users "StickyBit", revoke "StickyBit"
                                                        ![Linux](Images/13.png "chown") 
                                                        ![Linux](Images/14.png "chmod")
                                                        ![Linux](Images/15.png "stickyBit")
                                                        ![Linux](Images/16.png "umask")
														![Linux](Images/17.png "umask_stickyBit")
9. Manual for using script command "man script"         ![Linux](Images/18.png "man_script")
														![Linux](Images/19.png "man_script")
														
														
														
														
		
		
