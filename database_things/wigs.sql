CREATE TABLE "wigs" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "brand_id" integer,
  "price" integer,
  "main_image" varchar,
  "color_id" int,
  "tags" varchar
);

CREATE TABLE "brands" (
  "id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "colors" (
  "id" integer PRIMARY KEY,
  "brand" integer,
  "color_name" varchar,
  "swatch_link" varchar
);

CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "full_name" varchar,
  "email" varchar,
  "user_image" varchar
);

CREATE TABLE "user_wigs" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "wig_id" integer,
  "owned" boolean,
  "wishlist" boolean
);

ALTER TABLE "wigs" ADD FOREIGN KEY ("brand_id") REFERENCES "brands" ("id");

ALTER TABLE "colors" ADD FOREIGN KEY ("brand") REFERENCES "brands" ("id");

ALTER TABLE "wigs" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("id");

ALTER TABLE "user_wigs" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "user_wigs" ADD FOREIGN KEY ("wig_id") REFERENCES "wigs" ("id");
