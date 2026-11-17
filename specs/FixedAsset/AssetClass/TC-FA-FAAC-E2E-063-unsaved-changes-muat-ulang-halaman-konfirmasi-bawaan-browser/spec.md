---
id: TC-FA-FAAC-E2E-063-unsaved-changes-muat-ulang-halaman-konfirmasi-bawaan-browser
title: "Unsaved Changes: Konfirmasi Bawaan Browser saat Muat Ulang Halaman pada Form Create dan Edit"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-664
  - TC-FA-FAAC-665
  - TC-FA-FAAC-666
sourceRules: ["§4.2f#b2", "T-02"]
smoke: []
dependsOn: []
trace:
  "§4.2f#b2": [8, 18]
  "T-02": 33
anchor: [4, 6, 14, 16, 22, 27, 35]
coverage:
  web: automated
---

# Unsaved Changes: Konfirmasi Bawaan Browser saat Muat Ulang Halaman pada Form Create dan Edit

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: Asset Class `B-ANCHOR` (Active) dengan Class Name `Anchor Heavy Equipment` (hanya diubah di form, tidak pernah disimpan); Asset Class `B-NODIRTY` (Active) disediakan fixture BE sebelum spec.
- Data yang diubah dan disimpan spec: Description `B-NODIRTY` menjadi `Saved once` pada langkah 31 dan 32; Last Updated `B-NODIRTY` ikut berubah. Hook `before` dan `after` memulihkan `B-NODIRTY` ke keadaan seed lewat fixture BE (pemulihan tidak mengandalkan setup berhasil penuh). Class Code `B-RELOAD` belum ada sebelum spec dan tidak pernah disimpan.
- Kemampuan teknis: tombol muat ulang browser (F5); menangani dialog bawaan browser `beforeunload` (memilih tetap di halaman) dan mengamati ketiadaannya (kemampuan disediakan tim FE).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-664: Muat ulang halaman saat form Create sudah diisi

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-RELOAD`
3. Muat ulang halaman (F5)
4. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul sebelum halaman dimuat ulang (perilaku terpicu, bukan teks karena teksnya ditentukan browser)
5. Pilih tetap di halaman
6. Verifikasi form Add Asset Class tetap terbuka dengan Class Code `B-RELOAD`
7. Klik breadcrumb `Asset Class`
8. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
9. Klik `[Leave]`

### TC-FA-FAAC-665: Muat ulang halaman saat form Edit sudah diubah

10. Ketik Search `B-ANCHOR`, tekan Enter
11. Klik link Class Code `B-ANCHOR` di tabel
12. Ubah Class Name menjadi `Anchor Edited` tanpa klik `[Save]`
13. Muat ulang halaman (F5)
14. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul sebelum halaman dimuat ulang (perilaku terpicu, bukan teks)
15. Pilih tetap di halaman
16. Verifikasi Detail `B-ANCHOR` tetap terbuka dengan Class Name `Anchor Edited`
17. Klik breadcrumb `Asset Class`
18. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
19. Klik `[Leave]`

### TC-FA-FAAC-666: Muat ulang halaman tanpa konfirmasi bawaan browser saat form tidak dirty atau sesudah Save sukses

20. Klik tombol `[+ Asset Class]` di toolbar tabel tanpa mengisi field apa pun
21. Muat ulang halaman (F5)
22. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
23. Buka Fixed Asset > Settings > Accounting > tab Asset Class
24. Ketik Search `B-NODIRTY`, tekan Enter
25. Klik link Class Code `B-NODIRTY` di tabel tanpa mengubah field
26. Muat ulang halaman (F5)
27. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
28. Buka Fixed Asset > Settings > Accounting > tab Asset Class
29. Ketik Search `B-NODIRTY`, tekan Enter
30. Klik link Class Code `B-NODIRTY` di tabel
31. Ubah Description menjadi `Saved once`
32. Klik `[Save]`
33. Verifikasi toast sukses `Success, asset class has been updated.`
34. Muat ulang halaman (F5)
35. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-664, 665, 666). Tidak ada TC hanya-BE di spec ini. Pembagian TC lintas spec: TC-FA-FAAC-132 dan 661 (Create), TC-FA-FAAC-659, 660, dan 663 (Edit), serta TC-FA-FAAC-662 dan 697 ada di spec 053, 054, dan 055.
- Pengecualian beralasan atas S-06 dan S-12: Class Code `B-RELOAD`, `B-ANCHOR`, dan `B-NODIRTY` literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama (keputusan yang disetujui user). `B-NODIRTY` adalah target aksi Save pada data Pre-setup (TC-666 langkah 3 mengubah Description); pemulihannya dijamin fixture BE dan efek Last Updated dicatat di Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 7 sampai 9 dan 17 sampai 19 (menutup form dirty lewat dialog `Unsaved Changes`, S-08), langkah 10, 24, dan 29 (Search untuk menemukan baris target), langkah 23 dan 28 (membuka kembali layar sesudah muat ulang; layar landing sesudah F5 tidak diandaikan, S-07).
- Langkah 22, 27, dan 35 mengasersi ketiadaan konfirmasi bawaan browser sebagai halaman dimuat ulang tanpa dialog `beforeunload` yang tertangani; halaman yang termuat ulang menjadi anchor positifnya (8b.2).
- Spec ini 35 langkah.
- Temuan untuk QA:
  - TC-666 langkah 1 tidak menyebut apakah muat ulang pada URL form Create tetap di form atau kembali ke tabel; spec membuka tab Asset Class secara eksplisit sesudah tiap muat ulang (langkah 23 dan 28).
