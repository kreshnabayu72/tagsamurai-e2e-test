---
id: TC-FA-FAAC-E2E-144-badge-category-tab-asset-names-dan-truncate
title: "Tab Asset Names: Badge Label dengan Chip +N more dan Badge Category dengan Pemotongan Nama Panjang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-684
  - TC-FA-FAAC-692
  - TC-FA-FAAC-693
coverage:
  web: automated
---

# Tab Asset Names: Badge Label dengan Chip +N more dan Badge Category dengan Pemotongan Nama Panjang

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (hanya dibaca): Asset Class Active `B-LABELS` memiliki Asset Name 'Label Rich Unit' (Machinery > Heavy Equipment; 0 aset aktif; Label Heavy, Insured, Rented, Fleet); Asset Class Active `B-TRUNC` memiliki Asset Name 'Climate Probe' (Category 'Sensors > Environmental Monitoring'; leaf 'Environmental Monitoring' 24 karakter; 0 aset aktif) dan 'Distribution Meter' (Category 'Region Jawa > Jakarta Selatan Distribution Center'; leaf 'Jakarta Selatan Distribution Center' 35 karakter; 0 aset aktif).
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-LABELS`, tekan Enter
2. Klik link Class Code `B-LABELS` di tabel
3. Klik tab `Asset Names`

### TC-FA-FAAC-684: Kolom Label menampilkan dua Badge dan chip +N more yang membuka popover

4. Verifikasi kolom Label baris `Label Rich Unit` menampilkan dua Badge `Heavy` dan `Insured`
5. Verifikasi kolom Label baris `Label Rich Unit` menampilkan satu chip `+2 more`
6. Arahkan kursor ke chip `+2 more` tanpa klik
7. Verifikasi hover pada chip tidak membuka popover (pola klik, bukan hover)
8. Klik chip `+2 more`
9. Verifikasi popover berisi daftar lengkap Label `Heavy`, `Insured`, `Rented`, dan `Fleet`
10. Klik di luar popover
11. Verifikasi popover tertutup

12. Klik breadcrumb `Asset Class`
13. Ganti isi kotak search dengan `B-TRUNC`, tekan Enter

### TC-FA-FAAC-692: Badge Category dengan nama 24 karakter tampil penuh

14. Klik link Class Code `B-TRUNC` di tabel
15. Klik tab `Asset Names`
16. Verifikasi badge Category baris `Climate Probe` berisi leaf `Environmental Monitoring` ditulis penuh (24 karakter, tidak melewati batas 25 karakter)
17. Verifikasi badge Category baris `Climate Probe` tanpa `..`
18. Verifikasi lebar kolom Category mengikuti isi badge (variable-width)

### TC-FA-FAAC-693: Badge Category lebih dari 25 karakter terpotong, hover menampilkan hierarki lengkap

19. Verifikasi badge Category baris `Distribution Meter` tampil `Jakarta Sela..ution Center` (12 huruf pertama, `..`, 12 huruf terakhir), bukan nama penuh
20. Arahkan kursor ke badge Category baris `Distribution Meter`
21. Verifikasi tooltip menampilkan hierarki lengkap `Region Jawa > Jakarta Selatan Distribution Center`

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}` dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `B-TRUNC` dibuka sekali untuk TC-692 dan TC-693 karena kedua Asset Name berada di Asset Class yang sama; langkah TC 'Klik link Class Code B-TRUNC' pada TC-693 terpenuhi oleh Detail yang sudah terbuka (bagian 3, satu pembukaan).
3. Anchor absence: asersi 'tidak membuka popover' (TC-684, hover) dan 'popover tertutup' didahului `Verifikasi` chip `+2 more` tampil dan `Verifikasi` popover sempat tampil (bagian 8b butir 2 dan 5).
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 12, 13, termasuk Search untuk menemukan baris target (R-16).
