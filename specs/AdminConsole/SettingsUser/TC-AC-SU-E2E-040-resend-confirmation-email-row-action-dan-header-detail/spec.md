---
id: TC-AC-SU-E2E-040-resend-confirmation-email-row-action-dan-header-detail
title: "Resend Email: Row Action Confirmation dan Tombol Header Detail User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-143
  - TC-AC-SU-144
  - TC-AC-SU-145
coverage:
  web: automated
---

# Resend Email: Row Action Confirmation dan Tombol Header Detail User

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Rina Putri {runId}-040` (Pending Email Confirmation, TC-143), `Dewi Lestari {runId}-040` (Pending Email Confirmation, TC-145), `Mike Tan {runId}-040` (Pending Activation, TC-144).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-040@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-040`.
- Cooldown 60 detik tidak dilewati di spec ini; jam tidak diatur.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-040` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-143: Resend Confirmation Email via row action: sukses

1. Ketik Search `{runId}-040`, tekan Enter
2. Klik `(⋯)` baris `Rina Putri {runId}-040`, klik `Resend Confirmation Email`
3. Verifikasi muncul toast sukses: "Success, email has been sent."
4. Klik `(⋯)` baris `Rina Putri {runId}-040` lagi
5. Verifikasi opsi `Resend Confirmation Email` masuk cooldown (disabled) dengan label tetap
6. Tutup menu `(⋯)` dengan Esc

### TC-AC-SU-144: Resend Activation Email dari header Detail User

7. Klik nama `Mike Tan {runId}-040` di User List, Settings > User > Detail terbuka
8. Klik tombol `Resend Activation Email` di header
9. Verifikasi muncul toast sukses: "Success, email has been sent."
10. Verifikasi tombol `Resend Activation Email` di header disabled
11. Verifikasi label tombol tetap `"Resend Activation Email"`
12. Hover tombol `Resend Activation Email`
13. Verifikasi tooltip countdown `"Please wait [Seconds] seconds before resending."`
14. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-145: Resend Confirmation Email dari header Detail User

15. Ketik Search `{runId}-040`, tekan Enter
16. Klik nama `Dewi Lestari {runId}-040` di User List, Settings > User > Detail terbuka
17. Klik tombol `Resend Confirmation Email` di header
18. Verifikasi muncul toast sukses: "Success, email has been sent."
19. Verifikasi tombol `Resend Confirmation Email` di header masuk cooldown (disabled)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 14, 15 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Temuan untuk QA:
  - TC-145 menulis target `Rina Putri`, yang sudah dalam cooldown setelah TC-143; spec memakai `Dewi Lestari {runId}-040` terpisah agar tombol header belum dalam cooldown.
  - TC-144 menyebut "tooltip 🔖 countdown" tanpa teks; spec memakai teks tooltip cooldown yang tertulis di TC-142.
  - Expected TC-143 butir b dan TC-145 butir b ("masuk cooldown") tidak menyebut teks atau label; spec mengasersi state disabled.
  - Post Condition TC-143 ("Email konfirmasi terkirim ke email baru yang pending") tidak punya langkah observasi dan tidak diasersi.
