from django.shortcuts import render
import io
from django.http import FileResponse

# Create your views here.
rep = """
        
        <div class="card">
              <div class="card-header">
                <h3 class="card-title"></h3>
              </div>
              <!-- /.card-header -->
              <div class="card-body">
                <table id="example2" class="table table-sm table-bordered ">
                  <thead>
                  <tr>
                    <th>اسم المرض</th>
                    <th>العدد</th>
                  </tr>
                  </thead>
                  <tbody>
                  """


def report(request):
   pass