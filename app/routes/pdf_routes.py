from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.services import pdf_service
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/pdf")

@router.get("/historial/{serial}")
def exportar_historial(
    serial: str,
    user: dict = Depends(get_current_user)
    ):
    
    pdf = pdf_service.generar_pdf_historial(serial)
    
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=historial.pdf"}
)