from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.services import excel_service
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/excel")

@router.get("/historial/{serial}")
def exportar_excel(
    serial: str,
    user = Depends(get_current_user)
    ):
    
    excel = excel_service.generar_excel_historial(serial)

    return StreamingResponse(
        excel,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=historial.xlsx"}
)