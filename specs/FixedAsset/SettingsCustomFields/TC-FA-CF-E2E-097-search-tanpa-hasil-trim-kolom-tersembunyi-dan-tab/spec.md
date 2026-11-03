---
id: TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab
title: "Search: Tanpa Hasil, Trim, Kolom Tersembunyi, State Per Tab, dan Irisan dengan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-366
  - TC-FA-CF-367
  - TC-FA-CF-368
  - TC-FA-CF-370
  - TC-FA-CF-371
  - TC-FA-CF-373
coverage:
  web: automated
---

# Search: Tanpa Hasil, Trim, Kolom Tersembunyi, State Per Tab, dan Irisan dengan Filter

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama baris; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral` dan `Fixture.faCustomFields.alphaPurchasing`):
  - Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12): `Asset Serial Tag` (Text), `Storage Capacity` (Numeric, Placeholder `Capacity in GB`), `Equipment Class` (Dropdown), `Operating Voltage` (Text), `Total Cost` (Formula), `Depreciated Ratio` (Percentage), `Compliance File` (Document), `Legacy Tag` (Text).
  - Tab Purchasing Company Alpha (Pre-setup #13): `Vendor Code` (Text), `Warranty Months` (Numeric), `Rated Precision` (Numeric), `Long Option Field` (Dropdown).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi kotak Search termasuk spasi di tepi, isi sel tabel, dan chip filter; membuka Overlay Column Visibility dari header kolom Actions `(⋯)`.
- State global: visibilitas kolom Placeholder disembunyikan pada langkah 13 dan ditampilkan kembali pada langkah 17. Hook `after` spec ini menghapus preferensi visibilitas kolom di browser sebagai cadangan (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-CF-366: Search tanpa hasil menampilkan empty state

1. Ketik Search `zzzxxx`, tekan Enter
2. Verifikasi ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.` tampil
3. Klik `(←)`

### TC-FA-CF-367: Nilai kolom non-searchable tidak menemukan baris

4. Ketik Search `17/10/26`, tekan Enter
5. Verifikasi empty state `No results found` tampil (pencarian tidak memfilter berdasarkan kolom Last Updated)
6. Ganti isi kotak search dengan `ON`, tekan Enter
7. Verifikasi empty state `No results found` tampil (pencarian tidak memfilter berdasarkan switch Active)
8. Klik `(←)`

### TC-FA-CF-368: Query Search di-trim saat Enter tanpa mengubah isi input

9. Ketik Search `  serial  ` (dengan dua spasi di awal dan akhir), tekan Enter
10. Verifikasi hasil sama dengan `serial` (tabel hanya menampilkan baris `Asset Serial Tag`)
11. Verifikasi isi input tetap `  serial  `
12. Klik `(←)`

### TC-FA-CF-370: Kolom tersembunyi dikecualikan dari Search dan kembali dicari setelah ditampilkan

13. Klik header kolom Actions `(⋯)`, hapus centang kolom `Placeholder` pada Overlay Column Visibility, lalu tutup overlay
14. Ketik Search `in gb`, tekan Enter
15. Verifikasi empty state `No results found` tampil (`in gb` tidak menemukan baris)
16. Klik `(←)`
17. Klik header kolom Actions `(⋯)`, centang kembali kolom `Placeholder` pada Overlay Column Visibility, lalu tutup overlay
18. Ketik Search `in gb`, tekan Enter
19. Verifikasi tabel hanya menampilkan baris `Storage Capacity`
20. Klik `(←)`

### TC-FA-CF-371: Search berlaku pada tab aktif dan state Search tiap tab terpisah

21. Ketik Search `serial` pada tab General, tekan Enter
22. Klik tab `Purchasing`
23. Ketik Search `vendor`, tekan Enter
24. Verifikasi tabel tab Purchasing hanya menampilkan baris `Vendor Code`
25. Verifikasi hasil tab Purchasing tidak dipengaruhi `serial` (kotak Search tab Purchasing hanya berisi `vendor`)
26. Klik tab `General`
27. Verifikasi Search `serial` masih aktif (kotak Search tab General berisi `serial`)
28. Verifikasi tabel tab General hanya menampilkan baris `Asset Serial Tag`

### TC-FA-CF-373: Kombinasi Search lalu Filter dan Filter lalu Search menghasilkan irisan yang sama

29. Klik `(←)`
30. Ketik Search `a`, tekan Enter
31. Klik ikon Filter, pilih Data Type `Text`, klik `[Apply]`
32. Verifikasi tabel menampilkan sedikitnya satu baris dan seluruh baris yang tampil bertipe `Text` serta memuat `a` pada kolom Searchable
33. Catat nama baris hasil langkah 32
34. Bersihkan Search dan Filter: klik `(←)`, klik `[Clear Field]`, klik `[Apply]`
35. Pilih Data Type `Text` pada Filter Panel, klik `[Apply]`
36. Ketik Search `a`, tekan Enter
37. Verifikasi baris yang tampil sama dengan baris yang dicatat pada langkah 33

## Notes

- Spec memuat 37 langkah, sedikit di atas ambang sekitar 35 langkah. Alasan: seluruhnya satu topik (Search tabel utama tab General dan Purchasing) pada satu dataset (Company Alpha) dan satu akun; tiap blok TC dimulai dari state Search tertutup dan tetap bermakna bila blok lain gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 8, 12, 16, 20, dan 29 (`(←)` menutup input dan mengosongkan keyword sebelum TC berikutnya, S-09); langkah 13 dan 17 (menyembunyikan dan menampilkan kembali kolom Placeholder, bagian dari TC-FA-CF-370); langkah 33 (mencatat hasil untuk perbandingan); langkah 34 (membersihkan Search dan Filter, mengikuti langkah "Bersihkan semua" pada TC-FA-CF-373).
- Urutan TC mengikuti urutan TC sumber. TC-FA-CF-371 meninggalkan Search `vendor` pada tab Purchasing; state itu tidak memengaruhi TC-FA-CF-373 yang berjalan di tab General.
- Asersi absence TC-FA-CF-367 dan TC-FA-CF-370 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2). Asersi universal langkah 32 didahului pembanding "sedikitnya satu baris" pada Verifikasi yang sama.
- Temuan untuk QA:
  - TC-FA-CF-373 Expected menyebut "baris Text yang memuat `a` pada kolom Searchable" tanpa menyebut nama baris; spec mengasersi himpunan baris hasil urutan pertama sama dengan urutan kedua (langkah 37) dan bahwa tiap baris bertipe `Text` serta memuat `a`.
  - TC-FA-CF-373 tidak menyebut apakah Filter Panel tetap terbuka setelah `[Apply]`; spec menulis langkah 35 tanpa membuka ulang panel.
  - TC-FA-CF-371 Expected a menyebut "tanpa dipengaruhi `serial`" tanpa cara memeriksanya; langkah 25 membaca isi kotak Search tab Purchasing.
  - Pre-setup #13 tidak menyebut Placeholder atau Modified By field Purchasing; spec hanya memakai nama field `Vendor Code`.
  - TC-FA-CF-366, TC-FA-CF-367, TC-FA-CF-368, TC-FA-CF-370, TC-FA-CF-371, dan TC-FA-CF-373 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
