import flet as ft
import random
import string


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window.title_bar_hidden = True
    page.window.width = 400
    page.window.min_width = 400
    page.window.height = 700
    page.window.min_height = 700

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary='#192233',
            on_primary='#ffffff',
            background='#0d121c',
        )
    )

    options = {}
    generate_button = ft.Ref[ft.Container]()
    txt_password = ft.Ref[ft.Text]()
    characters_count = ft.Ref[ft.Slider]()
    btn = ft.Ref[ft.IconButton]()

    def copy_password(e):
        pwd = txt_password.current.value
        if pwd:
            page.set_clipboard(pwd)
            btn.current.selected = True
            btn.current.update()

    def generate_password(e):
        pwd = ''
        if options.get('uppercase'):
            pwd += string.ascii_uppercase
        if options.get('lowercase'):
            pwd += string.ascii_lowercase
        if options.get('special'):
            pwd += string.punctuation
        if options.get('numbers'):
            pwd += string.digits

        count = int(characters_count.current.value)
        if pwd:
            password = ''.join(random.choices(pwd, k=count))
            txt_password.current.value = password
            txt_password.current.update()

        btn.current.selected = False
        btn.current.update()

    def toggle_option(e):
        nonlocal options
        options.update({e.control.data: e.control.value})

        if any(options.values()):
            generate_button.current.disabled = False
            generate_button.current.opacity = 1
        else:
            generate_button.current.disabled = True
            generate_button.current.opacity = 0.3

        generate_button.current.update()

    layout = ft.Container(
        # scroll=ft.ScrollMode.ADAPTIVE,
        expand=True,
        padding=ft.padding.only(40, 20, 20, 20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.PRIMARY, ft.colors.BACKGROUND],
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text(
                    value='GERADOR DE SENHAS',
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=30, thickness=0.5),

                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                    border_radius=ft.border_radius.all(5),
                    padding=ft.padding.all(10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                ref=txt_password,
                                selectable=True,
                                size=20,
                                height=40,
                            ),
                            ft.IconButton(
                                ref=btn,
                                icon=ft.icons.COPY,
                                icon_color=ft.colors.WHITE,
                                selected_icon=ft.icons.CHECK,
                                selected_icon_color=ft.colors.GREEN,
                                selected=False,
                                on_click=copy_password
                            )
                        ]
                    )
                ),

                ft.Text(
                    value='CARACTERES',
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Container(
                    bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                    border_radius=ft.border_radius.all(5),
                    content=ft.Slider(
                        ref=characters_count,
                        value=10,
                        min=4,
                        max=20,
                        divisions=16,
                        label="{value}",
                    )
                ),

                ft.Text(
                    value='PREFERÊNCIAS',
                    weight=ft.FontWeight.BOLD,
                ),

                ft.ListTile(
                    title=ft.Text(
                        value='Letras maiúsculas',
                        size=20,
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.GREEN,
                        data='uppercase',
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),

                ft.ListTile(
                    title=ft.Text(
                        value='Letras minúsculas',
                        size=20,
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.GREEN,
                        data='lowercase',
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),

                ft.ListTile(
                    title=ft.Text(
                        value='Caracteres especiais',
                        size=20,
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.GREEN,
                        data='special',
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),

                ft.ListTile(
                    title=ft.Text(
                        value='Números',
                        size=20,
                    ),
                    trailing=ft.Switch(
                        adaptive=True,
                        active_color=ft.colors.GREEN,
                        data='numbers',
                        on_change=toggle_option,
                    ),
                    toggle_inputs=True,
                ),

                ft.Container(
                    ref=generate_button,
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.INDIGO, ft.colors.BLUE],
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(20),
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value='GERAR SENHA',
                        weight=ft.FontWeight.BOLD,
                        size=20,
                        color=ft.colors.WHITE,
                    ),
                    on_click=generate_password,
                    disabled=True,
                    opacity=0.3,
                    animate_opacity=ft.Animation(
                        duration=1000,
                        curve=ft.AnimationCurve.DECELERATE
                    )
                )
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
