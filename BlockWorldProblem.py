from Action import Action
from State import State

initial_state = State(None, None, positive_literals=["onAtable", "onCA", "onBtable", "clearB", "clearC", "cleartable"],
                      negative_literals=["clearA", "onBA", "onBC", "onAB", "onAC", "onAB", "onCB"])

goal_state = State(None, None, positive_literals=["onAB", "onBC", "clearA"],
                   negative_literals=['onAB', 'onAC', 'onBC', 'onCA', "clearB", "clearC"])

def get_actions():
    actions = []
    blocks = ["A", "B", "C"]
    locations = ["A", "B", "C", "table"]

    for block in blocks:
        for location in locations:
            for location2 in locations:
                # if block == location and block == location2 and location == location2:
                #     neg_precond = ["on" + block + location, "clear" + block, "clear" + location2]
                if block != location and block != location2 and location != location2:
                    move_action = Action(name="move" + block + location + location2,
                                         positive_preconditions=["on" + block + location, "clear" + block,
                                                                 "clear" + location2],
                                         # negative_preconditions= neg_precon,
                                         negative_preconditions=[],
                                         add_list=["on" + block + location2],
                                         delete_list=["clear" + location2, "on" + block + location])
                actions.append(put_action)

    for block in blocks:
        for location in locations:
            move_to_table_action = Action(name="moveToTable" + block + location,
                                          positive_preconditions=["on" + block + location, "clear" + block],
                                          negative_preconditions=[],
                                          add_list=["on" + block + "table", "clear" + block],
                                          delete_list=["on" + block + location])
            actions.append(move_to_table_action)

    return actions
