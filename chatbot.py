import re
import loikhuyen as long #trich xuat duong dan vao file loikhuyen.py


def xacsuattinnhan(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Đếm số từ trong mỗi tin nhắn được xác định trước
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Tính phần trăm từ được nhận dạng trong tin nhắn của người dùng
    percentage = float(message_certainty) / float(len(recognised_words))

    # Kiểm tra xem các từ được yêu cầu có trong chuỗi không
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Phải có các từ được yêu cầu hoặc là một phản hồi duy nhấte
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def kiemtratinnhan(message):
    highest_prob_list = {}

    # Đơn giản hóa việc tạo phản hồi/thêm nó vào lệnh
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = xacsuattinnhan(message, list_of_words, single_response, required_words)

    # Phản hồi 
    response('Chào mừng quý khách đến với thế giới suit nam ABC, mình có thể giúp gì cho bạn ạ?', ['hello', 'hi', 'hey', 'xinchao', 'alo'], single_response=True)

    response('Dạ shop có rất nhiều mẫu vest không biết bạn đã chọn được mẫu nào chưa ạ? Shop có nhiều mẫu vest trẻ trung dành cho sinh viên cũng như nhiều mẫu quần mới ra phù hợp đi làm cũng như đi chơi. Bạn muốn mua mẫu nào ạ?', ['toi', 'muon', 'tu', 'van'], required_words=['tu', 'van'])
    
    response('Shop ABC chân thành cảm ơn. Tạm biệt, hẹn gặp lại!', ['tambiet', 'goodbye'], single_response=True)
    response('Dạ shop xin gửi bạn một số mẫu áo chữ V rất phù hợp với yêu cầu của bạn như: Phổ biến; thường gặp; dễ mặc; thoải mái; giá thành hợp lý; mẫu mã đa dạng.', ['ao', 'chu', 'v'], required_words=['v'])
    response('Aó da trơn trang trọng; lịch sự;vải lụa; satin bóng; trưởng thành; giá cả phải chăng; dễ mặc; mẫu mã đặc trưng', ['ao', 'da', 'tron'], required_words=['da','tron'])
    response('Dạ shop có rất nhiều mẫu quần không biết bạn đã chọn được mẫu nào chưa ạ? Shop có nhiều mẫu quần phù hợp sinh viên cũng như nhiều mẫu quần mới ra phù hợp đi làm cũng như đi chơi. Bạn muốn mua mẫunào ạ? ', ['toi', 'muon', 'mua', 'quan'], required_words=['quan'])
    
    response('quần slimfit tôn dáng; đĩnh đạc; lịch lãm; thon gọn; thon dài; ôm vừa phải; phù hợp dáng người', ['quan', 'slimfit'], required_words=['slimfit'])
    response('quần superslim năng động; trẻ trung; hơi bó sát; vải 4 chiều; thoải mái; nổi bật ', ['quan', 'superslim'], required_words=['superslim'])

    response('Dạ shop có rất nhiều setvest mẫu, không biếtbạn đã chọn được mẫunào chưa ạ? Bạn có yêucầu gì về sản phẩm khôngđể mình tư vấn cho bạn ạ.', ['toi', 'mua', 'set'], required_words=['set'])
    response('Dạ shop có nhiều loại set công sở phù hợp dành cho bạn như áo chữ V cùng quầnslim fit, set dành cho văn phòng, set dự tiệc', ['toi', 'mua', 'set', 'công','sở'], required_words=['cong',' so'])
    response('Mình muốn mua loại set dành cho đi dạ hội thì shop có set vest cho dịp tiệc tùng , vừa lịch lãm, vừa trang trọng để đi dự tiệc', ['set', 'di', 'da', 'hoi'], required_words=['da','hoi'])
    
    response('giá tiền một áo chữ V là 700 nghìn, áo da trơn là 850 nghìn, quần slimfit là 1 triệu và quần superslim là 1 triệu 2 ạ, nếu mình mua theo set thì sẽ được giảm giá 200 nghìn mỗi set ạ', ['gia', 'tien'], required_words=['gia','tien'])
    response('Dạ shop chúng em hiên có chương trình đại hạ giá 30% mừng sinh nhật 3 tuổi của shop ạ. Để được tư vấn kĩ hơn, quý khách vui lòng liênhệ cho ABC nhé!Hotline: 0987654321', ['khuyen', 'mai'], required_words=['khuyen','mai'])
    response('ABC có cơ sở chính tại số 12 chùa Bộc, Đống Đa, Hà Nội ạ.', ['dia', 'chi'], required_words=['dia','chi'])
    response('Dạ, ABC đã xác nhận đơn hàng của bạn. Bạn vui lòng cho mình xin họ tên, số điện thoại, địa chỉ để bên mình giao hàng ạ. Cho mình xin một chiếc feedback sau khi nhận được sản phẩm ạ. Bạn lưu ý có thể kiểm hàng trước khi nhận và chính sáchhỗ trợ đổi size nếu sản phẩmchưa vừa với bạn', ['dat','hang'], required_words=['dat','hang'])
    

    # Tạo phản hồi dài: 
    response(long.R_ADVICE, ['toi', 'mua'], required_words=['mua'])
    response(long.R_EATING, ['hang'], required_words=['hang'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)


    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Nhận dữ liệu đầu vào
def guitinnhan(user_input):
    chianho_tinnhan = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = kiemtratinnhan(chianho_tinnhan)
    return response

while True:
    print('Bot: ' + guitinnhan(input('You: ')))
