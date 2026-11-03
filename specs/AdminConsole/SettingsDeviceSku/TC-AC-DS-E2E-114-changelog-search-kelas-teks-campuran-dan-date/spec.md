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
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri, termasuk Delete `HHR-ARC-300` oleh `Jane S`, Edit Model/Type `HHR-ARC-100` (`H10` menjadi `H100`), Edit `SFR-VEL-4P` Field `Photo — Set as default` (`Photo 1` menjadi `Photo 2`), dan 17 entri oleh `Budi K` (18 oleh `Jane S`). Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-391: Search kelas teks

1. Klik ikon Changelog
2. Ketik Search pada modal `Delete`, tekan Enter
3. Verifikasi tabel menampilkan 1 entri: Delete `HHR-ARC-300`
4. Ganti isi kotak search modal dengan `HHR-ARC-300`, tekan Enter
5. Verifikasi tabel menampilkan 1 entri: Delete `HHR-ARC-300`
6. Ganti isi kotak search modal dengan `default`, tekan Enter
7. Verifikasi tabel menampilkan 1 entri dengan Field `Photo — Set as default`
8. Ganti isi kotak search modal dengan `Budi`, tekan Enter
9. Verifikasi tabel menampilkan 17 entri dalam 2 halaman pada 10 baris per halaman
10. Verifikasi seluruh baris pada halaman 1 bermodified by `Budi K`
11. Pindah ke halaman 2
12. Verifikasi halaman 2 memuat 7 baris, seluruhnya bermodified by `Budi K`

### TC-AC-DS-392: Search kelas campuran tipe

13. Ganti isi kotak search modal dengan `H10`, tekan Enter
14. Verifikasi tabel menampilkan 1 entri Edit Model/Type `HHR-ARC-100` (Old Value `H10`, New Value `H100`)
15. Ganti isi kotak search modal dengan `Photo 1`, tekan Enter
16. Verifikasi tabel menampilkan 1 entri dengan Field `Photo — Set as default`
17. Ganti isi kotak search modal dengan `Photo 2`, tekan Enter
18. Verifikasi tabel menampilkan entri yang sama dengan New Value `Photo 2`

### TC-AC-DS-393: Kolom Date tidak dapat dicari

19. Ganti isi kotak search modal dengan `03/10/26`, tekan Enter
20. Verifikasi kata kunci `03/10/26` tidak mencocokkan entri dan tampil "No results found"
21. Ganti isi kotak search modal dengan `14:20`, tekan Enter
22. Verifikasi kata kunci `14:20` tidak mencocokkan entri dan tampil "No results found"
23. Klik `(←)` pada kotak Search modal, lalu klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-14): langkah 11 memindahkan ke halaman 2 agar jumlah baris halaman terakhir teramati; langkah 23 menutup Search dan modal; tanpa asersi tambahan.
- Langkah 10 dan 12 mengasersi isi halaman yang teramati sebagai pengamatan atas "seluruhnya Modified By `Budi K`" (S-14, audit trail).
- Asersi absence langkah 20 dan 22 memakai empty state "No results found" sebagai anchor positif hasil Search. Expected b TC-AC-DS-393 ("penyaringan menurut tanggal lewat Filter Panel modal") bersifat informasi dan tidak punya langkah.
- Temuan untuk QA:
  - S-12: Pre-setup #33 menetapkan jumlah entri absolut (1, 17, dan 35 entri) sebagai keadaan awal; konvensi menyatakan total audit trail tidak boleh absolut karena tiap spec menambah entri. Spec mengikuti TC dan menggantungkan keadaan awal pada baseline data uji; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29 dan #30; Lampiran A tidak memuat butir modul ini.
  - TC-AC-DS-391 menyebut 17 entri `Budi K` tanpa menyebut tampilan jumlahnya; spec mengamatinya lewat jumlah halaman dan baris halaman terakhir.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
