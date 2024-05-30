class RecycleRewardSystem:
    def __init__(self):
        self.item_rewards = {
            'A': 0.10,
            'B': 0.05,
            'C': 0.15
        }
        self.reset_system()

    def add_item(self, item_type):
        if item_type in self.item_rewards:
            self.items.append(item_type)
            self.total_reward += self.item_rewards[item_type]
            print(f"Item {item_type} added. Current total reward: INR{self.total_reward:.2f}")
        else:
            print(f"Invalid item type: {item_type}. Please enter A, B, or C.")

    def view_total_reward(self):
        print(f"Total reward accumulated: INR{self.total_reward:.2f}")

    def reset_system(self):
        self.items = []
        self.total_reward = 0.0
        print("System reset for a new user session.")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. View total reward")
            print("3. Reset system")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                item_type = input("Enter item type (A, B, or C): ").upper()
                self.add_item(item_type)
            elif choice == '2':
                self.view_total_reward()
            elif choice == '3':
                self.reset_system()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    system = RecycleRewardSystem()
    system.run()
