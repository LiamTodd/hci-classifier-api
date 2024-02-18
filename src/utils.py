APP_USAGE = "app usage"
INCLUSIVENESS = "inclusiveness"
USER_REACTION = "user reaction"
NON_HC = "non hc"

def map_raw_output_to_labels(raw_output):
    result = {}
    result[APP_USAGE] = True if raw_output[0] == 1 else False
    result[INCLUSIVENESS] = True if raw_output[1] == 1 else False
    result[USER_REACTION] = True if raw_output[2]== 1 else False
    result[NON_HC] = True if raw_output[3] == 1 else False
    return result

    