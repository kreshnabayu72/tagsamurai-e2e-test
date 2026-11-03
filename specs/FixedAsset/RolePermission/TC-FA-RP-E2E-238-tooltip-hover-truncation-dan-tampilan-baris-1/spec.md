---
id: TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1
title: "Tooltip, hover, truncation, dan tampilan baris (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-778
  - TC-FA-RP-779
  - TC-FA-RP-780
  - TC-FA-RP-781
  - TC-FA-RP-782
coverage:
  web: automated
---

# Tooltip, hover, truncation, dan tampilan baris (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi), #36 (Tab Total Control terisi), #38 (Tab Group Manager terisi), #42 (Changelog Tab Total Control, enam entri). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Hover dan klik elemen UI; tidak ada pembacaan state backend.
- State yang diubah dan pemulihannya: Tidak ada state yang diubah.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-778: Tooltip ikon toolbar tabel Tab Total Control dan header Column Visibility

1. Hover ikon Search di toolbar Tab `Total Control`
2. Verifikasi tooltip `Search` tampil
3. Hover ikon Filter
4. Verifikasi tooltip `Filter` tampil
5. Hover ikon Download
6. Verifikasi tooltip `Download` tampil
7. Hover ikon Changelog
8. Verifikasi tooltip `Changelog` tampil
9. Hover header kolom Actions `(⋯)`
10. Verifikasi tooltip `Column Visibility` tampil

### TC-FA-RP-779: Tooltip tombol `[+ Assign]` tidak ada bagi Total Control

11. Hover tombol `[+ Assign]`
12. Verifikasi tombol `[+ Assign]` tampil Enabled bagi Total Control
13. Verifikasi tidak ada tooltip tambahan pada tombol `[+ Assign]`

### TC-FA-RP-780: Hover Modified By menampilkan nama lengkap pada Tab Total Control, Tab Group Manager, dan modal Changelog

14. Hover sel Modified By baris Ahmad Fauzi di Tab `Total Control`
15. Verifikasi tooltip `Siti Rahmawati` tampil
16. Klik Tab `Group Manager`
17. Hover sel Modified By baris Fajar Nugroho di Tab `Group Manager`
18. Verifikasi tooltip nama lengkap aktor penugasan Fajar Nugroho tampil
19. Klik Tab `Total Control` lalu klik ikon Changelog di toolbar Tab `Total Control`
20. Hover sel Modified By entri `Assign` Budi Santoso di modal Changelog Tab `Total Control`
21. Verifikasi tooltip `Prasetyo Hadi` tampil
22. Tutup modal Changelog

### TC-FA-RP-781: Hover Role Name Tab System berubah ke warna primary biru tanpa underline

23. Klik Tab `System`
24. Hover Role Name `Manage files`
25. Verifikasi warna teks Role Name berubah menjadi biru (primary Fixed Asset)
26. Verifikasi Role Name tanpa garis bawah
27. Verifikasi kursor menandakan Role Name dapat diklik

### TC-FA-RP-782: Kolom Name pada tabel user bukan link: tidak berubah warna dan tidak membuka Detail

28. Klik Tab `Total Control`
29. Hover nama Ahmad Fauzi pada baris Tab `Total Control`
30. Verifikasi teks nama tidak berubah warna
31. Klik nama Ahmad Fauzi
32. Verifikasi halaman tetap Tab `Total Control` (klik tidak membuka halaman Detail apa pun)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 16, 19, 22, 23, 28. Akun aktor pertama sudah login di hook `before` (S-07).
- Temuan untuk QA:
  - TC-FA-RP-780 Expected b menyebut tooltip "nama lengkap aktor penugasan Fajar Nugroho" tanpa menyebut nama; Pre-setup #38 mencatat Modified By `Siti R`, sehingga nama lengkapnya tidak ditulis di spec.
  - TC-FA-RP-780 precondition merujuk Pre-setup #36, #38, dan #42 (bukan #15); TC-FA-RP-778, 779, dan 782 merujuk #15 sedangkan data barisnya berasal dari #36; spec memakai semua rujukan itu.
  - TC-FA-RP-780 langkah 3 menyebut modal Changelog Tab Total Control tanpa langkah membukanya; spec menambah langkah penghubung (klik tab dan ikon Changelog).
