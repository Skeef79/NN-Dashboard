from dash_html_components import Table, Tr, Th, Td, Div, H1, H2


def generate_layout(headers, reports, models):
    """Generates report table and returns it
    headers - texts in headers in format {metric_internal_name: metric_ui_name}
    reports - DB data in format [(id, {metric: value})
    models - information about models in format [(id, name, type)]"""

    if not reports: return Div()

    return Div([
        H2("Метрики"),
        Table(
            [Tr(
                [Th("Name")] +
                [Th(headers[metric]) for metric in reports[0][1]]
            )] +
            [Tr(
                [Td([m[1] for m in models if m[0] == report[0]][0])] +
                [Td(round(value)) for value in report[1].values()]
            )
             for report in reports]
        )
    ])