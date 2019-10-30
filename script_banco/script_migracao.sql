\copy migracao_no(nome,sexo,nascimento,pais,cidade,uf,datacadastramento,projeto,datacorrida,diasemana,horaretirada,estacaoretirada,areaestacaoretirada,enderecoestacaoretirada,meioretirada,horadevolucao,
estacaodevolucao,areaestacaodevolucao,enderecoestacaodevolucao,duracaocorrida) 
from '/media/renato/SSD/desenvolvimento/python/dados/-bikebrasilia09-2019---sem-os-dados-pessoais.ods' ods;


insert into rotas_estado(estado) values ('AC');
insert into rotas_estado(estado) values ('AL');
insert into rotas_estado(estado) values ('AM');
insert into rotas_estado(estado) values ('AP');
insert into rotas_estado(estado) values ('BA');
insert into rotas_estado(estado) values ('CE');
insert into rotas_estado(estado) values ('DF');
insert into rotas_estado(estado) values ('ES');
insert into rotas_estado(estado) values ('GO');
insert into rotas_estado(estado) values ('MA');
insert into rotas_estado(estado) values ('MG');
insert into rotas_estado(estado) values ('MS');
insert into rotas_estado(estado) values ('MT');
insert into rotas_estado(estado) values ('PA');
insert into rotas_estado(estado) values ('PB');
insert into rotas_estado(estado) values ('PE');
insert into rotas_estado(estado) values ('PI');
insert into rotas_estado(estado) values ('PR');
insert into rotas_estado(estado) values ('RJ');
insert into rotas_estado(estado) values ('RN');
insert into rotas_estado(estado) values ('RO');
insert into rotas_estado(estado) values ('RR');
insert into rotas_estado(estado) values ('RS');
insert into rotas_estado(estado) values ('SC');
insert into rotas_estado(estado) values ('SE');
insert into rotas_estado(estado) values ('SP');
insert into rotas_estado(estado) values ('TO');



update migracao_no set pop_env =  '1' where migracao_no.pop_env = 'PoP-AC';
update migracao_no set pop_dest =  '1' where migracao_no.pop_dest = 'PoP-AC';

update migracao_no set pop_env =  '2' where migracao_no.pop_env = 'PoP-AL';
update migracao_no set pop_dest =  '2' where migracao_no.pop_dest = 'PoP-AL';

update migracao_no set pop_env =  '3' where migracao_no.pop_env = 'PoP-AM';
update migracao_no set pop_dest =  '3' where migracao_no.pop_dest = 'PoP-AM';

update migracao_no set pop_env =  '4' where migracao_no.pop_env = 'PoP-AP';
update migracao_no set pop_dest =  '4' where migracao_no.pop_dest = 'PoP-AP';

update migracao_no set pop_env =  '5' where migracao_no.pop_env = 'PoP-BA';
update migracao_no set pop_dest =  '5' where migracao_no.pop_dest = 'PoP-BA';

update migracao_no set pop_env =  '6' where migracao_no.pop_env = 'PoP-CE';
update migracao_no set pop_dest =  '6' where migracao_no.pop_dest = 'PoP-CE';

update migracao_no set pop_env =  '7' where migracao_no.pop_env = 'PoP-DF';
update migracao_no set pop_dest =  '7' where migracao_no.pop_dest = 'PoP-DF';

update migracao_no set pop_env =  '8' where migracao_no.pop_env = 'PoP-ES';
update migracao_no set pop_dest =  '8' where migracao_no.pop_dest = 'PoP-ES';

update migracao_no set pop_env =  '9' where migracao_no.pop_env = 'PoP-GO';
update migracao_no set pop_dest =  '9' where migracao_no.pop_dest = 'PoP-GO';

update migracao_no set pop_env =  '10' where migracao_no.pop_env = 'PoP-MA';
update migracao_no set pop_dest =  '10' where migracao_no.pop_dest = 'PoP-MA';

update migracao_no set pop_env =  '11' where migracao_no.pop_env = 'PoP-MG';
update migracao_no set pop_dest =  '11' where migracao_no.pop_dest = 'PoP-MG';

update migracao_no set pop_env =  '12' where migracao_no.pop_env = 'PoP-MS';
update migracao_no set pop_dest =  '12' where migracao_no.pop_dest = 'PoP-MS';

update migracao_no set pop_env =  '13' where migracao_no.pop_env = 'PoP-MT';
update migracao_no set pop_dest =  '13' where migracao_no.pop_dest = 'PoP-MT';

update migracao_no set pop_env =  '14' where migracao_no.pop_env = 'PoP-PA';
update migracao_no set pop_dest =  '14' where migracao_no.pop_dest = 'PoP-PA';

update migracao_no set pop_env =  '15' where migracao_no.pop_env = 'PoP-PB';
update migracao_no set pop_dest =  '15' where migracao_no.pop_dest = 'PoP-PB';

update migracao_no set pop_env =  '16' where migracao_no.pop_env = 'PoP-PE';
update migracao_no set pop_dest =  '16' where migracao_no.pop_dest = 'PoP-PE';

update migracao_no set pop_env =  '17' where migracao_no.pop_env = 'PoP-PI';
update migracao_no set pop_dest =  '17' where migracao_no.pop_dest = 'PoP-PI';

update migracao_no set pop_env =  '18' where migracao_no.pop_env = 'PoP-PR';
update migracao_no set pop_dest =  '18' where migracao_no.pop_dest = 'PoP-PR';

update migracao_no set pop_env =  '19' where migracao_no.pop_env = 'PoP-RJ';
update migracao_no set pop_dest =  '19' where migracao_no.pop_dest = 'PoP-RJ';

update migracao_no set pop_env =  '20' where migracao_no.pop_env = 'PoP-RN';
update migracao_no set pop_dest =  '20' where migracao_no.pop_dest = 'PoP-RN';

update migracao_no set pop_env =  '21' where migracao_no.pop_env = 'PoP-RO';
update migracao_no set pop_dest =  '21' where migracao_no.pop_dest = 'PoP-RO';

update migracao_no set pop_env =  '22' where migracao_no.pop_env = 'PoP-RR';
update migracao_no set pop_dest =  '22' where migracao_no.pop_dest = 'PoP-RR';

update migracao_no set pop_env =  '23' where migracao_no.pop_env = 'PoP-RS';
update migracao_no set pop_dest =  '23' where migracao_no.pop_dest = 'PoP-RS';

update migracao_no set pop_env =  '24' where migracao_no.pop_env = 'PoP-SC';
update migracao_no set pop_dest =  '24' where migracao_no.pop_dest = 'PoP-SC';

update migracao_no set pop_env =  '25' where migracao_no.pop_env = 'PoP-SE';
update migracao_no set pop_dest =  '25' where migracao_no.pop_dest = 'PoP-SE';

update migracao_no set pop_env =  '26' where migracao_no.pop_env = 'PoP-SP';
update migracao_no set pop_dest =  '26' where migracao_no.pop_dest = 'PoP-SP';

update migracao_no set pop_env =  '27' where migracao_no.pop_env = 'PoP-TO';
update migracao_no set pop_dest =  '27' where migracao_no.pop_dest = 'PoP-TO';


insert into rotas_no (data_migration, perda_mdn, lat_min, lat_med, lat_max, std_dvn, lat_ten_perc, lat_mdn, lat_nine_perc, pop_dest_id, pop_env_id)
	select data_migration, perda_mdn, lat_min, lat_med, lat_max, std_dvn, lat_ten_perc, lat_mdn, lat_nine_perc, cast(pop_dest as INTEGER), cast(pop_env as INTEGER) from migracao_no;


insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (1,7,true), (1,21,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (2,16,true), (2,25,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (3,7,true), (3,22,true), (3,14,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (4,14,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (5,11,true), (5,8,true),(5,25,true), (5,16,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (6,20,true), (6,10,true),(6,22,true),(6,11,true),(6,7,true), (6,26,true), (6,16,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (7,6,true), (7,11,true),(7,9,true),(7,1,true),(7,26,true),(7,19,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (8,5,true), (8,19,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (9,7,true), (9,13,true), (9,27,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (10,6,true), (10,14,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (11,6,true), (11,7,true), (11,5,true),(11,26,true),(11,19,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (12,13,true), (12,18,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (13,21,true), (13,12,true), (13,9,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (14,10,true), (14,17,true), (14,27,true),(14,3,true),(14,4,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (15,20,true), (15,16,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (16,15,true), (16,5,true), (16,17,true), (16,6,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (17,14,true), (17,16,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (18,23,true), (18,26,true),(18,12,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (19,11,true), (19,7,true), (19,26,true), (19,8,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (20,15,true), (20,6,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (21,13,true), (21,1,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (22,6,true), (22,3,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (23,24,true), (23,18,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (24,23,true), (24,26,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (25,2,true), (25,5,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (26,18,true), (26,7,true), (26,11,true), (26,6,true);

insert into rotas_ligacao(origem_id, destino_id, link_ativo) values (27,9,true),(27,14,true);
