import os
import time

def clear_screen():
    os.system('clear')

def banner():
    print("========================================")
    print("      TAMIM PREMIUM GAME BOOSTER       ")
    print("      Device: Vivo Y21 (Optimized)     ")
    print("========================================")

def optimize_system():
    print("\n[+] র‍্যাম (RAM) খালি করা হচ্ছে...")
    os.system('am kill-all')
    time.sleep(1)
    
    print("[+] গ্রাফিক্স বুস্ট করা হচ্ছে (GPU Turbo)...")
    os.system('settings put global window_animation_scale 0.5')
    os.system('settings put global transition_animation_scale 0.5')
    os.system('settings put global animator_duration_scale 0.5')
    
    print("[+] নেটওয়ার্ক ল্যাগ কমানো হচ্ছে (Ping Fix)...")
    os.system('settings put global sync_max_retry_delay_in_seconds 3600')
    
    print("[+] ব্যাটারি পারফরম্যান্স মোড অন করা হচ্ছে...")
    os.system('cmd power set-fixed-performance-mode-enabled true')
    print("\n[✔] সিস্টেম অপ্টিমাইজেশন সম্পন্ন!")

def launch_game(game_choice):
    games = {
        "1": ("Free Fire", "com.dts.freefireth"),
        "2": ("PUBG/BGMI", "com.tencent.ig"),
        "3": ("Mobile Legends", "com.mobile.legends"),
        "4": ("Custom Game (Enter Package Name)", "")
    }
    
    if game_choice in games:
        name, package = games[game_choice]
        if game_choice == "4":
            package = input("গেমের প্যাকেজ নাম দাও (যেমন: com.example.game): ")
            name = "Your Game"
        
        print(f"\n[!] {name} শুরু হচ্ছে... শুভকামনা!")
        os.system(f'monkey -p {package} -c android.intent.category.LAUNCHER 1')
    else:
        print("ভুল অপশন!")

def main():
    clear_screen()
    banner()
    print("১. বুস্ট এবং গেম খেলুন")
    print("২. শুধু সিস্টেম ক্লিন করুন")
    print("৩. বের হয়ে যান")
    
    choice = input("\nতোমার পছন্দ বেছে নাও (1/2/3): ")
    
    if choice == "1":
        optimize_system()
        print("\nকোন গেমটি খেলবে?")
        print("1. Free Fire")
        print("2. PUBG")
        print("3. Mobile Legends")
        print("4. অন্য গেম (Add New)")
        game_choice = input("\nঅপশন দাও: ")
        launch_game(game_choice)
    elif choice == "2":
        optimize_system()
        print("\nফোন এখন আগের চেয়ে ফাস্ট কাজ করবে।")
    else:
        print("ধন্যবাদ!")

if __name__ == "__main__":
    main()