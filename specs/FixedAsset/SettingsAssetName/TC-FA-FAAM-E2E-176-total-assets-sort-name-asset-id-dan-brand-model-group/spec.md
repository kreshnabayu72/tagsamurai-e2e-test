---
id: TC-FA-FAAM-E2E-176-total-assets-sort-name-asset-id-dan-brand-model-group
title: "Tab Total Assets Sort: Name, Asset ID, Brand, Model/Type, dan Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-517
  - TC-FA-FAAM-518
  - TC-FA-FAAM-519
coverage:
  web: automated
---

# Tab Total Assets Sort: Name, Asset ID, Brand, Model/Type, dan Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset `Dell Latitude - 1` sampai `Dell Latitude - 42`, Asset ID `AST-0001`..`AST-0042`, Group `Head Office`, `Finance`, `Warehouse`, Status `Active`, `Borrowed`, `Damaged`, `Missing`, `Permanently Missing`, `Draft`; Pre-setup #26).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Kolom yang diuji pada TC-FA-FAAM-519 (langkah 14 sampai 19):

| Kolom |
|---|
| Brand |
| Model/Type |
| Group |

- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-517: Sort kelas Name (increment numerik natural)

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik header Name 1 kali
3. Verifikasi klik 1: urutan `Dell Latitude - 1`, `Dell Latitude - 2`, `Dell Latitude - 10` (bukan urutan teks)
4. Klik header Name 1 kali lagi
5. Verifikasi klik 2: urutan kebalikannya
6. Klik header Name 1 kali lagi
7. Verifikasi klik 3: kembali ke default Last Updated Newest First

### TC-FA-FAAM-518: Sort kelas Asset ID

8. Klik header Asset ID 1 kali
9. Verifikasi klik 1: A-Z
10. Klik header Asset ID 1 kali lagi
11. Verifikasi klik 2: Z-A
12. Klik header Asset ID 1 kali lagi
13. Verifikasi klik 3: kembali ke default Last Updated Newest First

### TC-FA-FAAM-519: Sort kelas Brand, Model/Type, Group

Untuk setiap baris tabel "Kolom yang diuji" pada Prerequisites (langkah 14 sampai 19):

14. Klik header kolom 1 kali
15. Verifikasi klik 1: A-Z
16. Klik header kolom 1 kali lagi
17. Verifikasi klik 2: Z-A
18. Klik header kolom 1 kali lagi
19. Verifikasi klik 3: kembali ke default Last Updated Newest First

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 14 sampai 19 diulang untuk tiga kolom (ekspansi 18 langkah; total ekspansi spec 31 langkah); parameter tiap iterasi ada di tabel "Kolom yang diuji" (bagian 8b butir 7).
- Temuan untuk QA:
  - TC-FA-FAAM-519: `Dell Latitude` hanya memiliki Brand `Dell` dan model `3310`/`5420` pada aset yang tampil (TC-FA-FAAM-512), sehingga urutan A-Z dan Z-A kolom Brand tidak dapat dibedakan dengan satu nilai distinct (S-11/S-14); kolom Group (tiga nilai) dan Model/Type (dua nilai) memadai.
  - TC-FA-FAAM-517 Expected a menyebut `Dell Latitude - 10` tanpa menyebut posisinya; spec mengasersi urutan numerik natural.
