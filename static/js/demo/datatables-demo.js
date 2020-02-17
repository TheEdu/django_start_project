// Call the dataTables jQuery plugin
$(document).ready(function() {

  // Setup - add a text input to each footer cell
  $('#dataTable thead tr').clone(true).appendTo( '#dataTable thead' );
  $('#dataTable thead tr:eq(1) th').each( function (i) {
      var title = $(this).text();
      if (title != "Acciones") {
        $(this).html( '<input type="text" class="form-control filter-column-table" placeholder="'+title+'" />' );
        $(this).css('padding', '5px');
        $( 'input', this ).on( 'keyup change', function () {
          console.log("input: " + this.value)
          console.log(i, table_main.column(i))
            if ( table_main.column(i).search() !== this.value ) {
                table_main
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
      } else {
        $(this).html("");
      }
  } );

  const table_main = $('#dataTable').DataTable({
    bSort: true,
    bPaginate: true,
    bFilter: true,
    orderCellsTop: true,
    fixedHeader: true,
    lengthChange: false,
    lengthMenu: [ 5 ],
    language: {
      lengthMenu: "Mostrar _MENU_ registros por página",
      zeroRecords: "No hay datos para mostrar",
      info: "Página _PAGE_ de _PAGES_",
      infoEmpty: "No hay registros disponibles",
      infoFiltered: "(filtrado de _MAX_ registros)",
      search: "Buscar:",
      paginate: {
        "previous": "Anterior",
        "next": "Siguiente"
      }
    },
    buttons: [
            {
                extend: 'copyHtml5',
                text: 'Copiar',
                className: 'btn btn-warning py-0 px-1 mb-1',
                exportOptions: {
                    columns: '.export-col'
                }
            },
            {
                extend: 'excelHtml5',
                text: 'Excel',
                className: 'btn btn-success py-0 px-1 mb-1',
                exportOptions: {
                    columns: '.export-col'
                }
            },
            {
                extend: 'pdfHtml5',
                text: 'PDF',
                className: 'btn btn-danger py-0 px-1 mb-1',
                exportOptions: {
                    columns: '.export-col'
                }
            },
            {
                extend: 'print',
                text: 'Imprimir',
                className: 'btn btn-info py-0 px-1 mb-1',
                exportOptions: {
                    columns: '.export-col'
                }
            }
    ],
    dom: '<"col-12"B>rtl<"row"<"col-10"p><"col-2"i>>',
  });

  $('#dataTable_filter').hide();
});