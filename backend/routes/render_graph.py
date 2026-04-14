from flask import Blueprint, jsonify, request

from backend.services.json_loader import build_pda_from_dict
from backend.services.graph_renderer import render_pda_graph

render_graph_bp = Blueprint("render_graph", __name__)


@render_graph_bp.route("/render-graph", methods=["POST"])
def render_graph():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No se recibió un cuerpo JSON válido."
            }), 400

        pda_definition = data.get("pda")

        if not pda_definition:
            return jsonify({
                "error": "Falta la definición del PDA."
            }), 400

        pda = build_pda_from_dict(pda_definition)
        graph_data = render_pda_graph(pda)

        return jsonify(graph_data), 200

    except Exception as e:
        return jsonify({
            "error": f"Error interno al generar el grafo: {str(e)}"
        }), 500