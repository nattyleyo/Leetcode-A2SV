class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # m=len(bookings)
        pref = [0]*(n+1)
        for i in range(len(bookings)):
            # left = bookings[i][0]
            # right = bookings[i][1]
            # k = bookings[i][2]
            pref[bookings[i][0]-1]+=bookings[i][2]
            pref[bookings[i][1]]-=bookings[i][2]
        # print(pref)
        for i in range(1,n+1):
            pref[i]=pref[i-1] + pref[i]
        return pref[:n]

#1  2   3   4   5
#0  0   0   0   0 
#[10, 45, -10, -20, 0, -25]
#[10  55   45   25  25  0