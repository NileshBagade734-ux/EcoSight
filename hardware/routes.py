# Maps model output label → specific servo/bin
BIN_ROUTES = {
    "cardboard": "bin_cardboard",
    "glass": "bin_glass",
    "metal": "bin_metal",
    "paper": "bin_paper",
    "plastic": "bin_plastic",
}

def get_route(label: str):
    """
    Returns the servo/bin associated with the given label.
    """
    return BIN_ROUTES.get(label, "manual_review")
