# django-project

Some notes on Session:
https://docs.djangoproject.com/en/1.10/topics/http/sessions/#using-sessions-out-of-views

You can access session via 
1. SessionStore 
2. Session model 
3. request.session in a view

But you cannot modify session data via Session model. Unless you overwrite the session.session_data field, which is actually encoded.
If via Session model, you can only access session data via get_decoded().


You can access (udpdate) session out side a view via SessionStore.
Access SessionStore as dict.
