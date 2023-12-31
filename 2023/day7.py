class Solution:
    def hand_type(self, h) -> int:
        d = {}
        jc = 0
        for c in h:
            if not c in d:
                d[c] = 0
            if c == "J":
                jc += 1
            d[c]+=1

        mv = max(d.values())
        tk = [k for k, va in d.items() if va == mv]

        v = list(d.values())
        v.sort()
        v = v[::-1]
        vn = v[0]
        if "J" in tk and jc != 5:
            vn = jc + v[1]
        else:
            vn += jc

        if vn >= 5:
            return 7
        elif vn == 4:
            return 6
        elif vn == 3 and v[1] == 2:
            return 5
        elif vn == 3:
            return 4
        elif vn == 2 and v[1] == 2:
            return 3
        elif vn == 2:
            return 2
        else:
            return 1

    def compare(self, h1, h2, cd) -> int:
        t1 = self.hand_type(h1)
        t2 = self.hand_type(h2)
        if t1 > t2:
            return 0
        elif t2 > t1:
            return 1
        else:
            for i in range(5):
                v1 = h1[i]
                v2 = h2[i]
                if not v1.isnumeric():
                    v1 = cd[v1]
                if not v2.isnumeric():
                    v2 = cd[v2]
                if int(v1) > int(v2):
                    return 0
                if int(v2) > int(v1):
                    return 1

    def solve(self) -> int:
        file = open('input.txt', 'r')
        read = file.readlines()
        t = 0
        arr = []
        cd = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
        for l in read:
            h, b = l.replace("\n", "").split(" ")
            arr.append((h, b))

        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if self.compare(arr[j][0], arr[j + 1][0], cd) == 0:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        for k in range(len(arr)):
            t+= (k+1)*int(arr[k][1])
        return t

s = Solution()
print(s.solve())