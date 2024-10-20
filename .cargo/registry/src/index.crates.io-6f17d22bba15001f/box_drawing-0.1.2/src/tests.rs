#[test]
fn light_showcase() {
    let expected = "┌─┐";
    let actual = format!("{}{}{}", ::light::DOWN_RIGHT, ::light::HORIZONTAL, ::light::DOWN_LEFT);
    assert_eq!(expected, actual);
}

#[test]
fn heavy_showcase() {
    let expected = "┏━┓";
    let actual = format!("{}{}{}", ::heavy::DOWN_RIGHT, ::heavy::HORIZONTAL, ::heavy::DOWN_LEFT);
    assert_eq!(expected, actual);
}

#[test]
fn double_showcase() {
    let expected = "╔═╗";
    let actual = format!("{}{}{}", ::double::DOWN_RIGHT, ::double::HORIZONTAL, ::double::DOWN_LEFT);
    assert_eq!(expected, actual);
}

#[test]
fn arc_corners() {
    let expected = "╰╯╭╮";
    let actual = format!("{}{}{}{}", ::arc::UP_RIGHT, ::arc::UP_LEFT, ::arc::DOWN_RIGHT, ::arc::DOWN_LEFT);
    assert_eq!(expected, actual);
}