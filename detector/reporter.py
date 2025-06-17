import json
from datetime import datetime


def generate_html_report(defects: dict, output_file: str):
    """Генерация HTML отчета о дефектах"""
    report = {
        "date": datetime.now().isoformat(),
        "defects": {
            "self_intersections": len(defects.get("intersections", [])),
            "details": defects.get("intersections", []).tolist()
        }
    }

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Defect Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
            .defect-card {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .critical {{ border-left: 4px solid #e74c3c; }}
            .warning {{ border-left: 4px solid #f39c12; }}
            .normal {{ border-left: 4px solid #2ecc71; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>3D Model Defect Report</h1>
            <p>Generated on: {report['date']}</p>
        </div>

        <div class="summary">
            <h2>Summary</h2>
            <p>Total defects found: <strong>{report['defects']['self_intersections']}</strong></p>
        </div>

        <div class="details">
            <h2>Defect Details</h2>
            {"".join(
                f'<div class="defect-card critical">'
                f'<h3>Self-intersection #{i + 1}</h3>'
                f'<p>Position: ({d[0]:.4f}, {d[1]:.4f}, {d[2]:.4f})</p>'
                '</div>'
                for i, d in enumerate(report['defects']['details']))
        }
        </div>
    </body>
    </html>
    """

    with open(output_file, 'w') as f:
        f.write(html_content)