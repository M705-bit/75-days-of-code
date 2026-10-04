class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       
        def intersects(a,b, c, d):
            return a <= d and c<=b


        profit_days = []
        intervalos = []
        lista_de_intervalos = []
        lista_de_profit_days = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit_days.append((prices[i], prices[j]))
                    intervalos.append((i, j))
                lista_de_profit_days.append(profit_days)
                lista_de_intervalos.append(intervalos)
                profit_days = []
                intervalos = []
        lucro_maior= 0
       
                                                                   
        for j in range(i+1, len(lista_de_intervalos)):
                for par1 in lista_de_intervalos[i]:
                            for par2 in lista_de_intervalos[j]:
                                a, b = par1
                                c, d = par2
                                if not intersects(a, b, c, d):
                                    lucro1 = prices[b] - prices[a]
                                    lucro2 = prices[d] - prices[c]
                                    lucro_maior=max(lucro_maior, (lucro1 + lucro2))
                                    

        return lucro_maior
