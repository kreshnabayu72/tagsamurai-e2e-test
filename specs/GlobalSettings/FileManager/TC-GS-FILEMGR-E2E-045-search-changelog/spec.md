---
id: TC-GS-FILEMGR-E2E-045-search-changelog
title: "Search Modal Changelog: Siklus Toolbar, Substring Seluruh Kolom, dan Empty Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-31
  - TC-GS-FILEMGR-156
  - TC-GS-FILEMGR-157
coverage:
  web: automated
---

# Search Modal Changelog: Siklus Toolbar, Substring Seluruh Kolom, dan Empty Hasil

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A4 (14 entri Changelog File Manager; format tanggal General Settings default `dd/MM/yy HH:mm`). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Entri literal sesuai Tabel A4 karena asersi Search bergantung pada nilai Action, File Name, Field, Old Value, New Value, dan Modified By (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`). Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga hitungan entri tidak diasersi sebagai total absolut: hitungan dibatasi dengan Filter Date rentang Date Tabel A4 (`23/08/26` sampai `14/09/26`, inklusif; entri terlama 23/08/26 08:00 dan terbaru 14/09/26 02:00) yang hanya memuat populasi Tabel A4.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: memilih rentang Date `23/08/26` sampai `14/09/26` pada date range picker Filter Panel Changelog (Date entri Tabel A4 tetap, bukan relatif); membaca fokus dan lebar input Search, placeholder, serta ikon (✕) dan (←); membaca jumlah entri total pada pagination.

## Test Steps

1. Klik ikon Changelog di toolbar
2. Klik ikon Filter di toolbar modal, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik ikon Filter

### TC-GS-FILEMGR-156: Siklus interaksi Search toolbar modal Changelog (reveal, submit Enter, clear, collapse)

3. Klik ikon Search di toolbar modal
4. Verifikasi input Search melebar
5. Verifikasi input Search mendapat fokus otomatis
6. Verifikasi placeholder `Search action, file name...`
7. Ketik `retired` tanpa menekan Enter
8. Verifikasi ikon (✕) muncul di input Search
9. Verifikasi tabel belum tersaring (total 14 entri dalam rentang Date Tabel A4)
10. Tekan Enter
11. Verifikasi tabel hanya memuat entri C02 (`retired-photo.jpg`)
12. Klik ikon (✕) di input Search
13. Verifikasi input Search kosong
14. Verifikasi tabel tetap menampilkan entri C02
15. Tekan Enter pada input yang sudah kosong
16. Verifikasi tabel kembali menampilkan 14 entri (rentang Date Tabel A4)
17. Ketik Search `retired`, tekan Enter
18. Klik ikon panah (←) di kiri input Search
19. Verifikasi input Search menutup
20. Verifikasi tabel langsung kembali ke 14 entri (rentang Date Tabel A4)

### TC-GS-FILEMGR-157: Search substring pada kolom Action, File Name, Field, Old Value, New Value, dan Modified By

21. Ketik Search `PERMANENTLY`, tekan Enter
22. Verifikasi tabel memuat 12 entri Action `Permanently Delete` (C01–C03 dan C06–C14), tidak membedakan huruf besar-kecil
23. Ganti isi kotak search dengan `archive-photo-03`, tekan Enter
24. Verifikasi tabel hanya memuat entri `archive-photo-03.jpg`
25. Ganti isi kotak search dengan `File Name`, tekan Enter
26. Verifikasi tabel memuat seluruh 14 entri dalam rentang Date Tabel A4 (nilai Field `File Name`)
27. Ganti isi kotak search dengan `former`, tekan Enter
28. Verifikasi tabel hanya memuat entri C01 (Old Value `former-avatar.png`)
29. Ganti isi kotak search dengan `—`, tekan Enter
30. Verifikasi tabel memuat seluruh 14 entri dalam rentang Date Tabel A4 (New Value `—`)
31. Ganti isi kotak search dengan `agus`, tekan Enter
32. Verifikasi tabel memuat 4 entri: C03, `archive-photo-02.jpg`, `archive-photo-05.jpg`, `archive-photo-08.jpg`

### TC-GS-FILEMGR-31: Tampilan modal Changelog saat Search tidak menemukan hasil

33. Ganti isi kotak search dengan `zzzxyz-tidak-ada`, tekan Enter
34. Verifikasi ilustrasi dengan judul `No results found`
35. Verifikasi deskripsi `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 156, 157, 31. Siklus toolbar di awal, empty state di akhir supaya hasil kosong tidak mengganggu TC lain.
- Anchor asersi "hanya"/"tepat N entri": langkah 9 dan 16 membuktikan tabel Changelog memuat 14 entri (dalam rentang Date Tabel A4 dari langkah 2) sebelum Search menyaring (pembanding sedikitnya satu baris). Empty state "No results found" (langkah 34) adalah anchor positif sah untuk absence hasil Search.
- Jumlah entri pada langkah 22, 26, 30, 32 dibaca dari total pagination (10 baris per halaman, entri melebihi 10 berada di halaman 2).
- Kata kunci `File Name` (langkah 25) mencocokkan nilai Field `File Name` pada seluruh entri; tidak ada nilai kolom lain yang memuat teks itu.
- Langkah penghubung tambahan: langkah 2 (Filter Date rentang Tabel A4 agar hitungan hanya dari populasi Tabel A4; tidak ada di TC, dicatat per S-03). Tidak ada langkah penghubung lain selain langkah 17 (mengulang `retired` yang diwajibkan TC-GS-FILEMGR-156 langkah 6).
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4).
  - TC sumber (mis. TC-GS-FILEMGR-172 dan TC Changelog sejenis) menyatakan hitungan entri absolut ("14 entri", "5 baris") yang bertentangan dengan S-12 (Changelog tidak dapat di-seed ulang atau dibersihkan). Spec membatasi dengan Filter Date rentang Tabel A4 sebagai langkah penghubung; pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang Tabel A4 atau hitungan relatif.
  - Search `—` (langkah 29) memasukkan karakter em dash (`—`) ke input Search; TC tidak menjelaskan cara mengetiknya, sehingga skrip perlu memasukkan karakter Unicode langsung.
