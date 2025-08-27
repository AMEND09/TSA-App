import flet as ft
from django.urls import path
from flet_django.views import ft_view
from flet_django.pages import GenericApp

class Destination:
    def __init__(self, route, icon, selected_icon, label, nav_bar, action, nav_rail):
        self.route = route
        self.icon = icon
        self.selected_icon = selected_icon
        self.label = label
        self.nav_bar = nav_bar
        self.action = action
        self.nav_rail = nav_rail

def home(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Welcome to TSA Club App", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            ft.ElevatedButton("Organize Workshops", on_click=lambda e: page.go("/workshops")),
            ft.ElevatedButton("Organize Tryouts", on_click=lambda e: page.go("/tryouts")),
            ft.ElevatedButton("Manage IDs & Passwords", on_click=lambda e: page.go("/manage_ids")),
            ft.ElevatedButton("Event Help", on_click=lambda e: page.go("/event_help")),
            ft.ElevatedButton("Required Documents", on_click=lambda e: page.go("/documents")),
            ft.ElevatedButton("Manage Dues", on_click=lambda e: page.go("/manage_dues")),
            ft.ElevatedButton("Attendance", on_click=lambda e: page.go("/attendance")),
        ]
    )

def workshops(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Organize Workshops", size=20, color=ft.Colors.BLUE),
            ft.TextField(label="Workshop Name"),
            ft.TextField(label="Date"),
            ft.TextField(label="Description", multiline=True),
            ft.ElevatedButton("Create Workshop"),
        ]
    )

def tryouts(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Organize Tryouts", size=20, color=ft.Colors.BLUE),
            ft.TextField(label="Tryout Name"),
            ft.TextField(label="Date"),
            ft.TextField(label="Requirements"),
            ft.ElevatedButton("Create Tryout"),
        ]
    )

def manage_ids(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Manage IDs & Passwords", size=20, color=ft.Colors.BLUE),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Password")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("John")), ft.DataCell(ft.Text("****"))]),
                ]
            ),
            ft.ElevatedButton("Add New ID"),
        ]
    )

def event_help(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Event Help", size=20, color=ft.Colors.BLUE),
            ft.Text("Resources for TSA events:"),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Event Guidelines")),
                    ft.ListTile(title=ft.Text("Preparation Tips")),
                    ft.ListTile(title=ft.Text("Contact Info")),
                ]
            ),
        ]
    )

def documents(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Required Documents", size=20, color=ft.Colors.BLUE),
            ft.Text("Portfolio Template:"),
            ft.ElevatedButton("Download Template"),
            ft.Text("Other Documents:"),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Membership Form")),
                    ft.ListTile(title=ft.Text("Event Registration")),
                ]
            ),
        ]
    )

def manage_dues(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Manage Dues", size=20, color=ft.Colors.BLUE),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Member")),
                    ft.DataColumn(ft.Text("Dues Paid")),
                    ft.DataColumn(ft.Text("Amount")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("John")), ft.DataCell(ft.Text("Yes")), ft.DataCell(ft.Text("$20"))]),
                ]
            ),
            ft.ElevatedButton("Update Dues"),
        ]
    )

def attendance(page):
    return ft_view(
        page,
        controls=[
            ft.Text("Attendance", size=20, color=ft.Colors.BLUE),
            ft.TextField(label="Event Name"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Present")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("John")), ft.DataCell(ft.Checkbox())]),
                ]
            ),
            ft.ElevatedButton("Mark Attendance"),
        ]
    )

destinations = [
    Destination(
        route="/",
        icon=ft.Icons.HOME,
        selected_icon=ft.Icons.HOME_OUTLINED,
        label="Home",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/workshops",
        icon=ft.Icons.WORK,
        selected_icon=ft.Icons.WORK_OUTLINED,
        label="Workshops",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/tryouts",
        icon=ft.Icons.SPORTS,
        selected_icon=ft.Icons.SPORTS_OUTLINED,
        label="Tryouts",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/manage_ids",
        icon=ft.Icons.PERSON,
        selected_icon=ft.Icons.PERSON_OUTLINED,
        label="IDs",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/event_help",
        icon=ft.Icons.HELP,
        selected_icon=ft.Icons.HELP_OUTLINED,
        label="Help",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/documents",
        icon=ft.Icons.FILE_PRESENT,
        selected_icon=ft.Icons.FILE_PRESENT_OUTLINED,
        label="Docs",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/manage_dues",
        icon=ft.Icons.MONEY,
        selected_icon=ft.Icons.MONEY_OUTLINED,
        label="Dues",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
    Destination(
        route="/attendance",
        icon=ft.Icons.CHECKLIST,
        selected_icon=ft.Icons.CHECKLIST_OUTLINED,
        label="Attendance",
        nav_bar=True,
        action=True,
        nav_rail=False
    ),
]

urlpatterns = [
    path('', home, name="home"),
    path('workshops/', workshops, name="workshops"),
    path('tryouts/', tryouts, name="tryouts"),
    path('manage_ids/', manage_ids, name="manage_ids"),
    path('event_help/', event_help, name="event_help"),
    path('documents/', documents, name="documents"),
    path('manage_dues/', manage_dues, name="manage_dues"),
    path('attendance/', attendance, name="attendance"),
]

main = GenericApp(
    urls=urlpatterns,
    init_route="/"
)
