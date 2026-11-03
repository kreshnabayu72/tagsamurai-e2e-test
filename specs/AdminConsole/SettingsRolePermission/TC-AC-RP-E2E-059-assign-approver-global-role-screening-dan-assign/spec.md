---
id: TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign
title: "Additional Approver Global Role: Screening Popup, Pool, Assign oleh Total Control dan Manage user and role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-203
  - TC-AC-RP-204
  - TC-AC-RP-205
  - TC-AC-RP-413
coverage:
  web: automated
---

# Additional Approver Global Role: Screening Popup, Pool, Assign oleh Total Control dan Manage user and role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor kedua (ganti akun eksplisit): Manage user and role dengan Update `manageUserRoleU_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hendra Wijaya`), password `Spectra.env.AC_RP_MUR_U_PASSWORD`.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_MUR_U_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan` Active Activated, `Maya Putri` Pending Activation, `Yuni Lestari` Pending Email Confirmation, `Jane Smith` dan `Teguh Santoso` Inactive), #17 (approver `Manage TAG stock` = `Sarah Kimura`).
- Data Dinamis: spec ini tidak membuat Data Dinamis. Target Assign adalah user Pre-setup `Alex Tan` (nama tampil dipakai asersi TC). Nilai bersuffix `+{runId}-059` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: approver `Manage TAG stock` bertambah `Alex Tan` pada TC-AC-RP-204 dan TC-AC-RP-205. Pemulihan ke approver awal (`Sarah Kimura` saja) memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Changelog Role Detail `Manage TAG stock` menerima entri Add dan Remove; Last Updated approver berubah.
- Pemulihan Setup Column: preferensi kolom picker dihapus di browser pada hook `after` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`) karena spec mengubah approver Pre-setup bersama.
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-203: Screening popup Assign Approver Global Role dan pool

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Klik "+ Assign" pada section Approvers
4. Verifikasi header popup "Assign Approver — Manage TAG stock"
5. Verifikasi popup tidak memuat field Group
6. Verifikasi sedikitnya satu kandidat tampil di daftar kandidat
7. Klik header kolom Actions pada picker lalu pilih Column Visibility
8. Centang Activation Status
9. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
10. Verifikasi seluruh kandidat yang tampil berstatus `Active` pada kolom Status
11. Verifikasi seluruh kandidat yang tampil ber-Activation Status `Activated`, termasuk pemegang Total Control
12. Verifikasi daftar kandidat tidak memuat `Maya Putri`, `Yuni Lestari`, user Inactive (`Jane Smith`, `Teguh Santoso`), dan `Sarah Kimura`
13. Verifikasi aktor `Siti Nurhaliza` tidak muncul di daftar kandidat pada seluruh halaman Pagination popup
14. Klik `✕` pada popup

### TC-AC-RP-413: Aktor tidak muncul di picker Assign Approver

15. Klik "+ Assign" pada section Approvers
16. Ketik Search `Alex Tan`, tekan Enter
17. Verifikasi daftar kandidat memuat user Active berstatus Activated (mis. `Alex Tan`)
18. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter
19. Verifikasi pada kolom Name `Siti Nurhaliza` (aktor) tidak ada di daftar kandidat
20. Verifikasi empty state "No results found"
21. Klik `✕` pada popup

### TC-AC-RP-204: Assign Approver Global Role happy path

22. Klik "+ Assign" pada section Approvers
23. Centang `Alex Tan` lalu klik `[Assign]`
24. Verifikasi toast "Success, approver has been assigned."
25. Verifikasi tabel Approvers memuat `Alex Tan` dan `Sarah Kimura`
26. Pulihkan baseline automation: approver `Manage TAG stock` kembali hanya `Sarah Kimura`

### TC-AC-RP-205: Assign Approver oleh Manage user and role

27. Logout dari akun Total Control
28. Login sebagai `Hendra Wijaya` (Manage user and role dengan Update)
29. Buka halaman `Settings > Role & Permission`
30. Klik tab `System`
31. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
32. Klik "+ Assign" pada section Approvers
33. Centang `Alex Tan` lalu klik `[Assign]`
34. Verifikasi toast "Success, approver has been assigned."
35. Pulihkan baseline automation: approver `Manage TAG stock` kembali hanya `Sarah Kimura`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi; hanya kolom Expected Result yang menjadi `Verifikasi`.
- Urutan TC di spec: 203, 413, 204, 205. Alasan: blok yang tidak mengubah data (screening dan pencarian) didahulukan sebelum Assign, dan ganti akun ke `Hendra Wijaya` diletakkan di akhir (S-10).
- Langkah penghubung (S-03): langkah 14, 21 (tutup popup; popup picker ditutup `✕` tanpa dialog Unsaved Changes karena bukan form), 26 dan 35 (pemulihan baseline), 27 sampai 29 (ganti akun eksplisit, S-07), langkah 30 dan 31 (navigasi ke Role Detail), langkah 7 dan 8 (membuka Column Visibility dan mencentang Activation Status karena kolom itu tersembunyi default di picker, sehingga klausa Activation Status pada langkah 11 dapat diamati; keduanya diletakkan sebelum penelusuran halaman supaya satu penelusuran mencakup kolom Status dan Activation Status), langkah 9 (telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat sebelum asersi kandidat langkah 10 sampai 13; picker berpaginasi bawaan 10 baris, R-22, pola spec 045), langkah 16 (Search `Alex Tan` untuk menemukan kandidat target langkah 17, R-16) dan langkah 18 (ganti isi kotak search, bagian 8b butir 9).
- Asersi tambahan (S-03): langkah 6 memverifikasi sedikitnya satu kandidat tampil sebagai pembanding positif sebelum asersi universal dan absence (langkah 10, 11, 12, dan 13; bagian 8b butir 2); langkah 10 memverifikasi kolom Status dan langkah 11 kolom Activation Status sebagai dua klausa Expected b yang dipecah sesuai kolom yang teramati.
- Search (R-16): langkah 18 mencari target absence `Siti Nurhaliza` dan langkah 19 membaca hasilnya pada kolom Name; langkah 17 (`Alex Tan` tampil pada hasil Search di popup yang sama) dan empty state "No results found" menjadi anchor positif asersi absence langkah 19 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-203 Expected b menyebut "pemegang Total Control" tanpa nama; spec memverifikasi secara generik.
  - Daftar kandidat berpaginasi (ukuran halaman bawaan 10); TC-AC-RP-203 Expected b tidak menyebut Search atau halaman, sehingga spec menelusuri seluruh halaman Pagination popup (langkah 9) sebelum asersi kandidat langkah 10 sampai 13.
  - TC memakai user Pre-setup literal (`Alex Tan`) sebagai target Assign dan tidak memberi Data Dinamis bersuffix; pemulihan lewat "automation baseline" tidak didefinisikan mekanismenya di TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE/BE.
