"""Themes color definitions."""

from build import ColorSplit
from colors import Colors


class Components:
    transparent = ColorSplit(Colors.black).with_alpha(0)

    background = ColorSplit(Colors.neutral_50, Colors.neutral_950)
    background_foreground = ColorSplit(Colors.slate_950, Colors.slate_50)
    background_foregroundPrimary = ColorSplit(Colors.slate_800, Colors.slate_200)
    background_foregroundSecondary = ColorSplit(Colors.slate_500, Colors.slate_600)
    background_foregroundHint = ColorSplit(Colors.slate_400, Colors.slate_700)

    backgroundMuted = ColorSplit(Colors.slate_200, Colors.slate_500)
    backgroundMuted_foreground = ColorSplit(Colors.slate_950, Colors.slate_50)
    backgroundMuted_foregroundPrimary = ColorSplit(Colors.slate_800, Colors.slate_100)
    backgroundMuted_foregroundSecondary = ColorSplit(Colors.slate_500, Colors.slate_300)
    backgroundMuted_foregroundHint = ColorSplit(Colors.slate_300, Colors.slate_700)

    backgroundContrast = ColorSplit(Colors.neutral_300, Colors.neutral_700)
    backgroundContrast_foreground = ColorSplit(Colors.slate_950, Colors.slate_50)
    backgroundContrastHighlight = ColorSplit(
        Colors.neutral_300, Colors.neutral_700
    ).with_alpha(0.1)

    accent = ColorSplit(Colors.green_600, Colors.purple_600)
    accent_foreground = Colors.slate_50

    accentHighlight = accent.with_alpha(0.15, 0.25)
    accentHighlightStrong = accent.with_alpha(0.3, 0.5)
    accentHighlightLight = accent.with_alpha(0.05, 0.08)

    added = ColorSplit(Colors.lime_300, Colors.lime_400)
    addedHighlight = added.with_alpha(0.1, 0.2)
    deleted = ColorSplit(Colors.red_300, Colors.red_400)
    deletedHighlight = deleted.with_alpha(0.1, 0.2)

    error = ColorSplit(Colors.red_500, Colors.red_600)

    warning = ColorSplit(Colors.orange_500, Colors.orange_400)
    warning_foreground = Colors.black

    find = ColorSplit(Colors.yellow_400, Colors.amber_400).with_alpha(0.6)
    findHighlight = find.with_alpha(0.3)

    stackFocused = warning.with_alpha(0.6)
    stack = warning.with_alpha(0.3)
    border = ColorSplit(Colors.slate_200, Colors.slate_800)

    ansiBlack = backgroundMuted
    ansiBlue = Colors.blue_500
    ansiBrightBlack = backgroundMuted
    ansiBrightBlue = Colors.blue_400
    ansiBrightCyan = Colors.cyan_400
    ansiBrightGreen = Colors.green_400
    ansiBrightMagenta = Colors.fuchsia_400
    ansiBrightRed = Colors.red_400
    ansiBrightWhite = Colors.white
    ansiBrightYellow = Colors.yellow_400
    ansiCyan = Colors.cyan_500
    ansiGreen = Colors.green_500
    ansiMagenta = Colors.fuchsia_50
    ansiRed = Colors.red_500
    ansiWhite = Colors.white
    ansiYellow = Colors.yellow_500
    ansiForeground = backgroundMuted

    todo = Colors.pink_500


# Theme definitions

definitions = {
    "colors": {
        "activityBar.background": Components.background,
        "activityBar.border": Components.transparent,
        "activityBar.foreground": Components.background_foregroundSecondary,
        "activityBarBadge.background": Components.backgroundContrast,
        "activityBarBadge.foreground": Components.backgroundContrast_foreground,
        "badge.background": Components.backgroundMuted,
        "badge.foreground": Components.backgroundMuted_foregroundPrimary,
        "button.background": Components.accent,
        "button.foreground": Components.accent_foreground,
        "contrastBorder": Components.transparent,
        "debugToolBar.background": Components.backgroundContrast,
        "diffEditor.insertedTextBackground": Components.addedHighlight,
        "diffEditor.removedTextBackground": Components.deletedHighlight,
        "dropdown.background": Components.backgroundContrast,
        "dropdown.border": Components.border,
        "dropdown.foreground": Components.background_foregroundPrimary,
        "editor.background": Components.background,
        "editor.findMatchBackground": Components.find,
        "editor.findMatchHighlightBackground": Components.findHighlight,
        "editor.focusedStackFrameHighlightBackground": Components.stackFocused,
        "editor.foreground": Components.background_foregroundPrimary,
        "editor.lineHighlightBackground": Components.accentHighlightLight,
        "editor.lineHighlightBorder": Components.transparent,
        "editor.selectionBackground": Components.accentHighlightStrong,
        "editor.selectionForeground": Components.background_foregroundPrimary,
        "editor.selectionHighlightBorder": Components.todo,
        "editor.stackFrameHighlightBackground": Components.stack,
        "editor.wordHighlightBackground": Components.accentHighlight,
        "editor.wordHighlightStrongBackground": Components.accentHighlightStrong,
        "editorBracketMatch.background": Components.accentHighlightStrong,
        "editorBracketMatch.border": Components.transparent,
        "editorCursor.foreground": Components.accent,
        "editorError.foreground": Components.error,
        "editorGroup.border": Components.backgroundContrast,
        "editorGroupHeader.tabsBackground": Components.background,
        "editorGroupHeader.tabsBorder": Components.transparent,
        "editorGutter.addedBackground": Components.added,
        "editorGutter.deletedBackground": Components.deleted,
        "editorGutter.modifiedBackground": Components.backgroundMuted,
        "editorIndentGuide.background": Components.backgroundContrast,
        "editorLineNumber.activeForeground": Components.background_foregroundPrimary,
        "editorLineNumber.foreground": Components.background_foregroundHint,
        "editorLink.activeForeground": Components.accent,
        "editorOverviewRuler.addedForeground": Components.transparent,
        "editorOverviewRuler.border": Components.transparent,
        "editorOverviewRuler.bracketMatchForeground": Components.accentHighlightStrong,
        "editorOverviewRuler.errorForeground": Components.error,
        "editorOverviewRuler.findMatchForeground": Components.find,
        "editorOverviewRuler.modifiedForeground": Components.background_foregroundPrimary,
        "editorOverviewRuler.selectionHighlightForeground": Components.accentHighlightStrong,
        "editorOverviewRuler.warningForeground": Components.warning,
        "editorOverviewRuler.wordHighlightForeground": Components.accentHighlight,
        "editorOverviewRuler.wordHighlightStrongForeground": Components.accentHighlightStrong,
        "editorRuler.foreground": Components.backgroundContrast,
        "editorSuggestWidget.foreground": Components.background_foregroundPrimary,
        "editorWarning.foreground": Components.warning,
        "editorWidget.background": Components.backgroundContrast,
        "editorWidget.border": Components.border,
        "errorForeground": Components.error,
        "extensionButton.prominentBackground": Components.accent,
        "extensionButton.prominentForeground": Components.accent_foreground,
        "extensionButton.prominentHoverBackground": Components.accent,
        "focusBorder": Components.border,
        "foreground": Components.background_foregroundPrimary,
        "gitDecoration.ignoredResourceForeground": Components.background_foregroundSecondary,
        "gitDecoration.modifiedResourceForeground": Components.background_foregroundPrimary,
        "gitDecoration.untrackedResourceForeground": Components.background_foregroundPrimary,
        "input.background": Components.backgroundContrast,
        "input.border": Components.border,
        "input.foreground": Components.backgroundContrast_foreground,
        "input.placeholderForeground": Components.backgroundMuted_foregroundHint,
        "inputOption.activeBackground": Components.backgroundContrast,
        "inputOption.activeBorder": Components.backgroundContrast_foreground,
        "inputOption.activeForeground": Components.backgroundContrast_foreground,
        "list.activeSelectionBackground": Components.backgroundMuted,
        "list.activeSelectionForeground": Components.backgroundMuted_foregroundPrimary,
        "list.dropBackground": Components.accentHighlightStrong,
        "list.focusBackground": Components.accentHighlight,
        "list.focusForeground": Components.backgroundMuted,
        "list.highlightForeground": Components.backgroundMuted,
        "list.hoverBackground": Components.backgroundContrast,
        "list.inactiveSelectionBackground": Components.backgroundContrast,
        "list.inactiveSelectionForeground": Components.backgroundMuted,
        "panel.background": Components.backgroundContrast,
        "panel.border": Components.transparent,
        "panelTitle.activeBorder": Components.background_foregroundSecondary,
        "peekView.border": Components.backgroundMuted,
        "peekViewEditor.background": Components.transparent,
        "peekViewEditor.matchHighlightBackground": Components.find,
        "peekViewResult.background": Components.transparent,
        "peekViewResult.fileForeground": Components.backgroundMuted_foregroundSecondary,
        "peekViewResult.lineForeground": Components.backgroundMuted_foregroundSecondary,
        "peekViewResult.matchHighlightBackground": Components.find,
        "peekViewResult.selectionBackground": Components.backgroundMuted,
        "peekViewResult.selectionForeground": Components.background_foregroundPrimary,
        "peekViewTitle.background": Components.transparent,
        "peekViewTitleDescription.foreground": Components.background_foregroundSecondary,
        "peekViewTitleLabel.foreground": Components.backgroundMuted,
        "progressBar.background": Components.accent,
        "scrollbar.shadow": Components.transparent,
        "scrollbarSlider.background": Components.backgroundContrastHighlight,
        "scrollbarSlider.hoverBackground": Components.backgroundMuted,
        "sideBar.background": Components.background,
        "sideBar.foreground": Components.background_foregroundPrimary,
        "sideBarSectionHeader.background": Components.backgroundContrast,
        "sideBarSectionHeader.foreground": Components.backgroundContrast_foreground,
        "sideBarTitle.foreground": Components.background_foregroundPrimary,
        "statusBar.background": Components.background,
        "statusBar.debuggingBackground": Components.warning,
        "statusBar.debuggingForeground": Components.warning_foreground,
        "statusBar.foreground": Components.background_foregroundPrimary,
        "statusBar.noFolderBackground": Components.background,
        "tab.activeBackground": Components.backgroundMuted,
        "tab.activeForeground": Components.backgroundMuted_foregroundPrimary,
        "tab.activeModifiedBorder": Components.transparent,
        "tab.border": Components.transparent,
        "tab.inactiveBackground": Components.transparent,
        "tab.inactiveForeground": Components.background_foregroundSecondary,
        "tab.inactiveModifiedBorder": Components.backgroundMuted,
        "terminal.ansiBlack": Components.ansiBlack,
        "terminal.ansiBlue": Components.ansiBlue,
        "terminal.ansiBrightBlack": Components.ansiBrightBlack,
        "terminal.ansiBrightBlue": Components.ansiBrightBlue,
        "terminal.ansiBrightCyan": Components.ansiBrightCyan,
        "terminal.ansiBrightGreen": Components.ansiBrightGreen,
        "terminal.ansiBrightMagenta": Components.ansiBrightMagenta,
        "terminal.ansiBrightRed": Components.ansiBrightRed,
        "terminal.ansiBrightWhite": Components.ansiBrightWhite,
        "terminal.ansiBrightYellow": Components.ansiBrightYellow,
        "terminal.ansiCyan": Components.ansiCyan,
        "terminal.ansiGreen": Components.ansiGreen,
        "terminal.ansiMagenta": Components.ansiMagenta,
        "terminal.ansiRed": Components.ansiRed,
        "terminal.ansiWhite": Components.ansiWhite,
        "terminal.ansiYellow": Components.ansiYellow,
        "terminal.foreground": Components.ansiForeground,
        "terminal.selectionBackground": Components.accentHighlightStrong,
        "terminalCursor.foreground": Components.accent,
        "textLink.activeForeground": Components.accent,
        "textLink.foreground": Components.accent,
        "titleBar.activeBackground": Components.background,
        "titleBar.activeForeground": Components.background_foregroundPrimary,
        "titleBar.inactiveBackground": Components.background,
        "titleBar.inactiveForeground": Components.background_foregroundHint,
        "welcomePage.buttonBackground": Components.accent,
        "welcomePage.buttonHoverBackground": Components.accentHighlight,
        "widget.shadow": Components.transparent,
    },
    "tokenColors": [
        {
            "scope": ["comment", "string.quoted.docstring"],
            "settings": {"foreground": Components.background_foregroundHint},
        },
        {
            "scope": ["string"],
            "settings": {"foreground": Components.background_foregroundSecondary},
        },
        {
            "scope": ["punctuation.definition.string", "storage.type.string.python"],
            "settings": {"foreground": Components.background_foregroundPrimary},
        },
        {
            "scope": [
                "beginning.punctuation",
                "entity.name.section.group-title",
                "entity.name.tag",
                "entity.other.attribute-name.class",
                "entity.other.attribute-name.id",
                "keyword.const",
                "keyword.control",
                "keyword.function",
                "keyword.import",
                "keyword.operator.assignment",
                "keyword.operator.comparison",
                "keyword.operator.decrement",
                "keyword.operator.expression",
                "keyword.operator.increment",
                "keyword.operator.increment-decrement",
                "keyword.operator.logical",
                "keyword.operator.misc",
                "keyword.operator.new",
                "keyword.operator.other",
                "keyword.operator.ternary",
                "keyword.other.fn",
                "keyword.other.rust",
                "keyword.other.special-method",
                "keyword.other.where",
                "keyword.package",
                "keyword.type",
                "keyword.var",
                "markup.heading",
                "meta.tag.sgml.doctype.html",
                "punctuation.separator.key-value",
                "storage.modifier",
                "storage.type.class",
                "storage.type.enum",
                "storage.type.function",
                "storage.type.import",
                "storage.type.interface",
                "storage.type.js",
                "storage.type.namespace",
                "storage.type.property",
                "storage.type.rust",
                "storage.type.string.python",
                "storage.type.ts",
                "storage.type.tsx",
                "storage.type.type",
                "support.type.object.module",
            ],
            "settings": {
                "foreground": Components.background_foreground,
                "fontStyle": "bold",
            },
        },
    ],
}
