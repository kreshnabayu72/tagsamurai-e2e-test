---
id: TC-AC-DS-E2E-114-changelog-search-kelas-teks-campuran-dan-date
title: "Search Changelog: Kelas Teks, Campuran Old/New Value, dan Kolom Date Tidak Dapat Dicari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-391
  - TC-AC-DS-392
  - TC-AC-DS-393
coverage:
  web: automated
---

# Search Changelog: Kelas Teks, Campuran Old/New Value, dan Kolom Date Tidak Dapat Dicari

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (total pada modal dapat lebih besar karena entri yang ditulis spec lain; jumlah entri pada TC-AC-DS-391 dan TC-AC-DS-392 diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26`), termasuk Delete `HHR-ARC-300` oleh `Jane S`, Edit Model/Type `HHR-ARC-100` (`H10` menjadi `H100`), Edit `SFR-VEL-4P` Field `Photo — Set as default` (`Photo 1` menjadi `Photo 2`), dan 17 entri oleh `Budi K` (18 oleh `Jane S`). Entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-391: Search kelas teks

1. Klik ikon Changelog
2. Klik ikon Filter pada modal
3. Pada field Date pilih rentang `01/09/26` sampai `03/10/26`
4. Klik `[Apply]` pada Filter Panel modal
5. Ketik Search pada modal `Delete`, tekan Enter
6. Verifikasi tabel menampilkan 1 entri: Delete `HHR-ARC-300`
7. Ganti isi kotak search modal dengan `HHR-ARC-300`, tekan Enter
8. Verifikasi tabel menampilkan 1 entri: Delete `HHR-ARC-300`
9. Ganti isi kotak search modal dengan `default`, tekan Enter
10. Verifikasi tabel menampilkan 1 entri dengan Field `Photo — Set as default`
11. Ganti isi kotak search modal dengan `Budi`, tekan Enter
12. Verifikasi tabel menampilkan 17 entri dalam 2 halaman pada 10 baris per halaman
13. Verifikasi seluruh baris pada halaman 1 bermodified by `Budi K`
14. Pindah ke halaman 2
15. Verifikasi halaman 2 memuat 7 baris, seluruhnya bermodified by `Budi K`

### TC-AC-DS-392: Search kelas campuran tipe

16. Ganti isi kotak search modal dengan `H10`, tekan Enter
17. Verifikasi tabel menampilkan 1 entri Edit Model/Type `HHR-ARC-100` (Old Value `H10`, New Value `H100`)
18. Ganti isi kotak search modal dengan `Photo 1`, tekan Enter
19. Verifikasi tabel menampilkan 1 entri dengan Field `Photo — Set as default`
20. Ganti isi kotak search modal dengan `Photo 2`, tekan Enter
21. Verifikasi tabel menampilkan entri yang sama dengan New Value `Photo 2`

### TC-AC-DS-393: Kolom Date tidak dapat dicari

22. Klik `[Clear Field]`, lalu `[Apply]`
23. Ganti isi kotak search modal dengan `03/10/26`, tekan Enter
24. Verifikasi kata kunci `03/10/26` tidak mencocokkan entri dan tampil "No results found"
25. Ganti isi kotak search modal dengan `14:20`, tekan Enter
26. Verifikasi kata kunci `14:20` tidak mencocokkan entri dan tampil "No results found"
27. Klik `(←)` pada kotak Search modal, lalu klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-14): langkah 2 sampai 4 menerapkan Filter Date seed `01/09/26` sampai `03/10/26` (langkah TC-AC-DS-391 dan TC-AC-DS-392; filter tetap aktif untuk TC-AC-DS-392 sehingga tidak diulang); langkah 14 memindahkan ke halaman 2 agar jumlah baris halaman terakhir teramati; langkah 22 melepas Filter Date sebelum TC-AC-DS-393 (TC itu tanpa filter); langkah 27 menutup Search dan modal; tanpa asersi tambahan.
- Langkah 13 dan 15 mengasersi isi halaman yang teramati sebagai pengamatan atas "seluruhnya Modified By `Budi K`" (S-14, audit trail).
- Asersi absence langkah 24 dan 26 memakai empty state "No results found" sebagai anchor positif hasil Search. Expected b TC-AC-DS-393 ("penyaringan menurut tanggal lewat Filter Panel modal") bersifat informasi dan tidak punya langkah.
- Temuan untuk QA:
  - S-12: jumlah entri (1 dan 17) diasersi di bawah Filter Date seed `01/09/26` sampai `03/10/26` sesuai TC-AC-DS-391 dan TC-AC-DS-392, bukan total modal; asersi bergantung pada nama literal Pre-setup #29, #30, dan #33 (pengecualian S-12 A-11, `suite.md`).
  - TC-AC-DS-391 menyebut 17 entri `Budi K` tanpa menyebut tampilan jumlahnya; spec mengamatinya lewat jumlah halaman dan baris halaman terakhir.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
