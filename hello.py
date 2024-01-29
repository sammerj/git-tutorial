{% extends 'main.html' %}

{% block content %}
<div>
<form method="POST" action="">
    {% csrf_token %}
    <p>Are you sure you want to delete "{{obj}}"?</p>
    <a href="{{request.META.HTTP_REFERER}}">Go Back</a>
    
    <input type="submit" value="CONFIRM">
</form>
</div>

{% endblock content %}
