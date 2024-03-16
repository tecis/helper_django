# how to display view html in terminal

from django.contrib.auth.models import User
from django.test import RequestFactory
from operation.views import ProductionLogListView

# 1. Make request.
request = RequestFactory().get('/operation/productionlog/')
# 2. Asign user to request.
request.user = User.objects.get(id=1)
# 3. Create instance of view.
view = ProductionLogListView()
# 4. Setup view.
view.setup(request)
# 5. Get data.
response = view.get(request)
# 6. View context.
context = view.get_context_data()
# 7. View HTML.
#   7.1 Render view.
response = response.render()
#   7.2 Show HTML content.
print(response.content.decode())
