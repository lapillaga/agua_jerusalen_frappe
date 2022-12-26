frappe.views.calendar["Periodo Pago"] = {
    field_map: {
        "start": "start_date",
        "end": "end_date",
        "id": "name",
        "title": "description",
        "status": "status",
        "allDay": "allDay"
    },
    style_map: {
        Public: 'success',
        Private: 'info'
    },
    gantt: {
        order_by: 'start_date',
    },
    order_by: 'end_date',
    get_events_method: 'agua_jerusalen_frappe.junta_de_agua_potable_jerusalen.doctype.periodo_pago.periodo_pago.get_periods'
}
