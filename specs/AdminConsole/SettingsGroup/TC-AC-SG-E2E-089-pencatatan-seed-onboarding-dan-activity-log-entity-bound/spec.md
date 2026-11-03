---
id: TC-AC-SG-E2E-089-pencatatan-seed-onboarding-dan-activity-log-entity-bound
title: "Pencatatan Seed Onboarding Default Group dan Activity Log Entity-Bound"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-338
  - TC-AC-SG-339
coverage:
  web: automated
---

# Pencatatan Seed Onboarding Default Group dan Activity Log Entity-Bound

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`; dipakai hook `before` untuk mendaftarkan Distributor baru lewat form Create Distributor.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun di langkah 1): Total Control Distributor baru `Distributor Baru {runId}-089` yang didaftarkan hook `before` lewat Create Distributor. Email dan password akun ini tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Akun ketiga (ganti akun di langkah 8): Total Control entitas Distributor Pembanding, `totalControlPembanding_automated_{namaCompany}@qwertysystem.net` (Pre-setup #33), password `Spectra.env.AC_SG_PEMBANDING_PASSWORD`.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite untuk akun UI yang dipakai suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke form Create Distributor (Pre-setup #40) dan akses ke Activity Log Admin Console tersedia.
- Data milik spec: `Distributor Baru {runId}-089` (dibuat hook `before` lewat form Create Distributor; pembersihan entitas hasil Create Distributor disediakan tim FE/BE di hook `after`) dan group `Cabang Log {runId}-089` yang dibuat langkah spec pada tree Distributor Pembanding (dihapus hook `after` lewat Fixture BE).
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE). Sesi akun dikembalikan ke akun default spec di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-338: Seed onboarding Default Group: Modified By System tanpa entri Changelog

1. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Baru {runId}-089`
2. Buka halaman Settings > Group lewat sidebar
3. Verifikasi kolom Modified By baris `Default Group` bernilai `System`
4. Klik ikon Changelog pada toolbar
5. Verifikasi Modal "Changelog: Group" tampil
6. Verifikasi Changelog tidak memuat entri Create untuk `Default Group` (seed tidak membuat entri)
7. Tutup Modal Changelog dengan `✕`
8. Ganti akun: Logout, lalu login sebagai Total Control Distributor Pembanding

### TC-AC-SG-339: Activity Log Object Group bersifat entity-bound dengan target entitas pemilik tree

9. Buka halaman Settings > Group lewat sidebar
10. Klik `[+] Group` di Sidebar Group Tree
11. Ketik `Cabang Log {runId}-089` lalu klik `[Submit]`
12. Tunggu hingga entri log muncul
13. Buka Activity Log Admin Console dan saring Object `Group`
14. Verifikasi Activity Log memuat entri Action `Create`, Object `Group`, Name `Cabang Log {runId}-089`
15. Verifikasi entri itu memiliki target entity `Distributor Pembanding` (pemilik tree)

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 2 dan 9 (membuka Settings > Group sesudah ganti akun), penutupan Modal Changelog pada langkah 7, dan menunggu entri log muncul pada langkah 12 (pencatatan bersifat eventual).
- Langkah 1 dan 8 adalah ganti akun eksplisit (S-07). Akun default spec (Principal) dipulihkan hook `after`.
- P-1: Distributor baru hasil Create Distributor adalah state berat yang dibangun sebelum spec; asersi absence TC-AC-SG-338 ("Changelog tidak memuat entri Create untuk `Default Group`") tetap di spec ini karena state itu tidak dapat diulang untuk spec absence tanpa biaya yang sama. `Verifikasi` Modified By `System` (langkah 3) dan modal Changelog tampil (langkah 5) menjadi anchor positif absence pada surface yang sama; langkah 5 ditambahkan sebagai anchor (S-03) dan bukan klausa Expected.
- TC-AC-SG-338 Expected butir a menyebut `System` untuk Modified By; nilai ini diasersi apa adanya, bukan format `[First Name] [Last Initial]`.
- TC-AC-SG-339 memakai nama bersuffix `Cabang Log {runId}-089` agar entri dikenali tanpa baseline (baseline nol, S-12).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email, password, dan nama tampil akun Total Control untuk Distributor yang didaftarkan lewat Create Distributor (TC-AC-SG-338 Precondition b, langkah 1); Pre-setup #40 hanya menyebut akses modul secara umum. Spec menulis akun itu sebagai disediakan tim FE.
  - TC-AC-SG-339 tidak menyebut akses Activity Log untuk akun `Distributor Pembanding` (Pre-setup #40 hanya menyebut akses umum); spec mengasumsikan akses tersedia.
  - TC-AC-SG-338 Precondition b menyebut Distributor "didaftarkan lewat Create Distributor" tanpa menyebut field wajib form; field wajib disediakan tim FE.
