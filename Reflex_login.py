"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def render_user_entries(title: str, is_password: bool = False):
    return rx.vstack(
        rx.text(title, color="gray", font_size="13px", weight="bold"),
        rx.chakra.input(color="white", type_="text" if not is_password else "password"),
        width="100%",
    )


def render_event_trigger():
    return rx.badge(
        rx.text("Login", text_align="center", width="100%"),
        color_scheme="teal",
        variant="outline",
        size="2",
        font_size="15px",
        width="100%",
        padding="0.75em 0em",
    )


# Main card UI
def render_main_component():
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="lock", size=28, color="rgba(127, 127, 127, 1)"),
            width="100%",
            height="55px",
            bg="#181818",
            border_radius="10px 10px 0px 0px",
            display="flex",
            justify_content="center",
            align_items="center",
        ),
        rx.vstack(
            rx.color_mode.button(position="top-right"),  # 切換淺/深色模式
            rx.heading("系統登入", size="5"),
            render_user_entries("Email"),
            render_user_entries(
                title="Password",
                is_password=True,
            ),
            rx.spacer(),
            render_event_trigger(),
            rx.link(
                rx.button("Check out my GitHub"),
                href="https://github.com/DreamCasterX",
                is_external=True,
            ),
            rx.logo(),
            width="100%",
            padding_right="20px",  # 內置外框右側寬度
            padding_left="20px",  # 內置外框左側寬度
            padding="2em, 2em, 4em, 2em",
            spacing="5",
        ),
        width=[600, 600, 500],  # 最大外框寬度
        # width=["100%", "100%", "65%", "50%", "35%"],
        bg="rgba(21,21,21,0.55)",
        border="0.75px solid #2e2e2e",
        border_radius="10px",
        box_shadow="0px 8px 16px 6px rgba(0,0,0,0.25)",
    )


def index() -> rx.Component:
    return rx.center(
        render_main_component(),
        width="100%",
        height="100vh",
        padding="2em",
        bg="#121212",
    )


app = rx.App()
app.add_page(index)
