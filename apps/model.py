from dash.dependencies import Output, Input
from dash_core_components import Dropdown
from dash_html_components import Div

from app import app
from apps import learning_history, report_table

graphs = (
    ("accuracy", [0, 1.1]),
    ("val_accuracy", [-0.1, 1.1]),
    ("loss", [0, 8]),
    ("val_loss", [-0.1, 8]),
    ("f1", [-0.1, 1.1]),
    ("val_f1", [-0.1, 1.1]),
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


models = []
reports = []
histories = []


def update_models(new_models,new_reports,new_histories):
    global models, reports, histories
    models.clear()
    reports.clear()
    histories.clear()
    for new_model in new_models:
        models.append(new_model)
    for new_report in new_reports:
        reports.append(new_report)
    for new_history in new_histories:
        histories.append(new_history)


def get_layout():
    return Div([
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
