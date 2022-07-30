while(1):
       try:
              print("\nNote: Type of laptop --> it's corresponding input\n")
              print('gaming laptop --> 1')
              print('thin and light laptop --> 2')
              print('2 in 1 laptop --> 3')
              print('notebook --> 4')
              print('laptop --> 5')
              print('2 in 1 gaming laptop --> 6')
              print('business laptop --> 7')
              print('chromebook --> 8')
              print('creator laptop --> 9\n')
              print("Enter type of laptop: ",end='')
              type=int(input())
              
              print("\nNote: Valid laptop brands --> it's corresponding input\n")
              print('asus --> 1\nhp --> 2\nlenovo --> 3\ndell --> 4\nmsi --> 5\nrealme --> 6\navita --> 7\nacer --> 8\nsamsung --> 9\ninfinix --> 10\nlg --> 11\napple --> 12\nnokia --> 13\nredmibook --> 14\nmi --> 15\nvaio --> 16\n')
              print("Enter laptop brand: ",end='')
              laptop_brand=int(input())

              print("\nNote: Valid CPU brands --> it's corresponding input\n")
              print('intel --> 1')
              print('amd --> 2')
              print('qualcomm --> 3')
              print('apple --> 4')
              print('mediatek --> 5')
              print("\nEnter processor brand: ",end='')
              cpu_brand=int(input())

              print("Enter processor name: ",end='')
              cpu_name=input()

              print("\nNote: Valid GPU brands --> it's corresponding input\n")
              print('nvidia --> 1')
              print('intel --> 2')
              print('amd --> 3')
              print('qualcomm --> 4')
              print("Enter GPU brand: ",end='')
              gpu_brand=int(input())

              print("\nEnter GPU name: ",end='')
              gpu_name=input()

              print("Enter GPU memory capacity in GB (ex: for 4gb enter 4): ",end='')
              gpu_mem=int(input())

              print("Enter RAM capacity (ex: for 16 gb enter 16): ",end='')
              ram=int(input())

              print("Enter Storage capacity (input in gb): ",end='')
              storage=int(input())

              print("Enter Storage type (1 for ssd, 0 for hdd): ",end='')
              storage_type=int(input())

              print("Enter storage expandability (1 for yes, 0 for no): ",end='')
              storage_ex=int(input())

              print("Enter screen size (in inch): ",end='')
              screen_size=float(input())

              print("Enter screen resolution (ex: 720,1080,1440,2160): ",end='')
              screen_res=int(input())

              print("Touchscreen (1 for yes, 0 for no): ",end='')
              touchscreen=int(input())

              print("Enter laptop weight (in kg): ",end='')
              weight=float(input())

              print("Enter battery life (in hrs): ",end='')
              battery_life=int(input())
              
              print("\nNote: Valid operating system --> it's corresponding input\n")
              print('windows --> 1')
              print('chrome os --> 2')
              print('dos --> 3')
              print('mac --> 4')
              print('ubuntu --> 5')
              print("\nEnter operating system: ",end='')
              operating_sys=int(input())

              ar=[type,gpu_mem, cpu_brand,
                     cpu_name, storage_type, ram, storage_ex, operating_sys,
                     touchscreen, screen_size, weight, screen_res,gpu_brand,
                     laptop_brand, storage, battery_life, gpu_name]
              break
       except:
              print("\nWrong input. Please try again.\n")
              continue

