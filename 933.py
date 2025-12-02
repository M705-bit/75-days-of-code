class RecentCounter:

    def __init__(self):
        self.queue = [] 
    
    def ping(self, t: int) -> int:
        self.queue.append(t)
        #vai testando e tirando da fila até chegar em 
        for i in range(len(self.queue)-1, -1, -1):
            if self.queue[i] - t < -3000:
               self.queue = self.queue[i+1:]
               break
            
            #tira da fila
                 
        return len(self.queue)

