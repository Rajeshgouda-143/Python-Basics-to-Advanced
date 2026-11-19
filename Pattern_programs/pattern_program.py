# Pattern Programs
'''
(0,0) (0,1) (0,2) (0,3) (0,4) 
(1,0) (1,1) (1,2) (1,3) (1,4) 
(2,0) (2,1) (2,2) (2,3) (2,4) 
(3,0) (3,1) (3,2) (3,3) (3,4) 
(4,0) (4,1) (4,2) (4,3) (4,4)     '''

# for i in range(5):
#     for j in range(5):
#         print((i,j),end=" ")
#     print()


'''Q1. WAP TO PRINT 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         print("*",end=" ")
#     print()


'''Q2. WAP TO PRINT
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i == 0 or j == 0 or i == 4 or j == 4:   
#         if i == 0 or j == 0 or i == no-1 or j == no-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q3. WAP TO PRINT
    *     
    *     
* * * * * 
    *     
    *     
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i == 2 or j == 2:
#         if i == no//2 or j == no//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q4. WAP TO PRINT
*         
  *       
    *     
      *   
        * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i - j == 0:
#         if i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q5. WAP TO PRINT
        * 
      *   
    *     
  *       
*   
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i + j == 4:
#         if i + j == no-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q6. WAP TO PRINT
*         
* *       
*   *     
*     *   
* * * * *
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if j == 0 or i == 4 or i - j == 0:
#         if j == 0 or i == no-1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q7. WAP TO PRINT 
        * 
      * * 
    *   * 
  *     * 
* * * * * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if j==4 or i==4 or i+j==4:
#         if j==no-1 or i==no-1 or i+j == no-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q8. WAP TO PRINT 
* * * * * 
*     *   
*   *     
* *       
*  
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i == 0 or j==0 or i+j==4:
#         if i == 0 or j==0 or i+j==no-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q9. WAP TO PRINT
* * * * * 
  *     * 
    *   * 
      * * 
        * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i==0 or j==4 or i==j:
#         if i==0 or j==no-1 or i-j == 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q10. WAP TO PRINT 
*         
* *       
* * *     
* * * *   
* * * * * 
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         # if i>=j:
#         if i==j or i-j == 1 or i-j == 2 or i-j == 3 or i-j == 4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q11. WAP TO PRINT
        * 
      * * 
    * * * 
  * * * * 
* * * * *  
'''
# no = 5
# for i in range(no):
#     for j in range(no):
#         if i+j >= no - 1:
#         # if i+j == 4 or i+j==no or i+j == no+1 or i+j == no+2 or i+j == no+3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


'''Q12. WAP TO PRINT'''
no = 5
for i in range(no):
    for j in range(no):
        if 






