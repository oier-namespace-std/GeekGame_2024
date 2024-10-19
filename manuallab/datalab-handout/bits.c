/* 
 * CS:APP Data Lab 
 * 
 * <Please put your name and userid here>
 * 
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.  
 */

#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES:
 
  Replace the "return" statement in each function with one
  or more lines of C code that implements the function. Your code 
  must conform to the following style:
 
  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>
    
  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.

 
  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting an integer by more
     than the word size.

EXAMPLES OF ACCEPTABLE CODING STYLE:
  /*
   * pow2plus1 - returns 2^x + 1, where 0 <= x <= 31
   */
  int pow2plus1(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     return (1 << x) + 1;
  }

  /*
   * pow2plus4 - returns 2^x + 4, where 0 <= x <= 31
   */
  int pow2plus4(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     int result = (1 << x);
     result += 4;
     return result;
  }

FLOATING POINT CODING RULES

For the problems that require you to implent floating-point operations,
the coding rules are less strict.  You are allowed to use looping and
conditional control.  You are allowed to use both ints and unsigneds.
You can use arbitrary integer and unsigned constants.

You are expressly forbidden to:
  1. Define or use any macros.
  2. Define any additional functions in this file.
  3. Call any functions.
  4. Use any form of casting.
  5. Use any data type other than int or unsigned.  This means that you
     cannot use arrays, structs, or unions.
  6. Use any floating point data types, operations, or constants.


NOTES:
  1. Use the dlc (data lab checker) compiler (described in the handout) to 
     check the legality of your solutions.
  2. Each function has a maximum number of operators (! ~ & ^ | + << >>)
     that you are allowed to use for your implementation of the function. 
     The max operator count is checked by dlc. Note that '=' is not 
     counted; you may use as many of these as you want without penalty.
  3. Use the btest test harness to check your functions for correctness.
  4. Use the BDD checker to formally verify your functions
  5. The maximum number of ops for each function is given in the
     header comment for each function. If there are any inconsistencies 
     between the maximum ops in the writeup and in this file, consider
     this file the authoritative source.

/*
 * STEP 2: Modify the following functions according the coding rules.
 * 
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce 
 *      the correct answers.
 */


#endif
/* Copyright (C) 1991-2024 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <https://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2017, fifth edition, plus
   the following additions from Amendment 1 to the fifth edition:
   - 56 emoji characters
   - 285 hentaigana
   - 3 additional Zanabazar Square characters */
/* 
 * bitAnd - x&y using only ~ and | 
 *   Example: bitAnd(6, 5) = 4
 *   Legal ops: ~ |
 *   Max ops: 8
 *   Rating: 1
 */
int bitAnd(int x, int y) {
  return ~((~x)|(~y));
}
/* 
 * bitConditional - x ? y : z for each bit respectively
 *   Example: bitConditional(0b00110011, 0b01010101, 0b00001111) = 0b00011101
 *   Legal ops: & | ^ ~
 *   Max ops: 4
 *   Rating: 1
 */
int bitConditional(int x, int y, int z) {
    /* (0,a,b) -> a, (1,a,b) -> b (3 / 4 ops) */
    int rx = y ^ z;
    int dq = rx & x;
    int ret = z ^ dq;
    return ret;
}
/* 
 * implication - return x -> y in propositional logic - 0 for false, 1
 * for true
 *   Example: implication(1,1) = 1
 *            implication(1,0) = 0
 *   Legal ops: ! ~ ^ |
 *   Max ops: 5
 *   Rating: 2
 */
int implication(int x, int y) {
  return (!x)|y;
}
/* 
 * rotateRight - Rotate x to the right by n
 *   Can assume that 0 <= n <= 31
 *   Examples: rotateRight(0x87654321,4) = 0x18765432
 *   Legal ops: ~ & ^ | + << >>
 *   Max ops: 25
 *   Rating: 3 
 */
int rotateRight(int x, int n) {
  return (x >> n) ^ ((x ^ (x >> 31)) << (31 ^ n) << 1);
}
/* 
 * bang - Compute !x without using !
 *   Examples: bang(3) = 0, bang(0) = 1
 *   Legal ops: ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 4 
 */
int bang(int x) {
  return ((x | ((~x) + 1)) >> 31) + 1;
}
/* 
 * countTrailingZero - return the number of consecutive 0 from the lowest bit of 
 *   the binary form of x.
 *   YOU MAY USE BIG CONST IN THIS PROBLEM, LIKE 0xFFFF0000
 *   YOU MAY USE BIG CONST IN THIS PROBLEM, LIKE 0xFFFF0000
 *   YOU MAY USE BIG CONST IN THIS PROBLEM, LIKE 0xFFFF0000
 *   Examples countTrailingZero(0x0) = 32, countTrailingZero(0x1) = 0,
 *            countTrailingZero(0xFFFF0000) = 16,
 *            countTrailingZero(0xFFFFFFF0) = 8,
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 40
 *   Rating: 4
 */
int countTrailingZero(int x){
    int y = x&(~x+1), cnt = 0;
    cnt = !(y&0x0000ffff)<<4;
    cnt += !(y&0x00ff00ff)<<3;
    cnt += !(y&0x0f0f0f0f)<<2;
    cnt += !(y&0x33333333)<<1;
    cnt += !(y&0x55555555);
    cnt += !y;
    return cnt;
}
/* 
 * divpwr2 - Compute x/(2^n), for 0 <= n <= 30
 *  Round toward zero
 *   Examples: divpwr2(15,1) = 7, divpwr2(-33,4) = -2
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 15
 *   Rating: 2
 */
int divpwr2(int x, int n) {
    int b = x>>31;
    b = b^(b<<n);
    return (x+b)>>n;
}
/* 
 * sameSign - return 1 if x and y have same sign, and 0 otherwise
 *   Examples sameSign(0x12345678, 0) = 1, sameSign(0xFFFFFFFF,0x1) = 0
 *   Legal ops: ! ~ & ! ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */


int sameSign(int x, int y) {
  return !((x^y)>>31);
}
/*
 * multFiveEighths - multiplies by 5/8 rounding toward 0.
 *   Should exactly duplicate effect of C expression (x*5/8),
 *   including overflow behavior.
 *   Examples: multFiveEighths(77) = 48
 *             multFiveEighths(-22) = -13
 *             multFiveEighths(1073741824) = 13421728 (overflow)
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 3
 */
int multFiveEighths(int x) {
  int multFive = (x << 2) + x;
  
  // if multFive is negative, add 2^3 - 1 = 7 before right shift
  int addNum = 7 & (multFive >> 31);
  int divEight = (multFive + addNum) >> 3;
  
  return divEight;
}
/*
 * satMul3 - multiplies by 3, saturating to Tmin or Tmax if overflow
 *  Examples: satMul3(0x10000000) = 0x30000000
 *            satMul3(0x30000000) = 0x7FFFFFFF (Saturate to TMax)
 *            satMul3(0x70000000) = 0x7FFFFFFF (Saturate to TMax)
 *            satMul3(0xD0000000) = 0x80000000 (Saturate to TMin)
 *            satMul3(0xA0000000) = 0x80000000 (Saturate to TMin)
 *  Legal ops: ! ~ & ^ | + << >>
 *  Max ops: 25
 *  Rating: 3
 */
int satMul3(int x) {
    int TMin = 1<<31;
    int y = x+x, z = y+x;
    int sx = x>>31;
    int f = ((x^y)|(x^z))>>31;  // f = y's or z's sign differs x's? 111...111: 000...000
    int M = sx^TMin; // M = TMax when x is negative, TMin otherwise
    return (f&M)^(f|z); // bless of god
}
/* 
 * isLessOrEqual - if x <= y  then return 1, else return 0 
 *   Example: isLessOrEqual(4,5) = 1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 24
 *   Rating: 3
 */
int isLessOrEqual(int x, int y) {
  int s = (x^y)>>31;
  int t = ~(s|y);
  return (x+t)>>31&1;
}
/*
 * ilog2 - return floor(log base 2 of x), where x > 0
 *   Example: ilog2(16) = 4
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 90
 *   Rating: 4
 */
int ilog2(int x) {
  int ans = (!(x >> 16)) << 4;
  ans ^= (!(x << ans >> 24)) << 3;
  ans ^= 28;
  ans ^= (!(x >> ans)) << 2;
  x = x >> ans;
  ans ^= ((~0x5B) >> (x & 30)) & 3;
  return ans;
}
/* 
 * float_twice - Return bit-level equivalent of expression 2*f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representation of
 *   single-precision floating point values.
 *   When argument is NaN, return argument
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 1
 *   Rating: 4
 */

unsigned float_twice(unsigned uf) {
  const unsigned m_sexp = 0xff800000;  // (1<<30)-(1<<23)
  unsigned sexp = m_sexp & uf;

  switch (sexp){
    case 0x7f800000:
    case 0xff800000:  return uf;
    case 0x00000000:           
    case 0x80000000:  return sexp|(uf<<1);
    case 0x7f000000:  return 0x7f800000;
    case 0xff000000:  return 0xff800000;
    default:          return uf+0x800000;
  }
}
/* 
 * float_i2f - Return bit-level equivalent of expression (float) x
 *   Result is returned as unsigned int, but
 *   it is to be interpreted as the bit-level representation of a
 *   single-precision floating point values.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 4
 *   Rating: 4
 */
unsigned float_i2f(int x) {

      // Get the sign bit
      int sign = x & 0x80000000;
      //printf("sign = %d\n", sign);
      
      // Store the highest bit with 1 in x
      int frac = 0, exp = 0;

    // For bits needed to be discarded
      int leftover = 0;
    int leftoverCnt = 0;

      int fracMask = 0;
      
    // For operations in the middle shift
    int mid = 0;
      int shift = 0;
      int inter = 0;
        
      // Determine whether it's 0
      if(!x)
          return 0;
    
      //Determine if it's tmin
      if(x == 0x80000000) {
          return 0xcf000000;
      }    

      // Determine whether x is positive or negative
      if(sign == 0x80000000) {
          // x is negative - set it to be positive
          x = -x;
      }

      // Get highest bit of one
       while( (x >> exp) != 1){
          exp += 1;
      }
 
    // Whether all the bits can be stored
      if (exp > 23){
          leftoverCnt = exp - 23;
          shift = 1 << leftoverCnt;
          leftover = shift - 1 & x;

          frac = (x >> leftoverCnt) & 0x7fffff;
    
          mid = shift>>1;
    
          if(leftover > mid ) {
          inter = 1;
          } else if (leftover == mid) {
               inter = frac & 1;
          }
          frac = frac + inter;
      } else{
          frac = ((1 << exp) ^ x) << (23 - exp);
      } 

      if(frac == 0x800000) {
          exp = exp + 1;
          frac = 0;
      }

      exp = exp + 127;
      exp = exp << 23;
    
      return sign + exp + frac;
}
/* 
 * float64_f2i - Return bit-level equivalent of expression (int) f
 *   for 64 bit floating point argument f.
 *   Argument is passed as two unsigned int, but
 *   it is to be interpreted as the bit-level representation of a
 *   double-precision floating point value.
 *   Notice: uf1 contains the lower part of the f64 f
 *   Anything out of range (including NaN and infinity) should return
 *   0x80000000u.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 4
 *   Rating: 4
 */
int float64_f2i(unsigned uf1, unsigned uf2) {
  unsigned sign = (uf2 >> 31);
    int exp_mask = 0x7ff;
    int exp = ((uf2 >> 20) & exp_mask) - 1023;
    unsigned frac = ((uf2 & 0xfffff) << 11) | (((uf1 >> 21) & exp_mask)) | (0x80000000); // uf2的低20位+uf1的高11位
    if (exp < 0)
        return 0;
    if (exp >= 31)
        return 0x80000000;
    frac = (frac >> (31 - exp)) & ~(0x80000000 >> (31 - exp) << 1); // 避免算数右移导致的前导 1
    if (sign)
        return -frac;
    return frac;
}
/* 
 * float_negpwr2 - Return bit-level equivalent of the expression 2.0^-x
 *   (2.0 raised to the power -x) for any 32-bit integer x.
 *
 *   The unsigned value that is returned should have the identical bit
 *   representation as the single-precision floating-point number 2.0^-x.
 *   If the result is too small to be represented as a denorm, return
 *   0. If too large, return +INF.
 * 
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. Also if, while 
 *   Max ops: 1 
 *   Rating: 4
 */
unsigned float_negpwr2(int x) {
    // int e = x+127;
     if (x >= 0x00000096) return 0;

    switch (x){
case 0xffffff81: return 0x7f000000;
case 0xffffff82: return 0x7e800000;
case 0xffffff83: return 0x7e000000;
case 0xffffff84: return 0x7d800000;
case 0xffffff85: return 0x7d000000;
case 0xffffff86: return 0x7c800000;
case 0xffffff87: return 0x7c000000;
case 0xffffff88: return 0x7b800000;
case 0xffffff89: return 0x7b000000;
case 0xffffff8a: return 0x7a800000;
case 0xffffff8b: return 0x7a000000;
case 0xffffff8c: return 0x79800000;
case 0xffffff8d: return 0x79000000;
case 0xffffff8e: return 0x78800000;
case 0xffffff8f: return 0x78000000;
case 0xffffff90: return 0x77800000;
case 0xffffff91: return 0x77000000;
case 0xffffff92: return 0x76800000;
case 0xffffff93: return 0x76000000;
case 0xffffff94: return 0x75800000;
case 0xffffff95: return 0x75000000;
case 0xffffff96: return 0x74800000;
case 0xffffff97: return 0x74000000;
case 0xffffff98: return 0x73800000;
case 0xffffff99: return 0x73000000;
case 0xffffff9a: return 0x72800000;
case 0xffffff9b: return 0x72000000;
case 0xffffff9c: return 0x71800000;
case 0xffffff9d: return 0x71000000;
case 0xffffff9e: return 0x70800000;
case 0xffffff9f: return 0x70000000;
case 0xffffffa0: return 0x6f800000;
case 0xffffffa1: return 0x6f000000;
case 0xffffffa2: return 0x6e800000;
case 0xffffffa3: return 0x6e000000;
case 0xffffffa4: return 0x6d800000;
case 0xffffffa5: return 0x6d000000;
case 0xffffffa6: return 0x6c800000;
case 0xffffffa7: return 0x6c000000;
case 0xffffffa8: return 0x6b800000;
case 0xffffffa9: return 0x6b000000;
case 0xffffffaa: return 0x6a800000;
case 0xffffffab: return 0x6a000000;
case 0xffffffac: return 0x69800000;
case 0xffffffad: return 0x69000000;
case 0xffffffae: return 0x68800000;
case 0xffffffaf: return 0x68000000;
case 0xffffffb0: return 0x67800000;
case 0xffffffb1: return 0x67000000;
case 0xffffffb2: return 0x66800000;
case 0xffffffb3: return 0x66000000;
case 0xffffffb4: return 0x65800000;
case 0xffffffb5: return 0x65000000;
case 0xffffffb6: return 0x64800000;
case 0xffffffb7: return 0x64000000;
case 0xffffffb8: return 0x63800000;
case 0xffffffb9: return 0x63000000;
case 0xffffffba: return 0x62800000;
case 0xffffffbb: return 0x62000000;
case 0xffffffbc: return 0x61800000;
case 0xffffffbd: return 0x61000000;
case 0xffffffbe: return 0x60800000;
case 0xffffffbf: return 0x60000000;
case 0xffffffc0: return 0x5f800000;
case 0xffffffc1: return 0x5f000000;
case 0xffffffc2: return 0x5e800000;
case 0xffffffc3: return 0x5e000000;
case 0xffffffc4: return 0x5d800000;
case 0xffffffc5: return 0x5d000000;
case 0xffffffc6: return 0x5c800000;
case 0xffffffc7: return 0x5c000000;
case 0xffffffc8: return 0x5b800000;
case 0xffffffc9: return 0x5b000000;
case 0xffffffca: return 0x5a800000;
case 0xffffffcb: return 0x5a000000;
case 0xffffffcc: return 0x59800000;
case 0xffffffcd: return 0x59000000;
case 0xffffffce: return 0x58800000;
case 0xffffffcf: return 0x58000000;
case 0xffffffd0: return 0x57800000;
case 0xffffffd1: return 0x57000000;
case 0xffffffd2: return 0x56800000;
case 0xffffffd3: return 0x56000000;
case 0xffffffd4: return 0x55800000;
case 0xffffffd5: return 0x55000000;
case 0xffffffd6: return 0x54800000;
case 0xffffffd7: return 0x54000000;
case 0xffffffd8: return 0x53800000;
case 0xffffffd9: return 0x53000000;
case 0xffffffda: return 0x52800000;
case 0xffffffdb: return 0x52000000;
case 0xffffffdc: return 0x51800000;
case 0xffffffdd: return 0x51000000;
case 0xffffffde: return 0x50800000;
case 0xffffffdf: return 0x50000000;
case 0xffffffe0: return 0x4f800000;
case 0xffffffe1: return 0x4f000000;
case 0xffffffe2: return 0x4e800000;
case 0xffffffe3: return 0x4e000000;
case 0xffffffe4: return 0x4d800000;
case 0xffffffe5: return 0x4d000000;
case 0xffffffe6: return 0x4c800000;
case 0xffffffe7: return 0x4c000000;
case 0xffffffe8: return 0x4b800000;
case 0xffffffe9: return 0x4b000000;
case 0xffffffea: return 0x4a800000;
case 0xffffffeb: return 0x4a000000;
case 0xffffffec: return 0x49800000;
case 0xffffffed: return 0x49000000;
case 0xffffffee: return 0x48800000;
case 0xffffffef: return 0x48000000;
case 0xfffffff0: return 0x47800000;
case 0xfffffff1: return 0x47000000;
case 0xfffffff2: return 0x46800000;
case 0xfffffff3: return 0x46000000;
case 0xfffffff4: return 0x45800000;
case 0xfffffff5: return 0x45000000;
case 0xfffffff6: return 0x44800000;
case 0xfffffff7: return 0x44000000;
case 0xfffffff8: return 0x43800000;
case 0xfffffff9: return 0x43000000;
case 0xfffffffa: return 0x42800000;
case 0xfffffffb: return 0x42000000;
case 0xfffffffc: return 0x41800000;
case 0xfffffffd: return 0x41000000;
case 0xfffffffe: return 0x40800000;
case 0xffffffff: return 0x40000000;
case 0x00000000: return 0x3f800000;
case 0x00000001: return 0x3f000000;
case 0x00000002: return 0x3e800000;
case 0x00000003: return 0x3e000000;
case 0x00000004: return 0x3d800000;
case 0x00000005: return 0x3d000000;
case 0x00000006: return 0x3c800000;
case 0x00000007: return 0x3c000000;
case 0x00000008: return 0x3b800000;
case 0x00000009: return 0x3b000000;
case 0x0000000a: return 0x3a800000;
case 0x0000000b: return 0x3a000000;
case 0x0000000c: return 0x39800000;
case 0x0000000d: return 0x39000000;
case 0x0000000e: return 0x38800000;
case 0x0000000f: return 0x38000000;
case 0x00000010: return 0x37800000;
case 0x00000011: return 0x37000000;
case 0x00000012: return 0x36800000;
case 0x00000013: return 0x36000000;
case 0x00000014: return 0x35800000;
case 0x00000015: return 0x35000000;
case 0x00000016: return 0x34800000;
case 0x00000017: return 0x34000000;
case 0x00000018: return 0x33800000;
case 0x00000019: return 0x33000000;
case 0x0000001a: return 0x32800000;
case 0x0000001b: return 0x32000000;
case 0x0000001c: return 0x31800000;
case 0x0000001d: return 0x31000000;
case 0x0000001e: return 0x30800000;
case 0x0000001f: return 0x30000000;
case 0x00000020: return 0x2f800000;
case 0x00000021: return 0x2f000000;
case 0x00000022: return 0x2e800000;
case 0x00000023: return 0x2e000000;
case 0x00000024: return 0x2d800000;
case 0x00000025: return 0x2d000000;
case 0x00000026: return 0x2c800000;
case 0x00000027: return 0x2c000000;
case 0x00000028: return 0x2b800000;
case 0x00000029: return 0x2b000000;
case 0x0000002a: return 0x2a800000;
case 0x0000002b: return 0x2a000000;
case 0x0000002c: return 0x29800000;
case 0x0000002d: return 0x29000000;
case 0x0000002e: return 0x28800000;
case 0x0000002f: return 0x28000000;
case 0x00000030: return 0x27800000;
case 0x00000031: return 0x27000000;
case 0x00000032: return 0x26800000;
case 0x00000033: return 0x26000000;
case 0x00000034: return 0x25800000;
case 0x00000035: return 0x25000000;
case 0x00000036: return 0x24800000;
case 0x00000037: return 0x24000000;
case 0x00000038: return 0x23800000;
case 0x00000039: return 0x23000000;
case 0x0000003a: return 0x22800000;
case 0x0000003b: return 0x22000000;
case 0x0000003c: return 0x21800000;
case 0x0000003d: return 0x21000000;
case 0x0000003e: return 0x20800000;
case 0x0000003f: return 0x20000000;
case 0x00000040: return 0x1f800000;
case 0x00000041: return 0x1f000000;
case 0x00000042: return 0x1e800000;
case 0x00000043: return 0x1e000000;
case 0x00000044: return 0x1d800000;
case 0x00000045: return 0x1d000000;
case 0x00000046: return 0x1c800000;
case 0x00000047: return 0x1c000000;
case 0x00000048: return 0x1b800000;
case 0x00000049: return 0x1b000000;
case 0x0000004a: return 0x1a800000;
case 0x0000004b: return 0x1a000000;
case 0x0000004c: return 0x19800000;
case 0x0000004d: return 0x19000000;
case 0x0000004e: return 0x18800000;
case 0x0000004f: return 0x18000000;
case 0x00000050: return 0x17800000;
case 0x00000051: return 0x17000000;
case 0x00000052: return 0x16800000;
case 0x00000053: return 0x16000000;
case 0x00000054: return 0x15800000;
case 0x00000055: return 0x15000000;
case 0x00000056: return 0x14800000;
case 0x00000057: return 0x14000000;
case 0x00000058: return 0x13800000;
case 0x00000059: return 0x13000000;
case 0x0000005a: return 0x12800000;
case 0x0000005b: return 0x12000000;
case 0x0000005c: return 0x11800000;
case 0x0000005d: return 0x11000000;
case 0x0000005e: return 0x10800000;
case 0x0000005f: return 0x10000000;
case 0x00000060: return 0x0f800000;
case 0x00000061: return 0x0f000000;
case 0x00000062: return 0x0e800000;
case 0x00000063: return 0x0e000000;
case 0x00000064: return 0x0d800000;
case 0x00000065: return 0x0d000000;
case 0x00000066: return 0x0c800000;
case 0x00000067: return 0x0c000000;
case 0x00000068: return 0x0b800000;
case 0x00000069: return 0x0b000000;
case 0x0000006a: return 0x0a800000;
case 0x0000006b: return 0x0a000000;
case 0x0000006c: return 0x09800000;
case 0x0000006d: return 0x09000000;
case 0x0000006e: return 0x08800000;
case 0x0000006f: return 0x08000000;
case 0x00000070: return 0x07800000;
case 0x00000071: return 0x07000000;
case 0x00000072: return 0x06800000;
case 0x00000073: return 0x06000000;
case 0x00000074: return 0x05800000;
case 0x00000075: return 0x05000000;
case 0x00000076: return 0x04800000;
case 0x00000077: return 0x04000000;
case 0x00000078: return 0x03800000;
case 0x00000079: return 0x03000000;
case 0x0000007a: return 0x02800000;
case 0x0000007b: return 0x02000000;
case 0x0000007c: return 0x01800000;
case 0x0000007d: return 0x01000000;
case 0x0000007e: return 0x00800000;
case 0x0000007f: return 0x00400000;
case 0x00000080: return 0x00200000;
case 0x00000081: return 0x00100000;
case 0x00000082: return 0x00080000;
case 0x00000083: return 0x00040000;
case 0x00000084: return 0x00020000;
case 0x00000085: return 0x00010000;
case 0x00000086: return 0x00008000;
case 0x00000087: return 0x00004000;
case 0x00000088: return 0x00002000;
case 0x00000089: return 0x00001000;
case 0x0000008a: return 0x00000800;
case 0x0000008b: return 0x00000400;
case 0x0000008c: return 0x00000200;
case 0x0000008d: return 0x00000100;
case 0x0000008e: return 0x00000080;
case 0x0000008f: return 0x00000040;
case 0x00000090: return 0x00000020;
case 0x00000091: return 0x00000010;
case 0x00000092: return 0x00000008;
case 0x00000093: return 0x00000004;
case 0x00000094: return 0x00000002;
case 0x00000095: return 0x00000001;
case 0x00000096: return 0x00000000;
      default: return 0x7f800000;
    }
}
