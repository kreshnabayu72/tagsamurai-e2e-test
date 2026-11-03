---
id: TC-FA-TAG-E2E-050-download-tab-paired-pilihan-nama-berkas-search-filter-kolom-bagian-2
title: "Download Tab Paired: Urutan Mengikuti Sort, Tanpa Hasil, dan Ketersediaan untuk Role Read Only dan Read"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-228
  - TC-FA-TAG-229
  - TC-FA-TAG-234
  - TC-FA-TAG-235
coverage:
  web: automated
---

# Download Tab Paired: Urutan Mengikuti Sort, Tanpa Hasil, dan Ketersediaan untuk Role Read Only dan Read

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Kode | Email (Pre-setup TC) | Env password | Blok |
|---|---|---|---|---|
| Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-TAG-228 dan TC-FA-TAG-229 |
| Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` | TC-FA-TAG-234 |
| Manage asset & TAG (Read) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` | TC-FA-TAG-235 |

- Nama env password usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`. Login Total Control di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk ketiga akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0 (Total Assets berbeda antar grup: 20, 20, 25, 10).
- Data khusus: Search `zzzzqq` tidak cocok dengan data apa pun.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV (nama berkas, header kolom, jumlah baris, urutan baris); seed idempotent lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after`: kembalikan data Pre-setup tab Paired ke keadaan awal bila seeding mengubahnya. Sort kolom Total Assets dikembalikan pada langkah 5 dan Search dikosongkan pada langkah 13. Spec ini tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-228: urutan baris file mengikuti Sort aktif

1. Klik header kolom Total Assets sekali
2. Klik ikon Download pada Table Tools
3. Klik `Download as CSV`
4. Verifikasi urutan baris file mengikuti urutan detail yang aktif
5. Klik header kolom Total Assets dua kali lagi hingga Sort kembali ke urutan awal

### TC-FA-TAG-229: Download tanpa hasil

6. Klik ikon Search
7. Ketik `zzzzqq`, tekan Enter
8. Verifikasi tombol Download tetap aktif
9. Klik ikon Download pada Table Tools
10. Klik `Download as CSV`
11. Verifikasi tidak ada toast
12. Verifikasi file berisi hanya baris header kolom yang tampil
13. Klik `(←)` pada kotak Search

### TC-FA-TAG-234: Read Only

14. Ganti akun: Logout dari akun Total Control, login sebagai Read Only, lalu buka Fixed Asset > TAG tab Paired
15. Klik ikon Download pada Table Tools
16. Klik `Download as CSV`
17. Verifikasi file `Paired-TAGs.csv` terunduh

### TC-FA-TAG-235: Manage asset & TAG (Read)

18. Ganti akun: Logout dari akun Read Only, login sebagai Manage asset & TAG (Read), lalu buka Fixed Asset > TAG tab Paired
19. Klik ikon Download pada Table Tools
20. Klik `Download as CSV`
21. Verifikasi file `Paired-TAGs.csv` terunduh

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Blok role ditulis terpisah karena ganti akun menuntut langkah eksplisit (bagian 3a).
- Langkah penghubung (tanpa awalan `Verifikasi`): 5 (mengembalikan Sort), 13 (mengosongkan Search lewat `(←)`), 14 dan 18 (ganti akun).
- Absence toast (langkah 11) diletakkan sesudah pemicu klik pilihan format dan sebelum Verifikasi berkas (langkah 12); pemicu menjadi anchor positif (bagian 8b butir 11).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-228 Expected ("urutan baris file mengikuti urutan detail yang aktif") tidak menyebut arah urut (ascending atau descending) ataupun urutan Total Assets antar aset di file; Total Assets adalah nilai tingkat grup sedangkan file berisi satu baris per aset. Spec mengasersi apa adanya tanpa menambah arah urut.
  - TC-FA-TAG-229 Expected b ("hanya baris header kolom yang tampil") tidak menyebut kolom yang dipakai; spec memakai kolom yang tampil pada T-TAG-02.
  - TC-FA-TAG-228 dan TC-FA-TAG-229 tidak menyebut cara mengembalikan Sort dan Search; spec menambah langkah penghubung 5 dan 13.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
