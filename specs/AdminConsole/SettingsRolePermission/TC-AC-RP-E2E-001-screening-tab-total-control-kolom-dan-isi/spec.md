---
id: TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi
title: "Screening Tab Total Control: Layout Halaman, Kolom Default, Isi Baris, Badge Status, dan Hover Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-1
  - TC-AC-RP-2
  - TC-AC-RP-3
  - TC-AC-RP-4
  - TC-AC-RP-5
  - TC-AC-RP-6
coverage:
  web: automated
---

# Screening Tab Total Control: Layout Halaman, Kolom Default, Isi Baris, Badge Status, dan Hover Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip halaman ini disetel `seen`, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #13 (pemegang tingkat akses: Total Control `Bambang Hartono`, `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, `Siti Nurhaliza`), dan #12, #18 sebagai data Principal pendukung. Nilai di langkah mengikuti tabel itu; berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis sehingga tidak ada suffix `{runId}` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Pemulihan Setup Column: TC-AC-RP-5 mencentang kolom Activation Status lewat Column Visibility; langkah 28 mengembalikannya dan hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Format tanggal Last Updated mengikuti General Settings default entitas uji (contoh `15 Jun 2026, 10:05`), tidak diubah spec ini.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-1: Screening halaman Role & Permission saat pertama dibuka

1. Susuri halaman dari atas ke bawah dan kiri ke kanan tanpa mengklik apa pun
2. Verifikasi Breadcrumb "Settings > Role & Permission > Total Control" tampil di luar `SectionCard`
3. Verifikasi tombol `[?]` tampil tepat di kanan Breadcrumb
4. Verifikasi tidak ada Page Title Header
5. Verifikasi Tabs di dalam `SectionCard`: "Total Control" | "Read Only" | "Group Manager" | "System"
6. Verifikasi tab Total Control aktif
7. Verifikasi Toolbar rata kanan berisi ikon Search, Filter, Download, Changelog
8. Verifikasi tombol "+ Assign" (primary) tampil setelah ikon Changelog
9. Verifikasi tabel Tab Total Control dan Pagination berada di dalam `SectionCard`
10. Verifikasi tidak ada Sidebar Group Tree pada tab ini

### TC-AC-RP-2: Screening kolom default tabel Tab Total Control

11. Perhatikan header tabel dari kiri ke kanan
12. Verifikasi kolom berurutan: Name, Position, Division, Status, Modified By, Last Updated, Actions `⋯` (pinned kanan)
13. Verifikasi tidak ada kolom CRUD dan tidak ada kolom Checkbox
14. Verifikasi kolom Email, Activation Status, Temporary User, Temporary Until, TAG, dan kolom Custom Field aktif tidak tampil secara default
15. Hover header kolom Actions `⋯`
16. Verifikasi tooltip "Column Visibility" tampil pada header kolom Actions

### TC-AC-RP-3: Isi baris Tab Total Control dan urutan default Name A-Z

17. Verifikasi 6 baris berurutan Name A-Z: `Bambang Hartono`, `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, `Siti Nurhaliza`
18. Verifikasi sel Name berupa `[Avatar] Full Name` dalam satu sel dengan thumbnail circle
19. Verifikasi Name bukan link
20. Verifikasi baris `Bambang Hartono` (Default User): Position "CEO", Division "Board", Status `Active`, Modified By "—", Last Updated "—"
21. Verifikasi baris `John Doe`: Status `Active`, Modified By "Siti N", Last Updated "15 Jun 2026, 10:05"

### TC-AC-RP-4: Badge Status Active dan Inactive pada Tab Total Control

22. Verifikasi baris `John Doe` menampilkan badge `Active` (`severity="success"`)
23. Verifikasi baris `Sarah Kim` menampilkan badge `Inactive` (`severity="danger"`)
24. Verifikasi baris `Sarah Kim` tetap tampil dengan tingkat akses Total Control

### TC-AC-RP-5: Status Active modul independen dari Activation Status Pending

25. Klik header kolom Actions `⋯` untuk membuka dropdown Column Visibility
26. Centang kolom Activation Status lalu tutup dropdown
27. Verifikasi baris `Budi Santoso` menampilkan Status `Active` dan Activation Status `Pending Activation` (badge `severity="warning"`)
28. Buka dropdown Column Visibility, hilangkan centang kolom Activation Status, lalu tutup dropdown

### TC-AC-RP-6: Hover Modified By menampilkan nama lengkap

29. Hover nilai Modified By "Siti N" pada baris `John Doe`
30. Verifikasi tooltip menampilkan nama lengkap "Siti Nurhaliza"
31. Verifikasi sel Modified By tampil sebagai teks polos format "[First Name] [Last Initial]"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE (tanpa TC hanya-BE); spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 1 (susur halaman), 11 (penanda pengamatan header), dan 15 (hover prasyarat asersi tooltip); langkah 28 mengembalikan Column Visibility ke keadaan awal sebelum TC berikutnya (S-09). Klik header `⋯` dan pencentangan pada TC-AC-RP-5 adalah langkah TC sumber.
- Langkah "Perhatikan/Amati" pada kolom Langkah Uji TC sumber ditulis sebagai langkah aksi hanya bila menjadi prasyarat asersi (langkah 11); pada TC lain dihilangkan karena asersinya langsung mengikuti.
- Verifikasi tab Total Control aktif (langkah 6) berasal dari Expected b TC-AC-RP-1; keadaan awal halaman dibuka hook `beforeEach` suite.
- Temuan untuk QA:
  - TC-AC-RP-1 Expected c menyebut toolbar "ikon Search, Filter, Download, Changelog, lalu tombol '+ Assign' (primary)" tanpa menyatakan posisi ikon terhadap tombol selain urutan; asersi mengikuti urutan itu.
  - TC-AC-RP-5 tidak menyatakan apakah pencentangan Column Visibility menyimpan preferensi kolom di browser; spec memulihkannya secara eksplisit dan lewat hook `after`.
  - TC-AC-RP-4 Expected b tidak menyatakan cara membedakan "tetap tampil dengan tingkat akses Total Control" dari sekadar baris tampil di Tab Total Control; asersi hanya baris tampil di tab ini.
