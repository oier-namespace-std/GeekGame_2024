
rtree:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <.init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    rsp,0x8
    1008:	48 8b 05 d9 2f 00 00 	mov    rax,QWORD PTR [rip+0x2fd9]        # 3fe8 <__isoc99_scanf@plt+0x2e98>
    100f:	48 85 c0             	test   rax,rax
    1012:	74 02                	je     1016 <__cxa_finalize@plt-0xaa>
    1014:	ff d0                	call   rax
    1016:	48 83 c4 08          	add    rsp,0x8
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 5a 2f 00 00    	push   QWORD PTR [rip+0x2f5a]        # 3f80 <__isoc99_scanf@plt+0x2e30>
    1026:	f2 ff 25 5b 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f5b]        # 3f88 <__isoc99_scanf@plt+0x2e38>
    102d:	0f 1f 00             	nop    DWORD PTR [rax]
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    105f:	90                   	nop
    1060:	f3 0f 1e fa          	endbr64 
    1064:	68 03 00 00 00       	push   0x3
    1069:	f2 e9 b1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    106f:	90                   	nop
    1070:	f3 0f 1e fa          	endbr64 
    1074:	68 04 00 00 00       	push   0x4
    1079:	f2 e9 a1 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    107f:	90                   	nop
    1080:	f3 0f 1e fa          	endbr64 
    1084:	68 05 00 00 00       	push   0x5
    1089:	f2 e9 91 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    108f:	90                   	nop
    1090:	f3 0f 1e fa          	endbr64 
    1094:	68 06 00 00 00       	push   0x6
    1099:	f2 e9 81 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    109f:	90                   	nop
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	68 07 00 00 00       	push   0x7
    10a9:	f2 e9 71 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    10af:	90                   	nop
    10b0:	f3 0f 1e fa          	endbr64 
    10b4:	68 08 00 00 00       	push   0x8
    10b9:	f2 e9 61 ff ff ff    	bnd jmp 1020 <__cxa_finalize@plt-0xa0>
    10bf:	90                   	nop

Disassembly of section .plt.got:

00000000000010c0 <__cxa_finalize@plt>:
    10c0:	f3 0f 1e fa          	endbr64 
    10c4:	f2 ff 25 2d 2f 00 00 	bnd jmp QWORD PTR [rip+0x2f2d]        # 3ff8 <__isoc99_scanf@plt+0x2ea8>
    10cb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .plt.sec:

00000000000010d0 <free@plt>:
    10d0:	f3 0f 1e fa          	endbr64 
    10d4:	f2 ff 25 b5 2e 00 00 	bnd jmp QWORD PTR [rip+0x2eb5]        # 3f90 <__isoc99_scanf@plt+0x2e40>
    10db:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000000010e0 <puts@plt>:
    10e0:	f3 0f 1e fa          	endbr64 
    10e4:	f2 ff 25 ad 2e 00 00 	bnd jmp QWORD PTR [rip+0x2ead]        # 3f98 <__isoc99_scanf@plt+0x2e48>
    10eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

00000000000010f0 <write@plt>:
    10f0:	f3 0f 1e fa          	endbr64 
    10f4:	f2 ff 25 a5 2e 00 00 	bnd jmp QWORD PTR [rip+0x2ea5]        # 3fa0 <__isoc99_scanf@plt+0x2e50>
    10fb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001100 <__stack_chk_fail@plt>:
    1100:	f3 0f 1e fa          	endbr64 
    1104:	f2 ff 25 9d 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e9d]        # 3fa8 <__isoc99_scanf@plt+0x2e58>
    110b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001110 <setbuf@plt>:
    1110:	f3 0f 1e fa          	endbr64 
    1114:	f2 ff 25 95 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e95]        # 3fb0 <__isoc99_scanf@plt+0x2e60>
    111b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001120 <printf@plt>:
    1120:	f3 0f 1e fa          	endbr64 
    1124:	f2 ff 25 8d 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e8d]        # 3fb8 <__isoc99_scanf@plt+0x2e68>
    112b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001130 <read@plt>:
    1130:	f3 0f 1e fa          	endbr64 
    1134:	f2 ff 25 85 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e85]        # 3fc0 <__isoc99_scanf@plt+0x2e70>
    113b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001140 <malloc@plt>:
    1140:	f3 0f 1e fa          	endbr64 
    1144:	f2 ff 25 7d 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e7d]        # 3fc8 <__isoc99_scanf@plt+0x2e78>
    114b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001150 <__isoc99_scanf@plt>:
    1150:	f3 0f 1e fa          	endbr64 
    1154:	f2 ff 25 75 2e 00 00 	bnd jmp QWORD PTR [rip+0x2e75]        # 3fd0 <__isoc99_scanf@plt+0x2e80>
    115b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

0000000000001160 <.text>:
    1160:	f3 0f 1e fa          	endbr64 
    1164:	31 ed                	xor    ebp,ebp
    1166:	49 89 d1             	mov    r9,rdx
    1169:	5e                   	pop    rsi
    116a:	48 89 e2             	mov    rdx,rsp
    116d:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
    1171:	50                   	push   rax
    1172:	54                   	push   rsp
    1173:	4c 8d 05 16 0a 00 00 	lea    r8,[rip+0xa16]        # 1b90 <__isoc99_scanf@plt+0xa40>
    117a:	48 8d 0d 9f 09 00 00 	lea    rcx,[rip+0x99f]        # 1b20 <__isoc99_scanf@plt+0x9d0>
    1181:	48 8d 3d b3 08 00 00 	lea    rdi,[rip+0x8b3]        # 1a3b <__isoc99_scanf@plt+0x8eb>
    1188:	ff 15 52 2e 00 00    	call   QWORD PTR [rip+0x2e52]        # 3fe0 <__isoc99_scanf@plt+0x2e90>
    118e:	f4                   	hlt    
    118f:	90                   	nop
    1190:	48 8d 3d 79 2e 00 00 	lea    rdi,[rip+0x2e79]        # 4010 <__isoc99_scanf@plt+0x2ec0>
    1197:	48 8d 05 72 2e 00 00 	lea    rax,[rip+0x2e72]        # 4010 <__isoc99_scanf@plt+0x2ec0>
    119e:	48 39 f8             	cmp    rax,rdi
    11a1:	74 15                	je     11b8 <__isoc99_scanf@plt+0x68>
    11a3:	48 8b 05 2e 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e2e]        # 3fd8 <__isoc99_scanf@plt+0x2e88>
    11aa:	48 85 c0             	test   rax,rax
    11ad:	74 09                	je     11b8 <__isoc99_scanf@plt+0x68>
    11af:	ff e0                	jmp    rax
    11b1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    11b8:	c3                   	ret    
    11b9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    11c0:	48 8d 3d 49 2e 00 00 	lea    rdi,[rip+0x2e49]        # 4010 <__isoc99_scanf@plt+0x2ec0>
    11c7:	48 8d 35 42 2e 00 00 	lea    rsi,[rip+0x2e42]        # 4010 <__isoc99_scanf@plt+0x2ec0>
    11ce:	48 29 fe             	sub    rsi,rdi
    11d1:	48 89 f0             	mov    rax,rsi
    11d4:	48 c1 ee 3f          	shr    rsi,0x3f
    11d8:	48 c1 f8 03          	sar    rax,0x3
    11dc:	48 01 c6             	add    rsi,rax
    11df:	48 d1 fe             	sar    rsi,1
    11e2:	74 14                	je     11f8 <__isoc99_scanf@plt+0xa8>
    11e4:	48 8b 05 05 2e 00 00 	mov    rax,QWORD PTR [rip+0x2e05]        # 3ff0 <__isoc99_scanf@plt+0x2ea0>
    11eb:	48 85 c0             	test   rax,rax
    11ee:	74 08                	je     11f8 <__isoc99_scanf@plt+0xa8>
    11f0:	ff e0                	jmp    rax
    11f2:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    11f8:	c3                   	ret    
    11f9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1200:	f3 0f 1e fa          	endbr64 
    1204:	80 3d 3d 2e 00 00 00 	cmp    BYTE PTR [rip+0x2e3d],0x0        # 4048 <stderr@GLIBC_2.2.5+0x8>
    120b:	75 2b                	jne    1238 <__isoc99_scanf@plt+0xe8>
    120d:	55                   	push   rbp
    120e:	48 83 3d e2 2d 00 00 	cmp    QWORD PTR [rip+0x2de2],0x0        # 3ff8 <__isoc99_scanf@plt+0x2ea8>
    1215:	00 
    1216:	48 89 e5             	mov    rbp,rsp
    1219:	74 0c                	je     1227 <__isoc99_scanf@plt+0xd7>
    121b:	48 8b 3d e6 2d 00 00 	mov    rdi,QWORD PTR [rip+0x2de6]        # 4008 <__isoc99_scanf@plt+0x2eb8>
    1222:	e8 99 fe ff ff       	call   10c0 <__cxa_finalize@plt>
    1227:	e8 64 ff ff ff       	call   1190 <__isoc99_scanf@plt+0x40>
    122c:	c6 05 15 2e 00 00 01 	mov    BYTE PTR [rip+0x2e15],0x1        # 4048 <stderr@GLIBC_2.2.5+0x8>
    1233:	5d                   	pop    rbp
    1234:	c3                   	ret    
    1235:	0f 1f 00             	nop    DWORD PTR [rax]
    1238:	c3                   	ret    
    1239:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1240:	f3 0f 1e fa          	endbr64 
    1244:	e9 77 ff ff ff       	jmp    11c0 <__isoc99_scanf@plt+0x70>
    1249:	f3 0f 1e fa          	endbr64 
    124d:	55                   	push   rbp
    124e:	48 89 e5             	mov    rbp,rsp
    1251:	48 8b 05 d8 2d 00 00 	mov    rax,QWORD PTR [rip+0x2dd8]        # 4030 <stdin@GLIBC_2.2.5>
    1258:	be 00 00 00 00       	mov    esi,0x0
    125d:	48 89 c7             	mov    rdi,rax
    1260:	e8 ab fe ff ff       	call   1110 <setbuf@plt>
    1265:	48 8b 05 b4 2d 00 00 	mov    rax,QWORD PTR [rip+0x2db4]        # 4020 <stdout@GLIBC_2.2.5>
    126c:	be 00 00 00 00       	mov    esi,0x0
    1271:	48 89 c7             	mov    rdi,rax
    1274:	e8 97 fe ff ff       	call   1110 <setbuf@plt>
    1279:	48 8b 05 c0 2d 00 00 	mov    rax,QWORD PTR [rip+0x2dc0]        # 4040 <stderr@GLIBC_2.2.5>
    1280:	be 00 00 00 00       	mov    esi,0x0
    1285:	48 89 c7             	mov    rdi,rax
    1288:	e8 83 fe ff ff       	call   1110 <setbuf@plt>
    128d:	90                   	nop
    128e:	5d                   	pop    rbp
    128f:	c3                   	ret    
    1290:	f3 0f 1e fa          	endbr64 
    1294:	55                   	push   rbp
    1295:	48 89 e5             	mov    rbp,rsp
    1298:	48 83 ec 10          	sub    rsp,0x10
    129c:	bf 38 00 00 00       	mov    edi,0x38
    12a1:	e8 9a fe ff ff       	call   1140 <malloc@plt>
    12a6:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    12aa:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12ae:	48 c7 40 30 00 00 00 	mov    QWORD PTR [rax+0x30],0x0
    12b5:	00 
    12b6:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12ba:	48 8b 50 30          	mov    rdx,QWORD PTR [rax+0x30]
    12be:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12c2:	48 89 50 28          	mov    QWORD PTR [rax+0x28],rdx
    12c6:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12ca:	48 8b 50 28          	mov    rdx,QWORD PTR [rax+0x28]
    12ce:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12d2:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    12d6:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12da:	48 8b 50 20          	mov    rdx,QWORD PTR [rax+0x20]
    12de:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12e2:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    12e6:	48 8d 3d 1b 0d 00 00 	lea    rdi,[rip+0xd1b]        # 2008 <__isoc99_scanf@plt+0xeb8>
    12ed:	e8 ee fd ff ff       	call   10e0 <puts@plt>
    12f2:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    12f6:	48 89 c6             	mov    rsi,rax
    12f9:	48 8d 3d 22 0d 00 00 	lea    rdi,[rip+0xd22]        # 2022 <__isoc99_scanf@plt+0xed2>
    1300:	b8 00 00 00 00       	mov    eax,0x0
    1305:	e8 46 fe ff ff       	call   1150 <__isoc99_scanf@plt>
    130a:	48 8d 3d 17 0d 00 00 	lea    rdi,[rip+0xd17]        # 2028 <__isoc99_scanf@plt+0xed8>
    1311:	e8 ca fd ff ff       	call   10e0 <puts@plt>
    1316:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    131a:	48 83 c0 10          	add    rax,0x10
    131e:	48 89 c6             	mov    rsi,rax
    1321:	48 8d 3d fa 0c 00 00 	lea    rdi,[rip+0xcfa]        # 2022 <__isoc99_scanf@plt+0xed2>
    1328:	b8 00 00 00 00       	mov    eax,0x0
    132d:	e8 1e fe ff ff       	call   1150 <__isoc99_scanf@plt>
    1332:	48 8d 3d 11 0d 00 00 	lea    rdi,[rip+0xd11]        # 204a <__isoc99_scanf@plt+0xefa>
    1339:	e8 a2 fd ff ff       	call   10e0 <puts@plt>
    133e:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    1342:	8b 40 10             	mov    eax,DWORD PTR [rax+0x10]
    1345:	48 98                	cdqe   
    1347:	48 89 c7             	mov    rdi,rax
    134a:	e8 f1 fd ff ff       	call   1140 <malloc@plt>
    134f:	48 89 c2             	mov    rdx,rax
    1352:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    1356:	48 89 50 08          	mov    QWORD PTR [rax+0x8],rdx
    135a:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    135e:	8b 50 10             	mov    edx,DWORD PTR [rax+0x10]
    1361:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    1365:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1369:	48 89 c6             	mov    rsi,rax
    136c:	bf 00 00 00 00       	mov    edi,0x0
    1371:	b8 00 00 00 00       	mov    eax,0x0
    1376:	e8 b5 fd ff ff       	call   1130 <read@plt>
    137b:	48 8b 05 ce 2c 00 00 	mov    rax,QWORD PTR [rip+0x2cce]        # 4050 <stderr@GLIBC_2.2.5+0x10>
    1382:	48 85 c0             	test   rax,rax
    1385:	75 10                	jne    1397 <__isoc99_scanf@plt+0x247>
    1387:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    138b:	48 89 05 be 2c 00 00 	mov    QWORD PTR [rip+0x2cbe],rax        # 4050 <stderr@GLIBC_2.2.5+0x10>
    1392:	e9 c7 00 00 00       	jmp    145e <__isoc99_scanf@plt+0x30e>
    1397:	48 8b 05 b2 2c 00 00 	mov    rax,QWORD PTR [rip+0x2cb2]        # 4050 <stderr@GLIBC_2.2.5+0x10>
    139e:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    13a2:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13a6:	8b 10                	mov    edx,DWORD PTR [rax]
    13a8:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    13ac:	8b 00                	mov    eax,DWORD PTR [rax]
    13ae:	39 c2                	cmp    edx,eax
    13b0:	75 2c                	jne    13de <__isoc99_scanf@plt+0x28e>
    13b2:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13b6:	48 8b 40 30          	mov    rax,QWORD PTR [rax+0x30]
    13ba:	48 85 c0             	test   rax,rax
    13bd:	75 11                	jne    13d0 <__isoc99_scanf@plt+0x280>
    13bf:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13c3:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
    13c7:	48 89 50 30          	mov    QWORD PTR [rax+0x30],rdx
    13cb:	e9 8e 00 00 00       	jmp    145e <__isoc99_scanf@plt+0x30e>
    13d0:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13d4:	48 8b 40 30          	mov    rax,QWORD PTR [rax+0x30]
    13d8:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    13dc:	eb c4                	jmp    13a2 <__isoc99_scanf@plt+0x252>
    13de:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13e2:	8b 10                	mov    edx,DWORD PTR [rax]
    13e4:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    13e8:	8b 00                	mov    eax,DWORD PTR [rax]
    13ea:	39 c2                	cmp    edx,eax
    13ec:	7e 38                	jle    1426 <__isoc99_scanf@plt+0x2d6>
    13ee:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13f2:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    13f6:	48 85 c0             	test   rax,rax
    13f9:	75 1a                	jne    1415 <__isoc99_scanf@plt+0x2c5>
    13fb:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    13ff:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
    1403:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    1407:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    140b:	48 8b 55 f0          	mov    rdx,QWORD PTR [rbp-0x10]
    140f:	48 89 50 28          	mov    QWORD PTR [rax+0x28],rdx
    1413:	eb 49                	jmp    145e <__isoc99_scanf@plt+0x30e>
    1415:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1419:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    141d:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    1421:	e9 7c ff ff ff       	jmp    13a2 <__isoc99_scanf@plt+0x252>
    1426:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    142a:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    142e:	48 85 c0             	test   rax,rax
    1431:	75 1a                	jne    144d <__isoc99_scanf@plt+0x2fd>
    1433:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1437:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
    143b:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    143f:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    1443:	48 8b 55 f0          	mov    rdx,QWORD PTR [rbp-0x10]
    1447:	48 89 50 28          	mov    QWORD PTR [rax+0x28],rdx
    144b:	eb 11                	jmp    145e <__isoc99_scanf@plt+0x30e>
    144d:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1451:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    1455:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    1459:	e9 44 ff ff ff       	jmp    13a2 <__isoc99_scanf@plt+0x252>
    145e:	c9                   	leave  
    145f:	c3                   	ret    
    1460:	f3 0f 1e fa          	endbr64 
    1464:	55                   	push   rbp
    1465:	48 89 e5             	mov    rbp,rsp
    1468:	48 83 ec 20          	sub    rsp,0x20
    146c:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    1473:	00 00 
    1475:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    1479:	31 c0                	xor    eax,eax
    147b:	48 8d 3d de 0b 00 00 	lea    rdi,[rip+0xbde]        # 2060 <__isoc99_scanf@plt+0xf10>
    1482:	e8 59 fc ff ff       	call   10e0 <puts@plt>
    1487:	48 8d 45 ec          	lea    rax,[rbp-0x14]
    148b:	48 89 c6             	mov    rsi,rax
    148e:	48 8d 3d 8d 0b 00 00 	lea    rdi,[rip+0xb8d]        # 2022 <__isoc99_scanf@plt+0xed2>
    1495:	b8 00 00 00 00       	mov    eax,0x0
    149a:	e8 b1 fc ff ff       	call   1150 <__isoc99_scanf@plt>
    149f:	48 8b 05 aa 2b 00 00 	mov    rax,QWORD PTR [rip+0x2baa]        # 4050 <stderr@GLIBC_2.2.5+0x10>
    14a6:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    14aa:	eb 63                	jmp    150f <__isoc99_scanf@plt+0x3bf>
    14ac:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    14b0:	8b 10                	mov    edx,DWORD PTR [rax]
    14b2:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14b5:	39 c2                	cmp    edx,eax
    14b7:	75 2f                	jne    14e8 <__isoc99_scanf@plt+0x398>
    14b9:	48 8d 3d d2 0b 00 00 	lea    rdi,[rip+0xbd2]        # 2092 <__isoc99_scanf@plt+0xf42>
    14c0:	e8 1b fc ff ff       	call   10e0 <puts@plt>
    14c5:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    14c9:	8b 50 10             	mov    edx,DWORD PTR [rax+0x10]
    14cc:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    14d0:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    14d4:	48 89 c6             	mov    rsi,rax
    14d7:	bf 01 00 00 00       	mov    edi,0x1
    14dc:	b8 00 00 00 00       	mov    eax,0x0
    14e1:	e8 0a fc ff ff       	call   10f0 <write@plt>
    14e6:	eb 3a                	jmp    1522 <__isoc99_scanf@plt+0x3d2>
    14e8:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    14ec:	8b 10                	mov    edx,DWORD PTR [rax]
    14ee:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    14f1:	39 c2                	cmp    edx,eax
    14f3:	7e 0e                	jle    1503 <__isoc99_scanf@plt+0x3b3>
    14f5:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    14f9:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    14fd:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    1501:	eb 0c                	jmp    150f <__isoc99_scanf@plt+0x3bf>
    1503:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1507:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    150b:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    150f:	48 83 7d f0 00       	cmp    QWORD PTR [rbp-0x10],0x0
    1514:	75 96                	jne    14ac <__isoc99_scanf@plt+0x35c>
    1516:	48 8d 3d 8f 0b 00 00 	lea    rdi,[rip+0xb8f]        # 20ac <__isoc99_scanf@plt+0xf5c>
    151d:	e8 be fb ff ff       	call   10e0 <puts@plt>
    1522:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    1526:	64 48 33 04 25 28 00 	xor    rax,QWORD PTR fs:0x28
    152d:	00 00 
    152f:	74 05                	je     1536 <__isoc99_scanf@plt+0x3e6>
    1531:	e8 ca fb ff ff       	call   1100 <__stack_chk_fail@plt>
    1536:	c9                   	leave  
    1537:	c3                   	ret    
    1538:	f3 0f 1e fa          	endbr64 
    153c:	55                   	push   rbp
    153d:	48 89 e5             	mov    rbp,rsp
    1540:	48 83 ec 30          	sub    rsp,0x30
    1544:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    154b:	00 00 
    154d:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    1551:	31 c0                	xor    eax,eax
    1553:	48 8d 3d 6e 0b 00 00 	lea    rdi,[rip+0xb6e]        # 20c8 <__isoc99_scanf@plt+0xf78>
    155a:	e8 81 fb ff ff       	call   10e0 <puts@plt>
    155f:	48 8d 45 d4          	lea    rax,[rbp-0x2c]
    1563:	48 89 c6             	mov    rsi,rax
    1566:	48 8d 3d b5 0a 00 00 	lea    rdi,[rip+0xab5]        # 2022 <__isoc99_scanf@plt+0xed2>
    156d:	b8 00 00 00 00       	mov    eax,0x0
    1572:	e8 d9 fb ff ff       	call   1150 <__isoc99_scanf@plt>
    1577:	48 8b 05 d2 2a 00 00 	mov    rax,QWORD PTR [rip+0x2ad2]        # 4050 <stderr@GLIBC_2.2.5+0x10>
    157e:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
    1582:	e9 4b 03 00 00       	jmp    18d2 <__isoc99_scanf@plt+0x782>
    1587:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    158b:	8b 10                	mov    edx,DWORD PTR [rax]
    158d:	8b 45 d4             	mov    eax,DWORD PTR [rbp-0x2c]
    1590:	39 c2                	cmp    edx,eax
    1592:	0f 85 13 03 00 00    	jne    18ab <__isoc99_scanf@plt+0x75b>
    1598:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    159c:	48 8b 40 30          	mov    rax,QWORD PTR [rax+0x30]
    15a0:	48 85 c0             	test   rax,rax
    15a3:	74 4d                	je     15f2 <__isoc99_scanf@plt+0x4a2>
    15a5:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15a9:	48 8b 40 30          	mov    rax,QWORD PTR [rax+0x30]
    15ad:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    15b1:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15b5:	48 8b 50 18          	mov    rdx,QWORD PTR [rax+0x18]
    15b9:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    15bd:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    15c1:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15c5:	48 8b 50 20          	mov    rdx,QWORD PTR [rax+0x20]
    15c9:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    15cd:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    15d1:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15d5:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    15d9:	48 89 c7             	mov    rdi,rax
    15dc:	e8 ef fa ff ff       	call   10d0 <free@plt>
    15e1:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15e5:	48 89 c7             	mov    rdi,rax
    15e8:	e8 e3 fa ff ff       	call   10d0 <free@plt>
    15ed:	e9 f7 02 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    15f2:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    15f6:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    15fa:	48 85 c0             	test   rax,rax
    15fd:	0f 85 9f 00 00 00    	jne    16a2 <__isoc99_scanf@plt+0x552>
    1603:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1607:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    160b:	48 85 c0             	test   rax,rax
    160e:	0f 85 8e 00 00 00    	jne    16a2 <__isoc99_scanf@plt+0x552>
    1614:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1618:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    161c:	48 85 c0             	test   rax,rax
    161f:	75 2c                	jne    164d <__isoc99_scanf@plt+0x4fd>
    1621:	48 c7 05 24 2a 00 00 	mov    QWORD PTR [rip+0x2a24],0x0        # 4050 <stderr@GLIBC_2.2.5+0x10>
    1628:	00 00 00 00 
    162c:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1630:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1634:	48 89 c7             	mov    rdi,rax
    1637:	e8 94 fa ff ff       	call   10d0 <free@plt>
    163c:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1640:	48 89 c7             	mov    rdi,rax
    1643:	e8 88 fa ff ff       	call   10d0 <free@plt>
    1648:	e9 9c 02 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    164d:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1651:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1655:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    1659:	48 39 45 d8          	cmp    QWORD PTR [rbp-0x28],rax
    165d:	75 12                	jne    1671 <__isoc99_scanf@plt+0x521>
    165f:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1663:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1667:	48 c7 40 18 00 00 00 	mov    QWORD PTR [rax+0x18],0x0
    166e:	00 
    166f:	eb 10                	jmp    1681 <__isoc99_scanf@plt+0x531>
    1671:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1675:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1679:	48 c7 40 20 00 00 00 	mov    QWORD PTR [rax+0x20],0x0
    1680:	00 
    1681:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1685:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1689:	48 89 c7             	mov    rdi,rax
    168c:	e8 3f fa ff ff       	call   10d0 <free@plt>
    1691:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1695:	48 89 c7             	mov    rdi,rax
    1698:	e8 33 fa ff ff       	call   10d0 <free@plt>
    169d:	e9 47 02 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    16a2:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16a6:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    16aa:	48 85 c0             	test   rax,rax
    16ad:	0f 85 9a 00 00 00    	jne    174d <__isoc99_scanf@plt+0x5fd>
    16b3:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16b7:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    16bb:	48 85 c0             	test   rax,rax
    16be:	75 30                	jne    16f0 <__isoc99_scanf@plt+0x5a0>
    16c0:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16c4:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    16c8:	48 89 05 81 29 00 00 	mov    QWORD PTR [rip+0x2981],rax        # 4050 <stderr@GLIBC_2.2.5+0x10>
    16cf:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16d3:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    16d7:	48 89 c7             	mov    rdi,rax
    16da:	e8 f1 f9 ff ff       	call   10d0 <free@plt>
    16df:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16e3:	48 89 c7             	mov    rdi,rax
    16e6:	e8 e5 f9 ff ff       	call   10d0 <free@plt>
    16eb:	e9 f9 01 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    16f0:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    16f4:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    16f8:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    16fc:	48 39 45 d8          	cmp    QWORD PTR [rbp-0x28],rax
    1700:	75 16                	jne    1718 <__isoc99_scanf@plt+0x5c8>
    1702:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1706:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    170a:	48 8b 55 d8          	mov    rdx,QWORD PTR [rbp-0x28]
    170e:	48 8b 52 20          	mov    rdx,QWORD PTR [rdx+0x20]
    1712:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    1716:	eb 14                	jmp    172c <__isoc99_scanf@plt+0x5dc>
    1718:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    171c:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1720:	48 8b 55 d8          	mov    rdx,QWORD PTR [rbp-0x28]
    1724:	48 8b 52 20          	mov    rdx,QWORD PTR [rdx+0x20]
    1728:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    172c:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1730:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1734:	48 89 c7             	mov    rdi,rax
    1737:	e8 94 f9 ff ff       	call   10d0 <free@plt>
    173c:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1740:	48 89 c7             	mov    rdi,rax
    1743:	e8 88 f9 ff ff       	call   10d0 <free@plt>
    1748:	e9 9c 01 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    174d:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1751:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    1755:	48 85 c0             	test   rax,rax
    1758:	0f 85 9a 00 00 00    	jne    17f8 <__isoc99_scanf@plt+0x6a8>
    175e:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1762:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1766:	48 85 c0             	test   rax,rax
    1769:	75 30                	jne    179b <__isoc99_scanf@plt+0x64b>
    176b:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    176f:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    1773:	48 89 05 d6 28 00 00 	mov    QWORD PTR [rip+0x28d6],rax        # 4050 <stderr@GLIBC_2.2.5+0x10>
    177a:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    177e:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1782:	48 89 c7             	mov    rdi,rax
    1785:	e8 46 f9 ff ff       	call   10d0 <free@plt>
    178a:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    178e:	48 89 c7             	mov    rdi,rax
    1791:	e8 3a f9 ff ff       	call   10d0 <free@plt>
    1796:	e9 4e 01 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    179b:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    179f:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    17a3:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    17a7:	48 39 45 d8          	cmp    QWORD PTR [rbp-0x28],rax
    17ab:	75 16                	jne    17c3 <__isoc99_scanf@plt+0x673>
    17ad:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    17b1:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    17b5:	48 8b 55 d8          	mov    rdx,QWORD PTR [rbp-0x28]
    17b9:	48 8b 52 18          	mov    rdx,QWORD PTR [rdx+0x18]
    17bd:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    17c1:	eb 14                	jmp    17d7 <__isoc99_scanf@plt+0x687>
    17c3:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    17c7:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    17cb:	48 8b 55 d8          	mov    rdx,QWORD PTR [rbp-0x28]
    17cf:	48 8b 52 18          	mov    rdx,QWORD PTR [rdx+0x18]
    17d3:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    17d7:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    17db:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    17df:	48 89 c7             	mov    rdi,rax
    17e2:	e8 e9 f8 ff ff       	call   10d0 <free@plt>
    17e7:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    17eb:	48 89 c7             	mov    rdi,rax
    17ee:	e8 dd f8 ff ff       	call   10d0 <free@plt>
    17f3:	e9 f1 00 00 00       	jmp    18e9 <__isoc99_scanf@plt+0x799>
    17f8:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    17fc:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    1800:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
    1804:	eb 0c                	jmp    1812 <__isoc99_scanf@plt+0x6c2>
    1806:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    180a:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    180e:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
    1812:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    1816:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    181a:	48 85 c0             	test   rax,rax
    181d:	75 e7                	jne    1806 <__isoc99_scanf@plt+0x6b6>
    181f:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    1823:	8b 10                	mov    edx,DWORD PTR [rax]
    1825:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1829:	89 10                	mov    DWORD PTR [rax],edx
    182b:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    182f:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1833:	48 89 45 e8          	mov    QWORD PTR [rbp-0x18],rax
    1837:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    183b:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    183f:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1843:	48 89 50 08          	mov    QWORD PTR [rax+0x8],rdx
    1847:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    184b:	8b 50 10             	mov    edx,DWORD PTR [rax+0x10]
    184e:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    1852:	89 50 10             	mov    DWORD PTR [rax+0x10],edx
    1855:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    1859:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    185d:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    1861:	48 39 45 e0          	cmp    QWORD PTR [rbp-0x20],rax
    1865:	75 16                	jne    187d <__isoc99_scanf@plt+0x72d>
    1867:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    186b:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    186f:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
    1873:	48 8b 52 20          	mov    rdx,QWORD PTR [rdx+0x20]
    1877:	48 89 50 18          	mov    QWORD PTR [rax+0x18],rdx
    187b:	eb 14                	jmp    1891 <__isoc99_scanf@plt+0x741>
    187d:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    1881:	48 8b 40 28          	mov    rax,QWORD PTR [rax+0x28]
    1885:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
    1889:	48 8b 52 20          	mov    rdx,QWORD PTR [rdx+0x20]
    188d:	48 89 50 20          	mov    QWORD PTR [rax+0x20],rdx
    1891:	48 8b 45 e8          	mov    rax,QWORD PTR [rbp-0x18]
    1895:	48 89 c7             	mov    rdi,rax
    1898:	e8 33 f8 ff ff       	call   10d0 <free@plt>
    189d:	48 8b 45 e0          	mov    rax,QWORD PTR [rbp-0x20]
    18a1:	48 89 c7             	mov    rdi,rax
    18a4:	e8 27 f8 ff ff       	call   10d0 <free@plt>
    18a9:	eb 3e                	jmp    18e9 <__isoc99_scanf@plt+0x799>
    18ab:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    18af:	8b 10                	mov    edx,DWORD PTR [rax]
    18b1:	8b 45 d4             	mov    eax,DWORD PTR [rbp-0x2c]
    18b4:	39 c2                	cmp    edx,eax
    18b6:	7e 0e                	jle    18c6 <__isoc99_scanf@plt+0x776>
    18b8:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    18bc:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    18c0:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
    18c4:	eb 0c                	jmp    18d2 <__isoc99_scanf@plt+0x782>
    18c6:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
    18ca:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    18ce:	48 89 45 d8          	mov    QWORD PTR [rbp-0x28],rax
    18d2:	48 83 7d d8 00       	cmp    QWORD PTR [rbp-0x28],0x0
    18d7:	0f 85 aa fc ff ff    	jne    1587 <__isoc99_scanf@plt+0x437>
    18dd:	48 8d 3d c8 07 00 00 	lea    rdi,[rip+0x7c8]        # 20ac <__isoc99_scanf@plt+0xf5c>
    18e4:	e8 f7 f7 ff ff       	call   10e0 <puts@plt>
    18e9:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    18ed:	64 48 33 04 25 28 00 	xor    rax,QWORD PTR fs:0x28
    18f4:	00 00 
    18f6:	74 05                	je     18fd <__isoc99_scanf@plt+0x7ad>
    18f8:	e8 03 f8 ff ff       	call   1100 <__stack_chk_fail@plt>
    18fd:	c9                   	leave  
    18fe:	c3                   	ret    
    18ff:	f3 0f 1e fa          	endbr64 
    1903:	55                   	push   rbp
    1904:	48 89 e5             	mov    rbp,rsp
    1907:	48 83 ec 20          	sub    rsp,0x20
    190b:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    1912:	00 00 
    1914:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    1918:	31 c0                	xor    eax,eax
    191a:	48 8d 3d df 07 00 00 	lea    rdi,[rip+0x7df]        # 2100 <__isoc99_scanf@plt+0xfb0>
    1921:	e8 ba f7 ff ff       	call   10e0 <puts@plt>
    1926:	48 8d 45 ec          	lea    rax,[rbp-0x14]
    192a:	48 89 c6             	mov    rsi,rax
    192d:	48 8d 3d ee 06 00 00 	lea    rdi,[rip+0x6ee]        # 2022 <__isoc99_scanf@plt+0xed2>
    1934:	b8 00 00 00 00       	mov    eax,0x0
    1939:	e8 12 f8 ff ff       	call   1150 <__isoc99_scanf@plt>
    193e:	48 8b 05 0b 27 00 00 	mov    rax,QWORD PTR [rip+0x270b]        # 4050 <stderr@GLIBC_2.2.5+0x10>
    1945:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    1949:	eb 63                	jmp    19ae <__isoc99_scanf@plt+0x85e>
    194b:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    194f:	8b 10                	mov    edx,DWORD PTR [rax]
    1951:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    1954:	39 c2                	cmp    edx,eax
    1956:	75 2f                	jne    1987 <__isoc99_scanf@plt+0x837>
    1958:	48 8d 3d de 07 00 00 	lea    rdi,[rip+0x7de]        # 213d <__isoc99_scanf@plt+0xfed>
    195f:	e8 7c f7 ff ff       	call   10e0 <puts@plt>
    1964:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1968:	8b 50 10             	mov    edx,DWORD PTR [rax+0x10]
    196b:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    196f:	48 8b 40 08          	mov    rax,QWORD PTR [rax+0x8]
    1973:	48 89 c6             	mov    rsi,rax
    1976:	bf 00 00 00 00       	mov    edi,0x0
    197b:	b8 00 00 00 00       	mov    eax,0x0
    1980:	e8 ab f7 ff ff       	call   1130 <read@plt>
    1985:	eb 3a                	jmp    19c1 <__isoc99_scanf@plt+0x871>
    1987:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    198b:	8b 10                	mov    edx,DWORD PTR [rax]
    198d:	8b 45 ec             	mov    eax,DWORD PTR [rbp-0x14]
    1990:	39 c2                	cmp    edx,eax
    1992:	7e 0e                	jle    19a2 <__isoc99_scanf@plt+0x852>
    1994:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    1998:	48 8b 40 18          	mov    rax,QWORD PTR [rax+0x18]
    199c:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    19a0:	eb 0c                	jmp    19ae <__isoc99_scanf@plt+0x85e>
    19a2:	48 8b 45 f0          	mov    rax,QWORD PTR [rbp-0x10]
    19a6:	48 8b 40 20          	mov    rax,QWORD PTR [rax+0x20]
    19aa:	48 89 45 f0          	mov    QWORD PTR [rbp-0x10],rax
    19ae:	48 83 7d f0 00       	cmp    QWORD PTR [rbp-0x10],0x0
    19b3:	75 96                	jne    194b <__isoc99_scanf@plt+0x7fb>
    19b5:	48 8d 3d f0 06 00 00 	lea    rdi,[rip+0x6f0]        # 20ac <__isoc99_scanf@plt+0xf5c>
    19bc:	e8 1f f7 ff ff       	call   10e0 <puts@plt>
    19c1:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    19c5:	64 48 33 04 25 28 00 	xor    rax,QWORD PTR fs:0x28
    19cc:	00 00 
    19ce:	74 05                	je     19d5 <__isoc99_scanf@plt+0x885>
    19d0:	e8 2b f7 ff ff       	call   1100 <__stack_chk_fail@plt>
    19d5:	c9                   	leave  
    19d6:	c3                   	ret    
    19d7:	f3 0f 1e fa          	endbr64 
    19db:	55                   	push   rbp
    19dc:	48 89 e5             	mov    rbp,rsp
    19df:	48 8d 3d 72 07 00 00 	lea    rdi,[rip+0x772]        # 2158 <__isoc99_scanf@plt+0x1008>
    19e6:	e8 f5 f6 ff ff       	call   10e0 <puts@plt>
    19eb:	48 8d 3d ba 07 00 00 	lea    rdi,[rip+0x7ba]        # 21ac <__isoc99_scanf@plt+0x105c>
    19f2:	e8 e9 f6 ff ff       	call   10e0 <puts@plt>
    19f7:	48 8d 3d bf 07 00 00 	lea    rdi,[rip+0x7bf]        # 21bd <__isoc99_scanf@plt+0x106d>
    19fe:	e8 dd f6 ff ff       	call   10e0 <puts@plt>
    1a03:	48 8d 3d ce 07 00 00 	lea    rdi,[rip+0x7ce]        # 21d8 <__isoc99_scanf@plt+0x1088>
    1a0a:	e8 d1 f6 ff ff       	call   10e0 <puts@plt>
    1a0f:	48 8d 3d d3 07 00 00 	lea    rdi,[rip+0x7d3]        # 21e9 <__isoc99_scanf@plt+0x1099>
    1a16:	e8 c5 f6 ff ff       	call   10e0 <puts@plt>
    1a1b:	48 8d 3d e4 07 00 00 	lea    rdi,[rip+0x7e4]        # 2206 <__isoc99_scanf@plt+0x10b6>
    1a22:	e8 b9 f6 ff ff       	call   10e0 <puts@plt>
    1a27:	48 8d 3d e0 07 00 00 	lea    rdi,[rip+0x7e0]        # 220e <__isoc99_scanf@plt+0x10be>
    1a2e:	b8 00 00 00 00       	mov    eax,0x0
    1a33:	e8 e8 f6 ff ff       	call   1120 <printf@plt>
    1a38:	90                   	nop
    1a39:	5d                   	pop    rbp
    1a3a:	c3                   	ret    
    1a3b:	f3 0f 1e fa          	endbr64 
    1a3f:	55                   	push   rbp
    1a40:	48 89 e5             	mov    rbp,rsp
    1a43:	48 83 ec 10          	sub    rsp,0x10
    1a47:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    1a4e:	00 00 
    1a50:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    1a54:	31 c0                	xor    eax,eax
    1a56:	b8 00 00 00 00       	mov    eax,0x0
    1a5b:	e8 e9 f7 ff ff       	call   1249 <__isoc99_scanf@plt+0xf9>
    1a60:	b8 00 00 00 00       	mov    eax,0x0
    1a65:	e8 6d ff ff ff       	call   19d7 <__isoc99_scanf@plt+0x887>
    1a6a:	48 8d 45 f4          	lea    rax,[rbp-0xc]
    1a6e:	48 89 c6             	mov    rsi,rax
    1a71:	48 8d 3d aa 05 00 00 	lea    rdi,[rip+0x5aa]        # 2022 <__isoc99_scanf@plt+0xed2>
    1a78:	b8 00 00 00 00       	mov    eax,0x0
    1a7d:	e8 ce f6 ff ff       	call   1150 <__isoc99_scanf@plt>
    1a82:	8b 45 f4             	mov    eax,DWORD PTR [rbp-0xc]
    1a85:	83 f8 05             	cmp    eax,0x5
    1a88:	77 75                	ja     1aff <__isoc99_scanf@plt+0x9af>
    1a8a:	89 c0                	mov    eax,eax
    1a8c:	48 8d 14 85 00 00 00 	lea    rdx,[rax*4+0x0]
    1a93:	00 
    1a94:	48 8d 05 91 07 00 00 	lea    rax,[rip+0x791]        # 222c <__isoc99_scanf@plt+0x10dc>
    1a9b:	8b 04 02             	mov    eax,DWORD PTR [rdx+rax*1]
    1a9e:	48 98                	cdqe   
    1aa0:	48 8d 15 85 07 00 00 	lea    rdx,[rip+0x785]        # 222c <__isoc99_scanf@plt+0x10dc>
    1aa7:	48 01 d0             	add    rax,rdx
    1aaa:	3e ff e0             	notrack jmp rax
    1aad:	b8 00 00 00 00       	mov    eax,0x0
    1ab2:	e8 d9 f7 ff ff       	call   1290 <__isoc99_scanf@plt+0x140>
    1ab7:	eb 52                	jmp    1b0b <__isoc99_scanf@plt+0x9bb>
    1ab9:	b8 00 00 00 00       	mov    eax,0x0
    1abe:	e8 9d f9 ff ff       	call   1460 <__isoc99_scanf@plt+0x310>
    1ac3:	eb 46                	jmp    1b0b <__isoc99_scanf@plt+0x9bb>
    1ac5:	b8 00 00 00 00       	mov    eax,0x0
    1aca:	e8 69 fa ff ff       	call   1538 <__isoc99_scanf@plt+0x3e8>
    1acf:	eb 3a                	jmp    1b0b <__isoc99_scanf@plt+0x9bb>
    1ad1:	b8 00 00 00 00       	mov    eax,0x0
    1ad6:	e8 24 fe ff ff       	call   18ff <__isoc99_scanf@plt+0x7af>
    1adb:	eb 2e                	jmp    1b0b <__isoc99_scanf@plt+0x9bb>
    1add:	48 8d 3d 2e 07 00 00 	lea    rdi,[rip+0x72e]        # 2212 <__isoc99_scanf@plt+0x10c2>
    1ae4:	e8 f7 f5 ff ff       	call   10e0 <puts@plt>
    1ae9:	b8 00 00 00 00       	mov    eax,0x0
    1aee:	48 8b 4d f8          	mov    rcx,QWORD PTR [rbp-0x8]
    1af2:	64 48 33 0c 25 28 00 	xor    rcx,QWORD PTR fs:0x28
    1af9:	00 00 
    1afb:	74 18                	je     1b15 <__isoc99_scanf@plt+0x9c5>
    1afd:	eb 11                	jmp    1b10 <__isoc99_scanf@plt+0x9c0>
    1aff:	48 8d 3d 14 07 00 00 	lea    rdi,[rip+0x714]        # 221a <__isoc99_scanf@plt+0x10ca>
    1b06:	e8 d5 f5 ff ff       	call   10e0 <puts@plt>
    1b0b:	e9 50 ff ff ff       	jmp    1a60 <__isoc99_scanf@plt+0x910>
    1b10:	e8 eb f5 ff ff       	call   1100 <__stack_chk_fail@plt>
    1b15:	c9                   	leave  
    1b16:	c3                   	ret    
    1b17:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    1b1e:	00 00 
    1b20:	f3 0f 1e fa          	endbr64 
    1b24:	41 57                	push   r15
    1b26:	4c 8d 3d 4b 22 00 00 	lea    r15,[rip+0x224b]        # 3d78 <__isoc99_scanf@plt+0x2c28>
    1b2d:	41 56                	push   r14
    1b2f:	49 89 d6             	mov    r14,rdx
    1b32:	41 55                	push   r13
    1b34:	49 89 f5             	mov    r13,rsi
    1b37:	41 54                	push   r12
    1b39:	41 89 fc             	mov    r12d,edi
    1b3c:	55                   	push   rbp
    1b3d:	48 8d 2d 3c 22 00 00 	lea    rbp,[rip+0x223c]        # 3d80 <__isoc99_scanf@plt+0x2c30>
    1b44:	53                   	push   rbx
    1b45:	4c 29 fd             	sub    rbp,r15
    1b48:	48 83 ec 08          	sub    rsp,0x8
    1b4c:	e8 af f4 ff ff       	call   1000 <__cxa_finalize@plt-0xc0>
    1b51:	48 c1 fd 03          	sar    rbp,0x3
    1b55:	74 1f                	je     1b76 <__isoc99_scanf@plt+0xa26>
    1b57:	31 db                	xor    ebx,ebx
    1b59:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    1b60:	4c 89 f2             	mov    rdx,r14
    1b63:	4c 89 ee             	mov    rsi,r13
    1b66:	44 89 e7             	mov    edi,r12d
    1b69:	41 ff 14 df          	call   QWORD PTR [r15+rbx*8]
    1b6d:	48 83 c3 01          	add    rbx,0x1
    1b71:	48 39 dd             	cmp    rbp,rbx
    1b74:	75 ea                	jne    1b60 <__isoc99_scanf@plt+0xa10>
    1b76:	48 83 c4 08          	add    rsp,0x8
    1b7a:	5b                   	pop    rbx
    1b7b:	5d                   	pop    rbp
    1b7c:	41 5c                	pop    r12
    1b7e:	41 5d                	pop    r13
    1b80:	41 5e                	pop    r14
    1b82:	41 5f                	pop    r15
    1b84:	c3                   	ret    
    1b85:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    1b8c:	00 00 00 00 
    1b90:	f3 0f 1e fa          	endbr64 
    1b94:	c3                   	ret    

Disassembly of section .fini:

0000000000001b98 <.fini>:
    1b98:	f3 0f 1e fa          	endbr64 
    1b9c:	48 83 ec 08          	sub    rsp,0x8
    1ba0:	48 83 c4 08          	add    rsp,0x8
    1ba4:	c3                   	ret    
