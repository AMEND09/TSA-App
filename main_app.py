import flet as ft

# ###############################################################
# Reusable Components
# ###############################################################

def Section(title: str, content: ft.Control):
    """Creates a visually distinct section with a title and content."""
    return ft.Column(
        spacing=10,
        controls=[
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD),
            content,
        ]
    )

def Card(content: ft.Control, width=None, height=None, expand=False):
    """A styled container for content blocks."""
    return ft.Card(
        expand=expand,
        elevation=2,
        content=ft.Container(
            width=width,
            height=height,
            padding=15,
            border_radius=ft.border_radius.all(8),
            content=content
        )
    )

# ###############################################################
# Modal (Dialog) Functions - THIS IS THE CORE MODAL LOGIC
# ###############################################################

def open_dialog(page: ft.Page, title: str, content_controls: list[ft.Control]):
    """Generic function to open a modal dialog."""
    def close_dialog(e):
        dialog.open = False
        page.update()

    # In a real app, this is where you would make an API call to your Django backend.
    def save_and_close(e):
        # 1. Collect data from text fields in the `content_controls` list.
        # 2. Make an API call to Django.
        # 3. On success, close the dialog and maybe refresh the page content.
        print("Save button clicked. API call would go here.")
        close_dialog(e)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Column(content_controls, tight=True, spacing=15),
        actions=[
            ft.ElevatedButton("Save", on_click=save_and_close),
            ft.TextButton("Cancel", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.dialog = dialog
    dialog.open = True
    page.update()

# ###############################################################
# Student View Content Builders
# ###############################################################

def get_student_home_content():
    announcements_box = ft.Container(height=150, padding=ft.padding.only(right=10), content=ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Text("Welcome back! Our first meeting is this Thursday.")), Card(ft.Text("State conference fees are due next Friday.")),]))
    workshops_carousel = ft.Row(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Column([ft.Text("Intro to Python"), ft.ElevatedButton("Sign Up")]), width=200), Card(ft.Column([ft.Text("3D Modeling Basics"), ft.ElevatedButton("Sign Up")]), width=200),])
    return [Section("Announcements", announcements_box), Section("Upcoming Workshops", workshops_carousel), Section("Your ID", Card(ft.Row([ft.Icon(ft.Icons.PERSON), ft.Text("1234567890", weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER))),]

def get_student_events_content():
    deadlines_box = ft.Container(height=150, padding=ft.padding.only(right=10), content=ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Text("State Conference Registration: Oct 15")), Card(ft.Text("National Competition Submission: Nov 1")),]))
    your_events_carousel = ft.Row(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Column([ft.Text("VEX Robotics"), ft.OutlinedButton("More Info")]), width=200), Card(ft.Column([ft.Text("Webmaster"), ft.OutlinedButton("More Info")]), width=200),])
    tryouts_carousel = ft.Row(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Column([ft.Text("Debate Team"), ft.OutlinedButton("More Info"), ft.ElevatedButton("Sign Up")]), width=200), Card(ft.Column([ft.Text("Coding Team"), ft.OutlinedButton("More Info"), ft.ElevatedButton("Sign Up")]), width=200),])
    return [Section("Deadlines", deadlines_box), Section("Your Events", your_events_carousel), Section("Tryouts", tryouts_carousel),]

def get_student_info_content():
    documents_carousel = ft.Row(scroll=ft.ScrollMode.AUTO, spacing=10, controls=[Card(ft.Column([ft.Text("Permission Slip"), ft.ElevatedButton("View")]), width=200), Card(ft.Column([ft.Text("Event Itinerary"), ft.ElevatedButton("View")]), width=200),])
    return [Section("ID & Password", ft.Column([Card(ft.ListTile(leading=ft.Icon(ft.Icons.LOCK), title=ft.Text("Student ID"), subtitle=ft.Text("1234567890"))), Card(ft.ListTile(leading=ft.Icon(ft.Icons.KEY), title=ft.Text("Password"), trailing=ft.IconButton(icon=ft.Icons.EDIT, tooltip="Change Password"))),])), Section("Documents", documents_carousel), Section("Dues Paid", Card(ft.Row([ft.Icon(ft.Icons.MONETIZATION_ON), ft.Text("$35", weight=ft.FontWeight.BOLD, size=20)], alignment=ft.MainAxisAlignment.CENTER))),]

# ###############################################################
# Officer View Content Builders
# ###############################################################

def get_officer_dashboard_content(page: ft.Page):
    announcements_list = ft.Column([
        Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
            ft.Text("Welcome Back Meeting!", expand=True),
            ft.Row(spacing=0, controls=[ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)])
        ])),
        # MODAL TRIGGER for adding announcements
        ft.ElevatedButton("Add New Announcement", icon=ft.Icons.ADD, on_click=lambda _: open_dialog(page, "Add Announcement", [ft.TextField(label="Title"), ft.TextField(label="Content", multiline=True, min_lines=3)])),
    ])

    workshops_list = ft.Column([
        Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
            ft.Column([ft.Text("Intro to Python", expand=True), ft.Text("Sign-ups: 15")]),
            ft.Row(spacing=0, controls=[ft.IconButton(icon=ft.Icons.PEOPLE), ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)])
        ])),
        # MODAL TRIGGER for adding workshops
        ft.ElevatedButton("Add New Workshop", icon=ft.Icons.ADD, on_click=lambda _: open_dialog(page, "Add Workshop", [ft.TextField(label="Title"), ft.TextField(label="Date & Time")])),
    ])

    return [Section("Club Overview", ft.Row([Card(ft.Column([ft.Text("Total Members"), ft.Text("78", size=24)], horizontal_alignment=ft.CrossAxisAlignment.CENTER), expand=True), Card(ft.Column([ft.Text("Dues Paid"), ft.Text("65 / 78", size=24)], horizontal_alignment=ft.CrossAxisAlignment.CENTER), expand=True),])), Section("Manage Announcements", announcements_list), Section("Manage Workshops", workshops_list),]

def get_officer_events_content(page: ft.Page):
    return [
        Section("Manage Deadlines", ft.Column([
            Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Text("State Conference Registration: Oct 15", expand=True),
                ft.Row(spacing=0, controls=[ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)])
            ])),
            # MODAL TRIGGER for adding deadlines
            ft.ElevatedButton("Add New Deadline", icon=ft.Icons.ADD, on_click=lambda _: open_dialog(page, "Add Deadline", [ft.TextField(label="Title"), ft.TextField(label="Date (e.g., Oct 15)")])),
        ])),
        Section("Manage Events & Tryouts", ft.Column([
            Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Column([ft.Text("Debate Team Tryouts", expand=True), ft.Text("Sign-ups: 22")]),
                ft.Row(spacing=0, controls=[ft.IconButton(icon=ft.Icons.PEOPLE), ft.IconButton(icon=ft.Icons.EDIT), ft.IconButton(icon=ft.Icons.DELETE)])
            ])),
            # MODAL TRIGGER for adding events/tryouts
            ft.ElevatedButton("Add New Event/Tryout", icon=ft.Icons.ADD, on_click=lambda _: open_dialog(page, "Add Event/Tryout", [ft.TextField(label="Title"), ft.TextField(label="Details")])),
        ])),
    ]

def get_officer_members_content(page: ft.Page):
    return [
        Section("Member List", ft.Column([
            ft.TextField(label="Search Members", prefix_icon=ft.Icons.SEARCH),
            Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Row(controls=[ft.Icon(ft.Icons.PERSON), ft.VerticalDivider(), ft.Column([ft.Text("John Doe"), ft.Text("Dues: Paid")])]),
                # MODAL TRIGGER for editing a member
                ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda _: open_dialog(page, "Edit Member", [ft.TextField(label="Name", value="John Doe"), ft.Checkbox(label="Dues Paid?", value=True)]))
            ])),
            Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Row(controls=[ft.Icon(ft.Icons.PERSON), ft.VerticalDivider(), ft.Column([ft.Text("Jane Smith"), ft.Text("Dues: Unpaid")])]),
                # MODAL TRIGGER for editing a member
                ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda _: open_dialog(page, "Edit Member", [ft.TextField(label="Name", value="Jane Smith"), ft.Checkbox(label="Dues Paid?", value=False)]))
            ])),
        ])),
        Section("Manage Documents", ft.Column([
            Card(ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                ft.Text("State Conference Permission Slip.pdf", expand=True), ft.IconButton(icon=ft.Icons.DELETE)])),
            # MODAL TRIGGER for uploading documents
            ft.ElevatedButton("Upload New Document", icon=ft.Icons.UPLOAD, on_click=lambda _: open_dialog(page, "Upload Document", [ft.Text("A FilePicker control would be added here.")])),
        ])),
    ]

# ###############################################################
# Main Application Router
# ###############################################################

def main(page: ft.Page):
    page.title = "TSA Club Manager"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()

        # Login View
        if page.route == "/login":
            id_field = ft.TextField(label="Student ID or Username")
            pw_field = ft.TextField(label="Password", password=True, can_reveal_password=True)

            def login_click(e):
                # Simple role-based login simulation
                if id_field.value == "officer":
                    page.go("/officer/dashboard")
                else:
                    page.go("/student/home")
            
            page.views.append(
                ft.View(route="/login", controls=[
                    ft.Container(
                        width=400,
                        padding=50,
                        border_radius=10,
                        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            controls=[
                                ft.Text("TSA Club Portal", size=24, weight=ft.FontWeight.BOLD),
                                id_field,
                                pw_field,
                                ft.ElevatedButton("Sign In", on_click=login_click, expand=True),
                            ]
                        )
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ))

        # Main App Views
        else:
            is_officer = page.route.startswith('/officer')
            
            def toggle_view(e):
                if e.control.value: page.go("/officer/dashboard")
                else: page.go("/student/home")
            
            app_bar = ft.AppBar(title=ft.Text("Officer View" if is_officer else "Student View"), center_title=True, bgcolor=ft.Colors.ON_SURFACE_VARIANT, actions=[ft.Row([ft.Text("Officer?"), ft.Switch(value=is_officer, on_change=toggle_view)]), ft.Container(width=10)])

            student_nav = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"), ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.Icons.CALENDAR_MONTH, label="Events"), ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, selected_icon=ft.Icons.PERSON, label="Your Info")], on_change=lambda e: page.go(f"/student/{['home', 'events', 'info'][e.control.selected_index]}"))
            officer_nav = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.Icons.DASHBOARD_OUTLINED, selected_icon=ft.Icons.DASHBOARD, label="Dashboard"), ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, selected_icon=ft.Icons.CALENDAR_MONTH, label="Events"), ft.NavigationBarDestination(icon=ft.Icons.GROUP_OUTLINED, selected_icon=ft.Icons.GROUP, label="Members")], on_change=lambda e: page.go(f"/officer/{['dashboard', 'events', 'members'][e.control.selected_index]}"))

            content = []
            navbar = student_nav
            if page.route == "/student/home": content, navbar.selected_index = get_student_home_content(), 0
            elif page.route == "/student/events": content, navbar.selected_index = get_student_events_content(), 1
            elif page.route == "/student/info": content, navbar.selected_index = get_student_info_content(), 2
            elif page.route == "/officer/dashboard": content, navbar = get_officer_dashboard_content(page), officer_nav; navbar.selected_index = 0
            elif page.route == "/officer/events": content, navbar = get_officer_events_content(page), officer_nav; navbar.selected_index = 1
            elif page.route == "/officer/members": content, navbar = get_officer_members_content(page), officer_nav; navbar.selected_index = 2

            page.views.append(ft.View(route=page.route, scroll=ft.ScrollMode.AUTO, appbar=app_bar, navigation_bar=navbar, controls=[ft.Container(width=450, padding=20, content=ft.Column(controls=content, spacing=20))], horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)