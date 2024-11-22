--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    category_name character varying(50)
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: payment_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment_list (
    id integer NOT NULL,
    pay_day date,
    category_id integer,
    pay_name character varying(100),
    pay_count smallint,
    pay_cost double precision,
    user_id integer
);


ALTER TABLE public.payment_list OWNER TO postgres;

--
-- Name: payment_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payment_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.payment_list_id_seq OWNER TO postgres;

--
-- Name: payment_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.payment_list_id_seq OWNED BY public.payment_list.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    fio character varying(200),
    login character varying(100),
    password character varying(200),
    pin_code smallint
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: payment_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment_list ALTER COLUMN id SET DEFAULT nextval('public.payment_list_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, category_name) FROM stdin;
1	Коммунальные платежи
2	Автомобиль
3	Питание и быт
4	Медицина
5	Разное
\.


--
-- Data for Name: payment_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payment_list (id, pay_day, category_id, pay_name, pay_count, pay_cost, user_id) FROM stdin;
61	2016-11-15	3	Еда	1	195.39	30
62	2016-11-16	3	Гипермаркет	1	3726	40
63	2016-11-17	3	Гипермаркет	1	2484	50
64	2016-11-18	3	Макароны	1	33	60
65	2016-11-19	3	Еда	1	144.75	70
66	2016-11-20	3	Еда	1	138.73	10
67	2016-11-21	3	Еда	1	24	20
68	2016-11-22	3	Еда	1	261.21	30
69	2016-11-23	3	Столовая	1	19.42	40
70	2016-11-24	3	Еда	1	80	50
71	2016-11-25	3	Столовая	1	58.86	60
72	2016-11-26	3	Еда	1	82	70
73	2016-11-27	3	Еда	1	81	10
74	2016-11-01	4	Прием врача	1	450	20
75	2016-11-03	4	Прием врача	1	400	30
76	2016-11-05	4	Прием врача	1	330	40
77	2016-11-07	4	ЭКГ	1	455	50
78	2016-11-09	4	Анализы	1	280	60
79	2016-11-11	4	Прием врача	1	220	70
80	2016-11-13	4	Контейнер для анализов	1	20	10
81	2016-11-15	4	Лекарства	1	449.5	20
82	2016-11-17	4	Лекарства	1	202.4	30
83	2016-11-19	4	Прием врача	1	800	40
95	2016-11-22	5	Маркеры	1	120	20
96	2016-11-25	1	Организационный сбор	2	500	30
100	2024-11-22	1	dddd	1	0.01	60
38	2016-11-01	1	Квартплата	1	2964.58	10
39	2016-11-01	1	Интернет	1	450	20
40	2016-11-01	1	Телефон	1	170	30
41	2016-11-01	1	Мобильный	1	300	40
42	2016-11-01	1	Электроэнергия	1	184	50
43	2016-11-01	1	Газоснабжение	1	3120	60
44	2016-11-01	1	Водоснабжение	1	16.41	70
45	2016-11-01	2	Взнос за гараж	1	5000	10
46	2016-11-30	2	Бензин	1	2238	20
47	2016-11-01	3	Сметана	1	45	30
48	2016-11-02	3	Томатный сок	1	15	40
49	2016-11-03	3	Губка для обуви	1	40	50
50	2016-11-04	3	Еда	1	159.2	60
51	2016-11-05	3	Булочки и тесто	1	240	70
52	2016-11-06	3	Творог и сметана	1	94.96	10
53	2016-11-07	3	Семечки	2	35	20
54	2016-11-08	3	Хачапури и морс	1	82	30
55	2016-11-09	3	Столовая	1	119.93	40
56	2016-11-10	3	Столовая	1	127.66	50
57	2016-11-11	3	Еда	1	258.84	60
58	2016-11-12	3	Еда	1	213.31	70
59	2016-11-13	3	Еда	1	137.18	10
60	2016-11-14	3	Еда	1	127.82	20
84	2016-11-21	4	Прием врача	1	400	50
85	2016-11-23	4	Анализы	1	1740	60
86	2016-11-25	4	Термометр для ванн	1	152.5	70
87	2016-11-27	4	Юниспорт	1	3500	10
88	2016-11-01	5	Туфли	1	699	20
89	2016-11-04	5	Диски, кейс, стяжки	1	933	30
90	2016-11-07	5	Маникюр	1	550	40
91	2016-11-10	5	Ушивание брюк	1	150	50
92	2016-11-13	5	Одежда	1	2871.84	60
93	2016-11-16	5	Плавательный набор	1	1040	70
94	2016-11-19	5	CD	1	165	10
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, fio, login, password, pin_code) FROM stdin;
10	Бойко Игорь Петрович	Boico	$2b$12$T6aOV5ccN/iJv91pD9DG9eUMkhlk8aWWrhLMtaqBa/fDVBGwt.22u	6039
20	Василенко Василий Александрович	Vasilenco	$2b$12$KHrByuQpU2z/ro3pXD5So.fRgfmhIpPBycmktTZa2JfYii7mT/xYu	8797
30	Контеенко Дмитрий Семенович	Konteenco	$2b$12$JgzdUqb05cKirFe2zSe3Yu1P9wM0rwf7.iU0iQEDAGY/iJvKdj0ne	961
40	Лазарьков Петр Михайлович	Lazarkov	$2b$12$4qXjOiuOxOiCsd81.dSD/OJBAmVXrsXybXDl5jGL1GQI3egRQsto6	4842
50	Кузнецов Василий Семенович	Kuznetsov	$2b$12$T5R7IoGD/mCasm1DstnXu.YEK/9tJGM4ry/3CxkmJuNVC4IcF2dky	8720
60	Дорофеева Анна Геннадьевна	Test	$2b$12$ri4IONdNdzREgAQjpnGnSuKBiA3WiGb8QjvzOOrXTQye6XJArlTBK	9812
70	Прокопьева Елена Петровна	Ann	$2b$12$h31EcU1czPRknaqbRQfCXOkfqWvVFcjX4P4vLcV1Qf2bsj4TJW4yK	9553
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 5, true);


--
-- Name: payment_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payment_list_id_seq', 100, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: payment_list payment_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: payment_list payment_list_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- Name: payment_list payment_list_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

