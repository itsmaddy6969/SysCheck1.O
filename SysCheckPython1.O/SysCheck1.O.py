import os
import platform
import subprocess

# Function to display CPU information
def get_cpu_info():
    print("CPU Information:")
    if platform.system() == "Windows":
        os.system("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status")
    elif platform.system() == "Linux":
        os.system("lscpu")
    print("\n")

# Function to display GPU information
def get_gpu_info():
    print("GPU Information:")
    if platform.system() == "Windows":
        subprocess.call("wmic path win32_videocontroller get caption, name, driverversion", shell=True)
    elif platform.system() == "Linux":
        os.system("lspci | grep VGA")
    print("\n")

# Function to display memory information
def get_memory_info():
    print("Memory Information:")
    if platform.system() == "Windows":
        os.system("wmic memorychip get capacity, speed")
    elif platform.system() == "Linux":
        os.system("free -h")
    print("\n")

# Function to display storage information
def get_storage_info():
    print("Storage Information:")
    if platform.system() == "Windows":
        os.system("wmic diskdrive get model, size, status")
    elif platform.system() == "Linux":
        os.system("lsblk")
    print("\n")

# Function to check the operating system version
def get_os_info():
    print("Operating System Information:")
    os_info = platform.platform()
    print(f"OS: {os_info}")
    print("\n")

# Run all functions to display hardware information
def display_hardware_info():
    print("==== PC Hardware Information ====\n")
    get_os_info()
    get_cpu_info()
    get_gpu_info()
    get_memory_info()
    get_storage_info()

# Run the hardware information display function
display_hardware_info()

