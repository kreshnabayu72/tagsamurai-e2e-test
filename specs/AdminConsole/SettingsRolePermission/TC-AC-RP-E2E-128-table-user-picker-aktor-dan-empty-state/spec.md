---
id: TC-AC-RP-E2E-128-table-user-picker-aktor-dan-empty-state
title: "Table User Picker: Aktor Tidak Muncul di Tiga Popup Assign dan Empty State Seluruh Kandidat Sudah Ter-assign"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-437
  - TC-AC-RP-231
coverage:
  web: automated
---

# Table User Picker: Aktor Tidak Muncul di Tiga Popup Assign dan Empty State Seluruh Kandidat Sudah Ter-assign

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor kedua (ganti akun eksplisit): Default User Partner `defaultUserPartRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Wulan Sari`), password `Spectra.env.AC_RP_PART_DU_PASSWORD`.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_PART_DU_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #9 (`Wulan Sari`, Default User `Partner Mandiri`), #11 (tree group Principal termasuk `Region A`), #19 (`Partner Mandiri` tanpa user Standard aktif; pohon group hanya `Default Group`).
- Data Dinamis: spec ini tidak membuat Data Dinamis dan tidak mengubah data. Nilai bersuffix `+{runId}-128` tidak dipakai karena tidak ada data yang dibuat spec.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-437: Aktor tidak muncul di picker Assign Total Control, Read Only, dan Group Manager

1. Klik tombol "+ Assign"
2. Ketik Search `Siti Nurhaliza` pada kolom Search picker, tekan Enter
3. Verifikasi `Siti Nurhaliza` (aktor) tidak ada di daftar kandidat popup Assign Total Control
4. Verifikasi pencarian menampilkan empty state "No results found"
5. Klik `✕` pada popup
6. Klik tab `Read Only`
7. Klik tombol "+ Assign"
8. Ketik Search `Siti Nurhaliza` pada kolom Search picker, tekan Enter
9. Verifikasi `Siti Nurhaliza` (aktor) tidak ada di daftar kandidat popup Assign Read Only
10. Verifikasi pencarian menampilkan empty state "No results found"
11. Klik `✕` pada popup
12. Klik tab `Group Manager`
13. Klik tombol "+ Assign"
14. Pilih Group `Region A`
15. Ketik Search `Siti Nurhaliza` pada kolom Search picker, tekan Enter
16. Verifikasi `Siti Nurhaliza` (aktor) tidak ada di daftar kandidat popup Assign Group Manager
17. Verifikasi pencarian menampilkan empty state "No results found"
18. Klik `✕` pada popup

### TC-AC-RP-231: Empty state picker saat seluruh kandidat sudah ter-assign

19. Logout dari akun Total Control
20. Login sebagai `Wulan Sari` (Default User `Partner Mandiri`)
21. Buka halaman `Settings > Role & Permission`
22. Klik tombol "+ Assign"
23. Verifikasi picker menampilkan Title "All eligible users have been assigned" dan Description "There are no additional eligible users available to select."
24. Verifikasi popup tetap terbuka

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Pembagian TC lintas spec: TC-AC-RP-221, TC-AC-RP-230, TC-AC-RP-232, dan TC-AC-RP-411 ada di spec 066.
- Langkah penghubung (S-03): langkah 5, 11, dan 18 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 6 dan 12 (pilih tab), 19 sampai 21 (ganti akun eksplisit dan buka halaman, S-07).
- Search (R-16): langkah 2, 8, dan 15 mencari target absence `Siti Nurhaliza`; empty state "No results found" yang diproses Search adalah anchor positif asersi absence (bagian 8b butir 2).
- Urutan TC: 437 lalu 231, agar ganti akun hanya terjadi satu kali (S-10).
- Temuan untuk QA:
  - TC-AC-RP-437 Langkah Uji 5 tidak menyebut cara memilih Group `Region A` di popup Assign Group Manager (field Group); spec menulis "Pilih Group `Region A`" tanpa rincian kontrol.
  - TC-AC-RP-231 Precondition c ("Entitas `Partner Mandiri` tanpa user Standard aktif") dan Pre-setup #19 menyebut `Wulan Sari` sebagai satu-satunya user; TC-AC-RP-231 Expected menyebut "seluruh kandidat sudah ter-assign" sedangkan skenario sebenarnya adalah tidak ada kandidat; judul skenario dan Expected tidak konsisten (diikuti persis).
