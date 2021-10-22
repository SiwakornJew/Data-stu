import time
start_time = time.time()

		 # N x N Board 			# number of solutions
def printBoard(b):
    print(b)
def putQueen(r, b, colFree, upFree, downFree,N):
    global numSol
    for c in range(N): # ใล่ใส่ไปทีละ column ทุก col.
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: #ใส่ได้?
            b[r] = c    # ใส่ ที่ r, c

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

            if r == N-1:       # ถ้าใส่ควีนครบแล้ว
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree,N)  # ใส่ควีนแถวถัดไป
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                             # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution
for N in range(2,17):
    b = N*[-1]  			
    colFree = N*[1] 			
    upFree = (2*N - 1)*[1] 		
    downFree = (2*N - 1)*[1]
    numSol = 0    
    putQueen(0, b, colFree, upFree, downFree,N)   #  first add at 1st  (ie. row 0)
    print('number of solutions = ', numSol)
    print(" Bord %s x %s --- %s milliseconds ---" % (N,N,(time.time() - start_time)*1000))
    start_time = time.time()