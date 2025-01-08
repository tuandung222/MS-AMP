import torch.amp.grad_scaler

def toggle_comment_line_in_module(module, line_number):
    import inspect
    file_path = inspect.getfile(module)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    if line_number > len(lines):
        print(f"File doesn't have {line_number} lines.")
        return
    idx = line_number - 1
    if lines[idx].lstrip().startswith('#'):
        lines[idx] = lines[idx].lstrip('#')
    else:
        lines[idx] = '#' + lines[idx]
    with open(file_path, 'w') as f:
        f.writelines(lines)

toggle_comment_line_in_module(torch.amp.grad_scaler, 256)

