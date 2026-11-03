---
id: TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang
title: "Filter: Clear Field, Kotak Cari Dropdown, dan Chip"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-385
  - TC-FA-CF-386
  - TC-FA-CF-387
  - TC-FA-CF-388
  - TC-FA-CF-638
coverage:
  web: automated
---

# Filter: Clear Field, Kotak Cari Dropdown, dan Chip

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama dan Value Type seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field: `Asset Serial Tag` (Text, Specific), `Storage Capacity` (Numeric, Specific), `Equipment Class` (Dropdown, Specific), `Operating Voltage` (Text, Global), `Total Cost` (Formula, Value Type `—`), `Depreciated Ratio` (Percentage, Specific), `Compliance File` (Document, Specific), `Legacy Tag` (Text, Specific). Opsi Data Type pada dropdown filter: `Document`, `Dropdown`, `Formula`, `Numeric`, `Percentage`, `Text`.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan chip filter di dalam field, centang opsi di dalam dropdown, kotak cari di dalam dropdown, dan baris hasil tabel.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-385: Memilih opsi Value Type menyaring keluar baris Formula yang bernilai kosong

1. Klik ikon Filter
2. Pilih Value Type `Specific`, klik `[Apply]`
3. Verifikasi tabel menampilkan baris Specific: `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Depreciated Ratio`, `Compliance File`, dan `Legacy Tag`
4. Verifikasi baris `Total Cost` (Value Type `—`) tidak tampil
5. Buka dropdown Value Type
6. Verifikasi dropdown Value Type hanya memuat opsi `Global` dan `Specific` (tidak ada opsi untuk nilai kosong)

### TC-FA-CF-386: Clear Field melepas filter tanpa mereset Search dan Sort

7. Tutup dropdown Value Type, klik `[Clear Field]`, klik `[Apply]`
8. Ketik Search `a`, tekan Enter
9. Klik header `Field Name` sekali (menaik)
10. Klik header `Field Name` sekali lagi (menurun)
11. Pilih Data Type `Text` pada Filter Panel, klik `[Apply]`
12. Klik `[Clear Field]`, klik `[Apply]`
13. Verifikasi filter Data Type dilepas (field Data Type pada Filter Panel kosong)
14. Verifikasi Search `a` tetap aktif (kotak Search berisi `a`)
15. Verifikasi Sort menurun tetap aktif (ikon sort turun aktif pada header `Field Name`)
16. Klik `(←)`, lalu klik header `Field Name` sekali hingga ikon sort netral

### TC-FA-CF-387: Kotak cari di dalam dropdown filter mempersempit opsi

17. Buka dropdown Data Type
18. Ketik `pe` pada kotak cari dropdown
19. Verifikasi daftar opsi menyempit menjadi opsi yang memuat `pe`, yaitu `Percentage`
20. Ganti isi kotak cari dropdown dengan `zzzxxx`
21. Verifikasi dropdown menampilkan `No results found`
22. Kosongkan kotak cari dropdown, lalu tutup dropdown Data Type

### TC-FA-CF-388: Menghapus chip lewat tombol silang menghapus centang opsi terkait di dalam dropdown

23. Buka dropdown Data Type, pilih `Text` dan `Numeric`
24. Verifikasi chip `Text` dan `Numeric` tampil di dalam field
25. Klik `✕` pada chip `Text`
26. Verifikasi chip `Text` terhapus dari field
27. Verifikasi chip `Numeric` tetap tampil
28. Buka dropdown Data Type
29. Verifikasi centang `Text` kosong
30. Verifikasi centang `Numeric` tetap tercentang

### TC-FA-CF-638: Menghapus centang di dalam dropdown filter menghapus chip terkait

31. Tutup dropdown Data Type, klik `[Clear Field]`
32. Buka dropdown Data Type, pilih `Text` dan `Numeric`
33. Hapus centang `Numeric` di dalam dropdown
34. Verifikasi chip `Numeric` hilang dari field
35. Verifikasi chip `Text` tetap ada
36. Verifikasi centang `Text` di dalam dropdown tetap tercentang

## Notes

- Spec memuat 36 langkah, sedikit di atas ambang sekitar 35 langkah. Alasan: seluruhnya satu topik (kontrol Filter Panel tabel utama tab General), satu dataset (Company Alpha) dan satu akun; tiap blok TC dimulai dari state panel yang dibersihkan dan tetap bermakna bila blok lain gagal, dan langkah `Verifikasi` per klausa mendominasi jumlah langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 12, dan 31 (`[Clear Field]` sebagai langkah "Bersihkan" antar TC; cara membersihkan tidak disebut TC); langkah 16 (mengosongkan Search dan mereset Sort sebelum TC berikutnya); langkah 22 (mengosongkan kotak cari dan menutup dropdown).
- Asersi absence langkah 4 didahului langkah 3 (baris Specific lainnya tampil) sebagai anchor positif (bagian 8b butir 2); asersi langkah 6 didahului langkah 5 (dropdown terbuka dengan opsi `Global` dan `Specific` tampil).
- Temuan untuk QA:
  - TC-FA-CF-387 Expected b menyebut "kata kunci tanpa kecocokan" tanpa menyebut nilainya; spec memakai `zzzxxx` (langkah 20).
  - TC-FA-CF-385 Expected a menyebut "baris Specific lainnya tampil" tanpa menyebut nama; spec menyebut keenam baris Specific baseline (jumlah enam disebut TC-FA-CF-397).
  - TC-FA-CF-386 Expected tidak menyebut cara memeriksa filter "dilepas"; langkah 13 membaca field Data Type pada Filter Panel.
  - TC-FA-CF-388 Expected b dan c sama-sama menyebut centang `Text` kosong; spec mengasersinya sekali di dalam dropdown (langkah 29).
  - Spec mengasumsikan Filter Panel tetap terbuka setelah `[Apply]` dan dropdown tidak menutup panel (TC tidak menyatakannya secara eksplisit).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
