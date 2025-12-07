import flet as ft
import math
import asyncio
import random
from flashcard_data import FLASHCARD_DATA
from grammar_data import GRAMMAR_DATA

# Combine both datasets
ALL_DATA = {**FLASHCARD_DATA, **GRAMMAR_DATA}


def main(page: ft.Page):
    # App Configuration
    page.title = "Japanese Flashcards"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window_width = 400
    page.window_height = 800

    # --- State Variables ---
    current_deck_key = "hiragana"
    current_index = 0
    is_flipped = False

    # --- Helper Functions ---
    def get_current_card():
        deck = ALL_DATA.get(current_deck_key, [])
        if not deck:
            return {"front": "?", "back": "Error", "reading": "", "romaji": "", "type": "Error"}
        return deck[current_index]

    def create_front_face(card):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Text(card["type"], color="red500", size=12, weight="bold"),
                        bgcolor="red50", padding=5, border_radius=10
                    ),
                    # Dynamic Font Size: Smaller if text is long (common in grammar cards)
                    ft.Text(
                        card["front"],
                        size=60 if len(card["front"]) < 5 else 40,
                        weight="bold",
                        color="slate900",
                        text_align=ft.TextAlign.CENTER
                    ),
                    # Reading/Furigana on the front
                    ft.Text(card["reading"], size=20, color="slate500", weight="w500"),
                    ft.Container(height=10),
                    ft.Text("Tap to flip", color="slate400", size=12),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="white",
            border_radius=20,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=15, color="#1A000000"),
            border=ft.border.all(1, "slate100"),
            width=300,
            height=400,
            padding=20  # Added padding for long grammar text
        )

    def create_back_face(card):
        # We build the reading section dynamically
        reading_controls = []

        # If it's a Grammar Card, the layout handles specific grammar fields
        if "type" in card and "Grammar" in card["type"]:
            # 1. Meaning (Primary)
            reading_controls.extend([
                ft.Text("Meaning", color="slate400", size=12),
                ft.Text(card["back"], size=20, weight="bold", color="slate900", text_align=ft.TextAlign.CENTER),
            ])

            # 2. Formation / Connection (NEW: "What changes/What's the particle")
            if "connection" in card and card["connection"]:
                reading_controls.extend([
                    ft.Container(height=15),
                    ft.Text("Formation", color="slate400", size=12),
                    ft.Container(
                        content=ft.Text(card["connection"], size=14, color="indigo700", weight="w600",
                                        text_align=ft.TextAlign.CENTER),
                        bgcolor="indigo50", padding=8, border_radius=8, width=260
                    )
                ])

            # 3. Usage / Explanation (NEW: "How to use")
            if "usage" in card and card["usage"]:
                reading_controls.extend([
                    ft.Container(height=15),
                    ft.Text("Usage", color="slate400", size=12),
                    ft.Text(card["usage"], size=14, color="slate700", text_align=ft.TextAlign.CENTER),
                ])

            # Separator
            reading_controls.append(
                ft.Container(height=2, width=40, bgcolor="indigo500", margin=ft.margin.symmetric(vertical=20))
            )

            # 4. Example Sentence
            if "example" in card:
                reading_controls.extend([
                    ft.Text("Example", color="slate400", size=12),
                    ft.Text(card["example"], size=16, color="slate900", text_align=ft.TextAlign.CENTER, weight="w500"),
                    ft.Container(height=5),
                    ft.Text(card["meaning"], size=14, color="slate500", italic=True, text_align=ft.TextAlign.CENTER),
                ])

        else:
            # Standard Flashcard Layout (Kanji/Kana)
            reading_controls.extend([
                ft.Text("Reading", color="slate400", size=12),
                ft.Text(card["reading"], size=24, weight="bold", color="slate900"),
            ])

            if "romaji" in card and card["romaji"]:
                reading_controls.append(
                    ft.Text(card["romaji"], size=16, color="slate500")
                )

            reading_controls.append(
                ft.Container(height=2, width=40, bgcolor="indigo500", margin=ft.margin.symmetric(vertical=20))
            )

            reading_controls.extend([
                ft.Text("Meaning", color="slate400", size=12),
                ft.Text(card["back"], size=20, weight="bold", color="slate900"),
            ])

        return ft.Container(
            content=ft.Column(
                reading_controls,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO  # Crucial for scrolling long grammar explanations
            ),
            bgcolor="white",
            border_radius=20,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=15, color="#1A000000"),
            border=ft.border.all(1, "slate100"),
            width=300,
            height=400,
            padding=20
        )

    # --- UI Components ---

    # Inner content holder (swaps between front/back widgets)
    card_content = ft.Container(
        content=create_front_face(get_current_card()),
        alignment=ft.alignment.center,
    )

    # Outer container that handles the animation
    card_container = ft.Container(
        content=card_content,
        width=300,
        height=400,
        scale=ft.Scale(scale_x=1, scale_y=1),
        animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_IN_OUT),
        alignment=ft.alignment.center,
    )

    progress_text = ft.Text(
        f"Card 1 of {len(ALL_DATA['hiragana'])}",
        color="slate400"
    )

    # --- Event Handlers (Async for Animation Timing) ---

    def update_text_ui():
        """Refreshes the progress text only."""
        total_cards = len(ALL_DATA.get(current_deck_key, []))
        progress_text.value = f"Card {current_index + 1} of {total_cards}"
        progress_text.update()

    async def flip_card(e):
        nonlocal is_flipped

        # 1. Scale Width to 0
        card_container.scale = ft.Scale(scale_x=0, scale_y=1)
        card_container.update()

        # Wait for animation
        await asyncio.sleep(0.4)

        # 2. Swap Content
        is_flipped = not is_flipped
        card = get_current_card()
        if is_flipped:
            card_content.content = create_back_face(card)
        else:
            card_content.content = create_front_face(card)
        card_content.update()

        # 3. Scale Width back to 1
        card_container.scale = ft.Scale(scale_x=1, scale_y=1)
        card_container.update()

    async def next_card(e):
        nonlocal current_index, is_flipped

        if is_flipped:
            is_flipped = False
            card_container.scale = ft.Scale(scale_x=1, scale_y=1)
            card_container.update()

        deck_len = len(ALL_DATA.get(current_deck_key, []))
        if deck_len > 0:
            current_index = (current_index + 1) % deck_len

        card = get_current_card()
        card_content.content = create_front_face(card)
        card_content.update()
        update_text_ui()

    async def prev_card(e):
        nonlocal current_index, is_flipped

        if is_flipped:
            is_flipped = False
            card_container.scale = ft.Scale(scale_x=1, scale_y=1)
            card_container.update()

        deck_len = len(ALL_DATA.get(current_deck_key, []))
        if deck_len > 0:
            current_index = (current_index - 1) % deck_len

        card = get_current_card()
        card_content.content = create_front_face(card)
        card_content.update()
        update_text_ui()

    def shuffle_deck(e):
        nonlocal current_index, is_flipped

        if current_deck_key in ALL_DATA:
            random.shuffle(ALL_DATA[current_deck_key])

        current_index = 0
        is_flipped = False
        card_container.scale = ft.Scale(scale_x=1, scale_y=1)

        card = get_current_card()
        card_content.content = create_front_face(card)

        page.update()
        update_text_ui()

    async def on_rail_change(e):
        nonlocal current_deck_key, current_index, is_flipped

        selected_idx = e.control.selected_index
        # Updated key mapping to include grammar
        deck_keys = [
            "hiragana", "katakana",
            "n5", "n4", "n3", "n2",
            "grammar_n5", "grammar_n4", "grammar_n3", "grammar_n2"
        ]

        if 0 <= selected_idx < len(deck_keys):
            current_deck_key = deck_keys[selected_idx]
            current_index = 0
            is_flipped = False

            card_container.scale = ft.Scale(scale_x=1, scale_y=1)
            card = get_current_card()
            card_content.content = create_front_face(card)

            page.update()
            update_text_ui()

    # --- Layout Setup ---

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            # Basics
            ft.NavigationRailDestination(icon="abc", label="Hiragana"),
            ft.NavigationRailDestination(icon="abc_outlined", label="Katakana"),

            # Kanji Levels
            ft.NavigationRailDestination(icon="filter_1", label="N5 Kanji"),
            ft.NavigationRailDestination(icon="filter_2", label="N4 Kanji"),
            ft.NavigationRailDestination(icon="filter_3", label="N3 Kanji"),
            ft.NavigationRailDestination(icon="filter_4", label="N2 Kanji"),

            # Grammar Levels
            ft.NavigationRailDestination(icon="book", label="N5 Grammar"),
            ft.NavigationRailDestination(icon="book", label="N4 Grammar"),
            ft.NavigationRailDestination(icon="book", label="N3 Grammar"),
            ft.NavigationRailDestination(icon="book", label="N2 Grammar"),
        ],
        on_change=on_rail_change,
        bgcolor="white",
    )

    main_area = ft.Column(
        [
            ft.Container(height=20),
            progress_text,
            ft.Container(height=20),
            ft.GestureDetector(
                content=card_container,
                on_tap=flip_card
            ),
            ft.Container(height=40),
            ft.Row(
                [
                    ft.IconButton("shuffle", on_click=shuffle_deck, icon_size=24, tooltip="Shuffle Deck"),
                    ft.Container(width=10),
                    ft.IconButton("chevron_left", on_click=prev_card, icon_size=30),
                    ft.ElevatedButton("Flip Card", on_click=flip_card, color="white", bgcolor="indigo500"),
                    ft.IconButton("chevron_right", on_click=next_card, icon_size=30),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1, color="slate200"),
                main_area,
            ],
            expand=True,
        )
    )


ft.app(target=main)