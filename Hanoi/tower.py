#tower of Hanoi

def towerofHanoi(num, source, destination, helper):
    if num == 0:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towerofHanoi(num-1, source, helper, destination)
    print(f"Move disk {num} from {source} to {destination}")
    towerofHanoi(num-1, helper, destination, source)
    
towerofHanoi(3, 'A', 'C', 'B')