from flask import Blueprint, jsonify

from backend.services.sample_service import list_samples

samples_bp = Blueprint("samples", __name__)


@samples_bp.route("/samples", methods=["GET"])
def get_samples():
    try:
        samples = list_samples()
        return jsonify({
            "samples": samples
        }), 200

    except Exception as e:
        return jsonify({
            "error": f"Error al listar samples: {str(e)}"
        }), 500