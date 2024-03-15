import random

R_EATING = "Chúc bạn có một ngày tốt lành"
R_ADVICE = "hãy mua hàng shop nhé"


def unknown():
    response = ["Bạn vui lòng nhập điều muốn biết?",
                "...",
                "Tôi đồng tình với quan điểm của bạn.",
                "Điều bạn nói có ý nghĩa gì?"][
        random.randrange(4)]
    return response
