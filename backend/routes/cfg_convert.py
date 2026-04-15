from flask import Blueprint, jsonify, request

from backend.services.json_loader import build_pda_from_dict
from backend.converters.cfg_converter import convert_pda_to_cfg

cfg_convert_bp = Blueprint("cfg_convert", __name__)


@cfg_convert_bp.route("/cfg-convert", methods=["POST"])
def cfg_convert():
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
        cfg = convert_pda_to_cfg(pda)

        return jsonify(cfg), 200

    except Exception as e:
        return jsonify({
            "error": f"Error interno al convertir PDA a CFG: {str(e)}"
        }), 500