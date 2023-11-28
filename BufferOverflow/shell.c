
#include <stdio.h>

void foo () {
	asm (
		"jmp line \n\t"
		"address: pop %rsi \n\t"
		"mov %rsi, 0x08(%rsi) \n\t"
		"xor %rax, %rax \n\t"
		"mov %rax, 0x10(%rsi) \n\t"
		"mov %rax, 0x7(%rsi) \n\t"
		"mov %rax, %rdx \n\t"
		"movb $0x3b, %al \n\t"
		"mov %rsi, %rdi \n\t"
		"lea 0x08(%rsi), %rsi \n\t"
		"syscall \n\t"
		"xor %rax, %rax \n\t"
		"mov %rax, %rdi \n\t"
		"movb $0x3c, %al \n\t"
		"syscall \n\t"
		"line: call address\n\t"
		".string \"/bin/sh\" \n\t"
	);
}
int main()
{
	foo ();
}