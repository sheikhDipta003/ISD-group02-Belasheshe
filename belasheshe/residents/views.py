from django.shortcuts import render
from django.views import View
from .models import Member, ResidentMedCond

class DashboardView(View):
    template_name = 'residents/dashboard.html'  # Update with your actual template name

    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        return render(request, self.template_name, {'members': members})

class ResidentPhyStatusView(View):
    template_name = 'residents/phyStat.html'  # Update with your actual template name

    def get(self, request, member_id, *args, **kwargs):
        member = Member.objects.get(Member_ID=member_id)
        phy_status = ResidentMedCond.objects.filter(Member_ID=member_id)
        # return render(request, self.template_name, {'member': member, 'phy_status': phy_status})
        return render(request, self.template_name, {'member': member, 'phy_status': phy_status})

# class PrescriptionListView(View):
#     template_name = 'prescription_list.html'  # Update with your actual template name

#     def get(self, request, member_id, *args, **kwargs):
#         member = Member.objects.get(Member_ID=member_id)
#         prescriptions = Prescription.objects.filter(Member_ID=member_id)
#         return render(request, self.template_name, {'member': member, 'prescriptions': prescriptions})
