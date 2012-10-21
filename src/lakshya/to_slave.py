from django.contrib.contenttypes.models import ContentType

content_type_names = [
    "user",
    "team member",
    "person",
    "Donation Fund",
    "scholarship application",
    "scholar",
    "content type",
    "donation",
    "expense",
    "family detail",
    "grade update",
    "group",
    "innovation application",
    "innovation",
    "innovation payment",
    "innovation update",
    "innovation update image",
    "innovation update video",
    "lakshya update",
    "lakskhya testimonial",
    "log entry",
    "migration history",
    "other exam performance",
    "other scholarship",
    "payment temp",
    "permission",
    "person_preference",
    "repayment",
    "scholar academic update",
    "scholar update",
    "scholarship payment",
    "scholarship verification",
    "session",
    "sgpa",
]

content_types = []

for name in content_type_names:
    content_types.append(ContentType.objects.get(name=name))

def run():

 def do(Table):
  if Table is not None:
   table_objects = Table.objects.all()
   for i in table_objects:
    i.save(using='slave')
 
 ContentType.objects.using('slave').all().delete()

 for i in content_types:
  do(i.model_class())
