	.file	"asm.c"
 # GNU C (tdm64-2) version 4.8.1 (x86_64-w64-mingw32)
 #	compiled by GNU C version 4.8.1, GMP version 4.3.2, MPFR version 2.4.2, MPC version 0.8.2
 # GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
 # options passed:  -imultilib 32
 # -iprefix c:\program files\dev-cpp\mingw64\bin\../lib/gcc/x86_64-w64-mingw32/4.8.1/
 # -D_REENTRANT asm.c -m32 -mtune=generic -march=x86-64
 # -auxbase-strip test.s -fverbose-asm
 # options enabled:  -faggressive-loop-optimizations
 # -fasynchronous-unwind-tables -fauto-inc-dec -fbranch-count-reg -fcommon
 # -fdelete-null-pointer-checks -fdwarf2-cfi-asm -fearly-inlining
 # -feliminate-unused-debug-types -ffunction-cse -fgcse-lm -fgnu-runtime
 # -fident -finline-atomics -fira-hoist-pressure -fira-share-save-slots
 # -fira-share-spill-slots -fivopts -fkeep-inline-dllexport
 # -fkeep-static-consts -fleading-underscore -fmath-errno
 # -fmerge-debug-strings -fmove-loop-invariants -fpeephole
 # -fprefetch-loop-arrays -freg-struct-return
 # -fsched-critical-path-heuristic -fsched-dep-count-heuristic
 # -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
 # -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
 # -fsched-stalled-insns-dep -fset-stack-executable -fshow-column
 # -fsigned-zeros -fsplit-ivs-in-unroller -fstrict-volatile-bitfields
 # -fsync-libcalls -ftrapping-math -ftree-coalesce-vars -ftree-cselim
 # -ftree-forwprop -ftree-loop-if-convert -ftree-loop-im
 # -ftree-loop-ivcanon -ftree-loop-optimize -ftree-parallelize-loops=
 # -ftree-phiprop -ftree-pta -ftree-reassoc -ftree-scev-cprop
 # -ftree-slp-vectorize -ftree-vect-loop-version -funit-at-a-time
 # -funwind-tables -fverbose-asm -fzero-initialized-in-bss -m32 -m80387
 # -m96bit-long-double -maccumulate-outgoing-args -malign-double
 # -malign-stringops -mfancy-math-387 -mfp-ret-in-387 -mfxsr -mieee-fp
 # -mlong-double-80 -mmmx -mms-bitfields -mno-red-zone -mno-sse4
 # -mpush-args -msahf -msse -msse2 -mstack-arg-probe

	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "%d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp	 #
	movl	%esp, %ebp	 #,
	andl	$-16, %esp	 #,
	subl	$32, %esp	 #,
	call	___main	 #
	movl	$0, 24(%esp)	 #, sum
	movl	$16, 20(%esp)	 #, x
	movl	$0, 28(%esp)	 #, i
	jmp	L2	 #
L3:
	movl	28(%esp), %eax	 # i, tmp60
	addl	%eax, 24(%esp)	 # tmp60, sum
	addl	$1, 28(%esp)	 #, i
L2:
	movl	28(%esp), %eax	 # i, tmp61
	cmpl	20(%esp), %eax	 # x, tmp61
	jl	L3	 #,
	movl	24(%esp), %eax	 # sum, tmp62
	movl	%eax, 4(%esp)	 # tmp62,
	movl	$LC0, (%esp)	 #,
	call	_printf	 #
	leave
	ret
	.ident	"GCC: (tdm64-2) 4.8.1"
	.def	_printf;	.scl	2;	.type	32;	.endef
