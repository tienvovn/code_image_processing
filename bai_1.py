#vẽ đường bao không có thuật toán canndy (dò bằng ngưỡng)

# import cv2
# import numpy as np
#
# # Đọc hình ảnh
# image = cv2.imread('hinh_buoi_1.2_ngay_1_3_2023.jpg')
#
# # Chuyển đổi sang ảnh xám
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Áp dụng ngưỡng
# _, threshold_image = cv2.threshold(gray_image, 249,255, 0)
#
# # Tìm contours
# contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # Vẽ contours lên hình ảnh gốc
# cv2.drawContours(image, contours, -1, (255, 0, 0), 2)
#
# # Hiển thị hình ảnh
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# #vẽ đường viền có thuật toán candy ()
# import cv2
#
# # Đọc ảnh
# image = cv2.imread("hinh_buoi_1.3_ngay_1_3_2023.jpg")
#
# # Chuyển đổi ảnh sang ảnh xám
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Áp dụng bộ lọc Canny
# edges = cv2.Canny(gray, 100, 500)
#
# # Tìm các đường viền
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Vẽ đường viền bao quanh các đối tượng
# for contour in contours:
#     cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
#
# # In ra số lượng đối tượng
# print("Số lượng đối tượng:", len(contours)) #hàm tính độ dài (số lượng phần tử) của danh sách contours.
#                                             # Trong trường hợp này, contours là danh sách các contours mà chúng
#                                             # ta đã tìm thấy trước đó
# # Hiển thị ảnh
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# đếm đối tượng có trong ảnh
# import cv2
#
# # Đọc ảnh
# image = cv2.imread("hinh_buoi_1.3_ngay_1_3_2023.jpg")
#
# # Chuyển đổi ảnh sang ảnh xám
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Áp dụng bộ lọc Canny
# edges = cv2.Canny(gray, 100, 500)
#
# # Tìm các đường viền
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Vẽ đường viền bao quanh các đối tượng
# for contour in contours:
#     cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
#
# # In ra số lượng đối tượng
# print("Số lượng đối tượng:", len(contours)) #hàm tính độ dài (số lượng phần tử) của danh sách contours.
#                                             # Trong trường hợp này, contours là danh sách các contours mà chúng
#                                             # ta đã tìm thấy trước đó
# # Hiển thị ảnh
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#############################################################################################################################################
# import numpy as np
# import cv2
#
# # Đọc ảnh từ tệp 'image3.jpg'
# img = cv2.imread('hinh_buoi_1_ngay_1_3_2023.jpg')
#
# # Chuyển ảnh sang ảnh grayscale
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Phân ngưỡng ảnh để tạo mask nhị phân
# _, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
#
# # Tìm các đường viền trong mask
# contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
# # Hiển thị ảnh gốc
# cv2.imshow("img", img)
#
# # Duyệt qua từng contour tìm được
# for contour in contours:
#     # Xấp xỉ đa giác từ contour
#     approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
#
#     # Vẽ đa giác xấp xỉ lên ảnh gốc
#     cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
#
#     # Xác định vị trí chú thích văn bản
#     x = approx.ravel()[0]
#     y = approx.ravel()[1] - 5
#
#     # Xác định hình dạng và thêm chú thích vào ảnh
#     if len(approx) == 3:
#         cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.01, (0, 0, 0))
#     elif len(approx) == 4:
#         x1, y1, w, h = cv2.boundingRect(approx)
#         aspectRatio = float(w) / h
#         if aspectRatio >= 0.95 and aspectRatio <= 1.05:
#             cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#         else:
#             cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 5:
#         cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 10:
#         cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.01, (0, 0, 0))
#     else:
#         cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#
# # Hiển thị ảnh với các đường viền và chú thích
# cv2.imshow("shapes", img)
#
# # Chờ và kiểm tra phím nhấn từ bàn phím
# cv2.waitKey(0)
#
# # Đóng tất cả cửa sổ khi kết thúc
# cv2.destroyAllWindows()


############################################################################################################################
# import cv2
# import numpy as np
#
# # Đọc hình ảnh và chuyển đổi sang ảnh xám
# img = cv2.imread('hinh_buoi_1_ngay_1_3_2023.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Áp dụng GaussianBlur để làm mờ hình ảnh và loại bỏ nhiễu
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
# # Phát hiện cạnh trong hình ảnh sử dụng phương pháp Canny
# edges = cv2.Canny(blurred, 50, 150)
#
# # Tìm contours trong hình ảnh
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Tìm hình trái tim trong contours
# heart_contour = None
# for contour in contours:
#     area = cv2.contourArea(contour)
#     perimeter = cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
#     if len(approx) > 6 and area > 5000:  # Điều kiện để xác định hình trái tim
#         heart_contour = approx
#         break
#
# # Vẽ hình trái tim trên hình ảnh gốc
# if heart_contour is not None:
#     cv2.drawContours(img, [heart_contour], -1, (0, 255, 0), 2)
#     cv2.putText(img, 'Heart', (heart_contour[0][0][0], heart_contour[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
# # Hiển thị hình ảnh
# cv2.imshow('Detected Heart', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


############################################################################################################################
# import cv2
# import numpy as np
#
# # Đọc hình ảnh và chuyển đổi sang ảnh xám
# img = cv2.imread('hinh_buoi_1_ngay_1_3_2023.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Áp dụng GaussianBlur để làm mờ hình ảnh và loại bỏ nhiễu
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
# # Phát hiện cạnh trong hình ảnh sử dụng phương pháp Canny
# edges = cv2.Canny(blurred, 50, 150)
#
# # Tìm contours trong hình ảnh
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Tìm hình trái tim trong contours
# heart_contour = None
# for contour in contours:
#     area = cv2.contourArea(contour)
#     perimeter = cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
#     if len(approx) == 11 and area > 5000 and perimeter > 1000:  # Điều kiện để xác định hình sấm sét
#         lightning_contour = approx
#         break
#
# # Vẽ hình trái tim trên hình ảnh gốc
# if heart_contour is not None:
#     cv2.drawContours(img, [heart_contour], -1, (0, 255, 0), 2)
#     cv2.putText(img, 'Heart', (heart_contour[0][0][0], heart_contour[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
# # Hiển thị hình ảnh
# cv2.imshow('Detected Heart', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import numpy as np
import cv2

img = cv2.imread("hinh_buoi_1_ngay_1_3_2023.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img1 = img.copy()

ret, thrash = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    M = cv2.moments(contour)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText(img, "Tam giác", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(img, "Hinh vuong", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Tam giac", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Ngu giac", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 7:
        cv2.putText(img, "mui ten", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) < 10:
        cv2.putText(img, "Set", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 12:
        cv2.putText(img, "Tron", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) > 11:
        cv2.putText(img, "Tim", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) > 10:
        cv2.putText(img, "Sao", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    # Xác định màu sắc
    pixel_center = hsv_frame[cY, cX]
    hue_value = pixel_center[0]

    color = "Không xác định"
    if hue_value < 10:
        color = "Red"
    elif hue_value < 22:
        color = "Orange"
    elif hue_value < 33:
        color = "Yellow"
    elif hue_value < 80:
        color = "Green"
    elif hue_value < 100:
        color = "Blue"
    elif hue_value < 150:
        color = "Lam"
    elif hue_value < 170:
        color = "Purple"
    elif hue_value < 200:
        color = "Pink"
    else:
        color = "Red"

    pixel_center_bgr = img[cY, cX]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(img, color, (cX + 10, cY + 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    cv2.circle(img, (cX, cY), 3, (255, 255, 255), -1)

cv2.imshow('Hình ảnh', img)
cv2.waitKey(0)
cv2.destroyAllWindows()