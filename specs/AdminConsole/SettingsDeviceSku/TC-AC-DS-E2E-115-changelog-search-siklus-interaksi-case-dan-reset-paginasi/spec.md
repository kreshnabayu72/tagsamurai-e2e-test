---
id: TC-AC-DS-E2E-115-changelog-search-siklus-interaksi-case-dan-reset-paginasi
title: "Search Changelog: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, Substring, dan Reset Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-394
  - TC-AC-DS-395
  - TC-AC-DS-396
coverage:
  web: automated
---

# Search Changelog: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, Substring, dan Reset Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (total pada modal dapat lebih besar karena entri yang ditulis spec lain; N dibaca dari info pagination pada langkah 2, tidak diturunkan dari seeding), termasuk entri Action `Create`, `Delete`, dan `Edit` serta Field `SKU`, `Model/Type`, dan `Photo — Set as default`. Entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-394: Siklus interaksi Search modal

1. Klik ikon Changelog
2. Catat jumlah entri total pada info pagination modal sebagai N
3. Klik ikon Search pada modal
4. Verifikasi kotak pencarian melebar
5. Verifikasi kursor fokus otomatis pada kotak pencarian
6. Verifikasi placeholder "Search action, SKU..." tampil
7. Ketik `Edit` tanpa menekan Enter
8. Verifikasi ikon `(✕)` muncul di dalam input
9. Verifikasi tabel belum tersaring: jumlah entri total pada info pagination masih sama dengan N
10. Tekan Enter
11. Verifikasi tabel menampilkan entri Action `Edit`
12. Klik ikon `(✕)` di dalam input
13. Verifikasi input kosong
14. Verifikasi tabel tidak reset (tetap menampilkan entri Action `Edit`)
15. Tekan Enter pada input kosong
16. Verifikasi tabel di-reset ke N entri (jumlah awal yang dicatat pada langkah 2)
17. Ketik Search `Edit`, tekan Enter
18. Klik ikon panah `(←)`
19. Verifikasi kotak pencarian menutup menjadi ikon Search
20. Verifikasi tabel langsung di-reset ke N entri (jumlah awal yang dicatat pada langkah 2)

### TC-AC-DS-395: Tidak membedakan huruf besar-kecil dan substring

21. Ketik Search `sKu`, tekan Enter
22. Verifikasi tabel menampilkan entri dengan Field `SKU` (Create, Delete, dan Edit kode SKU)
23. Ganti isi kotak search modal dengan `handheld reader (hhr-arc`, tekan Enter
24. Verifikasi tabel menampilkan entri dengan SKU `UHF Handheld Reader (HHR-ARC-...)`

### TC-AC-DS-396: Search mereset paginasi ke halaman 1

25. Klik ikon panah `(←)`
26. Pindah ke halaman 3 modal
27. Ketik Search `Edit`, tekan Enter
28. Verifikasi hasil Search tampil pada halaman 1 modal
29. Klik `(←)` pada kotak Search modal, lalu klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 2 mencatat N (TC-AC-DS-394 langkah 2); langkah 25 menutup Search dan mereset tabel sebelum TC-AC-DS-396; langkah 29 menutup Search dan modal; tanpa asersi tambahan.
- Langkah 9 membuktikan tabel belum tersaring lewat jumlah total yang masih N, dan langkah 16 dan 20 mengasersi jumlah total sama dengan N yang dicatat pada langkah 2 (S-12, baseline relatif).
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29, #30, dan #33 (pengecualian S-12 A-11, `suite.md`); jumlah entri memakai N dari info pagination.
  - TC-AC-DS-395 menyebut `UHF Handheld Reader (HHR-ARC-...)` tanpa merinci entri; spec mengikuti redaksi TC.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
