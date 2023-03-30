import tkinter as tk
import ipaddress

def network_info():
    
    clear_output()

    ip = ip_entry.get()
    subnet = subnet_entry.get()

    
    ip_int = int(ipaddress.IPv4Address(ip))

    
    subnet_int = (0xffffffff << (32 - int(subnet))) & 0xffffffff
    subnet_mask = ipaddress.IPv4Address(int(subnet_int)).exploded

    
    network_int = ip_int & subnet_int
    network_address = ipaddress.IPv4Address(int(network_int))
    first_ip = ipaddress.IPv4Address(int(network_int + 1))
    last_ip = ipaddress.IPv4Address(int(network_int + (2 ** (32 - int(subnet)) - 2)))

   
    network_label = tk.Label(output_frame, text="Network address: " + str(network_address))
    network_label.pack(pady=(10,0))
    subnet_label = tk.Label(output_frame, text="Subnet mask: " + subnet_mask)
    subnet_label.pack(pady=(10,0))
    first_label = tk.Label(output_frame, text="First IP address: " + str(first_ip))
    first_label.pack(pady=(10,0))
    last_label = tk.Label(output_frame, text="Last IP address: " + str(last_ip))
    last_label.pack(pady=(10,0))

def clear_output():
    
    for widget in output_frame.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Network Info")


root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#FFFFFF")


input_frame = tk.Frame(root, bg="#FFFFFF")
input_frame.pack(padx=20, pady=(20,10))

ip_label = tk.Label(input_frame, text="IP address:", bg="#FFFFFF")
ip_label.grid(row=0, column=0, padx=(0,10), pady=10, sticky="w")
ip_entry = tk.Entry(input_frame, width=20)
ip_entry.grid(row=0, column=1, padx=(0,10), pady=10, sticky="w")

subnet_label = tk.Label(input_frame, text="Subnet in CIDR notation:", bg="#FFFFFF")
subnet_label.grid(row=1, column=0, padx=(0,10), pady=10, sticky="w")
subnet_entry = tk.Entry(input_frame, width=20)
subnet_entry.grid(row=1, column=1, padx=(0,10), pady=10, sticky="w")


run_button = tk.Button(root, text="Run", bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12), command=network_info)
run_button.pack(pady=20)


output_frame = tk.Frame(root, bg="#FFFFFF")
output_frame.pack(padx=20, pady=(10,20))


root.mainloop()
