def right_Rotate_Deq_ByK(deq, K):
    K = K % len(deq)  # Ensure K is within the range of deque length
    deq[:] = deq[-K:] + deq[:-K]

def left_Rotate_Deq_ByK(deq, K):
    K = K % len(deq)  # Ensure K is within the range of deque length
    deq[:] = deq[K:] + deq[:K]

# Example usage
if __name__ == "__main__":
    # Initialize a deque with some elements using a list
    deq = [1, 2, 3, 4, 5]

    # Display the original deque
    print("Original Deque:", deq)

    # Type-1: Right Rotate by K places
    right_Rotate_Deq_ByK(deq, 2)
    print("After Right Rotation:", deq)

    # Type-2: Left Rotate by K places
    left_Rotate_Deq_ByK(deq, 3)
    print("After Left Rotation:", deq)
