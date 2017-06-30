from django.contrib import admin
from .models import Register
from django.http import HttpResponse
# Register your models here.
def export_xls(modeladmin, request, queryset):
	# print(queryset)
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=profile.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Profile")
    
    row_num = 0
    
    columns = [
        (u"City", 4000),
        (u"Level", 2000),
        (u"Name", 6000),
        (u"email", 6000),
        (u"Phone", 1000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            obj.city,
            obj.level,
            obj.name,
            obj.email,
            obj.phone,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response

export_xls.short_description = u"Export XLS"


class RegisterAdmin(admin.ModelAdmin):
	actions = [export_xls,]

admin.site.register(Register, RegisterAdmin)

