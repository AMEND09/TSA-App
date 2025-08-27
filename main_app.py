import flet as ft
import time

# ###############################################################
# Reusable Components
# ###############################################################

def Section(title: str, controls: list, expand=False):
    """Creates a visually distinct section with a title and content."""
    return ft.Container(
        expand=expand,
        margin=ft.margin.only(bottom=20),
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
                ft.Column(controls=controls, spacing=8),
            ]
        )
    )

def Card(content: ft.Control, expand=False):
    """A styled container for content blocks."""
    return ft.Card(
        expand=expand,
        elevation=2,
        content=ft.Container(
            padding=15,
            border_radius=ft.border_radius.all(8),
            content=content
        )
    )

# ###############################################################
# Student View Builder Functions
# ###############################################################

def build_student_home():
    """Builds the UI for the Student Home Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            Section("Announcements", [
                Card(ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")),
                Card(ft.Text("Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")),
            ]),
            Section("Upcoming Workshops", [
                ft.Row(
                    spacing=10,
                    controls=[
                        Card(ft.Column([ft.Text("Workshop A"), ft.ElevatedButton("Sign Up")]), expand=True),
                        Card(ft.Column([ft.Text("Workshop B"), ft.ElevatedButton("Sign Up")]), expand=True),
                    ]
                )
            ]),
            Section("Your ID", [
                Card(ft.Row([ft.Icon(ft.Icons.PERSON), ft.Text("1234567890", weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER)),
            ]),
        ]
    )

def build_student_events():
    """Builds the UI for the Student Events Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            Section("Deadlines", [
                Card(ft.Text("State Conference Registration: Oct 15")),
                Card(ft.Text("National Competition Submission: Nov 1")),
            ]),
            Section("Your Events", [
                ft.Row(
                    spacing=10,
                    controls=[
                        Card(ft.Column([ft.Text("VEX Robotics"), ft.OutlinedButton("More Info")]), expand=True),
                        Card(ft.Column([ft.Text("Webmaster"), ft.OutlinedButton("More Info")]), expand=True),
                    ]
                )
            ]),
            Section("Tryouts", [
                ft.Row(
                    spacing=10,
                    controls=[
                        Card(ft.Column([ft.Text("Debate Team"), ft.OutlinedButton("More Info"), ft.ElevatedButton("Sign Up")]), expand=True),
                        Card(ft.Column([ft.Text("Coding Team"), ft.OutlinedButton("More Info"), ft.ElevatedButton("Sign Up")]), expand=True),
                    ]
                )
            ]),
        ]
    )

def build_student_info():
    """Builds the UI for the Student Your Info Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            Section("ID & Password", [
                Card(ft.ListTile(leading=ft.Icon(ft.Icons.LOCK), title=ft.Text("Student ID"), subtitle=ft.Text("1234567890"))),
                Card(ft.ListTile(leading=ft.Icon(ft.Icons.KEY), title=ft.Text("Password"), trailing=ft.IconButton(icon=ft.Icons.EDIT, tooltip="Change Password"))),
            ]),
            Section("Documents", [
                 ft.Row(
                    spacing=10,
                    controls=[
                        Card(ft.Column([ft.Text("Permission Slip"), ft.ElevatedButton("View")]), expand=True),
                        Card(ft.Column([ft.Text("Event Itinerary"), ft.ElevatedButton("View")]), expand=True),
                    ]
                )
            ]),
            Section("Dues Paid", [
                Card(ft.Row([ft.Icon(ft.Icons.MONETIZATION_ON), ft.Text("$35", weight=ft.FontWeight.BOLD, size=20)], alignment=ft.MainAxisAlignment.CENTER)),
            ]),
        ]
    )


# ###############################################################
# Officer View Builder Functions
# ###############################################################

def build_officer_dashboard():
    """Builds the UI for the Officer Dashboard Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            Section("Club Overview", [
                ft.Row([
                    Card(ft.Column([ft.Text("Total Members", weight=ft.FontWeight.BOLD), ft.Text("78", size=24)]), expand=True),
                    Card(ft.Column([ft.Text("Dues Paid", weight=ft.FontWeight.BOLD), ft.Text("65 / 78", size=24)]), expand=True),
                ])
            ]),
            Section("Manage Announcements", [
                Card(ft.ListTile(title=ft.Text("Welcome Back Meeting!"), subtitle=ft.Text("Posted: Aug 25"), trailing=ft.Row([ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)]))),
                ft.ElevatedButton("Add New Announcement", icon=ft.Icons.ADD, expand=True),
            ]),
            Section("Manage Workshops", [
                Card(ft.ListTile(title=ft.Text("Intro to Python"), subtitle=ft.Text("Sign-ups: 15"), trailing=ft.Row([ft.IconButton(icon=ft.Icons.PEOPLE), ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)]))),
                ft.ElevatedButton("Add New Workshop", icon=ft.Icons.ADD, expand=True),
            ]),
        ]
    )

def build_officer_events():
    """Builds the UI for the Officer Event Management Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
            Section("Manage Deadlines", [
                Card(ft.ListTile(title=ft.Text("State Conference Registration"), subtitle=ft.Text("Date: Oct 15"), trailing=ft.Row([ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)]))),
                ft.ElevatedButton("Add New Deadline", icon=ft.Icons.ADD, expand=True),
            ]),
            Section("Manage Events & Tryouts", [
                Card(ft.ListTile(title=ft.Text("Debate Team Tryouts"), subtitle=ft.Text("Sign-ups: 22"), trailing=ft.Row([ft.IconButton(icon=ft.Icons.PEOPLE), ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)]))),
                Card(ft.ListTile(title=ft.Text("VEX Robotics Competition"), subtitle=ft.Text("Attendees: 12"), trailing=ft.Row([ft.IconButton(icon=ft.Icons.PEOPLE), ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)]))),
                ft.ElevatedButton("Add New Event/Tryout", icon=ft.Icons.ADD, expand=True),
            ]),
        ]
    )

def build_officer_members():
    """Builds the UI for the Officer Member Management Page."""
    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[
             Section("Member List", [
                ft.TextField(label="Search Members", prefix_icon=ft.Icons.SEARCH),
                Card(ft.ListTile(leading=ft.Icon(ft.Icons.PERSON), title=ft.Text("John Doe"), subtitle=ft.Text("Dues: Paid"), trailing=ft.IconButton(icon=ft.Icons.EDIT))),
                Card(ft.ListTile(leading=ft.Icon(ft.Icons.PERSON), title=ft.Text("Jane Smith"), subtitle=ft.Text("Dues: Unpaid"), trailing=ft.IconButton(icon=ft.Icons.EDIT))),
             ]),
             Section("Manage Documents", [
                 Card(ft.ListTile(title=ft.Text("State Conference Permission Slip.pdf"), trailing=ft.IconButton(icon=ft.Icons.DELETE))),
                 ft.ElevatedButton("Upload New Document", icon=ft.Icons.UPLOAD, expand=True),
             ]),
        ]
    )

# ###############################################################
# Main Application Class
# ###############################################################

class TSAApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "TSA Club Manager"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 0

        # App state
        self.is_officer_view = ft.Ref[ft.Switch]()

        # Student views
        self.student_views = {
            "Home": build_student_home(),
            "Events": build_student_events(),
            "Info": build_student_info(),
        }
        self.student_nav = self.create_navigation_bar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.Icons.CALENDAR_MONTH, label="Events"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, selected_icon=ft.Icons.PERSON, label="Your Info"),
            ],
            on_change=lambda e: self.navigate(e.control.selected_index, is_officer=False)
        )

        # Officer views
        self.officer_views = {
            "Dashboard": build_officer_dashboard(),
            "Events": build_officer_events(),
            "Members": build_officer_members(),
        }
        self.officer_nav = self.create_navigation_bar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.DASHBOARD_OUTLINED, selected_icon=ft.Icons.DASHBOARD, label="Dashboard"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.Icons.CALENDAR_MONTH, label="Events"),
                ft.NavigationBarDestination(icon=ft.Icons.GROUP_OUTLINED, selected_icon=ft.Icons.GROUP, label="Members"),
            ],
            on_change=lambda e: self.navigate(e.control.selected_index, is_officer=True)
        )

        # Content area
        self.content_area = ft.Container(
            expand=True,
            padding=ft.padding.all(20),
            content=self.student_views["Home"]
        )
        
        # Initial Build
        self.build_ui()

    def create_navigation_bar(self, destinations, on_change):
        return ft.NavigationBar(
            selected_index=0,
            destinations=destinations,
            on_change=on_change,
        )

    def toggle_view(self, e):
        """Switches between student and officer views."""
        is_officer = e.control.value
        if is_officer:
            self.page.navigation_bar = self.officer_nav
            self.page.appbar.title = ft.Text("Officer View")
            self.navigate(0, is_officer=True)
        else:
            self.page.navigation_bar = self.student_nav
            self.page.appbar.title = ft.Text("Student View")
            self.navigate(0, is_officer=False)
        self.page.update()

    def navigate(self, index, is_officer):
        """Updates the content area based on navigation."""
        if is_officer:
            view_key = list(self.officer_views.keys())[index]
            self.content_area.content = self.officer_views[view_key]
        else:
            view_key = list(self.student_views.keys())[index]
            self.content_area.content = self.student_views[view_key]
        self.page.update()

    def build_ui(self):
        """Builds the main application UI."""
        self.page.appbar = ft.AppBar(
            title=ft.Text("Student View"),
            center_title=True,
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            actions=[
                ft.Row([
                    ft.Text("Officer?"),
                    ft.Switch(ref=self.is_officer_view, on_change=self.toggle_view)
                ]),
                ft.Container(width=10) # Padding
            ]
        )
        self.page.navigation_bar = self.student_nav
        
        # This container constrains the width to simulate a mobile view
        app_container = ft.Container(
            width=400,
            height=800,
            content=self.content_area,
            border=ft.border.all(1, ft.Colors.BLACK12),
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.Colors.WHITE
        )

        self.page.add(app_container)
        self.page.update()

def main(page: ft.Page):
    TSAApp(page)

if __name__ == "__main__":
    ft.app(target=main)