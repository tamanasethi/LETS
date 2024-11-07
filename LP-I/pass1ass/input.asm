   START 100
   MOVER AREG, ='05'
   MOVER BREG, ='10'
up ADD AREG, BREG
   MOVEM A, ='5'
   ORIGIN up
   LTORG
   MOVEM B, ='7'
A  DS 02
B  DC '10'
   END
