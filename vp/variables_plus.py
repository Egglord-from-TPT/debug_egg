vp_sandbox={}
vp_sandbox_mode=False
sb="NoSandbox"
def variables_plus(cmd):
    global vp_sandbox, vp_sandbox_mode, sb
    cmd=cmd.strip()
    a=""
    b=""
    c=""
    if cmd.startswith("clear(") and cmd.endswith(")"):
        if not sb.isdigit():
            raise SyntaxError("You must create a sandbox. Use vp.vp('SANDBOX(ID)') to create and switch to a new sandbox (Replace ID with a number).")
        else:
            if cmd[6:-1] == "":
                for i in vp_sandbox[sb]:
                    vp_sandbox[sb][i]=""
            else:
                try:
                    vp_sandbox[sb][cmd[6:-1]]=""
                except Exception:
                    raise TypeError("Invalid variable! Enter a variables name or leave it blank to clear the variable(s).")
    elif cmd.startswith("create(") and cmd.endswith(")"):
        if not sb.isdigit():
            raise SyntaxError("You must create a sandbox. Use vp.vp('SANDBOX(ID)') to create and switch to a new sandbox (Replace ID with a number).")
        else:
            if not cmd[7:-1] == "":
                try:
                    if "=" in cmd[7:-1]:
                        if cmd[7:-1].count("=")==1:
                            a,b=cmd[7:-1].split("=", 1)
                            if not a in vp_sandbox[sb]:
                                if not a.strip()=="":
                                    vp_sandbox[sb][a]=b
                                else:
                                    raise SyntaxError("Cannot create an empty variable.")
                            else:
                                raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                        else:
                            raise SyntaxError("Use a singular '=' to set a variable.")
                    else:
                        a=cmd[7:-1]
                        if not a in vp_sandbox[sb]:
                            vp_sandbox[sb][a]=""
                        else:
                            raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't create a blank variable.")
    elif cmd.startswith("delete(") and cmd.endswith(")"):
        if not sb.isdigit():
            raise SyntaxError("You must create a sandbox. Use vp.vp('SANDBOX(ID)') to create and switch to a new sandbox (Replace ID with a number).")
        else:
            if not cmd[7:-1] == "":
                for i in vp_sandbox[sb]:
                    if i==cmd[7:-1]:
                        try:
                            del vp_sandbox[sb][i]
                            break
                        except Exception:
                            raise TypeError("Variable", i, "doesn't exist.")
            else:
                raise SyntaxError("You can't delete a non-existent variable.")
    elif cmd.startswith("read(") and cmd.endswith(")"):
        if not sb.isdigit():
            raise SyntaxError("You must create a sandbox. Use vp.vp('SANDBOX(ID)') to create and switch to a new sandbox (Replace ID with a number).")
        else:
            if cmd[5:-1] in vp_sandbox[sb]:
                return vp_sandbox[sb][cmd[5:-1]]
            else:
                raise TypeError("Variable", cmd[5:-1], "doesn't exist.")
    elif cmd.startswith("write(") and cmd.endswith(")"):
        if not sb.isdigit():
            raise SyntaxError("You must create a sandbox. Use vp.vp('SANDBOX(ID)') to create and switch to a new sandbox (Replace ID with a number).")
        else:
            if not cmd[6:-1] == "":
                try:
                    if "=" in cmd[6:-1]:
                        a,b=cmd[6:-1].split("=", 1)
                        if a in vp_sandbox[sb]:
                            vp_sandbox[sb][a]=b
                        else:
                            raise SyntaxError("Variable "+a+" doesn't exist! Use vp.vp('create()') to create a new variable.")
                    else:
                        a=cmd[6:-1]
                        raise SyntaxError("To modify variable "+a+", you must use '=' .")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't modify a non-existent variable.")
    elif cmd.startswith("SANDBOX(") and cmd.endswith(")"):
        if cmd[8:-1].isdigit():
            if not cmd[8:-1] in vp_sandbox:
                vp_sandbox[cmd[8:-1]]={}
            sb=cmd[8:-1]
        else:
            raise SyntaxError("You must enter a number for the sandbox ID.")
    else:
        raise TypeError("Invalid command! Use vp.vp('clear()'), vp.vp('create()'), vp.vp('write()'), vp.vp('SANDBOX()') or vp.vp('delete()'). Note: clear() doesn't delete the variable, it makes it a blank string.")
vp=variables_plus
