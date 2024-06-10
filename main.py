import argparse
import tools.italics as italics
import tools.pyduck as pyduck
import tools.nobuiltins as nobuiltins
import tools.blacklist_checker as blacklist_checker

def main():
    parser=argparse.ArgumentParser()
    subparsers=parser.add_subparsers(dest="mode")

    # Italic Mode
    italic=subparsers.add_parser('italic',help="Convert Command Into Mathematical Italic Letters")
    italic.add_argument("COMMAND",help="Argument(s)",type=str)

    # PyDuck Mode
    duck=subparsers.add_parser('duck', help="Convert Command Into A Bunch Of Boolean Weirdness")
    duck.add_argument("-eval",help="(Only Useful With -mess) Wrap output in eval()",action="store_true")
    duck.add_argument("type",help="1 | 2",type=int)
    duck.add_argument("COMMAND",help="Argument(s)",type=str)
    
    # Builtin Mode
    disabled_builtin=subparsers.add_parser('builtin',help="Use Class Tricks To Use Modules When Builtins Are Disabled")
    disabled_builtin.add_argument("module",help="Builtin Module To Use",type=str)
    disabled_builtin.add_argument("function",help="Function To Call",type=str)
    disabled_builtin.add_argument("ARGS",help="Argument(s)",type=str)

    # Blacklist Mode
    blacklist=subparsers.add_parser('blacklist',help="Disaplay List Of Builtins That Do Not Trigger A Specified Blacklist")
    blacklist.add_argument("blist",help="Blacklist",type=str)


    args=parser.parse_args()


    if args.mode=="italic":
        print("Payload: ", italics.italize(args.COMMAND))
        
    elif args.mode=="duck":
        if args.type==1:
            print("Payload: ", pyduck.mess(args.COMMAND,args.eval))
        elif args.type==2:
            print("Payload: ", pyduck.mess_all(args.COMMAND,args.eval))
        else:
            print("PyDuck: Invalid Type Value")
            
    elif args.mode=="builtin":
        print("Payload: ", nobuiltins.payload(args.module,args.function,args.ARGS))
        
    elif args.mode=="blacklist":
        print("List Of Available Builtins:")
        for fn in blacklist_checker.valid(args.blist):
            print(fn)

if __name__=="__main__":
    main()
