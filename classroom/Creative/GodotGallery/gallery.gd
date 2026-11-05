extends Node3D

var angle := deg_to_rad(24.0)
@onready var camera: Camera3D = $Camera
@onready var wall_label: Label = $HUD/Controls/WallLabel
@onready var label_button: Button = $HUD/Controls/Buttons/Label

func _ready() -> void:
    $HUD/Controls/Buttons/Left.pressed.connect(orbit.bind(-1))
    $HUD/Controls/Buttons/Right.pressed.connect(orbit.bind(1))
    label_button.pressed.connect(toggle_label)
    orbit(0)

func orbit(direction: int) -> void:
    angle += deg_to_rad(15.0) * direction
    camera.position = Vector3(16.0 * sin(angle), 8.0, 16.0 * cos(angle))
    camera.look_at(Vector3(0, 1.15, 0), Vector3.UP)

func toggle_label() -> void:
    wall_label.visible = not wall_label.visible
    label_button.text = " Hide wall label " if wall_label.visible else " Read wall label "
