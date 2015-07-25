    """Connectc an action to a function"""
    """Connect a triggered(bool) action to a function"""
    """Connect a button to a function"""
def button_action(button, action):
    """Make a button trigger an action"""
    connect_button(button, action.trigger)


def mkicon(icon, default=None):
    if icon is None and default is not None:
        icon = default()
    return icon


def confirm(title, text, informative_text, ok_text,
            icon=None, default=True,
            cancel_text=None, cancel_icon=None):
    """Confirm that an action should take place"""

    icon = mkicon(icon, ok_icon)

    cancel_icon = mkicon(cancel_icon, discard_icon)
    cancel.setIcon(cancel_icon)
    if cancel_text:
        cancel.setText(cancel_text)

    return theme_icon('list-add', fallback='add.svg')
    return theme_icon('list-remove', fallback='remove.svg')
    return theme_icon('document-open', fallback='open.svg')
    return theme_icon('configure', fallback='options.svg')
    return theme_icon('view-filter.png')
def theme_icon(name, fallback=None):
    Support older versions of Qt checking for fromTheme's availability.
    if hasattr(QtGui.QIcon, 'fromTheme'):
        if fallback:
            qicon = QtGui.QIcon.fromTheme(base, icon(fallback))
        else:
            qicon = QtGui.QIcon.fromTheme(base)
    return icon(fallback or name)
def make_format(fg=None, bg=None, bold=False):
    fmt = QtGui.QTextCharFormat()
    if fg:
        fmt.setForeground(fg)
    if bg:
        fmt.setBackground(bg)
    if bold:
        fmt.setFontWeight(QtGui.QFont.Bold)
    return fmt