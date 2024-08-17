sprites.on_fire_created(function on_fire_created(location: tiles.Location) {
    scene.createParticleEffectAtLocation(location, effects.fire)
    music.knock.play()
    sprites.set_flame_strength(location, 5)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            Fire Helicopter Left Animation
        `, 50, true)
})
sprites.on_fire_destroyed(function on_fire_destroyed(location2: tiles.Location) {
    scene.clearParticleEffectsAtLocation(location2)
    tiles.setTileAt(location2, assets.tile`
        burnt tree
    `)
    music.thump.play()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            Fire Helicopter Right Animation
        `, 50, true)
})
scene.onOverlapTile(SpriteKind.Water, assets.tile`
        tree fire
    `, function on_overlap_tile(sprite: Sprite, location3: tiles.Location) {
    sprite.destroy()
    sprites.change_flame_strength_by(location3, -1)
})
controller.A.onEvent(ControllerButtonEvent.Repeated, function on_a_repeated() {
    sprites.spray(mySprite, assets.image`
        water
    `)
    music.pewPew.play()
})
let mySprite : Sprite = null
game.set_health_of_trees(0)
game.set_strength_of_wind(0)
game.set_dryness_of_grass(0)
tiles.setTilemap(tilemap`
    level1
`)
mySprite = sprites.create(assets.image`
        Fire Helicopter Right
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
for (let index = 0; index < 4; index++) {
    sprites.create_spreading_fire(assets.tile`
            tree
        `, assets.tile`
            tree fire
        `)
}
hud.fire_hud(true)
hud.danger_hud(true)
hud.forest_hud(true)
game.onUpdate(function on_on_update() {
    sprites.random_spread()
})
