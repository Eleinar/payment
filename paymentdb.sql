PGDMP         %            
    |         	   paymentdb     13.16 (Debian 13.16-1.pgdg120+1)    15.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17223 	   paymentdb    DATABASE     t   CREATE DATABASE paymentdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE paymentdb;
                admin    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                admin    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   admin    false    4            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   admin    false    4            �            1259    17226 
   categories    TABLE     e   CREATE TABLE public.categories (
    id integer NOT NULL,
    category_name character varying(50)
);
    DROP TABLE public.categories;
       public         heap    admin    false    4            �            1259    17224    categories_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public          admin    false    4    201            �           0    0    categories_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;
          public          admin    false    200            �            1259    17242    payment_list    TABLE     �   CREATE TABLE public.payment_list (
    id integer NOT NULL,
    pay_day date,
    category_id integer,
    pay_name character varying(100),
    pay_count smallint,
    pay_cost double precision,
    user_id integer
);
     DROP TABLE public.payment_list;
       public         heap    admin    false    4            �            1259    17240    payment_list_id_seq    SEQUENCE     �   CREATE SEQUENCE public.payment_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.payment_list_id_seq;
       public          admin    false    205    4            �           0    0    payment_list_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.payment_list_id_seq OWNED BY public.payment_list.id;
          public          admin    false    204            �            1259    17234    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    fio character varying(200),
    login character varying(100),
    password character varying(200),
    pin_code smallint
);
    DROP TABLE public.users;
       public         heap    admin    false    4            �            1259    17232    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          admin    false    4    203            �           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          admin    false    202            I           2604    17229    categories id    DEFAULT     n   ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);
 <   ALTER TABLE public.categories ALTER COLUMN id DROP DEFAULT;
       public          admin    false    201    200    201            K           2604    17245    payment_list id    DEFAULT     r   ALTER TABLE ONLY public.payment_list ALTER COLUMN id SET DEFAULT nextval('public.payment_list_id_seq'::regclass);
 >   ALTER TABLE public.payment_list ALTER COLUMN id DROP DEFAULT;
       public          admin    false    205    204    205            J           2604    17237    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          admin    false    203    202    203            �          0    17226 
   categories 
   TABLE DATA           7   COPY public.categories (id, category_name) FROM stdin;
    public          admin    false    201   K       �          0    17242    payment_list 
   TABLE DATA           h   COPY public.payment_list (id, pay_day, category_id, pay_name, pay_count, pay_cost, user_id) FROM stdin;
    public          admin    false    205   �       �          0    17234    users 
   TABLE DATA           C   COPY public.users (id, fio, login, password, pin_code) FROM stdin;
    public          admin    false    203   O        �           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 5, true);
          public          admin    false    200            �           0    0    payment_list_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.payment_list_id_seq', 37, true);
          public          admin    false    204            �           0    0    users_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.users_id_seq', 1, false);
          public          admin    false    202            M           2606    17231    categories categories_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            admin    false    201            Q           2606    17247    payment_list payment_list_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.payment_list DROP CONSTRAINT payment_list_pkey;
       public            admin    false    205            O           2606    17239    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            admin    false    203            R           2606    17248 *   payment_list payment_list_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);
 T   ALTER TABLE ONLY public.payment_list DROP CONSTRAINT payment_list_category_id_fkey;
       public          admin    false    205    201    2893            S           2606    17253 &   payment_list payment_list_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment_list
    ADD CONSTRAINT payment_list_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);
 P   ALTER TABLE ONLY public.payment_list DROP CONSTRAINT payment_list_user_id_fkey;
       public          admin    false    2895    205    203            �   s   x����@D�v� )|��� q	������`)ɦ���g�i�'���ol$�yOn�YHޑ�bz���.�Xe�$���S�V5k��N��+�9�{L���/B!����CR�      �   q   x�36�4204�50�54�4�0�¦.6\l����n �����������P-��	�#��.l���¾��
@���A�/l������� �ɔ3�����24������ k<"      �   �  x�m��n�P���S���	�c�bc0`�n��6x��U�N�,:�R�V��(m�$�+\�Q�IHҪ��tt���s���܀Kpn2��n���8N�yr�B�\$oֳ4�#�{8�'�U�GkZ����8����p���������9�b&�c�e�%���H% �=X'�������pu.3��V��Wk�ƏG>zj`M��K�Ϯ"i�%b��ș��/k�G�t\��ؕ6uB��J���
S;DH��Pz���I� ���	�������oP�ު;5����Q�w����,� �A"��,9i�V7gI����j��s���(-|�M�����S��>��
���~	���j�����ѩ�b�V$�V9ЋxV�p�(��iO�e5T�	m�u����1jKA���H(�&����$����3���Ůd�]�z<�M�j0Ź t�(;��0&��0�|�L���+SUm�Н��C���I�t��N������dX�-8ު�Fd#wpߢ�bSo�q�2*I����NTc�ٷ�aQ��(��,���"�������h�O�˕��� ��vs�����K��#�I��uq-n�W�ےYVDǜ��}�V���k=\2�a`S�ЧV�L�$�,����-�	     