class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        di = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in di:
                    di[subdomain] += count
                else:
                    di[subdomain] = count
        result = []
        for subdomain, count in di.items():
            result.append(str(count) + ' ' + subdomain)
        
        return result