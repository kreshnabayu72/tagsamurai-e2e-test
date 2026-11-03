---
id: TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling
title: "Popup Edit Group: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-191
  - TC-FA-GRP-192
  - TC-FA-GRP-193
  - TC-FA-GRP-194
  - TC-FA-GRP-195
coverage:
  web: automated
---

# Popup Edit Group: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-192 dan TC-FA-GRP-195 menyimpan perubahan, TC-FA-GRP-194 butuh pengecekan duplikat sibling ke backend).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-061` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script), di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target", "Sibling Target"):
  - `Edit Target {runId}-061` (level 1, Code `ET`, Description `Edit me`, Function None) sebagai target Edit.
  - `Sibling Target {runId}-061` (level 1, sibling Edit Target) sebagai pembanding duplikat TC-FA-GRP-194; nilai yang diketik `SIBLING TARGET {runId}-061`.
  - `Parent Lain {runId}-061` (level 1) dengan child `Nama Bersama {runId}-061` sebagai pembanding "nama sama di parent lain" TC-FA-GRP-195 (dipakai sebagai precondition TC, tidak diasersi).
  - Nama 120 karakter (TC-FA-GRP-192) dan 121 karakter (TC-FA-GRP-193): string huruf `X` yang dihitung termasuk suffix `{runId}-061` sehingga total tepat 120 dan 121 karakter.
- Kemampuan teknis: pembacaan nilai Group Name node target lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); penantian debounce ±500 ms.
- Pemulihan (hook `before` dan `after`): hapus lewat API seluruh node dengan suffix `{runId}-061` dan group ber-Code literal `ET`.
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-061`, tekan Enter

### TC-FA-GRP-191: Group Name kosong ditolak saat submit

2. Buka elipsis (⋯) baris `Edit Target {runId}-061`, lalu klik Edit
3. Kosongkan Group Name, lalu klik [Save]
4. Verifikasi inline error `Group name must not be empty` di bawah Group Name
5. Verifikasi popup tetap terbuka
6. Verifikasi data tidak tersimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-061`

### TC-FA-GRP-193: Group Name 121 karakter langsung error

7. Ketik Group Name 121 karakter
8. Verifikasi inline error `Max. 120 characters` langsung tampil saat melebihi 120 karakter
9. Klik [Save] (memeriksa "Submit tidak tersimpan selama error")
10. Verifikasi perubahan tidak tersimpan: Group Name node target lewat fixture BE tetap `Edit Target {runId}-061`

### TC-FA-GRP-194: Group Name duplikat sibling (case-insensitive, debounce)

11. Ganti isi Group Name dengan `SIBLING TARGET {runId}-061`
12. Tunggu ±500 ms tanpa blur
13. Verifikasi inline error `Group name already exists in this level` muncul saat mengetik (debounce ~500 ms, tanpa menunggu blur)
14. Klik [Save] (memeriksa "[Save] tidak menyimpan data")
15. Verifikasi [Save] tidak menyimpan data: Group Name node target lewat fixture BE tetap `Edit Target {runId}-061`

### TC-FA-GRP-192: Group Name 120 karakter diterima (batas)

16. Ganti isi Group Name dengan string 120 karakter
17. Verifikasi field Group Name berisi 120 karakter utuh
18. Verifikasi tidak ada error panjang pada Group Name
19. Klik [Save]
20. Verifikasi toast sukses `Success, group has been updated.`
21. Ganti isi kotak Search dengan string 120 karakter tersebut, tekan Enter
22. Verifikasi nama 120 karakter tersimpan utuh pada baris hasil Search

### TC-FA-GRP-195: Group Name sama dengan group di parent lain diterima

23. Buka elipsis (⋯) baris hasil Search (node target yang kini bernama 120 karakter), lalu klik Edit
24. Ganti isi Group Name dengan `Nama Bersama {runId}-061` (nama yang sudah dipakai node di parent berbeda)
25. Tunggu ±500 ms tanpa blur
26. Verifikasi tidak ada error duplikat (keunikan per parent)
27. Klik [Save]
28. Verifikasi toast sukses `Success, group has been updated.`
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-191, 193, 194), lalu aksi sukses (TC-FA-GRP-192, 195) sesuai S-10; berbeda dari urutan nomor TC sumber. TC-FA-GRP-195 mengedit node target yang sama setelah diubah TC-FA-GRP-192 (data milik spec ini).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-061`, tekan Enter); langkah 9 (Klik [Save] (memeriksa "Submit tidak tersimpan selama error")); langkah 12 (Tunggu ±500 ms tanpa blur); langkah 14 (Klik [Save] (memeriksa "[Save] tidak menyimpan data")); langkah 21 (Ganti isi kotak Search dengan string 120 karakter tersebut, tekan Enter); langkah 29 (Klik `(←)` pada kotak Search). Langkah 25 (Tunggu ±500 ms tanpa blur) memberi waktu debounce sebelum absence error duplikat.
- Langkah 1 dan Search sesudah TC-FA-GRP-192 mencari baris target (R-16).
- Pembanding TC-FA-GRP-195 memakai node milik spec (`Nama Bersama {runId}-061`) menggantikan contoh `IT Department` Pre-setup (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-GRP-193 dan TC-FA-GRP-194 Expected "Submit tidak tersimpan / tidak menyimpan" tidak punya langkah klik [Save] di Langkah Uji; spec menambahkan klik sebagai langkah penghubung.
  - TC-FA-GRP-192 Expected a "Tidak ada error panjang" tidak menyebut cara membuktikan field terisi; spec lebih dulu memverifikasi isi field 120 karakter sebagai anchor.
  - TC-FA-GRP-194 menulis nama pembanding `SIBLING TARGET`; spec menambahkan suffix `{runId}-061` mengikuti nama sibling yang di-seed.

