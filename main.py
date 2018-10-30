import os

information = {}
sections = []


def parse(location):
    global inforamtion, sections
    with open(location, "r") as osu_file:
        for line in osu_file:
            try:
                if ":" in line:
                    line_array = line.split(":")
                    try:
                        if line_array[2]: #too many colons
                            pass
                    except:
                        #print(line_array[0],line_array[1])
                        information[line_array[0].strip()] = line_array[1].strip()
                elif "[" in line:
                    #print(line)
                    sections.append(line.strip())
                    
            except:
                pass

parse("beatmaps/example.osu")

print(information,sections)
