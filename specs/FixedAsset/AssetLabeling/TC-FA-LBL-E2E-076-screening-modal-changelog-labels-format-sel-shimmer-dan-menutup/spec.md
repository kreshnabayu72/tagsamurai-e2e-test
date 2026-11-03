---
id: TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup
title: "Screening Modal Changelog: Labels, Format Sel, Shimmer, dan Menutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-284
  - TC-FA-LBL-285
  - TC-FA-LBL-286
  - TC-FA-LBL-289
coverage:
  web: automated
---

# Screening Modal Changelog: Labels, Format Sel, Shimmer, dan Menutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons data Changelog Labels (TC-FA-LBL-286) dan melepasnya. Endpoint-nya disediakan tim FE (tidak tertulis di TC, PRD, atau LLD yang dibaca).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend.

## Test Steps

### TC-FA-LBL-284: Screening Modal Changelog: Labels (3 zona)

1. Klik icon Changelog di Table Tools
2. Verifikasi Zona Header memuat Title `Changelog: Labels` dan tombol Close `[✕]`
3. Verifikasi toolbar Zona Header memuat `Search | Filter | Download`
4. Verifikasi toolbar Zona Header tidak memuat `[+ Label]`
5. Verifikasi Zona Body memuat kolom `Date (sortable)`, `Action (sortable)`, `Label Name (sortable)`, `Field (sortable)`, `Old Value (sortable)`, `New Value (sortable)`, `Modified By (sortable)`, dan `Column Visibility (⋯)` (unsortable)
6. Klik icon Filter di toolbar modal
7. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
8. Verifikasi Zona Body menampilkan tepat tujuh baris seed hasil Filter Date dengan default sort Date Newest First
9. Verifikasi baris seed berurutan: `Edit High Priority` (15 Sep 2026 14:25), `Create High Priority` (15 Sep 2026 14:20), `Edit Finance Department` (14 Sep 2026 11:30), `Create Finance Department` (14 Sep 2026 11:15), `Create Audit Ready` (12 Sep 2026 09:40), `Create Executive Asset` (10 Sep 2026 16:30), `Delete Old Tag` (08 Sep 2026 13:00)
10. Verifikasi Zona Footer memuat pagination default 10 per halaman
11. Verifikasi Zona Footer tidak memuat tombol aksi

### TC-FA-LBL-285: Format sel Changelog: Action polos, nilai Create dan Delete, Modified By

12. Verifikasi kolom Action menampilkan teks polos `Create`, `Edit`, `Delete` tanpa badge
13. Verifikasi baris Create menampilkan Field `Label Name`, Old Value `—`, dan New Value berisi nama label
14. Verifikasi baris `Edit High Priority` menampilkan Field `Color`, Old Value `#DC2626`, dan New Value `#EF4444`
15. Verifikasi baris `Delete Old Tag` menampilkan Field `Label Name`, Old Value `Old Tag`, dan New Value `—`
16. Verifikasi kolom Modified By menampilkan `Sarah J`, `David K`, dan `Michael W`
17. Hover Modified By `Sarah J` pada baris `Edit High Priority`
18. Verifikasi tooltip hover menampilkan nama lengkap `Sarah Johnson`
19. Tutup Modal Changelog dengan `[✕]`

### TC-FA-LBL-286: State loading Modal Changelog menampilkan Shimmer

20. Tahan respons data Changelog Labels lewat `Spectra.intercept()`
21. Klik icon Changelog di Table Tools
22. Verifikasi area konten menampilkan Shimmer
23. Verifikasi header dan tombol `[✕]` tetap tampil
24. Lepas tahanan respons
25. Tutup Modal Changelog dengan `[✕]`

### TC-FA-LBL-289: Menutup Modal Changelog hanya lewat ✕ atau Esc

26. Klik icon Changelog di Table Tools
27. Klik area gelap di luar modal
28. Verifikasi klik backdrop tidak menutup modal
29. Verifikasi modal tidak memiliki tombol teks `Close`
30. Klik icon `[✕]`
31. Verifikasi modal tertutup
32. Klik icon Changelog di Table Tools
33. Tekan Esc
34. Verifikasi modal tertutup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal dibuka sekali pada TC-FA-LBL-284 dan tetap terbuka untuk TC-FA-LBL-285 karena precondition identik; Filter Date rentang seed yang di-Apply pada TC-FA-LBL-284 (langkah 6 dan 7) tetap berlaku, sehingga asersi TC-FA-LBL-285 dinilai atas tujuh baris seed hasil Filter Date itu (langkah TC-FA-LBL-285 untuk Filter identik dengan langkah 6 dan 7).
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup Modal Changelog dengan `[✕]` sebelum TC berikutnya dan "Lepas tahanan respons" sesudah asersi Shimmer.
- TC-FA-LBL-287 (empty state) dan TC-FA-LBL-288 (error load) berada di spec lain suite ini.
- Temuan untuk QA:
  - TC-FA-LBL-284 menyebut klik header `Column Visibility (⋯)` membuka overlay dengan CTA `[Setup Column]`, sedangkan TC-FA-LBL-312 menyebut item `Setup Column...`. Spec ini hanya mengasersi kolom `Column Visibility (⋯)` unsortable; perilaku klik headernya dicakup TC-FA-LBL-312 di spec lain.
  - TC-FA-LBL-285 hanya memberi nama lengkap Sarah Johnson (Pre-setup #17); nama lengkap David K dan Michael W tidak tertulis, sehingga tooltip hanya diasersi untuk `Sarah J`.
  - TC-FA-LBL-286 tidak menyatakan keadaan sesudah respons dilepas; spec hanya melepas tahanan lalu menutup modal tanpa asersi tambahan.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
