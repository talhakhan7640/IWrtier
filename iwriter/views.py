from django.shortcuts import render, redirect
import requests
from users.models import userSubscriptions
from django.contrib.auth.models import User
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import PostRequests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY

KEY = 'e5bee020-fdd2-443f-af0b-70dc475b3517'

tempUserHolder = ''
trialRequests = 0

class CreateCheckoutSessionView(View):
    global tempUserHolder
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(

            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LE7pJSEVlRAykiPJCbR7FVb',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        print('button pressed')
        tempUserHolder = request.user
        return redirect(checkout_session.url, code=303)

@login_required
def SuccessPage(request):
    return render(request, 'iwriter/success.html')

@login_required
def CancelPage(request):
    return render(request, 'iwriter/cancel.html')

@login_required
def home(request):
    global trialRequests
    global tempUserHolder

    aiText = ''
    topic = ''
    outOfTrialMessage = ''
    current_status = False

    current_user = userSubscriptions.objects.filter(user=request.user).first()
    print(current_user)
    if current_user != None:
        current_status = True
    else:
        current_status = False


    print(current_status)
    
    if request.method == "POST":
        tempUserHolder = request.user
        user = userSubscriptions.objects.filter(user=request.user).first()
        if user != None:
            status = userSubscriptions.objects.filter(user=request.user).first().subStatus
            if status:
                topic = request.POST['topic']
                r = requests.post(
                    "https://api.deepai.org/api/text-generator",
                data={
                    'text': topic,
                },
                headers={'api-key': KEY}
                )
                aiText = r.json()['output']
        else:

            create_user_instance, created = PostRequests.objects.get_or_create(user=request.user)

            if create_user_instance.post_request < 3:
                        
                create_user_instance.post_request = create_user_instance.post_request + 1
                create_user_instance.save()
                print(create_user_instance.post_request)

                topic = request.POST['topic']
                r = requests.post(
                    "https://api.deepai.org/api/text-generator",
                data={
                    'text': topic,
                },
                headers={'api-key': KEY}
                )
                aiText = r.json()['output']

            else:
                outOfTrialMessage = 'you ran out of trials. Please consider subscribing.'
        
    return render(request, 'iwriter/home.html', {'text': aiText, 'topic': topic, 'trialMessage': outOfTrialMessage, 'current_status': current_status })

@csrf_exempt
def stripe_webhook(request):
    global tempUserHolder

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

     # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        userSubscriptions.objects.create(user=tempUserHolder)
        currentUser = userSubscriptions.objects.get(user=tempUserHolder)
        currentUser.subStatus = True 
        currentUser.save()
        tempUserHolder = ''

        # Fulfill the purchase...
        print(session)

        # send Email 
        customer_email = session['customer_details']['email']
        send_mail(
            subject='From IWriter Creator',
            message='Thank you for subscribing on IWriter.',
            recipient_list=[customer_email],
            from_email='iwriter@support.com'
        )
   
    # Passed signature verification
    return HttpResponse(status=200)