from flask import Blueprint, jsonify
from backend.services.sample_service import list_samples, load_sample

samples_bp = Blueprint("samples", __name__)


@samples_bp.route("/samples", methods=["GET"])
def get_samples():
    try:
        samples = list_samples()
        return jsonify({"samples": samples}), 200
    except Exception as e:
        return jsonify({"error": f"Error al listar samples: {str(e)}"}), 500


@samples_bp.route("/samples/<sample_name>", methods=["GET"])
def get_sample(sample_name):
    try:
        pda = load_sample(sample_name)

        transitions = []
        for t in pda.transitions:
            transitions.append({
                "current_state": t.current_state,
                "input_symbol": t.input_symbol,
                "stack_top": t.stack_top,
                "next_state": t.next_state,
                "stack_push": t.stack_push
            })

        return jsonify({
            "pda": {
                "states": pda.states,
                "input_alphabet": pda.input_alphabet,
                "stack_alphabet": pda.stack_alphabet,
                "transitions": transitions,
                "start_state": pda.start_state,
                "start_stack": pda.start_stack,
                "accept_states": pda.accept_states
            }
        }), 200

    except Exception as e:
        return jsonify({"error": f"Error al cargar sample: {str(e)}"}), 500