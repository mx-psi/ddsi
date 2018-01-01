-- Script para creación de disparadores

-- RS-1.2. Un producto cultural no podrá estar asociado a sí mismo.
-- Asociado a: RD-1.1, RD-1.6, RF-1.1 y RF-1.2
CREATE TRIGGER inserta_producto
BEFORE INSERT ON asociadoA
WHEN NEW.id1 = NEW.id2
BEGIN
SELECT RAISE(ABORT, 'Un producto cultural no puede estar relacionado con sí mismo');
END;


-- Disparadores del sistema de entidades

-- RS-2.1. La entidad es creadora del producto. La entidad creadora
-- debe estar presente en la lista de entidades creadoras del producto
-- cultural. Asociado a: RF-2.2, RD-2.2, RD-2.4 y RD-1.2.
CREATE TRIGGER creadora_producto_premiado
BEFORE INSERT ON premiadaPor
WHEN NEW.id NOT IN (SELECT idProducto FROM creadoPor WHERE nombreCreador = NEW.nombre)
BEGIN
SELECT RAISE(ABORT, 'La entidad premiada debe figurar entre las creadoras del producto');
END;

-- RS-2.2. El género no es su propio subgénero. Un género no podrá ser
-- su propio supergénero. Asociado a: RF-2.4, RD-2.5 y RD-2.6.
CREATE TRIGGER supergenero_de_si_mismo
BEFORE INSERT ON generoSupergenero
WHEN NEW.superGenero = NEW.identificador
BEGIN
SELECT RAISE(ABORT, 'Un género no puede ser su propio supergénero');
END;
