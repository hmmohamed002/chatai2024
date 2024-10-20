#[cfg(test)]
mod tests;

/// This module contains light borders
/// #Example
/// ```
/// use box_drawing::light;
/// let expected = "┌─┐";
/// let actual = format!("{}{}{}", light::DOWN_RIGHT, light::HORIZONTAL, light::DOWN_LEFT);
/// assert_eq!(expected, actual);
/// ```
pub mod light;

/// This module contains heavy (bold) borders
pub mod heavy;

/// This module contains doubled borders
pub mod double;

/// Contains rounded corners
pub mod arc;