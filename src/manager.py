from graph import *
import os

cwd = os.getcwd()
db_path = "\\db"
db = cwd + db_path

mark = ';'

class PackageManager():

    global package_list
    global dependency_list
    global installed_list

    def __init__ (self, db_folder, usr_folder):
        self.db_folder = db_folder
        self.usr_folder = usr_folder
        self.g = Graph(0)

    def update_db(self):
        global installed_list
        installed_list = []
        for file in os.listdir(self.usr_folder):
            if file.endswith(".txt"):
                package_str = ''
                with open(self.usr_folder + "\\" + file, "r") as f:
                    for line in f:
                        line = line.strip(mark)
                        package_str += line
                installed_list = package_str.split(mark)

        global package_list
        package_list = []
        for package in os.listdir(self.db_folder):
            # print(package)
            package_name = package.split(".")[0]
            # print(package_name)
            package_list.append(package_name)

        package_list = list(dict.fromkeys(package_list))

    def update_installed(self):
        global installed_list
        with open(self.usr_folder + "\\installed.txt", "w") as f:
            for package in installed_list:
                f.write(package + mark)
                        
    def get_package(self, package_name):
        order = []
        global dependency_list
        dependency_list = self.get_dependencies(package_name)
        # print(dependency_list)

        self.g.n_v = len(dependency_list)
        self.g.list_v = dependency_list

        order += self.g.topologicalSort()
        return order

    def get_dependencies(self, package_name):
        d_list = []
        with open(self.db_folder + "\\" + package_name + ".txt", "r") as f:
            dependency = ''
            for line in f:
                line = line.strip()
                if line.strip(mark) == "dependency":
                    continue
                else:
                    dependency += line
            if dependency != '':
                for dep in dependency.strip(mark).split(mark):
                    d_list.append(dep)
                    d_list += self.get_dependencies(dep)

        d_list = list(dict.fromkeys(d_list))

        for dep in d_list:
            self.g.addEdge(package_name, dep)

        return d_list

    def install_package(self, package_name):
        if package_name not in package_list:
            print("Package name not found in database.")
            return
        global installed_list
        order = self.get_package(package_name)
        print("Solving dependencies:")
        install_list = []
        for package in order:
            if package in installed_list:
                print(package + " is already installed")
            else:
                install_list.append(package)
        print("Need to install:")
        if install_list == []:
            print("-")
            if package_name in installed_list:
                print(package_name + " is already installed")
                return
        for package in install_list:
            print(package)
        if package_name not in install_list:
            install_list.append(package_name)
        choice = input("Proceed with installation? [Y/n] ")
        if choice == 'Y' or choice == 'y':
            for package in install_list:
                print("Installing " + package)
                installed_list.append(package)
            self.update_installed()
            print()
            print("Installation complete")
        else:
            print("Installation aborted")
    
    def remove_package(self, package_name):
        global installed_list
        if package_name in installed_list:
            print("Deleting " + package_name)
            installed_list.remove(package_name)
        else:
            print(package_name + " is not installed")
        self.update_installed()

    def list_packages(self):
        global package_list
        print("All available packages:")
        for package in package_list:
            print(package)

    def list_installed(self):
        global installed_list
        print("Installed packages:")
        for package in installed_list:
            print(package)

    def delete_all(self):
        global installed_list
        installed_list = []
        self.update_installed()
        print("All packages deleted")

if __name__ == "__main__":
    pm = PackageManager(db, cwd)
    # pm.update_db()
    # pm.install_package("5")
    # pm.list_packages()