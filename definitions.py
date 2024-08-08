"""Themes color definitions."""

from build import ColorSplit

# Colors layer 1

colorNone = ColorSplit("#000000").set_alpha(0)
colorWhite = ColorSplit("#ffffff")
colorBlack = ColorSplit("#000000")

colorGray_25 = ColorSplit("#f0f0f0")
colorGray_50 = ColorSplit("#dedede")
colorGray_100 = ColorSplit("#1e1d27")
colorGray_150 = ColorSplit("#9e9e9e")
colorGray_200 = ColorSplit("#999999")
colorGray_300 = ColorSplit("#616161")
colorGray_350 = ColorSplit("#666666")
colorGray_400 = ColorSplit("#2e2e37")
colorGray_500 = ColorSplit("#a8a8b1")
colorGray_600 = ColorSplit("#212121")
colorGray_700 = ColorSplit("#1d1d1d")

# TODO:
colorGray_400OnBlack = ColorSplit("#65696e", colorGray_400)

colorPurple = ColorSplit("#7d46fc")
colorBlue = ColorSplit("#004bff")
colorCyan = ColorSplit("#00d2ff")
colorGreen = ColorSplit("#00ff68")
colorYellow = ColorSplit("#ffca00")
colorOrange = ColorSplit("#ff9900")
colorRed = ColorSplit("#ff0032")

# Colors layer 2

colorBackground = ColorSplit(colorWhite, colorBlack)
colorBackground_foreground = ColorSplit(colorGray_600, colorGray_50)
colorBackground_foregroundSecondary = ColorSplit(colorGray_350, colorGray_200)
colorBackground_foregroundHint = ColorSplit(colorGray_150, colorGray_300)

colorBackgroundNegative = ColorSplit(colorBlack, colorWhite)
colorBackgroundNegative_foreground = ColorSplit(colorGray_50, colorGray_600)
colorBackgroundNegative_foregroundSecondary = ColorSplit(colorGray_200, colorGray_350)
colorBackgroundNegative_foregroundHint = ColorSplit(colorGray_300, colorGray_150)

colorBackgroundContrast = ColorSplit(colorGray_25, colorGray_700)
colorBackgroundContrast_foreground = ColorSplit(colorGray_700, colorGray_150)

colorBackgroundContrastTransparent = ColorSplit(colorBlack, colorWhite).set_alpha(0.1)

colorPrimary = ColorSplit(colorBlue, colorPurple)
colorPrimaryNegative = colorWhite
colorPrimaryHighlight = ColorSplit("#0064ff", colorPrimary).set_alpha(0.15, 0.25)
colorPrimaryHighlightStrong = colorPrimaryHighlight.with_alpha(0.3, 0.5)
colorPrimaryHighlightLight = colorPrimaryHighlight.with_alpha(0.05, 0.08)

colorAdded = colorGreen
colorAddedHighlight = colorAdded.with_alpha(0.1, 0.2)
colorDeleted = colorRed
colorDeletedHighlight = colorDeleted.with_alpha(0.1, 0.2)

colorError = colorRed

colorWarning = colorOrange
colorWarning_foreground = colorBlack

colorFind = colorYellow.with_alpha(0.6)
colorFindHighlight = colorFind.with_alpha(0.3)

colorStackFocused = colorOrange.with_alpha(0.6)
colorStack = colorOrange.with_alpha(0.3)

colorBorder = ColorSplit(colorGray_300, colorGray_100)

# Theme definitions

definitions = {
    "colors": {
        "activityBar.background": colorBackground,
        "activityBar.border": colorNone,
        "activityBar.foreground": colorBackground_foregroundSecondary,
        "activityBarBadge.background": colorBackgroundContrast,
        "activityBarBadge.foreground": colorBackgroundContrast_foreground,
        "badge.background": colorBackgroundNegative,
        "badge.foreground": colorBackgroundNegative_foreground,
        "button.background": colorPrimary,
        "button.foreground": colorPrimaryNegative,
        "contrastBorder": colorNone,
        "debugToolBar.background": colorBackgroundContrast,
        "diffEditor.insertedTextBackground": colorAddedHighlight,
        "diffEditor.removedTextBackground": colorDeletedHighlight,
        "dropdown.background": colorBackgroundContrast,
        "dropdown.border": colorBorder,
        "dropdown.foreground": colorBackground_foreground,
        "editor.background": colorBackground,
        "editor.findMatchBackground": colorFind,
        "editor.findMatchHighlightBackground": colorFindHighlight,
        "editor.focusedStackFrameHighlightBackground": colorStackFocused,
        "editor.foreground": colorBackground_foreground,
        "editor.lineHighlightBackground": colorPrimaryHighlightLight,
        "editor.lineHighlightBorder": colorNone,
        "editor.selectionBackground": colorPrimaryHighlightStrong,
        "editor.selectionForeground": colorBackground_foreground,
        "editor.selectionHighlightBorder": ColorSplit(colorNone, colorPrimaryHighlight),
        "editor.stackFrameHighlightBackground": colorStack,
        "editor.wordHighlightBackground": colorPrimaryHighlight,
        "editor.wordHighlightStrongBackground": colorPrimaryHighlightStrong,
        "editorBracketMatch.background": colorPrimaryHighlightStrong,
        "editorBracketMatch.border": colorNone,
        "editorCursor.foreground": colorPrimary,
        "editorError.foreground": colorError,
        "editorGroup.border": colorBackgroundContrast,
        "editorGroupHeader.tabsBackground": colorBackground,
        "editorGroupHeader.tabsBorder": colorNone,
        "editorGutter.addedBackground": colorAdded,
        "editorGutter.deletedBackground": colorDeleted,
        "editorGutter.modifiedBackground": colorBackgroundNegative,
        "editorIndentGuide.background": colorBackgroundContrast,
        "editorLineNumber.activeForeground": colorBackground_foregroundSecondary,
        "editorLineNumber.foreground": ColorSplit("#ebf0f5", colorGray_100),
        "editorLink.activeForeground": colorPrimary,
        "editorOverviewRuler.addedForeground": colorNone,
        "editorOverviewRuler.border": colorNone,
        "editorOverviewRuler.bracketMatchForeground": colorPrimaryHighlightStrong,
        "editorOverviewRuler.errorForeground": colorError,
        "editorOverviewRuler.findMatchForeground": colorFind,
        "editorOverviewRuler.modifiedForeground": colorBackground_foreground,
        "editorOverviewRuler.selectionHighlightForeground": colorPrimaryHighlightStrong,
        "editorOverviewRuler.warningForeground": colorWarning,
        "editorOverviewRuler.wordHighlightForeground": colorPrimaryHighlight,
        "editorOverviewRuler.wordHighlightStrongForeground": colorPrimaryHighlightStrong,
        "editorRuler.foreground": colorBackgroundContrast,
        "editorSuggestWidget.foreground": colorBackground_foreground,
        "editorWarning.foreground": colorWarning,
        "editorWidget.background": colorBackgroundContrast,
        "editorWidget.border": colorBorder,
        "errorForeground": colorError,
        "extensionButton.prominentBackground": colorPrimary,
        "extensionButton.prominentForeground": colorPrimaryNegative,
        "extensionButton.prominentHoverBackground": colorPrimary,
        "focusBorder": colorBorder,
        "foreground": colorBackground_foreground,
        "gitDecoration.ignoredResourceForeground": colorBackground_foregroundSecondary,
        "gitDecoration.modifiedResourceForeground": colorBackground_foreground,
        "gitDecoration.untrackedResourceForeground": colorBackground_foreground,
        "input.background": colorBackgroundContrast,
        "input.border": colorBorder,
        "input.foreground": colorBackgroundContrast_foreground,
        "input.placeholderForeground": colorBackgroundNegative_foregroundHint,
        "inputOption.activeBackground": colorBackgroundContrast,
        "inputOption.activeBorder": colorBackgroundContrast_foreground,
        "inputOption.activeForeground": colorBackgroundContrast_foreground,
        "list.activeSelectionBackground": colorBackgroundNegative,
        "list.activeSelectionForeground": colorBackgroundNegative_foreground,
        "list.dropBackground": colorPrimaryHighlightStrong,
        "list.focusBackground": colorPrimaryHighlight,
        "list.focusForeground": colorBackgroundNegative,
        "list.highlightForeground": colorBackgroundNegative,
        "list.hoverBackground": colorBackgroundContrast,
        "list.inactiveSelectionBackground": colorBackgroundContrast,
        "list.inactiveSelectionForeground": colorBackgroundNegative,
        "panel.background": colorBackgroundContrast,
        "panel.border": colorNone,
        "panelTitle.activeBorder": colorBackground_foregroundSecondary,
        "peekView.border": colorBackgroundNegative,
        "peekViewEditor.background": colorNone,
        "peekViewEditor.matchHighlightBackground": colorFind,
        "peekViewResult.background": colorNone,
        "peekViewResult.fileForeground": colorBackgroundNegative_foregroundSecondary,
        "peekViewResult.lineForeground": colorBackgroundNegative_foregroundSecondary,
        "peekViewResult.matchHighlightBackground": colorFind,
        "peekViewResult.selectionBackground": colorBackgroundNegative,
        "peekViewResult.selectionForeground": colorBackground_foreground,
        "peekViewTitle.background": colorNone,
        "peekViewTitleDescription.foreground": colorBackground_foregroundSecondary,
        "peekViewTitleLabel.foreground": colorBackgroundNegative,
        "progressBar.background": colorPrimary,
        "scrollbar.shadow": colorNone,
        "scrollbarSlider.background": colorBackgroundContrastTransparent,
        "scrollbarSlider.hoverBackground": colorBackgroundNegative,
        "sideBar.background": colorBackground,
        "sideBar.foreground": colorBackground_foreground,
        "sideBarSectionHeader.background": colorBackgroundContrast,
        "sideBarSectionHeader.foreground": colorBackgroundContrast_foreground,
        "sideBarTitle.foreground": colorBackground_foreground,
        "statusBar.background": colorBackground,
        "statusBar.debuggingBackground": colorWarning,
        "statusBar.debuggingForeground": colorWarning_foreground,
        "statusBar.foreground": colorBackground_foreground,
        "statusBar.noFolderBackground": colorBackground,
        "tab.activeBackground": colorBackgroundNegative,
        "tab.activeForeground": colorBackground,
        "tab.activeModifiedBorder": colorNone,
        "tab.border": colorNone,
        "tab.inactiveBackground": colorNone,
        "tab.inactiveForeground": colorBackground_foregroundSecondary,
        "tab.inactiveModifiedBorder": colorBackgroundNegative,
        "terminal.ansiBlack": colorBackgroundNegative,
        "terminal.ansiBlue": colorBlue,
        "terminal.ansiBrightBlack": colorBackgroundNegative,
        "terminal.ansiBrightBlue": colorBlue,
        "terminal.ansiBrightCyan": colorCyan,
        "terminal.ansiBrightGreen": colorGreen,
        "terminal.ansiBrightMagenta": colorPurple,
        "terminal.ansiBrightRed": colorRed,
        "terminal.ansiBrightWhite": colorWhite,
        "terminal.ansiBrightYellow": colorYellow,
        "terminal.ansiCyan": colorCyan,
        "terminal.ansiGreen": colorGreen,
        "terminal.ansiMagenta": colorPurple,
        "terminal.ansiRed": colorRed,
        "terminal.ansiWhite": colorWhite,
        "terminal.ansiYellow": colorYellow,
        "terminal.foreground": colorBackgroundNegative,
        "terminal.selectionBackground": colorPrimaryHighlightStrong,
        "terminalCursor.foreground": colorPrimary,
        "textLink.activeForeground": colorPrimary,
        "textLink.foreground": colorPrimary,
        "titleBar.activeBackground": colorBackground,
        "titleBar.activeForeground": colorGray_500,
        "titleBar.inactiveBackground": colorBackground,
        "titleBar.inactiveForeground": colorBackground_foregroundSecondary,
        "welcomePage.buttonBackground": colorBackgroundContrast,
        "welcomePage.buttonHoverBackground": colorPrimaryHighlight,
        "widget.shadow": colorNone,
    },
    "tokenColors": [
        {
            "scope": ["comment", "string.quoted.docstring"],
            "settings": {"foreground": colorBackground_foregroundSecondary},
        },
        {"scope": ["string"], "settings": {"foreground": colorGray_500}},
        {
            "scope": ["punctuation.definition.string", "storage.type.string.python"],
            "settings": {"foreground": colorBackgroundNegative},
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
            "settings": {"fontStyle": "bold"},
        },
    ],
}
