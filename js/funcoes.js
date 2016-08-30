function minhaFuncao1()
{
  $('#area1').css({
    color: '#ff0000',
    textTransform: 'uppercase',
    width: '75%'
  });

};

function minhaFuncao2()
{
  $('#area2').empty();

  var alunos = ['aluno01', 'aluno02', 'aluno03'];

  // $.each(alunos, function(index, value){
  //   $('#area2').append(value);
  // });
  for (i = 0; i < alunos.length; i++) {
    $('#area2').append(alunos[i]);
  }

};

function minhaFuncao3()
{
  $('#area2').empty();

  var alunos = [
    {
      nome: 'Aluno1',
      idade: 11
    },

    {
      nome: 'Aluno2',
      idade: 23
    },

    {
      nome: 'Aluno3',
      idade: 44
    }
  ];

  for (i = 0; i < alunos.length; i++) {
    console.log(alunos[i]);
  }

  var list = $('#area2').append('<ul></ul>').find('ul');
  $.each(alunos, function(index, value) {
    list.append('<li>' + value.nome + ' - ' + value.idade + '</li>');


  });



};
