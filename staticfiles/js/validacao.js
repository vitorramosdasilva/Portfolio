   $("#form_contato").validate({
      rules : {
            name: {
					required: true,
					minlength: 5,
					maxlength: 50
				},
			email: {
					required: true,
					maxlength: 50,
				    email: true
				},
			message: {
					required: true,
					minlength: 10,
					maxlength: 400
				},
			subject: {
					required: true,
					minlength: 5,
					maxlength: 100
				},
			captcha: {
			        required: true
			}
       },
      messages:{
            name:{
                    required:"Por favor, informe seu nome",
                    minlength:"O nome deve ter pelo menos 5 caracteres",
                    maxlength:"O nome deve ter no máximo 50 caracteres"
            },
             email:{
                    required:"É necessário informar um email",
                    maxlength:"O email deve ter no máximo 50 caracteres"
             },
             message:{
                    required:"A mensagem não pode ficar em branco",
                    minlength:"A menssagem deve ter pelo menos 10 caracteres",
                    maxlength:"O menssagem deve ter no máximo 40 caracteres"
             },
            subject:{
                    required:"O assunto não pode ficar em branco",
                    minlength:"O assunto deve ter pelo menos 5 caracteres",
                    maxlength:"O assunto deve ter no máximo 400 caracteres"
             },
             captcha: {
                    required:"A Captcha não poder estar vazia"
            }
       }
});
