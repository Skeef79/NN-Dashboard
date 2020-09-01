from dash.dependencies import Output, Input
from dash_core_components import Dropdown
from dash_html_components import Div

from app import app
from apps import learning_history, report_table

models = [
    (0, "Test Dummy Model #1", "EFN"),
    (1, "Test Dummy Model #2", "EFN"),
]

reports = [
    (0, {
        "accuracy": "0.1979166716337204",
        "val_accuracy": "0.0",
        "loss": "3.4406051635742188",
        "val_loss": "4.19291353225708",
        "f1": "0.0",
        "val_f1": "0.0",
        "test_accuracy": "0.0",
        "test_loss": "4.24012565612793",
        "test_f1": "0.0"
    }),
    (1, {
        "accuracy": "0.1979166716337204",
        "val_accuracy": "0.0",
        "loss": "3.4406051635742188",
        "val_loss": "4.19291353225708",
        "f1": "0.0",
        "val_f1": "0.0",
        "test_accuracy": "0.0",
        "test_loss": "4.24012565612793",
        "test_f1": "0.0"
    })
]

reports = [
    (id, {
        name: float(value)
        for name, value in report.items()
    })
    for id, report in reports
]

histories = [
    (0, {
        "loss": ["3.946352958679199", "3.4406051635742188"],
        "accuracy": ["0.0572916679084301", "0.1979166716337204"],
        "f1": ["0.0", "0.0"],
        "val_loss": ["4.087198734283447", "4.19291353225708"],
        "val_accuracy": ["0.0", "0.0"],
        "val_f1": ["0.0", "0.0"],
        "lr": ["0.001", "0.001"]
    }),
    (1, {
        "loss": ["2.946352958679199", "1.4406051635742188"],
        "accuracy": ["0.0572916679084301", "0.1979166716337204"],
        "f1": ["0.0", "0.0"],
        "val_loss": ["4.087198734283447", "4.19291353225708"],
        "val_accuracy": ["0.0", "0.0"],
        "val_f1": ["0.0", "0.0"],
        "lr": ["0.001", "0.001"]
    }),
]

histories = [
    (id, {
        name: [float(value) for value in values]
        for name, values in history.items()
    })
    for id, history in histories
]

graphs = (
    ("loss", [0, 1.1]),
    ("accuracy", [0, 1.1]),
    ("f1", [-0.1, 3]),
    ("val_loss", [-0.1, 3]),
    ("val_f1", [-0.1, 1.1]),
    ("lr", [-0.1, 1.1])
)

table_headers = {
    "accuracy": "Accuracy",
    "val_accuracy": "Validation accuracy",
    "loss": "Train loss",
    "val_loss": "Validation loss",
    "f1": "Train F1",
    "val_f1": "Validation F1",
    "test_accuracy": "Test accuracy",
    "test_loss": "Test loss",
    "test_f1": "Test F1"
}


def get_dropdown_list(models):
    return [
        {'label': str(model[1]),
         'value': model[0]} for model in models
    ]


layout = Div([
    Dropdown(
        id='models-dropdown',
        options=get_dropdown_list(models),
        clearable=True,
        multi=True,
        value=[],
    ),
    Div(
        id='report'
    ),
    Div(
        learning_history.generate_layout(graphs),
    ),
    Div(id='dummy')
])


@app.callback(
    [Output('report', 'children')] + [Output(graph, 'figure') for graph, _ in graphs],
    [Input('models-dropdown', 'value')])
def display_page(value):
    return (
        report_table.generate_layout(
            table_headers,
            [report for report in reports if report[0] in value],
            models
        ),
        *learning_history.update_figures(
            graphs,
            [h[1] for h in histories if h[0] in value],
            [m[1] for m in models if m[0] in value]))