---
id: TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope
title: "Search: Pencocokan Kolom Teks, Enum, Modified By, Value Setting, dan Scope"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-361
  - TC-FA-CF-362
  - TC-FA-CF-363
  - TC-FA-CF-364
  - TC-FA-CF-365
coverage:
  web: automated
---

# Search: Pencocokan Kolom Teks, Enum, Modified By, Value Setting, dan Scope

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama, Modified By, dan nilai kolom seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field:
  - `Asset Serial Tag`: Text; Scope General; Value Type Specific; Required Yes; Placeholder kosong; Modified By `Budi S` (Budi Santoso).
  - `Storage Capacity`: Numeric 0 Decimal Places; Scope `Generator`, `Pump`; Value Type Specific; Required No; Placeholder `Capacity in GB`; Modified By `Siti A` (Siti Amelia).
  - `Equipment Class`: Dropdown opsi `Class A`, `Class B`, `Class C` (`Class C` di balik chip `+1 more`); Scope `Compressor`, `Generator`, `Pump` (`Pump` di balik chip `+1 more`); Modified By `Siti A`.
  - `Operating Voltage`: Text; Scope `Generator`; Value Type Global (`Generator`=`220V`); Required Yes; Modified By `Budi S`.
  - `Total Cost`: Formula `Purchase Price + 10`; Scope General; Value Type `—`; Modified By `Joko W` (Joko Widodo).
  - `Depreciated Ratio`: Percentage 2 Decimal Places; Scope General; Value Type Specific; Inactive; Modified By `Joko W`.
  - `Compliance File`: Document; Scope General; Value Type Specific; Modified By `Budi S`.
  - `Legacy Tag`: Text; Scope kosong; Value Type Specific; Modified By `Joko W`.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi sel tabel (Field Name, Value Setting, Modified By) dan badge pada Page Object.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-361: Search kelas teks bebas (Field Name dan Placeholder nilai efektif)

1. Ketik Search `SERIAL`, tekan Enter
2. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag` (kolom Field Name, tidak peka huruf besar-kecil)
3. Ganti isi kotak search dengan `in gb`, tekan Enter
4. Verifikasi tabel hanya menampilkan baris `Storage Capacity` karena Placeholder efektif `Capacity in GB`
5. Klik `(←)`

### TC-FA-CF-362: Search kelas enum dan badge (Data Type, Value Type, Required)

6. Ketik Search `formula`, tekan Enter
7. Verifikasi tabel hanya menampilkan baris `Total Cost`
8. Ganti isi kotak search dengan `global`, tekan Enter
9. Verifikasi tabel hanya menampilkan baris `Operating Voltage` (Value Type Global)
10. Ganti isi kotak search dengan `yes`, tekan Enter
11. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag` dan `Operating Voltage` (Required Yes)
12. Klik `(←)`

### TC-FA-CF-363: Search kolom Modified By mencocokkan nama lengkap user

13. Ketik Search `santoso`, tekan Enter
14. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Compliance File`, dan `Operating Voltage`
15. Verifikasi sel Modified By ketiga baris menampilkan `Budi S`
16. Ganti isi kotak search dengan `Widodo`, tekan Enter
17. Verifikasi tabel hanya menampilkan baris `Depreciated Ratio`, `Legacy Tag`, dan `Total Cost`
18. Klik `(←)`

### TC-FA-CF-364: Search kolom Value Setting (opsi di balik +N more dan teks Decimal Places)

19. Ketik Search `class c`, tekan Enter
20. Verifikasi tabel hanya menampilkan baris `Equipment Class`
21. Verifikasi `Class C` tidak tampil sebagai badge pada sel Value Setting baris `Equipment Class`
22. Ganti isi kotak search dengan `2 decimal`, tekan Enter
23. Verifikasi tabel hanya menampilkan baris `Depreciated Ratio` (Value Setting `2 Decimal Places`)
24. Klik `(←)`

### TC-FA-CF-365: Search kolom Scope (General dan nama Asset Name)

25. Ketik Search `pump`, tekan Enter
26. Verifikasi tabel hanya menampilkan baris `Equipment Class` dan `Storage Capacity`
27. Ganti isi kotak search dengan `general`, tekan Enter
28. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Compliance File`, `Depreciated Ratio`, dan `Total Cost`
29. Klik `(←)`

## Notes

- Spec memuat 29 langkah, di bawah ambang sekitar 35 langkah. Satu topik (pencocokan kolom Searchable), satu dataset, satu akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 12, 18, 24, dan 29 (`(←)` menutup input dan mengosongkan keyword sebelum TC berikutnya, S-09). Search ditulis atomik (bagian 8b butir 9); klik ikon Search eksplisit tidak dipakai karena siklus input diuji di spec lain.
- Asersi hasil Search ditulis "hanya menampilkan baris X" dengan menyebut nama baris, sehingga baris yang disebut menjadi anchor positif bagi asersi universal (bagian 8b butir 2). Daftar baris pada Expected TC diperlakukan sebagai himpunan lengkap hasil.
- Langkah 15 mengasersi klausa "meskipun sel menampilkan `Budi S`" pada Expected a TC-FA-CF-363. Langkah 21 mengasersi klausa "walau `Class C` tidak tampil sebagai badge" pada Expected a TC-FA-CF-364. Kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Temuan untuk QA:
  - Pada TC-FA-CF-362 Expected b dan c, TC-FA-CF-364 Expected b, dan TC-FA-CF-365 Expected a dan b, TC menulis "menemukan X" tanpa kata "saja"; spec mengasersi X sebagai himpunan lengkap hasil.
  - TC-FA-CF-365 Data Uji menyebut `Pump` di balik chip `+1 more` pada `Equipment Class`, tetapi Expected tidak memuat klausa tentang chip itu; spec tidak mengasersinya.
  - TC-FA-CF-361 sampai TC-FA-CF-365 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
