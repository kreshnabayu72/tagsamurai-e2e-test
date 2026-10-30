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
- Suite serial (`parallel: false`): hitungan entri hanya valid bila tidak ada spec lain yang menghasilkan entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca fokus dan lebar input Search, placeholder, serta ikon (✕) dan (←); membaca jumlah entri total pada pagination.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-GS-FILEMGR-156: Siklus interaksi Search toolbar modal Changelog (reveal, submit Enter, clear, collapse)

2. Klik ikon Search di toolbar modal
3. Verifikasi input Search melebar
4. Verifikasi input Search mendapat fokus otomatis
5. Verifikasi placeholder `Search action, file name...`
6. Ketik `retired` tanpa menekan Enter
7. Verifikasi ikon (✕) muncul di input Search
8. Verifikasi tabel belum tersaring (total 14 entri)
9. Tekan Enter
10. Verifikasi tabel hanya memuat entri C02 (`retired-photo.jpg`)
11. Klik ikon (✕) di input Search
12. Verifikasi input Search kosong
13. Verifikasi tabel tetap menampilkan entri C02
14. Tekan Enter pada input yang sudah kosong
15. Verifikasi tabel kembali menampilkan 14 entri
16. Ketik Search `retired`, tekan Enter
17. Klik ikon panah (←) di kiri input Search
18. Verifikasi input Search menutup
19. Verifikasi tabel langsung kembali ke 14 entri

### TC-GS-FILEMGR-157: Search substring pada kolom Action, File Name, Field, Old Value, New Value, dan Modified By

20. Ketik Search `PERMANENTLY`, tekan Enter
21. Verifikasi tabel memuat 12 entri Action `Permanently Delete` (C01–C03 dan C06–C14), tidak membedakan huruf besar-kecil
22. Ganti isi kotak search dengan `archive-photo-03`, tekan Enter
23. Verifikasi tabel hanya memuat entri `archive-photo-03.jpg`
24. Ganti isi kotak search dengan `File Name`, tekan Enter
25. Verifikasi tabel memuat seluruh 14 entri (nilai Field `File Name`)
26. Ganti isi kotak search dengan `former`, tekan Enter
27. Verifikasi tabel hanya memuat entri C01 (Old Value `former-avatar.png`)
28. Ganti isi kotak search dengan `—`, tekan Enter
29. Verifikasi tabel memuat seluruh 14 entri (New Value `—`)
30. Ganti isi kotak search dengan `agus`, tekan Enter
31. Verifikasi tabel memuat 4 entri: C03, `archive-photo-02.jpg`, `archive-photo-05.jpg`, `archive-photo-08.jpg`

### TC-GS-FILEMGR-31: Tampilan modal Changelog saat Search tidak menemukan hasil

32. Ganti isi kotak search dengan `zzzxyz-tidak-ada`, tekan Enter
33. Verifikasi ilustrasi dengan judul `No results found`
34. Verifikasi deskripsi `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 156, 157, 31. Siklus toolbar di awal, empty state di akhir supaya hasil kosong tidak mengganggu TC lain.
- Anchor asersi "hanya"/"tepat N entri": langkah 8 dan 15 membuktikan tabel Changelog memuat 14 entri sebelum Search menyaring (pembanding sedikitnya satu baris). Empty state "No results found" (langkah 33) adalah anchor positif sah untuk absence hasil Search.
- Jumlah entri pada langkah 21, 25, 29, 31 dibaca dari total pagination (10 baris per halaman, entri melebihi 10 berada di halaman 2).
- Kata kunci `File Name` (langkah 24) mencocokkan nilai Field `File Name` pada seluruh entri; tidak ada nilai kolom lain yang memuat teks itu.
- Tidak ada langkah penghubung selain langkah 16 (mengulang `retired` yang diwajibkan TC-GS-FILEMGR-156 langkah 6).
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4); hitungan 14 entri mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Search `—` (langkah 28) memasukkan karakter em dash (`—`) ke input Search; TC tidak menjelaskan cara mengetiknya, sehingga skrip perlu memasukkan karakter Unicode langsung.
