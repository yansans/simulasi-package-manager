import manager

cwd = manager.os.getcwd()
db_path = "\\db"
db = cwd + db_path

def menu():
    print("""   Menu
    1. Install package
    2. List of available packages
    3. List of installed packages
    4. Delete package
    5. Delete all installed packages
    6. Exit
    """
    )
    choice = input("Insert your choice: ")
    return choice

if __name__ == "__main__":
    pm = manager.PackageManager(db, cwd)
    pm.update_db()

    print("Welcome to package manager!")

    while(1):

        try:
            choice = int(menu())
        except ValueError:
            choice = 0

        if choice == 1:
            package = input("Input the name of the package: ")
            pm.install_package(package)
        elif choice == 2:
            pm.list_packages()
        elif choice == 3:
            pm.list_installed()
        elif choice == 4:
            pm.list_installed()
            package = input("Input the name of the package: ")
            pm.remove_package(package)
        elif choice == 5:
            pm.delete_all()
        elif choice == 6:
            exit(0)
        else:
            print("Choice not found!")

        print()
        print("Press enter to continue...")
        input()


