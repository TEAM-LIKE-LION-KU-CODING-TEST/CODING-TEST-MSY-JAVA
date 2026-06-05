def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    song_sum_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict.keys():
            genre_dict[genres[i]] = []
            song_sum_dict[genres[i]] = 0
        genre_dict[genres[i]].append([plays[i], i])
        song_sum_dict[genres[i]] += plays[i]
    song_sum_list = list(song_sum_dict.items())
    song_sum_list = sorted(song_sum_list, key=lambda x : -x[1])
    for song_sum in song_sum_list:
        cnt = 0
        genre_list = genre_dict[song_sum[0]]
        genre_list = sorted(genre_list, key=lambda x : -x[0])
        for g in genre_list:
            if cnt == 2:
                break
            answer.append(g[1])
            cnt += 1    
    return answer