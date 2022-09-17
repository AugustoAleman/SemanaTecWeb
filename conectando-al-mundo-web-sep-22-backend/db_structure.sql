-- public."user" definition

-- Drop table

-- DROP TABLE public."user";

CREATE TABLE public."user" (
	id serial NOT NULL,
	"name" varchar NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (id),
	CONSTRAINT user_un UNIQUE (id)
);
CREATE INDEX user_id_idx ON public."user" USING btree (id);


-- public."assignment" definition

-- Drop table

-- DROP TABLE public."assignment";

CREATE TABLE public."assignment" (
	id serial NOT NULL,
	due_date timestamptz(0) NULL,
	"name" varchar NOT NULL,
	CONSTRAINT assignment_pk PRIMARY KEY (id)
);


-- public."class" definition

-- Drop table

-- DROP TABLE public."class";

CREATE TABLE public."class" (
	id serial NOT NULL,
	"name" varchar NOT NULL,
	professor varchar NOT NULL,
	CONSTRAINT class_pk PRIMARY KEY (id),
	CONSTRAINT class_un UNIQUE (id)
);


-- public.user_has_assignment definition

-- Drop table

-- DROP TABLE public.user_has_assignment;

CREATE TABLE public.user_has_assignment (
	user_id int4 NOT NULL,
	assignment_id int4 NOT NULL,
	CONSTRAINT user_has_assignment_fk FOREIGN KEY (user_id) REFERENCES "user"(id),
	CONSTRAINT user_has_assignment_fk_1 FOREIGN KEY (assignment_id) REFERENCES assignment(id)
);


-- public.class_has_user definition

-- Drop table

-- DROP TABLE public.class_has_user;

CREATE TABLE public.class_has_user (
	user_id int4 NOT NULL,
	class_id int4 NOT NULL,
	CONSTRAINT class_has_user_fk FOREIGN KEY (user_id) REFERENCES "user"(id),
	CONSTRAINT class_has_user_fk_1 FOREIGN KEY (class_id) REFERENCES class(id)
);
