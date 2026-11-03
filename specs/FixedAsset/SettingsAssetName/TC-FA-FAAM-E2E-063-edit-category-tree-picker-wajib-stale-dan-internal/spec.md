---
id: TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal
title: "Edit: Ganti Category, Category Dikosongkan, Dihapus Sesi Lain, dan Berubah Menjadi Internal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-195
  - TC-FA-FAAM-196
  - TC-FA-FAAM-197
  - TC-FA-FAAM-198
coverage:
  web: automated
---

# Edit: Ganti Category, Category Dikosongkan, Dihapus Sesi Lain, dan Berubah Menjadi Internal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; dipakai TC-196, 197, 198 hanya untuk dibuka dan ditolak validasi, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #22 (pohon kategori: `IT Equipment`, `Office Equipment`, dan seterusnya), #22b `Temp Category 197`, dan #22c `Temp Leaf 198`; `Temp Category 197` dihapus dan `Temp Leaf 198` diberi subcategory oleh sesi API aktor di dalam spec, lalu dibersihkan di hook `after`.
- Data Dinamis (salinan seed fixture #13d, Dinamis #22): `Edit Target Item 195 {runId}-063` (Code `ETI195`) untuk TC-195.
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-063` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-196: Category dikosongkan lewat Clear Field memunculkan error required saat Save

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Klik `[Clear Field]`
4. Isi ulang Asset Name `Edit Target Item`, Code `ETI`, TAG Type `QR`, Brand `Dell`, dan UoM `Unit` tanpa mengisi Category
5. Klik `[Save]`
6. Verifikasi error inline `Category must not be empty`
7. Klik `[✕]` pada modal Edit
8. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
9. Klik `[Leave]`

### TC-FA-FAAM-197: Category dihapus sesi lain saat Edit ditolak dan field ter-clear

10. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
11. Klik `[Select Category]`, pilih `Temp Category 197` dari Tree Picker, klik `[Select]`
12. Hapus `Temp Category 197` lewat sesi API aktor hingga penghapusan tersimpan
13. Klik `[Save]`
14. Verifikasi error inline `This category no longer exists. Please select another.`
15. Verifikasi field Category ter-clear
16. Klik `[✕]` pada modal Edit
17. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
18. Klik `[Leave]`

### TC-FA-FAAM-198: Category berubah menjadi internal sebelum Save ditolak dengan pesan khusus

19. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
20. Klik `[Select Category]`, pilih leaf `Temp Leaf 198`, klik `[Select]`
21. Tambahkan subcategory pada `Temp Leaf 198` lewat sesi API aktor hingga penambahan tersimpan
22. Klik `[Save]`
23. Verifikasi error inline `This category can no longer be selected. Please select another.`
24. Verifikasi field Category ter-clear
25. Klik `[✕]` pada modal Edit
26. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
27. Klik `[Leave]`

### TC-FA-FAAM-195: Mengganti Category lewat Tree Picker pada Asset Name tanpa aset

28. Ganti isi kotak search dengan `Edit Target Item 195 {runId}-063`, tekan Enter
29. Klik `⋯` baris `Edit Target Item 195 {runId}-063` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
30. Klik `[Select Category]`, pilih leaf `Office Equipment`, klik `[Select]`
31. Klik `[Save]`
32. Verifikasi toast `Success, asset name has been updated.` tampil
33. Verifikasi kolom Category baris `Edit Target Item 195 {runId}-063` menjadi `Office Equipment`
34. Verifikasi tidak ada dialog dampak karena Total Asset 0

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 28 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 7, 16, dan 25 (✕, dialog Unsaved Changes, `[Leave]`, S-08) agar TC berikutnya mulai dari form bersih.
- Urutan TC: validasi yang diblokir (TC-FA-FAAM-196, 197, 198) lebih dulu, lalu aksi sukses TC-FA-FAAM-195 pada salinan (S-10). Pelaku kedua pada TC-FA-FAAM-197 dan 198 memakai sesi API aktor (bukan konteks UI kedua), sehingga tidak memakai P-2.
- Langkah Uji TC-FA-FAAM-196 "Isi ulang semua field kecuali Category" dijalankan dengan nilai tersimpan `Edit Target Item`; Brand `Dell` diisi tanpa model, UoM `Unit`.
- Pada TC-FA-FAAM-195 Expected b (tidak ada dialog dampak) diasersi sesudah toast sukses dan kolom Category yang menjadi anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-197 dan TC-FA-FAAM-198 berlabel Manual Only dua sesi paralel; spec memakai sesi API aktor sebagai pelaku kedua sesuai keputusan 2026-10-21 (sesi UI kedua hanya bila hasilnya diasersi).
