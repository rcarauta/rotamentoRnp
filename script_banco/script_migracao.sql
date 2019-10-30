select  distinct  split_part(re.estacaoretirada, '-',1) as id, split_part(re.estacaoretirada, '-',2) as estacao 
from migracao_no re
except
select  distinct split_part(re.estacaodevolucao, '-',1) as id, split_part(re.estacaodevolucao, '-',2) as estacao 
from migracao_no re;

insert into rotas_estacao 
	select  distinct  cast(split_part(re.estacaoretirada, '-',1) as INTEGER) as id, split_part(re.estacaoretirada, '-',2) as estacao 
from migracao_no re;


insert into rotas_distancia 
	select id, nome, sexo, nascimento, pais, cidade, uf, datacadastramento, projeto, datacorrida, diasemana, horaretirada,
			 areaestacaoretirada, enderecoestacaoretirada, meioretirada, horadevolucao,areaestacaodevolucao, enderecoestacaodevolucao,
			 duracaocorrida, cast(split_part(estacaodevolucao, '-',1) as INTEGER), cast(split_part(estacaoretirada, '-',1) as INTEGER)
	from migracao_no;

