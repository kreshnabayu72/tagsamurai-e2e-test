---
id: TC-FA-CAT-E2E-005-client-baru-onboard-seed-default-category
title: "Client Baru Onboard: Seed Default Category, Changelog Kosong, dan Edit Seed"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-10
  - TC-FA-CAT-392
  - TC-FA-CAT-616
  - TC-FA-CAT-581
coverage:
  web: automated
---

# Client Baru Onboard: Seed Default Category, Changelog Kosong, dan Edit Seed

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) pada client CatFresh (Pre-setup #25), `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = CatFresh, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client CatMain).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatFresh (Pre-setup #25, plan Enterprise) baru onboard: hanya satu kategori seed `Default Category` (Code `DC`, leaf, Modified By `System`, Last Updated = waktu onboarding). Tidak ada riwayat Changelog (seed tidak dicatat). Waktu onboarding dibaca lewat kemampuan baca yang disediakan tim FE/BE.
- Spec mengubah data Pre-setup (S-06, pengecualian): TC-FA-CAT-581 mengubah nama `Default Category` menjadi `Renamed Seed` karena seed client baru tidak dapat dimiliki spec. Efek: Last Updated, Modified By, dan satu baris Changelog. Pemulihan CatFresh ke keadaan baru onboard (seed `Default Category`, Changelog kosong) dijamin fixture BE yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`. Suite berjalan serial.
- Kemampuan teknis: membuka Detail User aktor > Tab System Log dan Activity Log, mengatur Filter Date mulai dari waktu onboarding client, serta mencari baris per Name (TC-FA-CAT-10 butir d); mekanisme pencarian dan filter tidak diuraikan TC dan disediakan tim FE/BE tanpa endpoint karangan.
- Waktu: jam server dan jam browser sinkron (dasar asersi Last Updated sama dengan waktu Edit, toleransi satu menit, S-12).
- Format Modified By diasersi `[First Name] [Last Initial]`; nama lengkap aktor Total Control client CatFresh dibaca dari fixture (nama tidak tertulis di Pre-setup TC; disediakan tim FE).
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-10: Client baru onboard menampilkan satu baris seed Default Category tanpa CTA kosong

1. Verifikasi tabel memuat tepat 1 baris `Default Category` tampil normal tanpa empty state dan tanpa CTA kosong
2. Verifikasi Code baris `Default Category` `DC` (hasil auto-generate dari Category Name, bukan `—`)
3. Verifikasi Modified By baris `Default Category` `System`
4. Verifikasi Last Updated baris `Default Category` berisi waktu onboarding client (format General Settings)
5. Verifikasi Sidebar Category Tree memuat root `All Categories` dan satu node `Default Category`
6. Verifikasi node `Default Category` berupa leaf yang selectable

### TC-FA-CAT-392: Modal Changelog kosong menampilkan empty state S-07

7. Klik icon Changelog di Table Tools
8. Verifikasi Modal Changelog menampilkan ilustrasi, Title `No changelog yet`, dan Description `Activities and changes will appear here.`

### TC-FA-CAT-616: Modal Changelog kosong (genuine empty): toolbar tetap tampil, Download hanya header, dropdown Filter menampilkan No options available

9. Verifikasi toolbar Modal Changelog menampilkan Search, Filter, dan Download
10. Klik Download > `Download as CSV`
11. Verifikasi tidak ada toast
12. Verifikasi berkas `Changelog-Category.csv` terunduh
13. Verifikasi berkas `Changelog-Category.csv` hanya berisi baris header kolom yang visible, tanpa baris data
14. Klik icon Filter lalu buka dropdown Action
15. Verifikasi dropdown Action menampilkan teks `No options available`
16. Tutup Modal Changelog

### TC-FA-CAT-10 butir d: System Log dan Activity Log tidak memuat baris untuk seed

17. Buka Detail User aktor > Tab System Log, atur Filter Date mulai dari waktu onboarding client (dibaca pada Prerequisites), dan cari baris Name `Default Category`
18. Verifikasi System Log aktor menampilkan empty state `No results found`
19. Buka Activity Log, atur Filter Date mulai dari waktu onboarding client, dan cari baris `Default Category`
20. Verifikasi Activity Log menampilkan empty state `No results found`
21. Buka Fixed Asset > Settings > Categories

### TC-FA-CAT-581: Seed Default Category setelah diedit: Modified By dan Last Updated mengikuti aktor Edit

22. Verifikasi Modified By baris `Default Category` `System`
23. Verifikasi Last Updated baris `Default Category` berisi waktu onboarding client
24. Klik elipsis (⋯) pada baris `Default Category` > `Edit`
25. Ubah Category Name menjadi `Renamed Seed`
26. Klik `[Save]`
27. Catat waktu sesudah `[Save]`
28. Verifikasi Modified By baris `Renamed Seed` berformat `[First Name] [Last Initial]` aktor yang mengedit (bukan `System`)
29. Hover nilai Modified By
30. Verifikasi tooltip menampilkan nama lengkap aktor
31. Verifikasi Last Updated berubah ke waktu Edit (sama dengan waktu yang dicatat pada langkah 27, toleransi satu menit)
32. Verifikasi Code tetap `DC`
33. Klik icon Changelog di Table Tools
34. Verifikasi Modal Changelog memuat tepat satu baris: Action `Edit`, Field `Category Name`, Old Value `Default Category`, New Value `Renamed Seed`, Modified By aktor
35. Tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Urutan (8b butir 11): pada TC-FA-CAT-616 butir c, absence toast diasersi tepat sesudah klik Download (langkah 11) sebelum asersi berkas terunduh; klik Download (langkah 10) menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Urutan (S-10): blok baca (TC-FA-CAT-10, 392, 616) mendahului TC-FA-CAT-581 karena Edit seed menambah baris Changelog; setelah Edit Changelog tidak lagi kosong.
- Langkah penghubung (S-03, R-16): langkah 16 dan 35 (menutup Modal Changelog), langkah 17 dan 19 (membuka surface log dan mencari entri), langkah 21 (kembali ke Categories), langkah 27 (mencatat waktu). Langkah "Buka Fixed Asset > Settings > Categories" pada TC-FA-CAT-10 dan TC-FA-CAT-581 dipenuhi hook `beforeEach` (bagian 4).
- `Verifikasi` langkah 8 memenuhi TC-FA-CAT-392 dan butir a TC-FA-CAT-616 (empty state sama; TC-FA-CAT-616 butir a), serta butir d TC-FA-CAT-10 untuk Changelog.
- Absence log seed (S-05, P-1): butir d TC-FA-CAT-10 diasersi di spec ini untuk tiga surface: Changelog (langkah 8, empty state), System Log aktor (langkah 18), dan Activity Log (langkah 20), memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2). Pencarian dibatasi Filter Date mulai dari waktu onboarding client (langkah 17 dan 19) sehingga baris log lama dari run sebelumnya (mis. rename seed TC-FA-CAT-581) tidak ikut terhitung; fixture BE pemulihan CatFresh menetapkan ulang waktu onboarding pada hook `before`. P-1: asersi ini bergantung pada state berat client baru onboard (seed CatFresh yang dipulihkan fixture BE di hook `before` dan `after`) dan harus dibaca sebelum TC-FA-CAT-581 menambah entri; karena itu tetap di spec asal. TC-FA-CAT-473 di spec absence 167 memuat aksi nyata untuk seed yang sama dengan baseline sendiri.
- Temuan untuk QA:
  - TC-FA-CAT-10 butir d menyebut System Log dan Activity Log tidak memuat baris seed tanpa langkah membuka kedua surface itu; spec menambah langkah penghubung (membuka surface, Filter Date mulai waktu onboarding, dan Search Name `Default Category`) mengikuti pola TC-FA-CAT-473. Karena log permanen dari run sebelumnya dibatasi Filter Date, QA hanya perlu mengonfirmasi bahwa Filter Date tersedia di kedua surface log dan bahwa waktu onboarding diperbarui fixture saat CatFresh dipulihkan.
  - TC-FA-CAT-581 dan TC-FA-CAT-10 memakai seed Default Category CatFresh sebagai target (Pre-setup); pemulihan CatFresh butuh fixture dari tim FE/BE.
  - Email akun Total Control client CatFresh tidak tertulis eksplisit di Pre-setup TC; spec memakai pola Pre-setup #1 dengan `{namaCompany}` CatFresh.
- Ukuran spec 35 langkah, di sekitar ambang 35 (blok baca-log berpola, prinsip 13 bagian 3).
