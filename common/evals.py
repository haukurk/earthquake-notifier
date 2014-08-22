__author__ = 'haukurk'
import config


# evaluate the quake.
def eval_quake(entry):
    """
    Evaluate if quake should be notified or not, based on config threshold.
    :param entry: quake entry
    :return: quake entry or None.
    """
    if float(entry["size"]) > config.QUAKE_SIZE_THRESHOLD:
        return entry
    return None