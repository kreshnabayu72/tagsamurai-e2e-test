---
id: TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field
title: "Popup Edit Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field]"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-206
  - TC-FA-GRP-207
  - TC-FA-GRP-208
  - TC-FA-GRP-209
  - TC-FA-GRP-210
coverage:
  web: automated
---

# Popup Edit Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field]

## Prerequisites

- Mode: FE+BE (backend nyata; hanya TC-FA-GRP-206 menyimpan perubahan dan membaca Detail, TC lain tanpa submit).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-064` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-064` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target"). TC-FA-GRP-207: Description 361 karakter. TC-FA-GRP-210: sebelum [Clear Field], Group Name `Clear Edit {runId}-064`, Code `CLR3`, Description `Clear me`, dan Function Assignable diisi di form. TC-FA-GRP-206: Name `Edit Target {runId}-064` dan Description 360 karakter.
- Kemampuan teknis: pengetikan 361 karakter; klik icon info Function (tooltip on click).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-064` dan group ber-Code literal `ET` dan `CLR3`.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-064`, tekan Enter

### TC-FA-GRP-207: Description 361 karakter langsung error

2. Buka elipsis (⋯) baris `Edit Target {runId}-064`, lalu klik Edit
3. Ketik Description 361 karakter
4. Verifikasi inline error `Max. 360 characters` langsung tampil

### TC-FA-GRP-208: Tooltip icon info Function (on click) per opsi

5. Klik icon info None
6. Verifikasi tooltip None: `This group is for organizing only. It won't hold assets or appear as a disposal destination.`
7. Klik icon info Assignable
8. Verifikasi tooltip Assignable: `Assets can be registered or transferred directly into this group.`
9. Klik icon info Disposal Group
10. Verifikasi tooltip Disposal Group: `This group becomes a destination for disposed assets. You can have more than one Disposal Group.`

### TC-FA-GRP-209: Function radio mutually exclusive

11. Pilih Function Assignable
12. Pilih Function Disposal Group
13. Verifikasi hanya satu opsi terpilih pada satu waktu (Disposal Group terpilih)
14. Verifikasi Assignable otomatis tidak terpilih

### TC-FA-GRP-210: Tombol [Clear Field]

15. Isi Group Name `Clear Edit {runId}-064`, Code `CLR3`, Description `Clear me`, dan pilih Function Assignable
16. Klik [Clear Field]
17. Verifikasi Group Name dikosongkan
18. Verifikasi Code dikosongkan
19. Verifikasi Description dikosongkan
20. Verifikasi Function kembali ke None (bukan revert ke nilai tersimpan)
21. Verifikasi popup tetap terbuka
22. Verifikasi tidak ada dialog konfirmasi

### TC-FA-GRP-206: Description 360 karakter diterima

23. Isi Group Name `Edit Target {runId}-064` dan Description 360 karakter, lalu klik [Save]
24. Verifikasi toast sukses `Success, group has been updated.`
25. Klik nama `Edit Target {runId}-064` untuk membuka Popup Detail Group
26. Verifikasi Description tersimpan utuh 360 karakter di Detail
27. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: kasus tanpa submit lebih dulu dalam satu pembukaan popup, lalu aksi sukses TC-FA-GRP-206 di akhir (S-10); berbeda dari urutan nomor TC sumber. Field diisi ulang oleh TC-FA-GRP-206 setelah [Clear Field] (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-064`, tekan Enter); langkah 25 (Klik nama `Edit Target {runId}-064` untuk membuka Popup Detail Group); langkah 27 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search).
- Langkah Search mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-206 Expected b "Description tersimpan utuh di Detail" tidak menyebut langkah membuka Detail; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-210 menyebut Function "kembali ke None" sedangkan Edit Target sudah ber-Function None; spec memilih Function Assignable sebelum [Clear Field] supaya perpindahan ke None teramati.
  - TC-FA-GRP-210 menyebut "Isi/ubah seluruh field" tanpa data; spec memakai nilai bersuffix milik spec.

