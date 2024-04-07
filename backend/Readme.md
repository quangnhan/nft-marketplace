## Start celery beat
- celery -A main beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
- celery -A main worker -l INFO --pool=solo
- celery -A main status

## Kill beat process
- ps aux | grep 'celery -A main beat'
- kill <PID>