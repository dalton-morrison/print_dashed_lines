def print_dashed_line(length, lineType="double"):
    if lineType == "double":
        print("="*length)
    elif lineType == "single":
        print("-"*length)
    elif lineType == "underscore":
        print("_"*length)
