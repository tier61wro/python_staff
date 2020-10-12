def arg_printer(arg, *args, **kwargs):
	print(f"arg={arg}, sum = {(args)}, kwargs={kwargs}")

arg_printer(1, *[2, 3], **{'c' : 9})
