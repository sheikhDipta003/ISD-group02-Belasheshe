from django.shortcuts import render, redirect
from django.views import View
from nurse.models import MemberAppoint, MedicineChart,Medicine,Dosage, SpecialCheckupSchedule, CheckupSchedule
from residents.models import CheckupItem
# from .models import Doctor

# Create your views here.
# def doctor_dashboard(request):
#     return render(request, 'doctors/dashboard.html')

# def member_medical_conditions(request):
#     # Retrieve all members with associated medical conditions and current conditions
#     members = Member.objects.all()
    
#     # Sort members based on Risk_rate (ascending order)
#     members = members.order_by('currentcond__Risk_rate')

#     # Paginate the members list (adjust the items per page as needed)
#     paginator = Paginator(members, 10)  # Show 10 members per page
#     page_number = request.GET.get('page')
#     page_members = paginator.get_page(page_number)

#     medical_conditions = []

#     for member in page_members:
#         # Retrieve the member's general information
#         member_info = {
#             'name': member.Name,
#             'address': member.Address,
#             'room_no': member.Room_no,
#             'email': member.Email,
#             'phone': member.Phone,
#             'dob': member.DOB,
#             'religion': member.Religion,
#         }

#         # Retrieve the medical conditions for each member
#         med_conditions = ResidentMedCond.objects.filter(Member_ID=member.Member_ID)
#         med_condition_info = []

#         for med_cond in med_conditions:
#             # Retrieve the details of each medical condition
#             condition = MedCond.objects.get(Cond_ID=med_cond.Cond_ID)
#             med_condition_info.append({
#                 'condition_name': condition.Name,
#                 'advice': condition.Advice,
#                 'guideline': condition.Guideline,
#             })

#         # Retrieve the current condition for each member
#         try:
#             current_condition = CurrentCond.objects.get(Member_ID=member.Member_ID)
#             risk_rate = current_condition.Risk_rate
#         except CurrentCond.DoesNotExist:
#             risk_rate = None

#         medical_conditions.append({
#             'member_info': member_info,
#             'conditions': med_condition_info,
#             'risk_rate': risk_rate,
#         })

#     return render(request, 'doctors/medical_conditions.html', {'medical_conditions': medical_conditions, 'page_members': page_members})


class DashboardView(View):
    template_name = 'doctors/dashboard.html'  # Update with your actual template name

    def getAppointments(self,doctor_id,date):
        appoints = MemberAppoint.objects.filter(Doctor_ID=doctor_id,Date=date)
        sorted_rows = sorted(appoints, key=lambda row: row['Time'])
        return sorted_rows

    def getCheckups(self,doctor_id):
        checkups=CheckupSchedule.objects.filter(Doctor_ID=doctor_id)
        specialCheckups=SpecialCheckupSchedule.objects.filter(Doctor_ID=doctor_id)
        rows = []
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            data = {
                'item': checkup_item,
                'type': "regular checkup",
                'riskrate': checkup.Riskrate,
            }
            rows.append(data)

        for checkup in specialCheckups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            data = {
                'item': checkup_item,
                'type': "special checkup",
                'riskrate': checkup.Riskrate,
            }
            rows.append(data)

        sorted_rows = sorted(rows, key=lambda row: row['riskrate'])
        return sorted_rows

    def get(self, request, doctor_id, date, *args, **kwargs):
        appointments = self.getAppointments(doctor_id)
        checkups=self.getCheckups(doctor_id)
    # def get(self, request, *args, **kwargs):  # testing
    #     appointments =[]
    #     checkups=[]
        return render(request, self.template_name, {'appointments': appointments, "checkups": checkups})

class addSuggesions(View):
    template_name = 'doctors/addPrescription.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def addPrescriptopn(self, request, member_id):
        if request.method == 'POST':
            # Get data from the POST request
            medicine_name = request.POST.get('medicine_name')
            time = request.POST.get('time')
            quantity = request.POST.get('quantity')
            duration= request.POST.get('duration')
            date = request.POST.get('date')

            medicine_id = Medicine.objects.filter(Name=medicine_name)

            new_instance = MedicineChart(Member_id=member_id, Date=date)
            new_instance.save()

            chart_id=new_instance.Chart_id

            instance = Dosage(Chart_id=chart_id, Medicine_id=medicine_id, Time=time, Quantity=quantity)
            instance.save()
            return redirect('success_page')

class createAppointment(View):
    template_name = 'doctors/createAppointment.html'  # Update with your actual template name
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def addAppointment(self, request, doctor_id,member_id):
        if request.method == 'POST':
            # Get data from the POST request
            member_id = request.POST.get('member_id')
            time = request.POST.get('time')
            date = request.POST.get('date')

            new_instance = MemberAppoint(Member_ID=member_id, Doctor_ID=doctor_id)
            new_instance.save()
            return redirect('success_page')




