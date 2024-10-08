def on_fire_created(location):
    scene.create_particle_effect_at_location(location, effects.fire)
    music.knock.play()
    sprites.set_flame_strength(location, 5)
sprites.on_fire_created(on_fire_created)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            Fire Helicopter Left Animation
        """),
        50,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_fire_destroyed(location2):
    scene.clear_particle_effects_at_location(location2)
    tiles.set_tile_at(location2, assets.tile("""
        burnt tree
    """))
    music.thump.play()
sprites.on_fire_destroyed(on_fire_destroyed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            Fire Helicopter Right Animation
        """),
        50,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile(sprite, location3):
    sprite.destroy()
    sprites.change_flame_strength_by(location3, -1)
scene.on_overlap_tile(SpriteKind.water,
    assets.tile("""
        tree fire
    """),
    on_overlap_tile)

def on_a_repeated():
    sprites.spray(mySprite, assets.image("""
        water
    """))
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

mySprite: Sprite = None
game.set_health_of_trees(0)
game.set_strength_of_wind(0)
game.set_dryness_of_grass(0)
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
        Fire Helicopter Right
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
for index in range(4):
    sprites.create_spreading_fire(assets.tile("""
            tree
        """),
        assets.tile("""
            tree fire
        """))
hud.fire_hud(True)
hud.danger_hud(True)
hud.forest_hud(True)

def on_on_update():
    sprites.random_spread()
game.on_update(on_on_update)
