from fastapi import FastAPI
import uvicorn
from scripts.config import app_configurations
from starlette.middleware.cors import CORSMiddleware
from scripts.core.services import consultant_request_service
from scripts.core.services import previous_templates_service
from scripts.core.services import get_projects_service
from scripts.core.services import profile_service
from scripts.core.services import common_service
from scripts.core.services import employee_list_service
from scripts.core.services import event_service
from scripts.core.services import interview_schedule_list_service
from scripts.core.services import project_details_service
from scripts.core.services import current_project_details_service
from scripts.core.services import company_projects_service
# from scripts.core.services import profile_upload_service
# from scripts.core.services import document_upload_service
from scripts.core.services import customer_schedule_interview_service
from scripts.core.services import send_notifications_service
from scripts.core.services import profile_upload_service
from scripts.core.services import document_upload_service
from scripts.core.services import project_employee_details_service
from scripts.core.services import fetch_common_status_service

from scripts.core.services import employees_shortlisted_service

from scripts.core.services import profile_get_service
app = FastAPI(
    title="On Boarding Portal",
    description="On-boarding Portal"
)

app.include_router(consultant_request_service.consultant_requirement)
app.include_router(get_projects_service.get_project)
app.include_router(profile_service.profile_router)
app.include_router(common_service.common_router)
app.include_router(employee_list_service.emp_list_process)
app.include_router(event_service.event_process)
app.include_router(interview_schedule_list_service.interview_list_process)
# app.include_router(profile_upload_service.profile_process)
# app.include_router(document_upload_service.document_process)
app.include_router(profile_upload_service.profile_process)
app.include_router(document_upload_service.document_process)
app.include_router(customer_schedule_interview_service.schedule_interview)
app.include_router(previous_templates_service.template_router)
app.include_router(project_details_service.get_project_details)
app.include_router(current_project_details_service.currProject_list_process)
app.include_router(company_projects_service.company_project)
app.include_router(profile_get_service.profile_get_process)
app.include_router(project_employee_details_service.project_employee_details)
app.include_router(fetch_common_status_service.employee_status_process)
app.include_router(employees_shortlisted_service.employee_shortlisted)


app.include_router(send_notifications_service.send_notification)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(app_configurations.PORT))
