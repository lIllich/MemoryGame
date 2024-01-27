# import json
# from tkinter import messagebox
# from tkinter import ttk
# import tkinter as tk
# from tkinter import filedialog

# # Load the JSON data
# with open('categories.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)


# def update_json():
#     with open('categories.json', 'w') as f:
#         json.dump(data, f, indent=4)

# def delete_category(id):
#     for i, category in enumerate(data['category']):
#         if category['id'] == id:
#             confirm = tk.messagebox.askyesno('Potvrda', f'Jeste li sigurni da želite izbrisati kategoriju pod nazivom {category["name"]}?')
#             if confirm:
#                 del data['category'][i]
#                 update_json()
#                 refresh_window()
#             break


# def refresh_window():
#     for widget in root.winfo_children():
#         widget.destroy()
#     create_widgets()

# def create_widgets():
#     tk.Label(root, text='Ime kategorije').grid(row=0, column=0, padx=10)
#     tk.Label(root, text='Vrsta').grid(row=0, column=1, padx=10)
#     tk.Label(root, text='Aktivna').grid(row=0, column=2, padx=10)
#     tk.Label(root, text=' ').grid(row=0, column=3, padx=10)  # Empty label for alignment

#     for i, category in enumerate(data['category']):
#         tk.Label(root, text=category['name']).grid(row=i+1, column=0, padx=10)
#         tk.Label(root, text=category['iterate']).grid(row=i+1, column=1, padx=10)

#         var = tk.BooleanVar(value=category['active'])
#         chk = tk.Checkbutton(root, variable=var)
#         chk.grid(row=i+1, column=2, padx=10)
#         chk['command'] = lambda v=var, id=category['id']: toggle_active(v, id)

#         if category['type'] != 0:
#             tk.Button(root, text='Izbriši', command=lambda id=category['id']: delete_category(id)).grid(row=i+1, column=3, padx=10)
#             tk.Button(root, text='Postavi', command=lambda id=category['id']: add_card(id)).grid(row=i+1, column=4, padx=10)
    
#     tk.Button(root, text='Nova kategorija', command=create_category).grid(row=i+2, pady=10)

# def add_card(id):
#     entries = []
#     for category in data['category']:
#         if category['id'] == id:
#             top = tk.Toplevel(root)
#             top.title('Add Card')

#             for i, card in enumerate(category['cards'][:10]):
#                 tk.Label(top, text=str(card)).grid(row=i, column=0, columnspan=2)

#             if category['iterate'] == 'single_string':
#                 entries.append(tk.Entry(top))
#                 entries[-1].grid(row=11, column=0)
#             elif category['iterate'] == 'double_string':
#                 entries.append(tk.Entry(top))
#                 entries.append(tk.Entry(top))
#                 entries[-2].grid(row=11, column=0)
#                 entries[-1].grid(row=11, column=1)
#             elif category['iterate'] in ('name_and_image', 'double_image'):
#                 entries.append(tk.Entry(top))
#                 entries.append(tk.Entry(top))
#                 entries[-2].grid(row=11, column=0)
#                 tk.Button(top, text='Browse', command=lambda: entries[-1].insert(0, filedialog.askopenfilename(filetypes=[('PNG Images', '*.png')]))).grid(row=11, column=1)

#             tk.Button(top, text='Dodaj', command=lambda: submit_card(id, entries)).grid(row=12, columnspan=2)
#             break

# def submit_card(id, entries):
#     for category in data['category']:
#         if category['id'] == id:
#             if category['iterate'] == 'single_string':
#                 add_to_json(id, entries[0].get())
#             elif category['iterate'] == 'double_string':
#                 add_to_json(id, {'value1': entries[0].get(), 'value2': entries[1].get()})
#             elif category['iterate'] in ('name_and_image', 'double_image'):
#                 add_to_json(id, {'name': entries[0].get(), 'img': entries[1].get()})


# def add_to_json(id, card):
#     for category in data['category']:
#         if category['id'] == id:
#             category['cards'].append(card)
#             with open('your_json_file.json', 'w') as f:
#                 json.dump(data, f)


# def toggle_active(var, id):
#     for category in data['category']:
#         if category['id'] == id:
#             category['active'] = var.get()
#             break
#     update_json()

# def create_category():
#     top = tk.Toplevel(root)
#     top.title('Create Category')

#     tk.Label(top, text='Name').grid(row=0, column=0)
#     name_entry = tk.Entry(top)
#     name_entry.grid(row=0, column=1)

#     tk.Label(top, text='Iterate').grid(row=1, column=0)
#     iterate_var = tk.StringVar()
#     iterate_combobox = tk.ttk.Combobox(top, textvariable=iterate_var)
#     iterate_combobox['values'] = ('tekst', 'dva teksta', 'tekst i slika', 'dvije slike')
#     iterate_combobox.grid(row=1, column=1)

#     active_var = tk.BooleanVar(value=False)
#     tk.Checkbutton(top, text='Active', variable=active_var).grid(row=2, columnspan=2)

#     tk.Button(top, text='Submit', command=lambda: submit_category(name_entry.get(), iterate_var.get(), active_var.get())).grid(row=3, columnspan=2)

# def submit_category(name, iterate, active):
#     iterate_mapping = {
#         'tekst': 'single_string',
#         'dva teksta': 'double_string',
#         'tekst i slika': 'name_and_image',
#         'dvije slike': 'double_image'
#     }
#     new_category = {
#         'id': max(category['id'] for category in data['category']) + 1,
#         'type': 1,
#         'active': active,
#         'name': name,
#         'iterate': iterate_mapping.get(iterate, 'single_string'),
#         'cards': []
#     }
#     data['category'].append(new_category)
#     update_json()
#     refresh_window()


# root = tk.Tk()
# create_widgets()
# root.mainloop()

