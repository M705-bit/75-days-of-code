def solution(A):
    N = len(A)
    max_sum_ending_at = [0] * N
    max_sum_starting_from = [0] * N

    # Forward Kadane
    for i in range(1, N - 1):
        max_sum_ending_at[i] = max(0, max_sum_ending_at[i - 1] + A[i])

    # Reverse Kadane
    for i in range(N - 2, 0, -1):
        max_sum_starting_from[i] = max(0, max_sum_starting_from[i + 1] + A[i])

    # Combine results
    max_double_slice = 0
    for Y in range(1, N - 1):
        max_double_slice = max(
            max_double_slice,
            max_sum_ending_at[Y - 1] + max_sum_starting_from[Y + 1]
        )

    return max_double_slice
