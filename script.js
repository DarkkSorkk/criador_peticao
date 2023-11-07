
        $(document).ready(function() {
            $("#petition-form").submit(function(event) {
                event.preventDefault();
        
                var formData = {
                    lawyerName: $("#lawyerName").val(),
                    oabNumber: $("#oabNumber").val(),
                    clientName: $("#clientName").val(),
                    caseFacts: $("#caseFacts").val(),
                    petitionType: $("#petitionType").val(),
                    processNumber: $("#processNumber").val(),
                    courtDistrict: $("#courtDistrict").val()
                }            
        
                // Desabilita o botão de enviar e mostra o indicador de carregamento
                $("#submit-button").prop('disabled', true);
                $("#loading-indicator").show();
        
                $.ajax({
                    type: "POST",
                    url: "http://localhost:5000/submit_form",
                    contentType: "application/json",
                    data: JSON.stringify(formData),
                    success: function(response) {
                        console.log("Resposta recebida do Flask:", response);
                        // Esconde o indicador de carregamento e habilita o botão
                        $("#loading-indicator").hide();
                        $("#submit-button").prop('disabled', false);
        
                        // Exibe a resposta no DOM
                        $("#response-container").html(response.response);
                    },
                    error: function(err) {
                        $("#loading-indicator").hide();
                        $("#submit-button").prop('disabled', false);
                        console.log(err);
                        $("#response-container").html("Erro ao enviar formulário.");
                    }
                });
            });
        });
        