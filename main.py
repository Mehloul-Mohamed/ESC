import argparse
import tools.italics as italics
import tools.esotericpy as esotericpy
import tools.nobuiltins as nobuiltins
import tools.blacklist_checker as blacklist_checker

def main():
    parser=argparse.ArgumentParser()
    subparsers=parser.add_subparsers(dest="mode")

    # Italic Mode
    italic=subparsers.add_parser('italic',help="Transform Text Into Mathematical Italic Letters (Useful to avoid blacklists)")
    italic.add_argument("Text",help="Text To Change",type=str)

    # PyDuck Mode
    duck=subparsers.add_parser('esoteric', help="Transform Text into Esoteric Python Using Boolean Tricks")
    duck.add_argument("-eval",help="Wrap Output In eval()",action="store_true")
    duck.add_argument("Type",help="Technique To Use",type=int)
    duck.add_argument("Text",help="Text To Change",type=str)
    
    # Builtin Mode
    disabled_builtin=subparsers.add_parser('builtin',help="Generate Payload To Call Function When Builtins Are Disabled")
    disabled_builtin.add_argument("Module",help="Module To Use",type=str)
    disabled_builtin.add_argument("Function",help="Function To Call",type=str)
    disabled_builtin.add_argument("Params",help="Arguments To The Function",type=str)

    # Blacklist Mode
    blacklist=subparsers.add_parser('blacklist',help="Generate List Of Builtins That Don't Trigger A Specified Blacklist")
    blacklist.add_argument("blist",help="Blacklist String",type=str)


    args=parser.parse_args()


    if args.mode=="italic":
        print("Payload: ", italics.italize(args.Text))
        
    elif args.mode=="esoteric":
        if args.Type==1:
            print("Payload: ", esotericpy.transform(args.Text,args.eval))
        elif args.Type==2:
            print("Payload: ", esotericpy.transform2(args.Text,args.eval))
        else:
            print("EsotericPy: Invalid Type Value")
            
    elif args.mode=="builtin":
        print("Payload: ", nobuiltins.payload(args.Module,args.Function,args.params))
        
    elif args.mode=="blacklist":
        print("List Of Available Builtins:")
        for fn in blacklist_checker.valid(args.blist):
            print(fn)

if __name__=="__main__":
    main()
