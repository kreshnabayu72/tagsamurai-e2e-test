---
id: TC-FA-GRP-E2E-065-edit-group-hover-saving-save-double-click-dan-aksesibilitas
title: "Popup Edit Group: Hover dan Saving State [Save], Double-Click [Save], dan Aksesibilitas"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-211
  - TC-FA-GRP-215
  - TC-FA-GRP-217
coverage:
  web: automated
---

# Popup Edit Group: Hover dan Saving State [Save], Double-Click [Save], dan Aksesibilitas

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-211 dan TC-FA-GRP-217 menyimpan perubahan; respons simpan ditahan lewat intercept hanya untuk mengamati state saving, bukan kegagalan yang dipaksa).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-065` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `Edit Target {runId}-065` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target"). Nilai ubah: TC-FA-GRP-211 Description `Hover Save`; TC-FA-GRP-217 Description `Double Click Save`.
- Kebutuhan intercept (`Spectra.intercept()`): menahan respons simpan group pada langkah 15 dan melepasnya pada langkah 18; nama endpoint tidak disebut di TC dan PRD (ditentukan tim FE di tahap script). Intercept dilepas di hook `after` bila spec gagal di tengah.
- Kemampuan teknis: pembacaan atribut ARIA (`aria-required`, `aria-describedby`) dan fokus keyboard (Tab berulang); double-click cepat; pembacaan jumlah entri Changelog node lewat kemampuan baca Changelog (disediakan tim FE/BE; selisih terhadap baseline, S-12).
- Pemulihan (hook `before` dan `after`): lepas intercept; hapus lewat API node dengan suffix `{runId}-065` dan group ber-Code literal `ET`.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-065`, tekan Enter

### TC-FA-GRP-215: Aksesibilitas Popup Edit Group

2. Buka elipsis (⋯) baris `Edit Target {runId}-065`, lalu klik Edit
3. Kosongkan Group Name, lalu klik [Save]
4. Verifikasi Group Name ber-`aria-required`
5. Verifikasi error terhubung ke Group Name via `aria-describedby`
6. Tekan Tab berulang
7. Verifikasi fokus berputar di dalam popup (focus trap)
8. Tekan Esc
9. Verifikasi dialog `Unsaved changes` muncul karena Group Name sudah dikosongkan (ada perubahan)
10. Klik [Leave]
11. Verifikasi Esc menutup popup (setelah [Leave])

### TC-FA-GRP-211: Hover dan Saving state tombol [Save]

12. Buka elipsis (⋯) baris `Edit Target {runId}-065`, klik Edit, lalu ubah Description menjadi `Hover Save`
13. Hover [Save]
14. Verifikasi [Save] menampilkan state hover
15. Tahan respons simpan group lewat intercept
16. Klik [Save]
17. Verifikasi [Save] masuk saving state (disabled + loading)
18. Lepas tahanan respons dan tunggu popup tertutup

### TC-FA-GRP-217: Double-click [Save] hanya 1 request

19. Buka elipsis (⋯) baris `Edit Target {runId}-065`, klik Edit, lalu ubah Description menjadi `Double Click Save`
20. Tunggu toast lama hilang otomatis
21. Catat jumlah entri Changelog node `Edit Target {runId}-065` sebagai baseline
22. Double-click cepat [Save]
23. Verifikasi tombol [Save] disabled setelah klik pertama
24. Verifikasi hanya 1 toast sukses `Success, group has been updated.`
25. Verifikasi hanya 1 record diubah: jumlah entri Changelog node bertambah tepat 1 terhadap baseline langkah 21
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata, intercept hanya menahan respons untuk mengamati saving state; bukan kegagalan yang dipaksa sehingga bukan kelas b). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-215 (diblokir) lebih dulu, lalu TC-FA-GRP-211 dan TC-FA-GRP-217 yang menyimpan perubahan (S-10); berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-065`, tekan Enter); langkah 15 (Tahan respons simpan group lewat intercept); langkah 18 (Lepas tahanan respons dan tunggu popup tertutup); langkah 20 (Tunggu toast lama hilang otomatis); langkah 21 (Catat jumlah entri Changelog node `Edit Target {runId}-065` sebagai ba...); langkah 26 (Klik `(←)` pada kotak Search).
- Langkah Search mencari baris target (R-16).
- Temuan untuk QA:
  - TC-FA-GRP-217 Expected a "Hanya 1 record dibuat/diubah" tidak menyebut cara membaca; spec memakai selisih jumlah entri Changelog node terhadap baseline (kemampuan baca disediakan tim FE/BE).
  - TC-FA-GRP-217 Expected b "Tombol disabled setelah klik pertama" adalah state sementara; diasersi tepat setelah double-click (8b butir 5). Jika popup sudah menutup sebelum asersi, tim script perlu menahan respons seperti langkah 15; TC tidak menyebut penundaan respons.
  - TC-FA-GRP-215 Langkah Uji "Submit kosong" pada Popup Edit (yang pre-filled) tidak menyebut cara mengosongkan form; spec mengosongkan Group Name. Akibatnya Esc memunculkan dialog `Unsaved changes` (Expected c "dialog Unsaved changes bila ada perubahan"), yang ditutup lewat [Leave].
  - TC-FA-GRP-211 Expected b "sampai response" tidak menyebut keadaan setelah respons; spec hanya menunggu popup tertutup (langkah 18) tanpa `Verifikasi` tambahan.

