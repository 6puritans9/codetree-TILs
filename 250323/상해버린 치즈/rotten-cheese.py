def find_rotten_cheese(m:int, s:int, eat_log:list[tuple[int]], ill_log:list[tuple[int]]) -> list[int]:
    # TC = O(D*S)
    # SC = O(M)
    global MAX_CHEESE

    result = []
    cheese_list = [0 for _ in range(MAX_CHEESE+1)]

    for ill_person, ill_time in ill_log:
        for eat_person, cheese, eat_time in eat_log:
            if ill_person == eat_person and eat_time < ill_time:
                cheese_list[cheese] += 1
    
    for number, count in enumerate(cheese_list):
        if count == s:
            result.append(number)

    return result


def find_medicine_counts(eat_log:list[tuple[int]], rotten_cheese:list[int]) -> int:
    # TC = O(D*M)
    # SC = O(N)
    
    candidates = set()

    for eat_person, cheese, eat_time in eat_log:
        for rotten in rotten_cheese:
            if cheese == rotten:
                candidates.add(eat_person)


    return len(candidates)


if __name__ == "__main__":
    # N people eat M cheese.
    # Among M cheese, a specific one is rotten.
    # The history of which person eats which cheese is given for D times.
    # Records of being ill is given for next S times.
    # Since the records do not cover all the history of illness yet,
    # find the maximum number of medicine that might be needed.
    # A person who eats rotten cheese become ill after 1 second.

    # Constraints
    # 1 <= N, M <= 50
    # 1 <= D <= 1000
    # 1 <= S <= N
    # 1 <= p <= N
    # 1 <= m <= M
    # 1 <= t <= 100
    
    # Approach
    # 1. Find all the possible rotten cheese
    #   sort eat_log by x[0], x[2], x[1] (person, time, cheese)
    # 2. for illness in ill_log:
    #   find the cheese which matches person, time < illness_time
    # 3. Find people who ate the possible rotten cheese
    #   use set()
    # 4. Return the number of people

    # TC = O(dlogd) sort

    MAX_CHEESE = 50

    n, m, d, s = map(int, input().split())
    eat_log = []
    ill_log = []
    for _ in range(d):
        p, m, t = map(int, input().split())
        eat_log.append((p, m, t)) # person, cheese, time
    for _ in range(s):
        p, t = map(int, input().split())
        ill_log.append((p, t)) # person, time

    eat_log.sort(key=lambda x:(x[0], x[2], x[1]))
    rotten_cheese = find_rotten_cheese(m, s, eat_log, ill_log)
    print(find_medicine_counts(eat_log, rotten_cheese))