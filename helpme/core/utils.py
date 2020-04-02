

def get_module(current_module: str, relative_module_path: str = None) -> str:
    module_str = current_module.rsplit('.', 1)[0]
    if relative_module_path:
        module_str += f".{relative_module_path}"
    return module_str
