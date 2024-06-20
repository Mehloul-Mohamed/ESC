import argparse
import os
import tools.italics as italics
import tools.esotericpy as esotericpy
import tools.nobuiltins as nobuiltins
import tools.blacklist_checker as blacklist_checker

def main():
    parser=argparse.ArgumentParser()
    subparsers=parser.add_subparsers(dest="mode")
    parser.add_argument("-o", metavar="Output File",help="Output File")

    # Italic Mode
    italic=subparsers.add_parser('italic',help="Transform Text Into Mathematical Italic Letters")
    italic.add_argument("Text",help="Text To Change",type=str)

    # Esoteric Mode
    duck=subparsers.add_parser('esoteric', help="Transform Text into Esoteric Python Using Boolean Tricks")
    duck.add_argument("-eval",help="Wrap Output In eval()",action="store_true")
    duck.add_argument("Type",help="Technique To Use",choices=[1,2],type=int)
    duck.add_argument("Text",help="Text To Change",type=str)

    # Builtin Mode
    disabled_builtin=subparsers.add_parser('builtin',help="Generate output To Call Function When Builtins Are Disabled")
    disabled_builtin.add_argument("Module",help="Module To Use",type=str)
    disabled_builtin.add_argument("Function",help="Function To Call",type=str)
    disabled_builtin.add_argument("Params",help="Arguments To The Function",type=str)

    # Blacklist Mode
    blacklist=subparsers.add_parser('blacklist',help="Generate List Of Builtins That Don't Trigger A Specified Blacklist")
    blacklist.add_argument("blist",help="Blacklist String",type=str)


    args=parser.parse_args()
    output=''

    if args.mode=="italic":
        output+=italics.italize(args.Text)

    elif args.mode=="esoteric":
        if args.Type==1:
            output+=esotericpy.transform(args.Text,args.eval)
        elif args.Type==2:
            output+=esotericpy.transform2(args.Text,args.eval)

    elif args.mode=="builtin":
        output+=nobuiltins.payload(args.Module,args.Function,args.Params)

    elif args.mode=="blacklist":
        output='\n'.join(blacklist_checker.valid(args.blist))

    if args.o != None:
        if os.path.exists(args.o):
            print("ERROR: Output File Already Exists")
        else:
            with open(args.o,'w') as f:
                f.write(output+'\n')
                f.close()
    else:
        print(output)

if __name__=="__main__":
    main()
