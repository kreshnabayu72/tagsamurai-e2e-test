---
id: TC-FA-CF-E2E-123-changelog-download-dan-paginasi
title: "Modal Changelog: Download dan Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-476
  - TC-FA-CF-478
coverage:
  web: automated
---

# Modal Changelog: Download dan Paginasi

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Changelog (Pre-setup #19) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Changelog (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CHANGELOG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_CHANGELOG_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Changelog (Pre-setup #19; Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Jakarta) dengan dua belas entri Changelog tab General (dua belas menurut seed: halaman 1 memuat sepuluh entri dan halaman 2 memuat dua entri) dan dua entri Create tab Purchasing, dirujuk lewat fixture baru `Fixture.faCustomFields.changelogSeed` (fixture belum ada, disediakan tim FE). Seed dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Entri seed yang dipakai: `17/10/26, 10:45` `Create` `Asset Serial Tag` (Field `Name`, Old Value `—`, New Value `Asset Serial Tag`, Modified By Budi Santoso) dan entri `Edit` `Storage Capacity` (satu-satunya entri `Storage Capacity`).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data dan tidak menambah entri Changelog.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: penangkapan berkas unduhan; pembacaan nama berkas, jumlah baris data, dan isi sel berkas CSV dan XLSX (disediakan tim FE); pembacaan jumlah entri Changelog tab General sebelum aksi (N_G; audit trail tidak diasersi sebagai angka absolut, bagian 8b butir 10; dua belas menurut seed).
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah entri Changelog tab General (N_G) sebelum aksi pertama
2. Klik icon Changelog di toolbar

### TC-FA-CF-476: Download Modal Changelog: nama berkas, scope baris, dan isi sel

3. Ketik Search `Storage`, tekan Enter
4. Klik icon Download > `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Changelog-Custom-Field.csv` terunduh
7. Verifikasi berkas memuat entri `Storage Capacity` hasil Search
8. Verifikasi berkas tidak memuat entri selain hasil Search
9. Klik `(←)` pada kotak Search
10. Klik icon Download > `Download as XLSX`
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Changelog-Custom-Field.xlsx` terunduh
13. Verifikasi berkas memuat seluruh entri tab General (N_G baris data)
14. Verifikasi sel Modified By berisi nama lengkap (entri `Asset Serial Tag` `Create` berisi `Budi Santoso`)
15. Verifikasi sel kosong ditulis `-` (sel Old Value entri `Asset Serial Tag` `Create`)

### TC-FA-CF-478: Paginasi Modal Changelog default 10 dengan pilihan 10, 25, 50, 100

16. Perhatikan footer Modal Changelog
17. Verifikasi halaman 1 memuat 10 entri
18. Klik next ke halaman 2
19. Verifikasi halaman 2 memuat sisa entri sejumlah N_G dikurangi 10 (dua menurut seed)
20. Buka pilihan page size
21. Verifikasi pilihan page size: `10`, `25`, `50`, `100`
22. Tutup pilihan page size
23. Klik icon `[✕]` untuk menutup modal

## Notes

- Spec memuat 23 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Download dan paginasi Modal Changelog), satu akun, satu dataset (Company Changelog) tanpa mengubah data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencatat N_G), langkah 2 (membuka modal sesuai langkah uji TC), langkah 9 (`(←)` menutup kotak Search dan mereset tabel sesuai langkah "Bersihkan Search" TC-FA-CF-476), langkah 22 dan 23 (menutup pilihan page size dan modal). Search pada langkah 3 menyaring baris target dan menjadi bagian langkah uji TC-FA-CF-476 (R-16).
- Anchor absence: langkah 7 (entri `Storage Capacity` tampil di berkas) mendahului absence langkah 8; langkah 5 dan 11 (tidak ada toast) ditulis tepat setelah pemicu unduh dan sebelum asersi berkas (bagian 8b butir 11).
- Langkah 14 dan 15 (isi sel berkas) termasuk kelas binary buffer; keduanya berada di TC-FA-CF-476 yang juga memuat nama berkas dan scope baris (kelas fungsional). TC-FA-CF-476 tidak dipecah karena satu TC satu spec dan Expected c mengikutinya.
- Urutan TC di spec: 476 lalu 478.
- Temuan untuk QA:
  - Email akun Total Control Company Changelog tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-476 bercampur kelas: Expected a dan b (nama berkas dan scope baris) fungsional, sedangkan Expected c (isi sel) kelas binary buffer. Spec memuat keduanya karena satu TC satu spec; usulan: pisahkan Expected c ke TC tersendiri di spec kelas binary buffer.
  - TC-FA-CF-476 Expected c ("sel kosong ditulis `-`") tidak menyebut sel mana; spec memakai Old Value entri `Create` (`—` pada tabel).
  - TC-FA-CF-478 Expected a ("halaman 2 memuat 2 entri") menyebut angka absolut; karena audit trail tidak boleh diasersi sebagai angka absolut (S-12), spec memakai N_G yang dibaca sebelum aksi.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
