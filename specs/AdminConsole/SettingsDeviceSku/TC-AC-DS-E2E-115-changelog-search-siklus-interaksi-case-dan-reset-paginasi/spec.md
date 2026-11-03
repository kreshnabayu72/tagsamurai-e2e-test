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
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): 35 entri (4 halaman pada 10 baris per halaman), termasuk entri Action `Create`, `Delete`, dan `Edit` serta Field `SKU`, `Model/Type`, dan `Photo — Set as default`. Keadaan awal 35 entri dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-394: Siklus interaksi Search modal

1. Klik ikon Changelog
2. Klik ikon Search pada modal
3. Verifikasi kotak pencarian melebar
4. Verifikasi kursor fokus otomatis pada kotak pencarian
5. Verifikasi placeholder "Search action, SKU..." tampil
6. Ketik `Edit` tanpa menekan Enter
7. Verifikasi ikon `(✕)` muncul di dalam input
8. Verifikasi tabel belum tersaring: entri Delete `HHR-ARC-300` masih tampil
9. Tekan Enter
10. Verifikasi tabel menampilkan entri Action `Edit`
11. Klik ikon `(✕)` di dalam input
12. Verifikasi input kosong
13. Verifikasi tabel tidak reset (tetap menampilkan entri Action `Edit`)
14. Tekan Enter pada input kosong
15. Verifikasi tabel di-reset ke 35 entri (4 halaman pada 10 baris per halaman)
16. Ketik Search `Edit`, tekan Enter
17. Klik ikon panah `(←)`
18. Verifikasi kotak pencarian menutup menjadi ikon Search
19. Verifikasi tabel langsung di-reset ke 35 entri (4 halaman pada 10 baris per halaman)

### TC-AC-DS-395: Tidak membedakan huruf besar-kecil dan substring

20. Ketik Search `sKu`, tekan Enter
21. Verifikasi tabel menampilkan entri dengan Field `SKU` (Create, Delete, dan Edit kode SKU)
22. Ganti isi kotak search modal dengan `handheld reader (hhr-arc`, tekan Enter
23. Verifikasi tabel menampilkan entri dengan SKU `UHF Handheld Reader (HHR-ARC-...)`

### TC-AC-DS-396: Search mereset paginasi ke halaman 1

24. Klik ikon panah `(←)`
25. Pindah ke halaman 3 modal
26. Ketik Search `Edit`, tekan Enter
27. Verifikasi hasil Search tampil pada halaman 1 modal
28. Klik `(←)` pada kotak Search modal, lalu klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 24 menutup Search dan mereset tabel sebelum TC-AC-DS-396; langkah 28 menutup Search dan modal; tanpa asersi tambahan.
- Langkah 15 dan 19 mengasersi total 35 entri dengan angka dari Pre-setup #33 (lihat Temuan untuk QA).
- Temuan untuk QA:
  - S-12: Pre-setup #33 menetapkan total 35 entri (4 halaman) sebagai angka absolut; konvensi menyatakan total audit trail tidak boleh absolut karena tiap spec menambah entri. Spec mengikuti TC dan menggantungkan keadaan awal pada baseline data uji; keputusan pengecualian masih terbuka. Asersi juga bergantung pada nama literal Pre-setup #29 dan #30; Lampiran A tidak memuat butir modul ini.
  - TC-AC-DS-394 Expected d menyebut "me-reset tabel ke 35 entri" dan TC-AC-DS-395 menyebut `UHF Handheld Reader (HHR-ARC-...)` tanpa merinci entri; spec mengikuti redaksi TC.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
