"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.divider(),
            rx.heading("¿Qué es la ciberseguridad?", size="9"),

            rx.flex(
                rx.center(rx.text(
                "La ciberseguridad, también conocida como seguridad digital, es la práctica de proteger su información digital, dispositivos y activos. Esto incluye información personal, cuentas, archivos, fotos e incluso el dinero.",
                size="5",
                ),),
                rx.spacer(),
                rx.center(rx.image(src="ciberseguridad.jpg", width="100%", height="100%"),),
                width="100%",
            ),
            rx.divider(),
            rx.heading("CIA", size="7"),
            rx.text(
                "El acrónimo 'CIA' se usa a menudo para representar los tres pilares de la ciberseguridad.",
                size="5",
            ),
            rx.flex(
                rx.hstack(
                    rx.icon("file-lock", stroke_width=2.5),
                    rx.text(
                        rx.text.strong("Confidencialidad: "),
                        "Mantener los secretos y garantizar que solo los usuarios autorizados puedan obtener acceso a sus archivos y cuentas.",
                        as_="p"
                    ),
                    spacing="2"
                ),
                rx.hstack(
                    rx.icon("shield-check", stroke_width=2.5),
                    rx.text(
                        rx.text.strong("Integridad: "),
                        "Garantizar que su información es la que debe ser y que nadie ha insertado, modificado o eliminado cosas sin su permiso.",
                        as_="p"
                    ),
                    spacing="2"
                ),
                rx.hstack(
                    rx.icon("folder-key", stroke_width=2.5),
                    rx.text(
                        rx.text.strong("Acceso: "),
                        "Garantizar que puede tener acceso a su información y sistemas cuando lo necesite.",
                        as_="p"
                    ),
                    spacing="2"
                ),
                direction="column",
                spacing="3"
            ),
            rx.divider(),
            rx.heading("La seguridad es un proceso, no un producto", size="7"),
            rx.text(
                "Aunque las aplicaciones de seguridad y los dispositivos, como el software antimalware y los firewalls, son esenciales, no basta con conectar esas herramientas y darlo por hecho. La seguridad digital también requiere que se establezca un conjunto de procesos y procedimientos adecuados. Son, entre otros:",
                size="5",
            ),
            rx.flex(
                rx.center(
                    rx.list.unordered(
                        rx.list.item("Copias de seguridad de datos"),
                        rx.list.item("Buenos hábitos cibernéticos"),
                        rx.list.item("Mantenga su software actualizado"),
                        rx.list.item("Usar contraseñas seguras y únicas"),
                        rx.list.item("Usar la autenticación multifactor"),
                        rx.list.item("Bloquear los dispositivos"),
                    ),
                ),
                rx.spacer(),
                rx.center(
                    rx.image(src="imagen2.png", width="200px", height="200px"),
                ),
                width="100%",
                direction="row",
                align="center",
                justify="between",
            ),
            rx.divider(),
            rx.heading("Vea también", size="5"),
            rx.text(
                "Entérate de las noticias más recientes ",
                rx.link(
                    rx.button("Aquí"),
                    href="https://www.youtube.com/@AsperisSecurity",
                    is_external=True,
                ),
            ),
            rx.video(
                url="https://youtu.be/TM-OT1U3P0k?si=lApepEd66mT3vsBr",
                width="50%",
                height="300px",
            ),
                        rx.text(
                "Introduccion a la ciberseguridad ",
                rx.link(
                    rx.button("Aquí"),
                    href="https://www.educaopen.com/digital-lab/blog/guias-digitales/introduccion-a-la-ciberseguridad",
                    is_external=True,
                ),
            ),

            rx.divider(),

            rx.image(
                src="logo.png",
                width="100px",
                height="auto",
                border_radius="15px 50px",
                border="5px solid #555",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        
    )


app = rx.App(
    theme=rx.theme(
        has_background=True,
        appearance="dark",
        radius="large",
        accent_color="ruby",
    )
)
app.add_page(index)
