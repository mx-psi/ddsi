-- Script para creación de disparadores

CREATE TRIGGER inserta_producto
BEFORE UPDATE OF idPadre ON productoCulturalPadre
WHEN NEW.idPadre = old.id
BEGIN
-- TODO?:  Evitar que un nodo tenga como padre a uno de sus hijos/nietos...
SELECT RAISE(ABORT, 'Un producto cultural no puede ser su propio padre');
END;
