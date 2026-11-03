---
id: TC-FA-CF-E2E-104-interaksi-search-filter-sort-dengan-create-dan-edit
title: "Interaksi Search, Filter, dan Sort dengan Create dan Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-405
  - TC-FA-CF-645
  - TC-FA-CF-646
coverage:
  web: automated
---

# Interaksi Search, Filter, dan Sort dengan Create dan Edit

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (bernama literal tanpa suffix karena asersi bergantung pada nama baris; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field: `Asset Serial Tag` (Text), `Storage Capacity` (Numeric), `Equipment Class` (Dropdown), `Operating Voltage` (Text), `Total Cost` (Formula), `Depreciated Ratio` (Percentage), `Compliance File` (Document), `Legacy Tag` (Text). `Asset Serial Tag` adalah satu-satunya field yang cocok dengan Search `serial`.
- Data Pre-setup yang diubah spec ini: `Asset Serial Tag` di-rename pada langkah 24 sampai 25 (TC-FA-CF-646 memakai baris itu sebagai satu-satunya hasil Search `serial`; S-06 pengecualian karena Search `serial` mensyaratkan field baseline itu). Pemulihan ke keadaan awal dijamin seed reset baseline Company Alpha (fixture backend, kemampuan disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after`. Efek: Last Updated, Modified By, dan entri audit trail (Changelog, Activity Log, System Log) field itu berubah; suite berjalan serial.
- Data Dinamis milik spec: `Filter Hidden {runId}-104` (Numeric), dibuat lewat UI pada langkah 14 sampai 16; `Tag Renamed {runId}-104` adalah nama hasil rename pada langkah 24.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Filter Hidden {runId}-104` lewat API dan pulihkan `Asset Serial Tag` lewat seed reset baseline.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan ikon sort per header kolom, isi kotak Search, field filter, baris tabel, dan toast.
- State global: tidak ada yang diubah selain data field di atas.

## Test Steps

### TC-FA-CF-405: Mengganti kolom sort tidak mereset Search dan Filter

1. Ketik Search `a`, tekan Enter
2. Klik ikon Filter, pilih Data Type `Text`, klik `[Apply]`
3. Klik header `Data Type` sekali
4. Klik header `Last Updated` sekali
5. Verifikasi kolom `Data Type` kembali netral (ikon sort netral)
6. Verifikasi siklus `Last Updated` mulai dari klik pertama (Oldest First aktif)
7. Verifikasi Search `a` tetap aktif (kotak Search berisi `a`)
8. Verifikasi Filter Data Type `Text` tetap aktif (field filter `Data Type` berisi `Text`)
9. Bersihkan Search dan Filter: klik `(←)`, klik `[Clear Field]`, klik `[Apply]`
10. Klik header `Last Updated` dua kali hingga ikon sort netral
11. Klik ikon Filter untuk menutup Filter Panel

### TC-FA-CF-645: Create field yang tidak cocok dengan filter aktif tidak muncul di tabel terfilter

12. Klik ikon Filter
13. Pilih Data Type `Text`, klik `[Apply]`
14. Klik `[+ Custom Field]`
15. Isi Field Name `Filter Hidden {runId}-104`, pilih Data Type `Numeric`
16. Klik `[Submit]`
17. Verifikasi toast `Success, custom field has been created.` tampil
18. Verifikasi tabel terfilter menampilkan sedikitnya satu baris Text (baris `Asset Serial Tag`)
19. Verifikasi baris `Filter Hidden {runId}-104` tidak tampil pada tabel terfilter
20. Klik `[Clear Field]`, klik `[Apply]`
21. Verifikasi baris `Filter Hidden {runId}-104` tampil

### TC-FA-CF-646: Edit field sehingga tidak cocok dengan Search aktif menghilangkan barisnya dari tabel

22. Ketik Search `serial`, tekan Enter
23. Klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`
24. Ubah Field Name menjadi `Tag Renamed {runId}-104`
25. Klik `[Save]`
26. Verifikasi toast `Success, custom field has been updated.` tampil
27. Verifikasi baris `Tag Renamed {runId}-104` hilang dari tabel karena tidak lagi cocok dengan `serial`
28. Verifikasi tabel menampilkan empty state `No results found`
29. Klik `(←)`

## Notes

- Spec memuat 29 langkah, di bawah ambang sekitar 35 langkah. Satu topik (interaksi kontrol tabel dengan Create dan Edit), satu akun, satu dataset Company Alpha.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 10, dan 11 (membersihkan Search, Filter, dan Sort serta menutup Filter Panel sebelum TC-FA-CF-645, S-09); langkah 20 (`[Clear Field]` melepas filter, bagian dari TC-FA-CF-645 "Bersihkan filter Data Type"); langkah 22 (Search `serial` menemukan baris target `Asset Serial Tag` yang diedit pada langkah 23, R-16); langkah 29 (`(←)` menutup input dan mengosongkan keyword).
- Langkah 17 dan 26 (toast sukses) adalah `Verifikasi` tambahan di luar Expected TC (S-03): toast hasil server menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence baris pada langkah 19 dan 27 (bagian 8b butir 2). Langkah 18 menjadi pembanding positif bagi asersi absence langkah 19.
- Alur langkah 14 sampai 16 menyalin langkah Create yang dipakai TC Create (`[+ Custom Field]`, isi Field Name, pilih Data Type, `[Submit]`); langkah 23 sampai 25 menyalin langkah Edit (row action `Edit`, ubah Field Name, `[Save]`).
- Temuan untuk QA:
  - TC-FA-CF-645 Expected tidak menyebut toast; langkah 17 menambahnya sebagai anchor (lihat butir di atas).
  - TC-FA-CF-646 Expected b menyebut empty state `No results found` tanpa Description; langkah 28 hanya mengasersi `No results found`.
  - TC-FA-CF-646 memakai data Pre-setup (`Asset Serial Tag`) sebagai target aksi tulis; pemulihannya bergantung pada seed reset baseline Company Alpha.
  - TC-FA-CF-405 menyebut "siklus Last Updated mulai dari klik pertama" tanpa menyebut ikon sort yang diharapkan; langkah 6 mengasersi Oldest First aktif sesuai TC-FA-CF-403 (klik pertama).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
