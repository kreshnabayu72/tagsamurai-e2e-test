---
id: TC-GS-FILEMGR-E2E-039-search-recycle-bin
title: "Search Modal Recycle Bin: Siklus Toolbar, Substring Kolom, dan Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-24
  - TC-GS-FILEMGR-201
  - TC-GS-FILEMGR-202
  - TC-GS-FILEMGR-203
coverage:
  web: automated
---

# Search Modal Recycle Bin: Siklus Toolbar, Substring Kolom, dan Size

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A3 karena asersi Search bergantung pada nama (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan "16 baris" hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca fokus dan lebar input Search, placeholder, serta ikon (✕) dan (←).

## Test Steps

1. Klik tombol Recycle Bin di toolbar

### TC-GS-FILEMGR-201: Siklus interaksi Search toolbar modal Recycle Bin (reveal, submit Enter, clear, collapse)

2. Klik ikon Search di toolbar modal
3. Verifikasi input Search melebar
4. Verifikasi input Search mendapat fokus otomatis
5. Verifikasi placeholder `Search file name, user name...`
6. Ketik `legacy` tanpa menekan Enter
7. Verifikasi ikon (✕) muncul di input Search
8. Verifikasi tabel belum tersaring (total 16 baris)
9. Tekan Enter
10. Verifikasi tabel hanya memuat `legacy-photo.jpeg`
11. Klik ikon (✕) di input Search
12. Verifikasi input Search kosong
13. Verifikasi input Search tetap terbuka
14. Verifikasi tabel tetap menampilkan `legacy-photo.jpeg`
15. Tekan Enter pada input yang sudah kosong
16. Verifikasi tabel kembali menampilkan 16 baris
17. Ketik Search `legacy`, tekan Enter
18. Klik ikon panah (←) di kiri input Search
19. Verifikasi input Search menutup
20. Verifikasi tabel langsung kembali ke 16 baris

### TC-GS-FILEMGR-202: Search substring dan case-insensitive pada File Name, File Format, User Name, dan Deleted By

21. Ketik Search `LEGACY`, tekan Enter
22. Verifikasi tabel hanya memuat `legacy-photo.jpeg` (tidak membedakan huruf besar-kecil)
23. Ganti isi kotak search dengan `jpeg`, tekan Enter
24. Verifikasi tabel hanya memuat `legacy-photo.jpeg` (File Format `JPEG`)
25. Ganti isi kotak search dengan `siti`, tekan Enter
26. Verifikasi tabel hanya memuat `legacy-photo.jpeg` (User Name `Siti Rahmawati`)
27. Ganti isi kotak search dengan `agus`, tekan Enter
28. Verifikasi tabel memuat tepat 5 baris: `expired-avatar.jpg`, `recycled-photo-05.jpg`, `recycled-photo-06.jpg`, `recycled-photo-07.jpg`, `recycled-photo-08.jpg` (Deleted By `Agus Wibowo`)

### TC-GS-FILEMGR-203: Search pada kolom Size mencocokkan nilai yang tampil

29. Ganti isi kotak search dengan `2.0 MB`, tekan Enter
30. Verifikasi tabel hanya memuat `old-avatar.png`

### TC-GS-FILEMGR-24: Tampilan Recycle Bin saat Search tidak menemukan hasil

31. Ganti isi kotak search dengan `zzzxyz-tidak-ada`, tekan Enter
32. Verifikasi ilustrasi dengan judul `No results found`
33. Verifikasi deskripsi `Try adjusting your search or filter.`
34. Verifikasi bukan empty state `Recycle bin is empty`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 201, 202, 203, 24. Siklus toolbar (screening state input) di awal; TC-GS-FILEMGR-24 (empty state) di akhir supaya Search berisi hasil kosong tidak mengganggu TC lain.
- Anchor asersi "hanya"/"tepat N baris": langkah 8 dan 16 membuktikan tabel Recycle Bin memuat 16 baris sebelum Search disaring (pembanding sedikitnya satu baris). Empty state "No results found" (langkah 32) adalah anchor positif yang sah untuk absence hasil Search.
- TC-GS-FILEMGR-201 dan 202 memakai kata kunci `legacy` pada langkah 17 dan 21 tanpa membuka ulang modal; kotak Search yang ditutup lewat (←) pada langkah 18 dibuka lagi secara atomik oleh "Ketik Search ..." (bagian 8b butir 9).
- Tidak ada langkah penghubung selain langkah 17 (mengulang `legacy` yang diwajibkan TC-GS-FILEMGR-201 langkah 6).
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A3 serta kondisi waktu relatif tidak didefinisikan di TC; ditulis sebagai kemampuan "disediakan tim FE/BE" (Q-4). Hitungan 16 baris mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Baris `due-photo.png` (sekarang − 31 hari) tampil sampai job auto-purge berikutnya; pada spec ini baris itu tidak diasersi tetapi ikut dalam hitungan 16 baris (langkah 8 dan 16), sehingga hitungan tidak stabil bila job berjalan antara seeding dan asersi (Q-3).
  - Search `agus` pada TC-GS-FILEMGR-202 butir d mengharapkan 5 baris Deleted By `Agus Wibowo`; hasil mengasumsikan tidak ada kolom lain yang memuat `agus` pada data Tabel A3 (pemeriksaan data: tidak ada).
