import sys

class Show:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <FILENAME>")
        return

    shows = []

    # Read text file
    with open(sys.argv[1], 'r') as file:
        for line in file:
            split = line.strip().split(" ")
            name  = split[0]
            start = int(split[1])
            end   = int(split[2])
            shows.append(Show(name, start, end))

    # Solve
    plan_index = 0
    while len(shows) > 0:
        current_plan = []
        to_consider = shows
        shows = []

        print("Plan", plan_index)

        while len(to_consider) > 0:
            # First show to end
            show = min(to_consider, key=lambda x: x.end)

            # Print selected show
            print("  ", show.name, show.start, show.end)
            current_plan.append(show)

            to_consider_new = []
            for s in to_consider:
                # Remove the show
                if s == show:
                    continue
        
                if s.start <= show.end:
                    shows.append(s)
                else:
                    to_consider_new.append(s)
            to_consider = to_consider_new

        plan_index += 1
           
if __name__ == "__main__":
    main()
