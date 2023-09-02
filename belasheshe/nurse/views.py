from django.shortcuts import render, redirect
from django.views import View
from residents.models import Member
from .models import Medicine, MedicineChart,Dosage,CheckupSchedule,CheckupItem

class DashboardView(View):
    template_name = 'nurse/dashboard.html'  # Update with your actual template name

    def getMedicineSchedule(nurse_id):
        members = Member.objects.filter(Nurse_id=nurse_id)
        rows=[]
        for member in members:
            medicine_chart=MedicineChart.objects.filter(Member_id=member.Mem_id)
            dosage=Dosage.objects.filter(Chart_id=medicine_chart.Chart_id)
            medicine_name=Medicine.objects.filter(Medicine_id=dosage.Medicine_id).Name
            data = {
                'name': medicine_name,
                'time': dosage.Time,
                'quantity': dosage.Quantity
            }
            rows.append(data)

        sorted_rows = sorted(rows, key=lambda row: row['time'])
        return sorted_rows

    def getCheckupSchedule(nurse_id,date):
        checkups = CheckupSchedule.objects.filter(Nurse_id=nurse_id,Date=date).order_by('Time')
        rows=[]
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            data = {
                'item': checkup_item,
                'time': checkup.Time,
            }
            rows.append(data)
        return rows

    def get(self, request, nurse_id,date, *args, **kwargs):
        schedules= self.getMedicineSchedule(nurse_id)
        schedules.append(self.getCheckupSchedule(nurse_id, date))
        sorted_rows = sorted(schedules, key=lambda row: row['time'])
        return render(request, self.template_name, {'schedules': schedules})

class CheckupDataEntryView(View):
    template_name = 'nurse/addCheckupData.html'  # Update with your actual template name
    def get(self, request,*args, **kwargs):
        return render(request, self.template_name)

    def addData(self,request,*args, **kwargs):
        if request.method == 'POST':
            # Get data from the POST request
            bp = request.POST.get('Blood_pressure')
            sugar = request.POST.get('Sugar')
            hr = request.POST.get('Heartrate')

            # Create a new instance of MyModel and set values
            new_instance = CheckupItem(Blood_pressure=bp, Sugar=sugar, Heartrate=hr)

            # Save the instance to the database
            new_instance.save()
            return redirect('success_page')

# fetches all the checkup data for all members and sorts them according to BloodPressure, Sugar and Heartrate as the user desires
class CheckupDataListView(View):
    template_name = 'nurse/checkup_data_list.html'  # Update with your actual template name

    def get_checkup_data(self, order_by):
        checkup_data = (
            CheckupSchedule.objects
            .filter(completed=True)  # Filter completed checkups, adjust as needed
            .order_by(order_by)  # Order by the selected field (Blood_pressure, Sugar, or Heartrate)
        )
        return checkup_data

    def get(self, request, *args, **kwargs):
        # Determine the desired order field from the query parameter (default to Blood_pressure)
        order_by = request.GET.get('order_by', 'Blood_pressure')

        # Get the sorted checkup data
        sorted_checkup_data = self.get_checkup_data(order_by)

        return render(request, self.template_name, {'checkup_data': sorted_checkup_data})


class ResidentConditionView(View):
    template_name = 'nurse/residentCondition.html'  # Update with your actual template name

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def retrieveData(self, request, nurse_id, *args, **kwargs):
        checkups = CheckupSchedule.objects.filter(Nurse_id=nurse_id, Completed="true")
        rows = []
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            bp = checkup_item.Blood_pressure
            sugar = checkup_item.Sugar
            hr = checkup_item.Heartrate

            bpRiskRate=self.getRiskRate(bp)
            sugarRiskRate=self.getSugarRiskRate(sugar)
            riskrate=max(bpRiskRate,sugarRiskRate)
            data = {
                'memid':checkup.Member_id,
                'checkupid':checkup.Checkup_id,
                'bp': bp,
                'sugar':sugar,
                'riskrate': riskrate
            }
            rows.append(data)
        sorted_rows = sorted(rows, key=lambda row: row['riskrate'])
        return sorted_rows

    def getSugarRiskrate(self, sugar):
        riskrate = 0
        if (sugar >= 5 and sugar <= 6.5):
            riskrate = 0
        elif (sugar >= 6.5 and sugar <= 6.9):
            riskrate = 1
        elif (sugar >= 7 and sugar <= 12):
            riskrate = 2
        elif (sugar >= 12):
            riskrate = 3
        return riskrate

    def getBpRiskrate(self, bp):
        riskrate = 0
        if (bp >= 115 and bp <= 125):
            riskrate = 0
        elif (bp >= 125 and bp <= 135):
            riskrate = 1
        elif (bp >= 135 and bp <= 160):
            riskrate = 2
        elif (bp >= 160):
            riskrate = 3
        return riskrate

    # def reportDoctor(self, request, member_id,*args, **kwargs):
