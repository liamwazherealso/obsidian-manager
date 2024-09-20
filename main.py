import shutil

BASE_PATH = "/Users/lpieri/Dropbox/notes/"
LAST_WEEK_PATH = BASE_PATH + "2022-11-20.md"
CURR_WEEK_PATH = BASE_PATH + "2022-12-11.md"
LAST_WEEK_PATH_TMP = LAST_WEEK_PATH + ".tmp"

with open(LAST_WEEK_PATH) as f:
    last_week_lines = f.readlines()

t_total = 0
t_done = 0

curr_week_lines = []

with open(CURR_WEEK_PATH, 'w') as f:
    for l in last_week_lines:
        if any([s in l for s in ["- [x]", "+ [x]"]]):
            t_done += 1
            continue
        elif any([s in l for s in ["- [ ]", "+ [ ]"]]):
            t_total += 1 
            l = l.replace("\n", "*\n")
        curr_week_lines.append(l)

meta_data = """
---
t_total: {}
t_done: {}
---
""".format(t_total, t_done)

# write new week
with open(CURR_WEEK_PATH, "w") as f:   
    for l in curr_week_lines:
        f.write(l)

# add metadata to old week staging
with open(LAST_WEEK_PATH_TMP, 'w') as f:
    f.write(meta_data)
    for l in last_week_lines:
        f.write(l)

shutil.move(LAST_WEEK_PATH_TMP, LAST_WEEK_PATH)
