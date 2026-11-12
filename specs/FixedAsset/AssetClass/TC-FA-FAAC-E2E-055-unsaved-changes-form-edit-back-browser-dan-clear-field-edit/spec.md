---
id: TC-FA-FAAC-E2E-055-unsaved-changes-form-edit-back-browser-dan-clear-field-edit
title: "Form Edit Asset Class: Unsaved Changes dengan Tombol Back Browser dan Clear Field pada Mode Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-662
  - TC-FA-FAAC-697
coverage:
  web: automated
---

# Form Edit Asset Class: Unsaved Changes dengan Tombol Back Browser dan Clear Field pada Mode Edit

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (diubah hanya di form, tidak pernah disimpan): Asset Class `B-ANCHOR` (Active) belum pernah diposting sehingga Class Code tidak terkunci, dengan Class Name `Anchor Heavy Equipment`, Description `Asset class fixture group B`, Method Straight Line, dan Useful Life 120, disediakan fixture BE sebelum spec; Last Updated `B-ANCHOR` tidak berubah.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: tombol Back browser.
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-ANCHOR`, tekan Enter

### TC-FA-FAAC-662: Tombol Back browser pada Edit yang sudah diubah: Cancel dan Leave

2. Klik link Class Code `B-ANCHOR` di tabel
3. Ubah Class Name menjadi `Anchor Edited` tanpa klik `[Save]`
4. Klik tombol Back browser
5. Verifikasi dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
6. Klik `[Cancel]`
7. Verifikasi dialog menutup
8. Verifikasi tetap di Detail `B-ANCHOR` dengan Class Name `Anchor Edited`
9. Klik tombol Back browser lagi
10. Klik `[Leave]`
11. Verifikasi kembali ke tab Asset Class
12. Verifikasi baris `B-ANCHOR` tetap bernama `Anchor Heavy Equipment`

### TC-FA-FAAC-697: Clear Field pada Detail mode Edit mengosongkan field tanpa mengembalikan ke nilai tersimpan

13. Klik link Class Code `B-ANCHOR` di tabel
14. Pada tab General verifikasi Class Code `B-ANCHOR` terisi
15. Verifikasi Class Name `Anchor Heavy Equipment` terisi
16. Verifikasi Description `Asset class fixture group B` terisi
17. Klik `[Clear Field]` di footer
18. Verifikasi halaman `Edit Asset Class` tetap terbuka
19. Verifikasi tidak ada dialog apa pun, termasuk Unsaved Changes
20. Verifikasi Class Code kosong (dikosongkan, bukan dikembalikan ke nilai tersimpan)
21. Verifikasi Class Name kosong (dikosongkan, bukan dikembalikan ke nilai tersimpan)
22. Verifikasi Description kosong (dikosongkan, bukan dikembalikan ke nilai tersimpan)
23. Klik tab `Depreciation`
24. Verifikasi Method belum terpilih (placeholder `Select method`)
25. Klik breadcrumb `Asset Class`
26. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
27. Klik `[Leave]`
28. Verifikasi baris `B-ANCHOR` di tabel tetap berisi Class Code `B-ANCHOR` dan Class Name `Anchor Heavy Equipment`, tanpa data tersimpan

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-662, 697). TC-FA-FAAC-665 (muat ulang pada form Edit) ada di spec 063. Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Asset Class `B-ANCHOR` dan nilai literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; `B-ANCHOR` hanya dibuka di form dan tidak pernah disimpan, sehingga Last Updated tidak berubah (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1 (Search untuk menemukan baris target; kotak Search mempertahankan nilainya sesudah Back dan Leave sehingga langkah 13 tidak mengulang Search, 8b.9).
- Langkah 18 menjadi anchor positif untuk asersi absence dialog pada langkah 19 (8b.2). Form ditutup deterministik lewat dialog `Unsaved Changes` pada kedua TC (S-08); langkah 26 adalah `Verifikasi` dialog yang diwajibkan S-08.
- Temuan untuk QA:
  - TC-697 Expected e ("tidak ada data tersimpan") disalin satu `Verifikasi` dengan nilai baris karena tidak teramati terpisah.
