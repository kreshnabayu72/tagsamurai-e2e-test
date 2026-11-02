---
id: TC-AC-SU-E2E-191-resend-activation-email-tanpa-batas-harian
title: "Resend Activation Email: Pengiriman Berulang Tanpa Batas Harian"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-149
coverage:
  web: automated
---

# Resend Activation Email: Pengiriman Berulang Tanpa Batas Harian

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (Pending Activation, seed lewat Fixture BE): `Mike Tan {runId}-191`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-191@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-191`.
- Jam server dan jam browser/klien diatur bersama (bagian 6 konvensi); waktu terbit tiap pengiriman dibaca lewat API seeding. Jam dipulihkan di langkah penghubung terakhir dan di hook `after`. Kemampuan atur jam disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-191` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-149: Tidak ada batas harian: resend berulang setelah tiap cooldown

1. Ketik Search `{runId}-191`, tekan Enter
2. Klik `(⋯)` baris `Mike Tan {runId}-191` (Pending Activation), klik `Resend Activation Email`
3. Verifikasi muncul toast sukses pengiriman pertama: "Success, email has been sent."
4. Atur jam server dan jam browser ke waktu terbit pengiriman pertama + 60 detik
5. Tunggu toast lama hilang otomatis
6. Klik `(⋯)` baris `Mike Tan {runId}-191`, klik `Resend Activation Email`
7. Verifikasi muncul toast sukses pengiriman kedua: "Success, email has been sent."
8. Atur jam server dan jam browser ke waktu terbit pengiriman kedua + 60 detik
9. Tunggu toast lama hilang otomatis
10. Klik `(⋯)` baris `Mike Tan {runId}-191`, klik `Resend Activation Email`
11. Verifikasi muncul toast sukses pengiriman ketiga: "Success, email has been sent."
12. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 4, 5, 8, 9, 12 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: cooldown pengiriman pertama (TC-AC-SU-142, 146, 147) ada di spec 039 (`TC-AC-SU-E2E-039-resend-activation-email-row-action-dan-cooldown`).
- Langkah "Tunggu 60 detik → Resend lagi → Ulangi sekali lagi" dipenuhi dengan mengatur jam (bagian 6), bukan menunggu nyata.
- Temuan untuk QA:
  - Post Condition TC-149 ("3 email dan 3 entri log") tidak punya langkah observasi dan tidak diasersi.
