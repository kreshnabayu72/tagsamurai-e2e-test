---
id: TC-FA-FAAC-E2E-210-edit-end-of-life-treatment-tanpa-apply-changes-ganti-method-dan-asset-class-belum-dipakai
title: "Edit Asset Class Belum Dipakai Aset: Ganti Method Mengosongkan End-of-Life Treatment dan Edit End-of-Life Treatment Tersimpan Langsung Tanpa Apply Changes"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-723
  - TC-FA-FAAC-725
sourceRules: ["F-FAAC-02.k20", "F-FAAC-02.k11", "FAAC-LOGIC-07h", "FAAC-LOGIC-02h", "FLD-33", "FI-01", "ST-08", "L-02", "E-FAAC-120"]
smoke: []
dependsOn: []
trace:
  "F-FAAC-02.k20": [6, 7, 16, 17]
  "F-FAAC-02.k11": [10, 11, 33, 34]
  "FAAC-LOGIC-07h": [10, 11, 33, 34]
  "FAAC-LOGIC-02h": [7, 17, 25, 38]
  "FLD-33": [7, 17, 38]
  "FI-01": [6, 7, 16, 17]
  "ST-08": [7, 17]
  "L-02": [22, 23, 24, 25]
  "E-FAAC-120": [16, 17, 19]
coverage:
  web: automated
---

# Edit Asset Class Belum Dipakai Aset: Ganti Method Mengosongkan End-of-Life Treatment dan Edit End-of-Life Treatment Tersimpan Langsung Tanpa Apply Changes

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke nilai awal oleh fixture BE di hook `before` dan `after`): Asset Class `B-EOLSWAP` (belum dipakai aset; Method `Declining Balance`, Useful Life 48, Declining Rate 40, End-of-Life Treatment `Keep depreciating`, Tax Depreciation Class `Bukan bangunan – Kelompok 1`, Tax Method `Declining Balance`); Asset Class `B-EOLFREE` (belum dipakai aset; Method `Declining Balance`, Useful Life 48, Declining Rate 50, End-of-Life Treatment `Switch to straight-line`, Tax Depreciation Class `Bukan bangunan – Kelompok 1`, Tax Method `Declining Balance`). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data Dinamis: tidak ada. Spec mengubah `B-EOLSWAP` (Method menjadi `Straight Line`) dan `B-EOLFREE` (End-of-Life Treatment menjadi `Charge in final period`); keduanya dipulihkan fixture BE.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog dibaca tepat sebelum aksi pemicu (audit trail permanen, total tidak diturunkan dari seeding, S-12); fixture BE untuk pemulihan seed.
- State global: entri Changelog yang tercatat adalah audit trail permanen dan tidak dipulihkan.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-723: Edit Method dari Declining Balance ke Straight Line mengosongkan Declining Rate dan End-of-Life Treatment

1. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
2. Ketik Search `B-EOLSWAP`, tekan Enter
3. Klik link Class Code `B-EOLSWAP` di tabel
4. Klik tab `Depreciation`
5. Ganti Method menjadi `Straight Line`
6. Verifikasi field Declining Rate tidak tampil
7. Verifikasi field End-of-Life Treatment tidak tampil
8. Klik `Save`
9. Verifikasi halaman kembali ke tabel
10. Verifikasi toast sukses `Success, asset class has been updated.`
11. Verifikasi dialog `Apply Changes` tidak tampil
12. Ganti isi kotak search dengan `B-EOLSWAP`, tekan Enter
13. Klik link Class Code `B-EOLSWAP` di tabel
14. Klik tab `Depreciation`
15. Ganti Method menjadi `Declining Balance`
16. Verifikasi Declining Rate kosong
17. Verifikasi End-of-Life Treatment bernilai `Switch to straight-line` (bukan `Keep depreciating`)
18. Klik breadcrumb `Asset Class`
19. Verifikasi dialog `Unsaved Changes` tampil karena Method diubah (form tidak disimpan)
20. Klik `[Leave]`
21. Klik ikon Changelog di toolbar tabel (modal `Changelog: Asset Class`)
22. Verifikasi jumlah entri Changelog bertambah tepat 3 dari Nc
23. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLSWAP`, Field `Method`, Old Value `Declining Balance`, New Value `Straight Line`
24. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLSWAP`, Field `Declining Rate`, Old Value `40`, New Value `—`
25. Verifikasi baris Changelog: Action `Edit`, Class Code `B-EOLSWAP`, Field `End-of-Life Treatment`, Old Value `Keep depreciating`, New Value `—`
26. Tutup modal Changelog

### TC-FA-FAAC-725: Edit End-of-Life Treatment pada Asset Class yang belum dipakai aset tersimpan langsung tanpa Apply Changes

27. Ganti isi kotak search dengan `B-EOLFREE`, tekan Enter
28. Klik link Class Code `B-EOLFREE` di tabel
29. Klik tab `Depreciation`
30. Ubah End-of-Life Treatment menjadi `Charge in final period`
31. Klik `Save`
32. Verifikasi halaman kembali ke tabel
33. Verifikasi toast sukses `Success, asset class has been updated.`
34. Verifikasi dialog `Apply Changes` tidak tampil
35. Ganti isi kotak search dengan `B-EOLFREE`, tekan Enter
36. Klik link Class Code `B-EOLFREE` di tabel
37. Klik tab `Depreciation`
38. Verifikasi End-of-Life Treatment `Charge in final period`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-723, TC-FA-FAAC-725). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (baseline Changelog, S-12), langkah 2 (Search untuk menemukan baris target, R-16 dan bagian 8b butir 13), langkah 12, 27, dan 35 (Search ulang sesuai langkah TC "cari di kotak Search tabel"; "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah kembali ke tabel), dan langkah 26 (menutup modal Changelog). Langkah 21 membuka Changelog sebagai langkah observasi TC-723.
- Urutan asersi pada langkah 9 sampai 11 dan 32 sampai 34 mengikuti urutan state (bagian 8b butir 5): kembali ke tabel dan toast sukses (anchor positif) mendahului asersi absence dialog `Apply Changes`.
- Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Menutup form dirty (S-08): langkah 18 sampai 20 memakai breadcrumb, verifikasi dialog `Unsaved Changes`, lalu `[Leave]` (Expected TC-723 butir c).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): `B-EOLSWAP` dan `B-EOLFREE` adalah seed bertanda `B-*` per TC yang dipakai apa adanya dan dipulihkan fixture BE.
- Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah; kedua blok TC satu topik (Edit Asset Class belum dipakai aset tanpa Apply Changes), tiap blok memakai seed sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; blok baca-log berpola (langkah 21 sampai 26) tidak dihitung menurut bagian 3 smell.
- Temuan untuk QA: (a) TC-723 butir c tidak menyebut Declining Rate dan End-of-Life Treatment sesudah Method dikembalikan di form yang belum disimpan selain nilai kosong dan nilai awal; spec mengasersi sesuai Expected. (b) TC-723 butir d menyebut tiga baris Changelog tanpa urutan; spec mengasersi himpunannya dengan selisih jumlah tepat 3.
