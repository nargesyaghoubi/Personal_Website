from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        massage_name = request.POST['massage_name']
        massage_email = request.POST['massage_email']
        subject = request.POST['subject']
        massage = request.POST['massage']
        msg = "name:\n{0}\nemail:\n{1}\nmessage:\n{2}".format(massage_name, massage_email, massage, subject)
        send_mail(
                  subject,
                  msg,
                  'nargesyaghoubi8007@gmail.com',
                  ['nargesyaghoubi8007@gmail.com'],
                  fail_silently=False)

        return render(request, template_name='contact.html', context={'massage_name': massage_name})

    else:
        return render(request, template_name='index.html')
