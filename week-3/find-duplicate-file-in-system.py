class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        n=len(paths)
        di={}
        dpath=''
        fname=''
        content=''
        res=[]
        for i in range(n):
            parts=paths[i].split()
            dpath=parts[0]
            for part in parts[1:]:
                open_par=part.index('(')
                fname = part[:open_par]
                content = part[open_par+1:-1]
                di[dpath+'/'+fname]=content
        print(di)
        g_dict=defaultdict(list)
        for key,val in di.items():
            g_dict[val].append(key)
        print(g_dict)
        g_dict=dict(g_dict)
        g_dict = dict(sorted(g_dict.items(), key=lambda x: len(x[1]), reverse=True))
        for key,val in g_dict.items():
                res.append(val)
        return [v for v in g_dict.values() if len(v) > 1]
        
        

            







        