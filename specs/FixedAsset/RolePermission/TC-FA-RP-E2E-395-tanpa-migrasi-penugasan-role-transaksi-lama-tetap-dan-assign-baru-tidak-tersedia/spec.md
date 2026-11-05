---
id: TC-FA-RP-E2E-395-tanpa-migrasi-penugasan-role-transaksi-lama-tetap-dan-assign-baru-tidak-tersedia
title: "Tanpa migrasi: penugasan Role Transaksi lama di luar constraint tetap berlaku, sedangkan assign baru di luar constraint tidak tersedia"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1236
coverage:
  web: automated
---

# Tanpa migrasi: penugasan Role Transaksi lama di luar constraint tetap berlaku, sedangkan assign baru di luar constraint tidak tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`), #18 (pohon Group: `Data Center` dan `Helpdesk` bersaudara di bawah `IT Infrastructure`), dan #19 (baris pola Asset Admin pada `Helpdesk` sub-tab `Disposal`).
- Kemampuan teknis (disediakan tim FE/BE; kemampuan ini tidak dinamai di Pre-setup TC dan dicatat di "Temuan untuk QA"): seeding penugasan Role Transaksi yang melewati gate Home Group constraint, sehingga Gunawan Halim (Home Group `Data Center`) dapat memegang Asset Admin pada `Helpdesk` sub-tab `Disposal`, node di luar constraint yang tidak dapat dibentuk lewat UI atau request biasa.
- Seeding precondition (hook `before`, dipakai sebagai precondition TC, tidak diasersi): Gunawan Halim dengan Home Group `Data Center` (Pre-setup #17) diberi Asset Admin pada `Helpdesk` sub-tab `Disposal` lewat kemampuan seeding yang melewati gate di atas.
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: spec tidak mengubah state (langkah 7 menutup popup tanpa Assign). Seed baris Asset Admin Gunawan Halim di `Helpdesk` dicabut pada langkah 8 lewat fixture BE (bukan lewat UI, supaya tidak menambah entri `Remove`) dan di hook `after` sebagai cadangan; Home Group Gunawan Halim tetap `Data Center` (Pre-setup #17). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1236: Penugasan Role Transaksi lama di luar constraint tidak dimigrasi dan assign baru di luar constraint tidak tersedia

1. Klik Tab `Transaction Role`, klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Verifikasi Gunawan Halim tetap tampil di section Asset Admin `Helpdesk`
3. Klik `[+ Assign]` pada section Staff
4. Verifikasi sedikitnya satu kandidat tampil di daftar picker
5. Ketik Search `Gunawan Halim`, tekan Enter
6. Verifikasi Gunawan Halim tidak ada di daftar picker
7. Tutup popup lewat `✕`
8. Pulihkan lewat fixture BE: cabut baris seed Asset Admin Gunawan Halim pada `Helpdesk` sub-tab `Disposal`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 8 langkah.
- Anchor positif absence (bagian 8b butir 2): `Verifikasi` kandidat lain pada daftar picker (langkah 4) membuktikan picker termuat dan Gunawan Halim dicari dengan Search (langkah 5) mendahului asersi tidak ada di daftar (langkah 6). Search pada langkah 5 adalah langkah TC ("cari Gunawan Halim"), bukan penghubung (R-22).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (navigasi Tab, node, dan sub-tab), langkah 7 (menutup popup tanpa Assign), langkah 8 (pemulihan, S-09). `Verifikasi` langkah 4 adalah anchor positif yang tidak ada di Expected TC (S-03).
- Node `Helpdesk` bersaudara dengan `Data Center` (keduanya anak `IT Infrastructure`), sehingga berada di luar constraint Home Group `Data Center` Gunawan Halim (gate menilai node penugasan, FARP-LOGIC-16c).
- Temuan untuk QA:
  - NC-20 (PRD Open Item #9) menunggu PM: tanpa migrasi dan arah gate belum dikonfirmasi; asersi langkah 2 dan 6 bergantung pada keputusan itu.
  - Precondition TC-FA-RP-1236 menyebut penugasan lama "di-seed lewat fixture BE tanpa melewati gate", tetapi Pre-setup TC tidak menamai kemampuan BE itu. Spec menulisnya sebagai kebutuhan kemampuan teknis di Prerequisites; tim FE/BE perlu menyediakan seeding penugasan Role Transaksi yang melewati gate Home Group constraint (sama dengan kebutuhan spec 384 dan 120).
  - TC-FA-RP-1236 langkah 2 hanya menyebut "cari Gunawan Halim"; spec menambah `Verifikasi` kandidat lain sebagai anchor (langkah 4) dan menutup popup lewat `✕` sebagai langkah penghubung.
  - Post Condition TC-FA-RP-1236 kosong ("-").
