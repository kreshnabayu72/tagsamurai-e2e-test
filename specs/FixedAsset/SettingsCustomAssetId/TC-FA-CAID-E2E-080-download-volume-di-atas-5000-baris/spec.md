---
id: TC-FA-CAID-E2E-080-download-volume-di-atas-5000-baris
title: "Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background dan Cakupan Seluruh Halaman"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-156
  - TC-FA-CAID-223
  - TC-FA-CAID-227
coverage:
  web: automated
---

# Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background dan Cakupan Seluruh Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Company Export (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Export, Pre-setup No 17). Email akun disediakan tim FE/BE (Pre-setup No 17 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_EXPORT_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID).
- Akun aktor kedua: Total Control Company Log Volume (Pre-setup No 1, pola yang sama; Company Log Volume, Pre-setup No 18), email disediakan tim FE/BE (Pre-setup No 18 hanya menyebut env var), kredensial `Spectra.env.FA_LOGVOL_TC_PASSWORD`. Ganti akun lewat langkah eksplisit (11, 12, 13); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_EXPORT_TC_PASSWORD`, `FA_LOGVOL_TC_PASSWORD`, dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; ketiga nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 17 Company Export dengan 5.001 Asset Name berkode (seed API); No 18 Company Log Volume dengan 5.001 entri Changelog Custom Asset ID (seed API) dengan campuran Action `Create` dan `Edit` (lebih dari 10 entri `Edit` agar Filter `Action = Edit` melebihi satu halaman); No 27 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam). Data Dinamis: tidak ada. Fixture modul Custom Asset ID untuk nilai ini belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Seeding (volume, kelas e): hook `before` men-seed kedua Company lewat API sesi aktor masing-masing; cara membuat 5.001 Asset Name berkode dan 5.001 entri Changelog tidak disebut TC, PRD, atau LLD: disediakan tim BE/FE. Kedua Company dikembalikan tim FE/BE ke keadaan awal sebelum tiap run; spec hanya membaca.
- Kemampuan teknis: menangkap berkas unduhan browser ke direktori bersih; membaca jumlah baris data dan nilai kolom Action berkas CSV besar (5.001 baris); mengamati loading screen selama berkas disiapkan; membaca jumlah entri Changelog `Edit` Company Log Volume sebagai pembanding jumlah baris berkas (disediakan tim FE/BE; TC tidak menyebut caranya).
- Precondition TC-FA-CAID-156: login sebagai Total Control; Company Export dengan 5.001 Asset Name berkode; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID. Precondition TC-FA-CAID-223 dan 227: login sebagai Total Control; Company Log Volume dengan 5.001 entri Changelog; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Suite serial (`parallel: false`) karena kedua Company volume dipakai bersama spec volume lain.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: berkas unduhan dihapus di hook `after`.

## Test Steps

### TC-FA-CAID-156: Download di atas 5.000 baris memakai loading screen tanpa job background

1. Klik tautan `[View Code List]`
2. Klik tab `Asset Name Codes`
3. Klik Download, lalu klik `Download as CSV`
4. Verifikasi loading screen tampil sampai berkas siap
5. Verifikasi tidak ada toast informasional
6. Verifikasi tidak ada notifikasi in-app
7. Verifikasi berkas `Code-List-Asset-Name-Codes.csv` langsung terunduh
8. Verifikasi berkas `Code-List-Asset-Name-Codes.csv` berisi 5.001 baris data
9. Verifikasi tidak ada halaman Export History
10. Klik `[✕]` pada Modal View Code List

### TC-FA-CAID-223: Download mengikuti Search dan Filter aktif dan mencakup seluruh halaman

11. Ganti akun: Logout dari akun Total Control Company Export
12. Login sebagai Total Control Company Log Volume (`totalControl_automated_{namaCompany}@qwertysystem.net`)
13. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
14. Klik tombol `[Changelog]` pada header kartu
15. Catat jumlah entri Changelog ber-Action `Edit` sebagai baseline
16. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
17. Klik Download, lalu klik `Download as CSV`
18. Verifikasi berkas memuat seluruh baris yang cocok dengan Filter `Action = Edit` (lebih dari 10 baris, bukan hanya baris pada halaman yang tampil)
19. Verifikasi jumlah baris data berkas sama dengan baseline jumlah entri Changelog ber-Action `Edit` pada langkah 15

### TC-FA-CAID-227: Download Changelog di atas 5.000 baris memakai loading screen tanpa job background

20. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik Download, lalu klik `Download as CSV`
22. Verifikasi loading screen tampil sampai berkas siap
23. Verifikasi tidak ada toast informasional
24. Verifikasi tidak ada notifikasi in-app
25. Verifikasi `Changelog-Custom-Asset-ID.csv` langsung terunduh
26. Verifikasi `Changelog-Custom-Asset-ID.csv` berisi 5.001 baris data
27. Verifikasi tidak ada Export History

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-CAID-156, 223, 227. Alasan: TC-FA-CAID-156 memakai Company Export (akun pertama, login di hook `before`); TC-FA-CAID-223 dan 227 memakai Company Log Volume sehingga ganti akun terjadi satu kali; TC-FA-CAID-223 (Filter aktif) sebelum TC-FA-CAID-227 (tanpa Filter) agar Filter dibersihkan satu kali. Modal Changelog dibuka sekali di langkah 14.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 10 (menutup Modal View Code List), langkah 11, 12, 13 (ganti akun dan membuka halaman; akun pertama login di hook `before`, S-07), langkah 15 (mencatat baseline jumlah entri `Edit`; S-12 dan bagian 8b butir 10), dan langkah 20 (membersihkan Filter sebelum Download tanpa saringan).
- Pada TC-FA-CAID-156 dan 227 `Verifikasi` loading screen, tidak ada toast, dan tidak ada notifikasi in-app diletakkan segera setelah pemicu Download dan sebelum `Verifikasi` berkas (bagian 8b butir 5 dan 11); berkas yang terunduh menjadi anchor positif bagi `Verifikasi` tidak ada halaman Export History.
- Kelas harness: volume data (kelas e, lebih dari 5.000 baris). Jumlah 5.001 baris data adalah jumlah seed milik Company Export dan Company Log Volume (data milik spec yang dikembalikan tim FE/BE ke keadaan awal sebelum tiap run), bukan total audit trail yang tumbuh (S-12). Jumlah baris TC-FA-CAID-223 dibandingkan dengan baseline jumlah entri `Edit` yang dicatat pada langkah 15 (dibaca tim FE/BE). Klausa "tidak memuat baris `Create`" tidak ada lagi di TC-FA-CAID-223 sehingga tidak diasersi di spec ini.
- Klausa gabungan pada Expected TC-FA-CAID-156 dan 227 ("langsung terunduh berisi 5.001 baris data") dipecah satu `Verifikasi` per klausa (langkah 7 dan 8, 25 dan 26; S-01).
- Pembagian TC lintas spec: isi berkas CSV dan XLSX Changelog (TC-FA-CAID-221, 222) ada di spec 059; Download Code List (TC-FA-CAID-148 sampai 154) ada di spec 058; Pagination 5.001 entri Changelog (TC-FA-CAID-214 sampai 219) ada di spec 078.
- Temuan untuk QA: (1) Kolom ACC TC-FA-CAID-156, 223, dan 227 memuat akun #1 bersama Company Export (Pre-setup No 17) dan Company Log Volume (Pre-setup No 18) sehingga akun aktornya ambigu antara Company Alpha dan Company volume; spec memakai Total Control di masing-masing Company (Pre-setup No 17 dan 18) dan ganti akun eksplisit. (2) TC-FA-CAID-156 dan 227 Expected "langsung terunduh" tidak menyebut batas waktu loading screen; spec mengasersi loading screen tampil sampai berkas siap lalu berkas terunduh. (3) TC-FA-CAID-223 tidak menyebut cara membaca baseline jumlah entri `Edit`; spec mengasersi lebih dari 10 baris dan sama dengan baseline yang dibaca tim FE/BE.
