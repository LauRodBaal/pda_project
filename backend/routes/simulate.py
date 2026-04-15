from flask import Blueprint, jsonify, request
from backend.core.simulator import PDASimulator
from backend.core.trace_formatter import format_simulation_result
from backend.services.json_loader import build_pda_from_dict

simulate_bp = Blueprint("simulate", __name__)


@simulate_bp.route("/simulate", methods=["POST"])
def simulate_pda():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "accepted": False,
                "error": "No se recibió un cuerpo JSON válido."
            }), 400

        pda_definition = data.get("pda")
        input_string = data.get("input_string", "")

        if not pda_definition:
            return jsonify({
                "accepted": False,
                "error": "Falta la definición del PDA."
            }), 400

        pda = build_pda_from_dict(pda_definition)
        simulator = PDASimulator(pda)
        result = simulator.simulate(input_string=input_string)
        response = format_simulation_result(result)

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "accepted": False,
            "error": f"Error interno al simular el PDA: {str(e)}"
        }), 500