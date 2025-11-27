def on_on_chat():
    for index in range(4):
        mobs.spawn(CHICKEN, pos(0, 10, 0))
player.on_chat("chicken", on_on_chat)
