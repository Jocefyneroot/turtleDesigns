import random

class Ant:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.tools = []

    def attack(self, enemy):
        damage = random.randint(5, 20)
        enemy.health -= damage
        print(f"{self.name} attacked {enemy.name} and dealt {damage} damage.")

    def use_tool(self, tool):
        if tool in self.tools:
            self.tools.remove(tool)
            self.health += 10
            print(f"{self.name} used {tool} to gain 10 health.")

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def main():
    ant = Ant("Antma")
    enemies = [
        Enemy("Human", 50),
        Enemy("Rock", 30),
        Enemy("Water", 40),
        Enemy("Tree", 60),
        Enemy("Grass", 20),
    ]

    while ant.health > 0:
        print("\nAntma's Stats:")
        print(f"Health: {ant.health}")
        print("Tools:", ant.tools)

        print("\nEnemies:")
        for i, enemy in enumerate(enemies, start=1):
            print(f"{i}. {enemy.name} - Health: {enemy.health}")

        choice = input("\nEnter the number of the enemy you want to attack (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            break

        try:
            enemy_choice = int(choice) - 1
            selected_enemy = enemies[enemy_choice]

            ant.attack(selected_enemy)

            if selected_enemy.health <= 0:
                print(f"{selected_enemy.name} defeated!")
                ant.tools.append(selected_enemy.name)

            for enemy in enemies[:]:  # Remove defeated enemies
                if enemy.health <= 0:
                    enemies.remove(enemy)

            if random.random() < 0.3:
                tool_found = random.choice(["Sword", "Shield", "Healing Potion"])
                ant.tools.append(tool_found)
                print(f"{ant.name} found a {tool_found}!")

            ant.use_tool("Healing Potion")  # Automatically use a healing potion if available

        except (ValueError, IndexError):
            print("Invalid choice. Try again.")

    print("Game Over! Antma's journey has ended.")

if __name__ == "__main__":
    main()
