---
id: TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama
title: "Tooltip, Hover, dan Popover +N more Tabel Utama"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-437
  - TC-FA-FAAM-438
  - TC-FA-FAAM-439
  - TC-FA-FAAM-440
  - TC-FA-FAAM-441
  - TC-FA-FAAM-442
  - TC-FA-FAAM-443
  - TC-FA-FAAM-444
  - TC-FA-FAAM-445
coverage:
  web: automated
---

# Tooltip, Hover, dan Popover +N more Tabel Utama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Brand `Dell`, model `3310`, `5420`, `7420`, Modified By `Sarah J`), `Service Vehicle` (Pre-setup #14, Default Addon `Maintenance`, `Tracking`, `Maps`), `Multi Brand Item` (Pre-setup #14m, lebih dari 2 Brand), Asset Name dengan lebih dari 2 Default Label (Pre-setup #14n), dan baris ber-Category `Laptop` (anak `Electronics`; nama baris tidak tertulis di Pre-setup, lihat Temuan untuk QA).
- Kemampuan teknis: hover, navigasi fokus dengan Tab.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-437: Hover Brand dan Model/Type menampilkan nama penuh badge
1. Arahkan kursor ke badge Brand `Dell`
2. Verifikasi tooltip `Dell` pada badge Brand
3. Arahkan kursor ke badge Model/Type `3310`
4. Verifikasi tooltip `3310` pada badge Model/Type
### TC-FA-FAAM-438: Hover Category menampilkan hierarki lengkap
5. Arahkan kursor ke badge Category `Laptop` (anak `Electronics`)
6. Verifikasi tooltip `Electronics > Laptop`
### TC-FA-FAAM-439: Hover Modified By menampilkan nama lengkap
7. Arahkan kursor ke teks `Sarah J`
8. Verifikasi tooltip `Sarah Johnson`
### TC-FA-FAAM-440: Tooltip header Default Addon dan Default Label
9. Arahkan kursor ke header Default Addon
10. Verifikasi tooltip `Applied by default to new & existing assets under this asset name`
11. Arahkan kursor ke header Default Label
12. Verifikasi tooltip `Applied by default to new & existing assets under this asset name, locked per asset`
### TC-FA-FAAM-441: Tooltip icon toolbar dapat diakses lewat fokus keyboard
13. Fokuskan icon Search dengan Tab
14. Verifikasi tooltip `Search` tampil saat fokus
15. Fokuskan icon Filter dengan Tab
16. Verifikasi tooltip `Filter` tampil saat fokus
17. Fokuskan icon Download dengan Tab
18. Verifikasi tooltip `Download` tampil saat fokus
19. Fokuskan icon Changelog dengan Tab
20. Verifikasi tooltip `Changelog` tampil saat fokus
### TC-FA-FAAM-442: Kolom Asset Name dan Code tidak punya tooltip hover
21. Verifikasi baris `Dell Latitude` tampil di tabel
22. Arahkan kursor ke nama `Dell Latitude`
23. Verifikasi tidak ada tooltip pada nama baris `Dell Latitude`
24. Arahkan kursor ke Code `DLAT`
25. Verifikasi tidak ada tooltip pada Code baris `Dell Latitude`
### TC-FA-FAAM-443: Popover +N more kolom Brand dan Model/Type
26. Klik chip `+1 more` di sel Model/Type baris `Dell Latitude`
27. Verifikasi popover berjudul `Models` memuat seluruh model sebagai badge penuh A→Z (`3310`, `5420`, `7420`)
28. Klik di luar popover
29. Verifikasi popover tertutup
30. Klik chip `+N more` di sel Brand baris dengan lebih dari 2 Brand (`Multi Brand Item`)
31. Verifikasi popover berjudul `Brands` memuat seluruh Brand A→Z
32. Verifikasi popover scrollable
33. Verifikasi popover tanpa identitas record
34. Klik di luar popover
35. Verifikasi popover tertutup
### TC-FA-FAAM-444: Popover +N more kolom Default Addon dan Default Label
36. Ketik Search `Service Vehicle`, tekan Enter
37. Klik chip `+1 more` di sel Default Addon baris `Service Vehicle`
38. Verifikasi popover `Default Addons` memuat `Maintenance`, `Tracking`, `Maps` dengan urutan enum tetap
39. Klik di luar popover
40. Klik `(←)` pada kotak Search
41. Klik chip `+N more` di sel Default Label baris dengan lebih dari 2 label (Pre-setup #14n)
42. Verifikasi popover `Default Labels` memuat seluruh label berwarna hex masing-masing
43. Verifikasi badge pada popover tampil nama penuh tanpa truncation
44. Verifikasi popover tanpa identitas record
45. Klik di luar popover
### TC-FA-FAAM-445: Popover +N more tertutup oleh klik di luar dan tombol Esc
46. Klik chip `+1 more` di sel Model/Type baris `Dell Latitude`
47. Verifikasi popover `Models` tampil
48. Klik di luar popover
49. Verifikasi popover tertutup
50. Klik chip `+1 more` di sel Model/Type baris `Dell Latitude`
51. Tekan Esc
52. Verifikasi popover tertutup

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Ketik Search `Service Vehicle` (langkah 36) agar baris berada di halaman 1 daftar A-Z yang diawali 30 `Seed Item` (R-16), dan `(←)` pada kotak Search (langkah 40) untuk membersihkannya sebelum langkah berikutnya (S-09).
- Verifikasi baris `Dell Latitude` tampil pada TC-FA-FAAM-442 adalah anchor positif untuk asersi absence tooltip (bagian 8b butir 2); asersi tooltip pada blok sebelumnya membuktikan hover menghasilkan tooltip di tabel yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): klik di luar popover pada TC-FA-FAAM-444 yang menutup popover sebelum popover berikutnya dibuka.
- Penutupan popover lewat klik di luar diverifikasi pada TC-FA-FAAM-443 dan TC-FA-FAAM-445 (klausa "tertutup oleh klik di luar atau Esc" pada Expected c TC-FA-FAAM-443); Esc diverifikasi pada TC-FA-FAAM-445.
- Di atas smell 35 langkah. Spec berjumlah 52 langkah (melewati sekitar 35). Semua blok adalah asersi hover dan popover pada tabel utama yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-FA-FAAM-438 menyebut badge Category `Laptop` tanpa nama baris Asset Name; Pre-setup #12 (`MacBook Pro`) ber-Category internal `Electronics` sehingga baris ber-Category `Laptop` tidak teridentifikasi. TC-FA-FAAM-443 dan TC-FA-FAAM-444 memakai Pre-setup #14m dan #14n tanpa nama baris.
