"""Themes color definitions."""

from build import ColorSplit
from colors import Colors


class Components:
    transparent = ColorSplit(Colors.black).with_alpha(0)

    error = ColorSplit(Colors.red_500, Colors.red_600)

    warning = ColorSplit(Colors.orange_500, Colors.orange_400)
    warning_foreground = Colors.black

    info = ColorSplit(Colors.blue_500, Colors.blue_500)

    accent = ColorSplit(Colors.fuchsia_600, Colors.purple_600)
    accent_foreground = Colors.slate_50
    accentHighlight = accent.with_alpha(0.15, 0.25)
    accentHighlightLight = accent.with_alpha(0.8, 0.8)

    accentMuted = ColorSplit(Colors.fuchsia_700, Colors.purple_500)
    accentMuted_foreground = Colors.slate_50
    accentMutedHighlight = accentMuted.with_alpha(0.15, 0.25)
    accentMutedHighlightLight = accentMuted.with_alpha(0.8, 0.8)

    find = accent
    findHighlight_200 = find.with_alpha(0.1, 0.1)
    findHighlight_300 = find.with_alpha(0.15, 0.15)
    findHighlight_400 = find.with_alpha(0.3, 0.3)
    findHighlight_500 = find.with_alpha(0.45, 0.45)
    findHighlight_600 = find.with_alpha(0.6, 0.6)

    background = ColorSplit(Colors.white, Colors.black)
    background_foreground = ColorSplit(Colors.slate_950, Colors.neutral_50)
    background_foregroundPrimary = ColorSplit(Colors.slate_800, Colors.neutral_300)
    background_foregroundSecondary = ColorSplit(Colors.slate_500, Colors.neutral_500)
    background_foregroundHint = ColorSplit(Colors.slate_400, Colors.neutral_600)
    background_foregroundError = error
    background_foregroundWarning = warning
    background_foregroundInfo = accent
    background_foregroundOrnament = ColorSplit(Colors.slate_300, Colors.neutral_800)

    backgroundMuted = ColorSplit(Colors.neutral_200, Colors.neutral_950)
    backgroundMuted_foreground = background_foreground
    backgroundMuted_foregroundPrimary = background_foregroundPrimary
    backgroundMuted_foregroundSecondary = background_foregroundSecondary
    backgroundMuted_foregroundHint = background_foregroundHint

    backgroundContrast = ColorSplit(Colors.neutral_100, Colors.neutral_700)
    backgroundContrast_foreground = background_foreground
    backgroundContrast_foregroundPrimary = background_foregroundPrimary
    backgroundContrastHighlight = backgroundContrast.with_alpha(0.1)

    backgroundContrastStrong = background.to_reversed()
    backgroundContrastStrong_foreground = background_foreground.to_reversed()
    backgroundContrastStrong_foregroundPrimary = (
        background_foregroundPrimary.to_reversed()
    )
    backgroundContrastStrong_foregroundSecondary = (
        background_foregroundSecondary.to_reversed()
    )
    backgroundContrastStrongHighlight = backgroundContrastStrong.with_alpha(0.3, 0.3)

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

    gitAddedResource = ColorSplit(Colors.green_700)
    gitAddedResourceHighlight = gitAddedResource.with_alpha(0.2, 0.1)
    gitAddedResourceForeground = ColorSplit(Colors.green_700)

    gitConflictingResource = ColorSplit(Colors.blue_600)
    gitConflictingResourceHighlight = gitConflictingResource.with_alpha(0.2, 0.1)
    gitConflictingResourceForeground = ColorSplit(Colors.blue_600)

    gitDeletedResource = ColorSplit(Colors.rose_600)
    gitDeletedResourceHighlight = gitDeletedResource.with_alpha(0.2, 0.1)
    gitDeletedResourceForeground = ColorSplit(Colors.rose_600)

    gitIgnoredResource = ColorSplit(Colors.slate_600)
    gitIgnoredResourceHighlight = gitIgnoredResource.with_alpha(0.2, 0.1)
    gitIgnoredResourceForeground = ColorSplit(Colors.slate_600)

    gitModifiedResource = ColorSplit(Colors.amber_600)
    gitModifiedResourceHighlight = gitModifiedResource.with_alpha(0.2, 0.1)
    gitModifiedResourceForeground = ColorSplit(Colors.amber_600)

    gitStageDeletedResource = gitConflictingResource
    gitStageDeletedResourceHighlight = gitStageDeletedResource.with_alpha(0.2, 0.1)
    gitStageDeletedResourceForeground = gitConflictingResourceForeground

    gitStageModifiedResource = gitModifiedResource
    gitStageModifiedResourceHighlight = gitStageModifiedResource.with_alpha(0.2, 0.1)
    gitStageModifiedResourceForeground = gitModifiedResourceForeground

    gitSubmoduleResource = ColorSplit(Colors.blue_500)
    gitSubmoduleResourceHighlight = gitSubmoduleResource.with_alpha(0.2, 0.1)
    gitSubmoduleResourceForeground = ColorSplit(Colors.blue_500)

    gitUntrackedResource = ColorSplit(Colors.green_500)
    gitUntrackedResourceHighlight = gitUntrackedResource.with_alpha(0.2, 0.1)
    gitUntrackedResourceForeground = ColorSplit(Colors.green_500)

    todo = Colors.pink_300
    todo2 = Colors.purple_500


definitions = {
    "name": "Day 'n' Nite",
    "colors": {
        # General
        "foreground": Components.background_foregroundPrimary,
        "focusBorder": Components.background_foregroundOrnament,
        "progressBar.background": Components.backgroundContrastStrong,
        "selection.background": Components.accentHighlight,
        "scrollbar.shadow": Components.backgroundMuted,
        # Activity Bar
        "activityBar.foreground": Components.backgroundContrast_foregroundPrimary,
        "activityBar.background": Components.background,
        "activityBar.inactiveForeground": Components.background_foregroundHint,
        "activityBarBadge.foreground": Components.backgroundContrastStrong_foregroundPrimary,
        "activityBarBadge.background": Components.backgroundContrastStrong,
        "activityBar.border": Components.transparent,
        "activityBar.activeBackground": Components.backgroundContrast,
        # Side Bar
        "sideBar.background": Components.background,
        "sideBar.foreground": Components.background_foregroundPrimary,
        "sideBarSectionHeader.background": Components.backgroundContrast,
        "sideBarSectionHeader.foreground": Components.backgroundContrast_foregroundPrimary,
        "sideBarSectionHeader.border": Components.transparent,
        "sideBarTitle.foreground": Components.background_foregroundHint,
        "sideBar.border": Components.transparent,
        "list.inactiveSelectionBackground": Components.backgroundMuted,
        "list.inactiveSelectionForeground": Components.backgroundMuted_foregroundPrimary,
        "list.hoverBackground": Components.backgroundContrast,
        "list.hoverForeground": Components.backgroundContrast_foregroundPrimary,
        "list.activeSelectionBackground": Components.backgroundContrastStrong,
        "list.activeSelectionForeground": Components.backgroundContrastStrong_foregroundPrimary,
        "tree.indentGuidesStroke": Components.background_foregroundOrnament,
        "list.dropBackground": Components.backgroundContrast,
        "list.highlightForeground": Components.background_foreground,
        "list.focusBackground": Components.backgroundContrast,
        "list.focusForeground": Components.backgroundContrast_foregroundPrimary,
        "listFilterWidget.background": Components.backgroundContrast,
        "listFilterWidget.outline": Components.transparent,
        "listFilterWidget.noMatchesOutline": Components.error,
        # Status Bar
        "statusBar.foreground": Components.background_foregroundPrimary,
        "statusBar.background": Components.background,
        "statusBarItem.hoverBackground": Components.backgroundContrast,
        "statusBar.border": "default",
        "statusBar.debuggingBackground": Components.warning,
        "statusBar.debuggingForeground": Components.warning_foreground,
        "statusBar.debuggingBorder": "default",
        "statusBar.noFolderBackground": Components.accent,
        "statusBar.noFolderForeground": Components.accent_foreground,
        "statusBar.noFolderBorder": "default",
        "statusBarItem.remoteBackground": Components.accent,
        "statusBarItem.remoteForeground": Components.accent_foreground,
        # Title Bar
        "titleBar.activeBackground": Components.background,
        "titleBar.activeForeground": Components.background_foregroundPrimary,
        "titleBar.border": Components.transparent,
        "titleBar.inactiveBackground": Components.backgroundMuted,
        "titleBar.inactiveForeground": Components.backgroundMuted_foregroundPrimary,
        "menubar.selectionForeground": Components.backgroundContrast_foregroundPrimary,
        "menubar.selectionBackground": Components.backgroundContrast,
        "menubar.selectionBorder": "default",
        "menu.foreground": Components.background_foregroundPrimary,
        "menu.background": Components.background,
        "menu.selectionForeground": Components.backgroundContrastStrong_foregroundPrimary,
        "menu.selectionBackground": Components.backgroundContrastStrong,
        "menu.selectionBorder": Components.transparent,
        "menu.separatorBackground": Components.background_foregroundOrnament,
        "menu.border": Components.backgroundMuted,
        # Buttons
        "button.background": Components.accent,
        "button.foreground": Components.accent_foreground,
        "button.hoverBackground": Components.accentHighlightLight,
        "textLink.foreground": Components.accent,
        "button.secondaryForeground": Components.accentMuted,
        "button.secondaryBackground": Components.accentMuted_foreground,
        "button.secondaryHoverBackground": Components.accentMutedHighlightLight,
        # Inputs
        "input.background": Components.backgroundMuted,
        "input.border": Components.transparent,
        "input.foreground": Components.backgroundMuted_foreground,
        "input.placeholderForeground": Components.backgroundMuted_foregroundHint,
        "inputOption.activeBackground": Components.backgroundContrast,
        "inputOption.activeBorder": Components.transparent,
        "inputOption.activeForeground": Components.backgroundContrast_foreground,
        # Panel (Terminal)
        "panel.background": Components.background,
        "panel.border": Components.backgroundMuted,
        "panelTitle.activeBorder": Components.backgroundContrastStrong,
        "panelTitle.activeForeground": Components.background_foregroundPrimary,
        "panelTitle.inactiveForeground": Components.background_foregroundSecondary,
        "terminal.selectionBackground": Components.accentHighlight,
        "terminalCursor.foreground": Components.backgroundContrastStrong_foreground,
        "terminalCursor.background": Components.backgroundContrastStrong,
        "badge.background": Components.backgroundContrastStrong,
        "badge.foreground": Components.backgroundContrastStrong_foreground,
        "terminal.border": Components.backgroundMuted,
        # Terminal Text
        "terminal.foreground": Components.background,
        "terminal.ansiWhite": Components.ansiWhite,
        "terminal.ansiBrightWhite": Components.ansiBrightWhite,
        "terminal.ansiBlack": Components.ansiBlack,
        "terminal.ansiBrightBlack": Components.ansiBrightBlack,
        "terminal.ansiBlue": Components.ansiBlue,
        "terminal.ansiBrightBlue": Components.ansiBrightBlue,
        "terminal.ansiCyan": Components.ansiCyan,
        "terminal.ansiBrightCyan": Components.ansiBrightCyan,
        "terminal.ansiGreen": Components.ansiGreen,
        "terminal.ansiBrightGreen": Components.ansiBrightGreen,
        "terminal.ansiMagenta": Components.ansiMagenta,
        "terminal.ansiBrightMagenta": Components.ansiBrightMagenta,
        "terminal.ansiRed": Components.ansiRed,
        "terminal.ansiBrightRed": Components.ansiBrightRed,
        "terminal.ansiYellow": Components.ansiYellow,
        "terminal.ansiBrightYellow": Components.ansiBrightYellow,
        # Tabs
        "editorGroupHeader.tabsBackground": Components.background,
        "editorGroupHeader.tabsBorder": Components.transparent,
        "tab.activeForeground": Components.backgroundContrastStrong_foreground,
        "tab.border": Components.transparent,
        "tab.activeBackground": Components.backgroundContrastStrong,
        "tab.activeBorder": Components.transparent,
        "tab.activeBorderTop": Components.transparent,
        "tab.inactiveBackground": Components.background,
        "tab.inactiveForeground": Components.background_foregroundSecondary,
        "tab.hoverBackground": Components.backgroundContrast,
        "tab.hoverForeground": Components.backgroundContrast_foregroundPrimary,
        "tab.hoverBorder": Components.transparent,
        # Breadcrumbs
        "breadcrumb.background": Components.background,
        "breadcrumb.foreground": Components.background_foregroundHint,
        "breadcrumb.focusForeground": Components.background_foregroundPrimary,
        "editorGroupHeader.border": Components.transparent,
        # Symbol icons
        "symbolIcon.arrayForeground": Components.background_foregroundSecondary,
        "symbolIcon.booleanForeground": Components.background_foregroundSecondary,
        "symbolIcon.classForeground": Components.background_foregroundSecondary,
        "symbolIcon.colorForeground": Components.background_foregroundSecondary,
        "symbolIcon.constantForeground": Components.background_foregroundSecondary,
        "symbolIcon.constructorForeground": Components.background_foregroundSecondary,
        "symbolIcon.enumeratorForeground": Components.background_foregroundSecondary,
        "symbolIcon.enumeratorMemberForeground": Components.background_foregroundSecondary,
        "symbolIcon.eventForeground": Components.background_foregroundSecondary,
        "symbolIcon.fieldForeground": Components.background_foregroundSecondary,
        "symbolIcon.fileForeground": Components.background_foregroundSecondary,
        "symbolIcon.folderForeground": Components.background_foregroundSecondary,
        "symbolIcon.functionForeground": Components.background_foregroundSecondary,
        "symbolIcon.interfaceForeground": Components.background_foregroundSecondary,
        "symbolIcon.keyForeground": Components.background_foregroundSecondary,
        "symbolIcon.keywordForeground": Components.background_foregroundSecondary,
        "symbolIcon.methodForeground": Components.background_foregroundSecondary,
        "symbolIcon.moduleForeground": Components.background_foregroundSecondary,
        "symbolIcon.namespaceForeground": Components.background_foregroundSecondary,
        "symbolIcon.nullForeground": Components.background_foregroundSecondary,
        "symbolIcon.numberForeground": Components.background_foregroundSecondary,
        "symbolIcon.objectForeground": Components.background_foregroundSecondary,
        "symbolIcon.operatorForeground": Components.background_foregroundSecondary,
        "symbolIcon.packageForeground": Components.background_foregroundSecondary,
        "symbolIcon.propertyForeground": Components.background_foregroundSecondary,
        "symbolIcon.referenceForeground": Components.background_foregroundSecondary,
        "symbolIcon.snippetForeground": Components.background_foregroundSecondary,
        "symbolIcon.stringForeground": Components.background_foregroundSecondary,
        "symbolIcon.structForeground": Components.background_foregroundSecondary,
        "symbolIcon.textForeground": Components.background_foregroundSecondary,
        "symbolIcon.typeParameterForeground": Components.background_foregroundSecondary,
        "symbolIcon.unitForeground": Components.background_foregroundSecondary,
        "symbolIcon.variableForeground": Components.background_foregroundSecondary,
        # Scrollbar
        "scrollbarSlider.background": Components.backgroundMuted,
        "scrollbarSlider.hoverBackground": Components.backgroundContrast,
        "scrollbarSlider.activeBackground": Components.backgroundContrastStrong,
        # Widgets
        "widget.shadow": Components.backgroundContrast,
        "editorWidget.foreground": Components.background_foregroundPrimary,
        "editorWidget.background": Components.background,
        "pickerGroup.border": Components.transparent,
        "pickerGroup.foreground": Components.accent,
        "editorWidget.resizeBorder": Components.accent,
        "debugToolBar.background": Components.backgroundContrast,
        "debugToolBar.border": Components.backgroundMuted,
        # Notifications
        "notifications.foreground": Components.background_foreground,
        "notifications.background": Components.background,
        "notificationToast.border": Components.backgroundMuted,
        "notificationsErrorIcon.foreground": Components.background_foregroundError,
        "notificationsWarningIcon.foreground": Components.background_foregroundWarning,
        "notificationsInfoIcon.foreground": Components.background_foregroundInfo,
        "notificationCenterHeader.foreground": Components.background_foreground,
        "notificationCenterHeader.background": Components.background,
        "notifications.border": Components.background_foregroundOrnament,
        "notificationCenter.border": Components.backgroundMuted,
        # Git Decorations
        "gitDecoration.addedResourceForeground": Components.gitAddedResourceForeground,
        "gitDecoration.conflictingResourceForeground": Components.gitConflictingResourceForeground,
        "gitDecoration.deletedResourceForeground": Components.gitDeletedResourceForeground,
        "gitDecoration.ignoredResourceForeground": Components.gitIgnoredResourceForeground,
        "gitDecoration.modifiedResourceForeground": Components.gitModifiedResourceForeground,
        "gitDecoration.stageDeletedResourceForeground": Components.gitStageDeletedResourceForeground,
        "gitDecoration.stageModifiedResourceForeground": Components.gitStageModifiedResourceForeground,
        "gitDecoration.submoduleResourceForeground": Components.gitSubmoduleResourceForeground,
        "gitDecoration.untrackedResourceForeground": Components.gitUntrackedResourceForeground,
        # Editor
        "editor.background": Components.background,
        "editorLineNumber.foreground": Components.background_foregroundHint,
        "editorLineNumber.activeForeground": Components.background_foregroundPrimary,
        "editorCursor.foreground": Components.background_foreground,
        "editorCursor.background": Components.backgroundContrast,
        "editor.selectionBackground": Components.findHighlight_400,
        "editor.inactiveSelectionBackground": Components.findHighlight_200,
        "editorWhitespace.foreground": Components.background_foregroundOrnament,
        "editor.selectionHighlightBackground": Components.findHighlight_500,
        "editor.selectionHighlightBorder": Components.transparent,
        "editor.findMatchBackground": Components.findHighlight_600,
        "editor.findMatchBorder": Components.transparent,
        "editor.findMatchHighlightBackground": Components.findHighlight_400,
        "editor.findMatchHighlightBorder": Components.transparent,
        "editor.findRangeHighlightBackground": Components.findHighlight_300,
        "editor.findRangeHighlightBorder": Components.transparent,
        "editor.rangeHighlightBackground": Components.findHighlight_500,
        "editor.rangeHighlightBorder": Components.accentHighlight,
        "editor.hoverHighlightBackground": Components.findHighlight_200,
        "editor.wordHighlightStrongBackground": Components.findHighlight_400,
        "editor.wordHighlightStrongBorder": Components.transparent,
        "editor.wordHighlightBackground": Components.findHighlight_300,
        "editor.wordHighlightBorder": Components.transparent,
        "editor.lineHighlightBackground": Components.backgroundMuted,
        "editor.lineHighlightBorder": Components.transparent,
        "editorLink.activeForeground": Components.find,
        "editorIndentGuide.background": Components.background_foregroundOrnament,
        "editorIndentGuide.activeBackground": Components.background_foregroundHint,
        "editorRuler.foreground": Components.background_foregroundOrnament,
        "editorBracketMatch.background": Components.findHighlight_400,
        "editorBracketMatch.border": Components.transparent,
        "editor.foldBackground": Components.backgroundMuted,
        "editorOverviewRuler.background": Components.transparent,
        "editorOverviewRuler.border": Components.background_foregroundOrnament,
        "editorError.foreground": Components.background_foregroundError,
        "editorError.background": Components.transparent,
        "editorError.border": Components.transparent,
        "editorWarning.foreground": Components.background_foregroundWarning,
        "editorWarning.background": Components.transparent,
        "editorWarning.border": Components.transparent,
        "editorInfo.foreground": Components.background_foregroundInfo,
        "editorInfo.background": Components.transparent,
        "editorInfo.border": Components.transparent,
        "editorGutter.background": Components.background,
        "editorGutter.modifiedBackground": Components.gitModifiedResource,
        "editorGutter.addedBackground": Components.gitAddedResource,
        "editorGutter.deletedBackground": Components.gitDeletedResource,
        "editorGutter.foldingControlForeground": Components.background_foregroundSecondary,
        "editorCodeLens.foreground": Components.background_foregroundHint,
        "editorGroup.border": Components.backgroundMuted,
        # Diff Editor
        "diffEditor.insertedTextBackground": Components.gitAddedResourceHighlight,
        "diffEditor.insertedTextBorder": "default",
        "diffEditor.removedTextBackground": Components.gitDeletedResourceHighlight,
        "diffEditor.removedTextBorder": "default",
        "diffEditor.border": Components.backgroundMuted,
        # Marker Navigation
        "editorMarkerNavigation.background": Components.background,
        "editorMarkerNavigationError.background": Components.error,
        "editorMarkerNavigationWarning.background": Components.warning,
        "editorMarkerNavigationInfo.background": Components.info,
        # Merge Conflicts
        "merge.currentHeaderBackground": Components.gitAddedResource,
        "merge.currentContentBackground": Components.gitAddedResourceHighlight,
        "merge.incomingHeaderBackground": Components.gitConflictingResource,
        "merge.incomingContentBackground": Components.gitConflictingResourceHighlight,
        "merge.commonHeaderBackground": Components.gitUntrackedResource,
        "merge.commonContentBackground": Components.gitUntrackedResourceHighlight,
        # Suggest Widget
        "editorSuggestWidget.background": Components.background,
        "editorSuggestWidget.border": Components.backgroundMuted,
        "editorSuggestWidget.foreground": Components.background_foregroundSecondary,
        "editorSuggestWidget.highlightForeground": Components.background_foreground,
        "editorSuggestWidget.focusHighlightForeground": Components.backgroundContrastStrong_foregroundSecondary,
        "editorSuggestWidget.selectedBackground": Components.backgroundContrastStrong,
        "editorSuggestWidget.selectedForeground": Components.backgroundContrastStrong_foregroundPrimary,
        "editorSuggestWidget.selectedIconForeground": Components.backgroundContrastStrong_foregroundPrimary,
        # Hover Widget
        "editorHoverWidget.foreground": Components.background_foregroundPrimary,
        "editorHoverWidget.background": Components.background,
        "editorHoverWidget.border": Components.backgroundMuted,
        # Peek View Editor
        "peekView.border": Components.backgroundMuted,
        "peekViewEditor.background": Components.background,
        "peekViewEditorGutter.background": Components.background,
        "peekViewEditor.matchHighlightBackground": Components.findHighlight_300,
        "peekViewEditor.matchHighlightBorder": Components.transparent,
        "peekViewResult.background": Components.background,
        "peekViewResult.fileForeground": Components.background_foregroundPrimary,
        "peekViewResult.lineForeground": Components.background_foreground,
        "peekViewResult.matchHighlightBackground": Components.findHighlight_300,
        "peekViewResult.selectionBackground": Components.backgroundContrast,
        "peekViewResult.selectionForeground": Components.backgroundContrast_foregroundPrimary,
        "peekViewTitle.background": Components.background,
        "peekViewTitleDescription.foreground": Components.background_foregroundSecondary,
        "peekViewTitleLabel.foreground": Components.background_foreground,
    },
    "semanticHighlighting": "true",
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
                "foreground": Components.background_foregroundPrimary,
                "fontStyle": "bold",
            },
        },
    ],
}
