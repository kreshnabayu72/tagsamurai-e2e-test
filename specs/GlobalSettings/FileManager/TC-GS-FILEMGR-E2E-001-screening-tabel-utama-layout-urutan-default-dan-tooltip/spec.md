---
id: TC-GS-FILEMGR-E2E-001-screening-tabel-utama-layout-urutan-default-dan-tooltip
title: "Screening Tabel Utama File Manager: Layout, Urutan Default, Row Action, dan Tooltip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-01
  - TC-GS-FILEMGR-02
  - TC-GS-FILEMGR-09
  - TC-GS-FILEMGR-10
  - TC-GS-FILEMGR-11
coverage:
  web: automated
---

# Screening Tabel Utama File Manager: Layout, Urutan Default, Row Action, dan Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2, 33 file aktif (4 halaman pada page size 10), termasuk `budi-avatar.jpg` (JPG, Budi Santoso, `2.4 MB`, Upload Date 02/09/26 14:30) dan `siti-profile.png` (PNG, Siti Rahmawati, Uploaded By System, Upload Date 01/09/26 09:00). Spec tidak membuat, mengubah, atau menghapus data.
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE untuk memastikan Tabel A2 ada (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); membaca warna latar ikon, urutan opsi overlay, dan teks tooltip dari DOM.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Format tanggal General Settings memakai default `dd/MM/yy HH:mm` (tidak diubah spec).

## Test Steps

### TC-GS-FILEMGR-01: Screening halaman File Manager tabel utama oleh Total Control

1. Buka Global Settings > File Manager dari sidebar
2. Tunggu tabel selesai dimuat
3. Amati zona Header, Body, dan Footer dari atas ke bawah tanpa mengisi atau mengklik apa pun
4. Verifikasi Header: Breadcrumb `File Manager` dan tombol bantuan `[?]` tepat di sebelah kanan Breadcrumb
5. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | Recycle Bin` tanpa tombol Create
6. Verifikasi Header: Kartu Storage Usage berdiri sendiri di atas kartu tabel
7. Verifikasi Body: header kolom `Checkbox | File Name (sortable) | File Format (sortable) | User Name (sortable) | Size (sortable) | Uploaded By (sortable) | Upload Date (sortable) | Column Visibility (⋯) (unsortable)`
8. Verifikasi Body: kolom Checkbox terpin di kiri dan kolom Column Visibility (⋯) terpin di kanan
9. Verifikasi Body: baris pertama memuat nilai Tabel A2 `budi-avatar.jpg`, `JPG`, `Budi S`, `2.4 MB`, `Budi S`, dan `02/09/26 14:30` pada kolom File Name, File Format, User Name, Size, Uploaded By, dan Upload Date
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi overlay Column Visibility terbuka
12. Tutup overlay Column Visibility dengan menekan Esc
13. Verifikasi Footer: pagination default 10 baris per halaman

### TC-GS-FILEMGR-02: Urutan default tabel utama Upload Date terbaru di atas dan 10 baris per halaman

14. Verifikasi baris pertama halaman 1 adalah `budi-avatar.jpg` (02/09/26 14:30)
15. Verifikasi baris kedua halaman 1 adalah `siti-profile.png` (01/09/26 09:00)
16. Verifikasi baris ketiga dan seterusnya berurutan menurut Upload Date yang lebih lama (baris ketiga `alex-photo.jpeg`, 20/08/26 10:15)
17. Verifikasi tidak ada panah sort aktif pada kolom mana pun
18. Hitung jumlah baris di halaman pertama
19. Verifikasi halaman pertama memuat tepat 10 baris
20. Verifikasi info pagination menunjukkan total 33 baris

### TC-GS-FILEMGR-10: Tooltip ikon toolbar dan header kolom Actions pada tabel utama

21. Arahkan kursor ke ikon Search di toolbar
22. Verifikasi tooltip `Search`
23. Arahkan kursor ke ikon Filter
24. Verifikasi tooltip `Filter`
25. Arahkan kursor ke ikon Download
26. Verifikasi tooltip `Download`
27. Arahkan kursor ke ikon Changelog
28. Verifikasi tooltip `Changelog`
29. Arahkan kursor ke ikon (⋯) di header kolom Actions
30. Verifikasi tooltip `Column Visibility`

### TC-GS-FILEMGR-11: Tooltip tombol Recycle Bin di toolbar tabel utama

31. Arahkan kursor ke tombol Recycle Bin di toolbar
32. Verifikasi tooltip `Recycle Bin`

### TC-GS-FILEMGR-09: Overlay menu aksi baris tabel utama memuat Download dan Delete

33. Klik ikon elipsis (⋯) pada baris `budi-avatar.jpg`
34. Verifikasi opsi tampil berurutan `Download` (ikon Download2Line, severity dark) lalu `Delete` (ikon DeleteBin6Line, severity danger)
35. Verifikasi tidak ada opsi Preview, Edit, atau Detail
36. Tutup overlay dengan menekan Esc

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (prinsip 2 dan S-14): TC-10 dan TC-11 (hover tooltip) ditaruh sebelum TC-09 karena TC-09 membuka overlay row action; tooltip diasersi sebelum overlay mengubah state fokus (8b butir 5).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 12 dan 36 (tutup overlay dengan Esc), langkah 18 (menghitung baris halaman pertama, bagian dari langkah TC-02). Langkah 10 dan 11 (klik header Column Visibility dan overlay terbuka) ditambahkan karena Expected TC-01 butir b.i mendeskripsikan perilaku klik header itu ("header klik = buka overlay Column Visibility"); isi overlay tidak diasersi karena TC tidak merincinya.
- TC-01 butir a.iii: isi kartu Storage Usage tidak diuji di spec ini; kartu diuji di spec 065 sampai 067.
- Langkah 9 memakai bentuk `[First Name] [Last Initial]` (`Budi S`) untuk User Name dan Uploaded By sesuai Expected TC-04 (`Alexander G`); TC-01 hanya menulis "memuat nilai Tabel A2".
- Langkah 20: total 33 baris berlaku selama tidak ada spec lain yang menambah atau menghapus baris Tabel A2; suite berjalan serial dan spec yang menambah baris (mis. spec 002) memulihkan datanya di hook `after`.
- Alasan spec di atas sekitar 35 langkah (S-10): 36 langkah dihitung nominal, satu langkah di atas ambang; seluruh blok adalah screening baca-saja pada satu dataset Pre-setup yang sama (tanpa mengubah data), dan tiap blok (layout, urutan default, tooltip, overlay row action) berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Tidak ada kelas harness selain screening.
- Temuan untuk QA:
  - TC-01 Expected b.iii hanya menyebut "memuat nilai Tabel A2" tanpa merinci baris mana; spec memeriksa baris pertama default (newest first).
  - Mekanisme seeding Tabel A2 ("fixture BE") tidak disebut di TC, PRD, atau LLD yang dibaca; dicatat di Prerequisites sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
