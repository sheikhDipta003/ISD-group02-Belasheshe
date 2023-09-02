from django.shortcuts import render
from residents.models import Member, ResidentMedCond, MedCond

# Create your views here.
def doctor_dashboard(request):
    return render(request, 'doctors/dashboard.html')

from django.shortcuts import render
from residents.models import Member, ResidentMedCond, MedCond

def member_medical_conditions(request):
    # Retrieve all members and their associated medical conditions
    members = Member.objects.all()
    medical_conditions = []

    for member in members:
        # Retrieve the member's general information
        member_info = {
            'name': member.Name,
            'address': member.Address,
            'room_no': member.Room_no,
            'email': member.Email,
            'phone': member.Phone,
            'dob': member.DOB,
            'religion': member.Religion,
        }

        # Retrieve the medical conditions for each member
        med_conditions = ResidentMedCond.objects.filter(Member_ID=member.Member_ID)
        med_condition_info = []

        for med_cond in med_conditions:
            # Retrieve the details of each medical condition
            condition = MedCond.objects.get(Cond_ID=med_cond.Cond_ID)
            med_condition_info.append({
                'condition_name': condition.Name,
                'advice': condition.Advice,
                'guideline': condition.Guideline,
            })

        medical_conditions.append({
            'member_info': member_info,
            'conditions': med_condition_info,
        })

    return render(request, 'doctors/medical_conditions.html', {'medical_conditions': medical_conditions})
