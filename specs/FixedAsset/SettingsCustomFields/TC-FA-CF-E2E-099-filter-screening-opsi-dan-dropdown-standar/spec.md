---
id: TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar
title: "Filter: Screening Panel, Opsi dari Tab Aktif, dan Dropdown Multi-Select"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-374
  - TC-FA-CF-375
  - TC-FA-CF-376
  - TC-FA-CF-377
  - TC-FA-CF-392
coverage:
  web: automated
---

# Filter: Screening Panel, Opsi dari Tab Aktif, dan Dropdown Multi-Select

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama, Data Type, dan Scope seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field:
  - `Asset Serial Tag`: Text; Scope General; Required Yes; Active.
  - `Storage Capacity`: Numeric; Scope `Generator`, `Pump`; Required No; Active.
  - `Equipment Class`: Dropdown; Scope `Compressor`, `Generator`, `Pump`; Active.
  - `Operating Voltage`: Text; Scope `Generator`; Value Type Global; Required Yes; Active.
  - `Total Cost`: Formula; Scope General; Active.
  - `Depreciated Ratio`: Percentage; Scope General; Inactive.
  - `Compliance File`: Document; Scope General; Active.
  - `Legacy Tag`: Text; Scope kosong; Active.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan label, placeholder, dan urutan field pada Filter Panel; pembacaan opsi dropdown; pembacaan baris hasil tabel.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-374: Screening Filter Panel memuat tujuh field dengan label dan placeholder

1. Klik ikon Filter
2. Verifikasi icon Filter berubah gelap
3. Verifikasi field berurutan: `Active` (`All statuses`), `Data Type` (`All data types`), `Scope` (`All scopes`), `Value Type` (`All value types`), `Required` (`All required`), `Modified By` (`All users`), dan `Last Updated` date range (`Select date`)
4. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
5. Verifikasi Field Name, Value Setting, dan Placeholder tidak memiliki field filter

### TC-FA-CF-392: Kolom non-filterable tidak memiliki field di Filter Panel

6. Verifikasi tidak ada field untuk Field Name, Value Setting, dan Placeholder pada Filter Panel

### TC-FA-CF-375: Opsi dropdown filter diambil dari nilai yang ada di tabel tab aktif

7. Buka dropdown Data Type
8. Verifikasi opsi Data Type: `Document`, `Dropdown`, `Formula`, `Numeric`, `Percentage`, `Text`
9. Tutup dropdown Data Type, buka dropdown Required
10. Verifikasi opsi Required: `No`, `Yes`
11. Tutup dropdown Required, buka dropdown Value Type
12. Verifikasi opsi Value Type: `Global`, `Specific`
13. Tutup dropdown Value Type, buka dropdown Scope
14. Verifikasi opsi Scope: `General`, `Compressor`, `Generator`, `Pump`
15. Tutup dropdown Scope

### TC-FA-CF-376: Dropdown multi-select standar menyaring Active, Data Type, Value Type, dan Required

16. Pilih Data Type `Text`, klik `[Apply]`
17. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Legacy Tag`, dan `Operating Voltage`
18. Klik `[Clear Field]`, pilih Active `Inactive`, klik `[Apply]`
19. Verifikasi tabel hanya menampilkan baris `Depreciated Ratio`
20. Klik `[Clear Field]`, pilih Value Type `Global`, klik `[Apply]`
21. Verifikasi tabel hanya menampilkan baris `Operating Voltage`
22. Klik `[Clear Field]`, pilih Required `Yes`, klik `[Apply]`
23. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag` dan `Operating Voltage`

### TC-FA-CF-377: Filter Scope cocok bila himpunan Scope memuat Asset Name atau General terpilih

24. Klik `[Clear Field]`, pilih Scope `Pump`, klik `[Apply]`
25. Verifikasi tabel hanya menampilkan baris `Equipment Class` dan `Storage Capacity`
26. Klik `[Clear Field]`, pilih Scope `General`, klik `[Apply]`
27. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Compliance File`, `Depreciated Ratio`, dan `Total Cost`

## Notes

- Spec memuat 27 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Filter Panel tabel utama tab General), satu dataset, satu akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 11, 13, dan 15 (menutup dropdown sebelum membuka dropdown berikutnya); langkah 18, 20, 22, 24, dan 26 memuat `[Clear Field]` sebagai langkah "Bersihkan" dari TC-FA-CF-376 dan TC-FA-CF-377 (cara membersihkan tidak disebut TC; dipilih `[Clear Field]`).
- TC-FA-CF-392 diamati pada Filter Panel yang dibuka di langkah 1 (langkah TC "Klik icon Filter" sudah terpenuhi); asersi absence langkah 5 dan 6 memakai langkah 3 (tujuh field filter tampil) sebagai anchor positif (bagian 8b butir 2).
- Asersi hasil filter ditulis "hanya menampilkan baris X" dengan menyebut nama baris; daftar baris pada Expected TC diperlakukan sebagai himpunan lengkap hasil.
- Temuan untuk QA:
  - TC-FA-CF-392 Expected sama dengan klausa d TC-FA-CF-374 (Field Name, Value Setting, dan Placeholder tidak memiliki field filter); spec mengasersinya dua kali (langkah 5 dan langkah 6) karena tiap TC punya Expected sendiri.
  - TC-FA-CF-375 tidak menyebut urutan opsi di dalam dropdown; spec mengasersi opsi yang tampil sesuai daftar TC.
  - TC-FA-CF-376 dan TC-FA-CF-377 menulis "Bersihkan" tanpa menyebut kontrolnya; spec memakai `[Clear Field]`.
  - Spec mengasumsikan Filter Panel tetap terbuka setelah `[Apply]` (TC tidak menyatakannya secara eksplisit).
  - TC-FA-CF-374, TC-FA-CF-375, TC-FA-CF-376, TC-FA-CF-377, dan TC-FA-CF-392 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
