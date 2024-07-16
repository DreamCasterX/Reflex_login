"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def render_user_entries(title: str, is_password: bool = False):
    return rx.vstack(
        rx.text(title, color="gray", font_size="14px", weight="bold"),
        rx.chakra.input(type_="text" if not is_password else "password"),
        width="100%",
    )


def render_event_trigger():
    return rx.badge(
        rx.text("Sign in", text_align="center", width="100%"),
        color_scheme="teal",
        variant="outline",
        size="2",
        font_size="16px",
        width="100%",
        padding="0.75em 0em",
        border_radius="18px",
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
            # 淺深色模式切換器
            rx.hstack(
                rx.icon("sun", size=16),
                rx.switch(
                    checked=rx.style.color_mode != rx.style.LIGHT_COLOR_MODE,
                    on_change=rx.style.toggle_color_mode,
                    size="1",
                ),
                rx.icon("moon", size=16),
                margin_left="380px",
                margin_bottom="-10px",
            ),
            # 淺深色模式按鈕
            # rx.color_mode.button(position="top-right"),
            rx.heading("Account Login", size="7", margin_left="150px"),
            render_user_entries("✉️ Email"),
            render_user_entries(
                title="🔑 Password",
                is_password=True,
            ),
            rx.checkbox(text="Remember me", font_color="grey"),
            rx.spacer(), # 空白行
            render_event_trigger(),
            # 超連結按鈕
            rx.link(
                rx.button("Create an account"),
                href="https://github.com/DreamCasterX",
                is_external=True,
                margin_left="10px",
            ),
            # 超連結按鈕
            rx.link(
                rx.button("Forgot password?"),
                href="https://github.com/DreamCasterX",
                is_external=True,
                margin_left="304px",
                margin_top="-56px",
            ),
            # Reflex廣告Logo
            rx.logo(size="2"),
            width="100%",
            padding_right="25px",  # 內置外框右側寬度
            padding_left="25px",  # 內置外框左側寬度
            padding="2em, 2em, 4em, 2em",
            spacing="5",

        ),
        # 外框設置
        width=[600, 600, 500],  # 最大外框寬度,
        # bg="rgba(21,21,21,0.55)", # 預設app底色(灰)
        border="1px solid #2e2e2e",  # 邊界粗細
        border_radius="13px",  # 邊界圓角
        box_shadow="0px 8px 16px 6px rgba(0,0,0,0.25)",
    )


def index() -> rx.Component:
    return rx.center(
        render_main_component(),
        width="100%",
        height="100vh",
        padding="2em",
        # bg="#121212", #預設網頁底色(黑)
    )


app = rx.App()
app.add_page(index)
