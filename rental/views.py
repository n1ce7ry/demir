from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rental.models import Proposal, ProposalStatusEnum
from main.models import CustomUser, Car


@login_required
def add_proposal(request):
    if request.method != 'POST':
        return redirect('home_page')

    proposal_data = request.POST

    user = CustomUser.objects.get(id=request.user.id)
    car = Car.objects.get(id=proposal_data.get('car_id'))

    Proposal.objects.create(
        user=user,
        car=car,
        date_start=proposal_data.get('trip-start'),
        date_end=proposal_data.get('trip-end'),
        total_price=proposal_data.get('price'),
        status=ProposalStatusEnum.CREATED
    )
    return redirect('profile')


@login_required
def delete_proposal(request, proposal_id):
    if request.method != 'POST':
        return redirect('home_page')

    Proposal.objects.get(id=proposal_id).delete()
    return redirect('profile')