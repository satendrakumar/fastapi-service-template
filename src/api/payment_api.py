from fastapi import APIRouter, status

from src.service import payment_service
from src.util.logger import get_logger

payment_api_router = APIRouter(prefix=f"/payment", tags=["payment"])

logger = get_logger(__name__)


@payment_api_router.get("/status",
                        summary="Get status",
                        response_description="Return HTTP Status Code 200 OK",
                        status_code=status.HTTP_200_OK,
                        )
async def get_payment_status():
    try:
        logger.info(f"Get payment status")
        payment_status = payment_service.get_status()
        return {"payment_status": payment_status}
    except Exception as err:
        logger.exception(f"Error in getting status:  {err}")
        return {"error": "Oops! something didn't go well, please try again"}
