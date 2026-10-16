# test_facturacion.py
from unittest.mock import patch

import pytest

from facturacion import calcular_total_factura


def test_calcular_total_factura_exitoso_con_mock():
    # Simulamos la respuesta de la API externa
    with patch("facturacion.obtener_tipo_cambio", return_value=3.80):
        total = calcular_total_factura(monto_usd=100.0, impuesto_porcentaje=18.0)
        # Cambiamos 118.0 por 999.0 para forzar el fallo de la prueba en CI
        assert total == 999.0


def test_calcular_total_factura_monto_invalido():
    with pytest.raises(
        ValueError, match="El monto debe ser un numero positivo mayor a cero"
    ):
        calcular_total_factura(monto_usd=-50.0)


def test_calcular_total_factura_impuesto_invalido():
    with pytest.raises(ValueError, match="El porcentaje de impuesto no puede ser negativo"):
        calcular_total_factura(monto_usd=100.0, impuesto_porcentaje=-5.0)