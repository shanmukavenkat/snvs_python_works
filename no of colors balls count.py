def get_color_dict(ball_score_list):
    color_score_dict = {}
    for item in ball_score_list:
        pair = item.split(":")
        color,score = pair[0],int(pair[1])
        if color in color_score_dict:
            color_score_dict[color] = color_score_dict[color]+score
        else:
            color_score_dict[color] = score
    return color_score_dict

ball_score_list = input().split(",")
color_dict = get_color_dict(ball_score_list)
print(color_dict)