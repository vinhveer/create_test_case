import random
import os

def lcis(arr1, arr2):
    n, m = len(arr1), len(arr2)
    # dp[i] lưu độ dài LCIS kết thúc tại arr2[i]
    dp = [0] * m
    # prev[i] lưu chỉ số của phần tử trước trong LCIS kết thúc tại arr2[i]
    prev = [-1] * m
    # parent[i] lưu chỉ số của phần tử trong arr1 được chọn cho LCIS tại arr2[i]
    parent = [-1] * m
    
    for i in range(n):
        current = 0  # Độ dài LCIS hiện tại
        last = -1   # Chỉ số phần tử trước trong arr2
        for j in range(m):
            # Nếu arr1[i] == arr2[j], có thể thêm vào LCIS
            if arr1[i] == arr2[j] and dp[j] < current + 1:
                dp[j] = current + 1
                prev[j] = last
                parent[j] = i
            # Nếu arr2[j] < arr1[i], có thể cập nhật current
            if arr2[j] < arr1[i] and dp[j] > current:
                current = dp[j]
                last = j
    
    # Tìm độ dài LCIS và chỉ số kết thúc
    max_len = max(dp)
    end_idx = dp.index(max_len)
    
    # Khôi phục dãy LCIS
    result = []
    while end_idx != -1:
        result.append(arr2[end_idx])
        end_idx = prev[end_idx]
    
    return max_len, result[::-1]

def generate_test_case(test_num):
    # Tạo thư mục tests nếu chưa tồn tại
    if not os.path.exists("tests"):
        os.makedirs("tests")
    
    # Sinh độ dài mảng ngẫu nhiên
    n = random.randint(1, 100)
    m = random.randint(1, 100)
    
    # Sinh mảng ngẫu nhiên với các số từ 1 đến 1000
    arr1 = [random.randint(1, 1000) for _ in range(n)]
    arr2 = [random.randint(1, 1000) for _ in range(m)]
    
    # Ghi file .in
    with open(f"tests/{test_num}.in", "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, arr1)) + " \n")
        f.write(f"{m}\n")
        f.write(" ".join(map(str, arr2)) + " \n")
    
    # Tính LCIS và ghi file .out
    length, sequence = lcis(arr1, arr2)
    with open(f"tests/{test_num}.out", "w") as f:
        f.write(f"{length}\n")
        f.write(" ".join(map(str, sequence)) + " \n")

def main():
    # Sinh 10 test case
    for i in range(1, 11):
        generate_test_case(i)
    print("Generated 10 test cases in 'tests' directory.")

if __name__ == "__main__":
    main()