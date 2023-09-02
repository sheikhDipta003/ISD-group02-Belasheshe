from django.shortcuts import render
from django.core.paginator import Paginator
from residents.models import Member, ResidentMedCond, MedCond, CurrentCond

# Create your views here.
def doctor_dashboard(request):
    return render(request, 'doctors/dashboard.html')

def member_medical_conditions(request):
    # Retrieve all members with associated medical conditions and current conditions
    members = Member.objects.all()
    
    # Sort members based on Risk_rate (ascending order)
    members = members.order_by('currentcond__Risk_rate')

    # Paginate the members list (adjust the items per page as needed)
    paginator = Paginator(members, 10)  # Show 10 members per page
    page_number = request.GET.get('page')
    page_members = paginator.get_page(page_number)

    medical_conditions = []

    for member in page_members:
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

        # Retrieve the current condition for each member
        try:
            current_condition = CurrentCond.objects.get(Member_ID=member.Member_ID)
            risk_rate = current_condition.Risk_rate
        except CurrentCond.DoesNotExist:
            risk_rate = None

        medical_conditions.append({
            'member_info': member_info,
            'conditions': med_condition_info,
            'risk_rate': risk_rate,
        })

    return render(request, 'doctors/medical_conditions.html', {'medical_conditions': medical_conditions, 'page_members': page_members})
