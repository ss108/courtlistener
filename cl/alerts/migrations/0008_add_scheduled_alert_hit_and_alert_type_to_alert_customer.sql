BEGIN;
--
-- Create model ScheduledAlertHit
--
CREATE TABLE "alerts_scheduledalerthit" ("id" integer NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "date_created" timestamp with time zone NOT NULL, "date_modified" timestamp with time zone NOT NULL, "rate" varchar(10) NOT NULL, "document_content" jsonb NOT NULL);
--
-- Remove trigger update_or_delete_snapshot_delete from model alert
--
DROP TRIGGER IF EXISTS pgtrigger_update_or_delete_snapshot_delete_96037 ON "alerts_alert";
--
-- Remove trigger update_or_delete_snapshot_update from model alert
--
DROP TRIGGER IF EXISTS pgtrigger_update_or_delete_snapshot_update_1285f ON "alerts_alert";
--
-- Add field alert_type to alert
--
ALTER TABLE "alerts_alert" ADD COLUMN "alert_type" varchar(3) DEFAULT 'o' NOT NULL;
ALTER TABLE "alerts_alert" ALTER COLUMN "alert_type" DROP DEFAULT;
--
-- Add field alert to scheduledalerthit
--
ALTER TABLE "alerts_scheduledalerthit" ADD COLUMN "alert_id" integer NOT NULL CONSTRAINT "alerts_scheduledalerthit_alert_id_b407b0ad_fk_alerts_alert_id" REFERENCES "alerts_alert"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "alerts_scheduledalerthit_alert_id_b407b0ad_fk_alerts_alert_id" IMMEDIATE;
--
-- Add field user to scheduledalerthit
--
ALTER TABLE "alerts_scheduledalerthit" ADD COLUMN "user_id" integer NOT NULL CONSTRAINT "alerts_scheduledalerthit_user_id_d94bee5e_fk_auth_user_id" REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "alerts_scheduledalerthit_user_id_d94bee5e_fk_auth_user_id" IMMEDIATE;
CREATE INDEX "alerts_scheduledalerthit_date_created_eef6e1d2" ON "alerts_scheduledalerthit" ("date_created");
CREATE INDEX "alerts_scheduledalerthit_date_modified_085e80b9" ON "alerts_scheduledalerthit" ("date_modified");
CREATE INDEX "alerts_scheduledalerthit_alert_id_b407b0ad" ON "alerts_scheduledalerthit" ("alert_id");
CREATE INDEX "alerts_scheduledalerthit_user_id_d94bee5e" ON "alerts_scheduledalerthit" ("user_id");
COMMIT;
