---
id: TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling
title: "Popup New Subgroup: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-133
  - TC-FA-GRP-134
  - TC-FA-GRP-135
  - TC-FA-GRP-136
  - TC-FA-GRP-137
coverage:
  web: automated
---

# Popup New Subgroup: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-134 dan TC-FA-GRP-137 menyimpan subgroup, TC-FA-GRP-136 butuh pengecekan duplikat sibling ke backend).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-047` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script):
  - Group parent `Parent Lain {runId}-047` (level 1, Function None) dengan child `Nama Bersama {runId}-047`; di-seed lewat API di hook `before` sebagai pembanding "nama sama di parent lain" TC-FA-GRP-137 (dipakai sebagai precondition TC, tidak diasersi).
  - Nama 120 karakter (TC-FA-GRP-134) dan 121 karakter (TC-FA-GRP-135): string huruf `X` yang dihitung termasuk suffix `{runId}-047` sehingga total tepat 120 dan 121 karakter.
  - Pembanding duplikat sibling TC-FA-GRP-136: `FLOOR 2` (sibling Floor 2 di bawah Head Office).
- Kemampuan teknis: pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); penantian debounce ±500 ms.
- Pemulihan (hook `after`): hapus lewat API seluruh group dengan suffix `{runId}-047` (termasuk subgroup yang dibuat TC-FA-GRP-134 dan TC-FA-GRP-137) dan seed `Parent Lain`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-133: Group Name kosong ditolak saat submit

1. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
2. Biarkan Group Name kosong, lalu klik [Submit]
3. Verifikasi inline error `Group name must not be empty` di bawah Group Name
4. Verifikasi popup tetap terbuka
5. Verifikasi data tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-135: Group Name 121 karakter langsung error

6. Ketik Group Name 121 karakter
7. Verifikasi inline error `Max. 120 characters` langsung tampil saat melebihi 120 karakter
8. Klik [Submit] (memeriksa "Submit tidak tersimpan selama error")
9. Verifikasi subgroup tidak tersimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-136: Group Name duplikat sibling (case-insensitive, debounce)

10. Ganti isi Group Name dengan `FLOOR 2`
11. Tunggu ±500 ms tanpa blur
12. Verifikasi inline error `Group name already exists in this level` muncul saat mengetik (debounce ~500 ms, tanpa menunggu blur)
13. Klik [Submit] (memeriksa "[Submit] tidak menyimpan data")
14. Verifikasi [Submit] tidak menyimpan data: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-134: Group Name 120 karakter diterima (batas)

15. Ganti isi Group Name dengan string 120 karakter
16. Verifikasi field Group Name berisi 120 karakter utuh
17. Verifikasi tidak ada error panjang pada Group Name
18. Klik [Submit]
19. Verifikasi toast sukses `Success, group has been created.`
20. Klik Head Office di sidebar, lalu ketik Search string 120 karakter tersebut, tekan Enter
21. Verifikasi nama 120 karakter tersimpan utuh pada baris hasil Search
22. Klik `(←)` pada kotak Search

### TC-FA-GRP-137: Group Name sama dengan group di parent lain diterima

23. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
24. Ketik Group Name `Nama Bersama {runId}-047` (nama yang sudah dipakai node di parent berbeda)
25. Verifikasi tidak ada error duplikat (keunikan per parent)
26. Klik [Submit]
27. Verifikasi toast sukses `Success, group has been created.`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-133, 135, 136), lalu aksi sukses (TC-FA-GRP-134, 137) sesuai S-10; berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 8 (Klik [Submit] (memeriksa "Submit tidak tersimpan selama error")); langkah 11 (Tunggu ±500 ms tanpa blur); langkah 13 (Klik [Submit] (memeriksa "[Submit] tidak menyimpan data")); langkah 20 (Klik Head Office di sidebar, lalu ketik Search string 120 karakter ter...); langkah 22 (Klik `(←)` pada kotak Search).
- Langkah 20 mencari baris target yang baru dibuat (R-16).
- Pembanding TC-FA-GRP-137 memakai node milik spec (`Nama Bersama {runId}-047`) menggantikan contoh `IT Department` Pre-setup (S-06, S-12).
- Temuan untuk QA:
  - TC-FA-GRP-135 dan TC-FA-GRP-136 Expected "Submit tidak tersimpan / tidak menyimpan" tidak punya langkah klik [Submit] di Langkah Uji; spec menambahkan klik sebagai langkah penghubung.
  - TC-FA-GRP-134 Expected a "Tidak ada error panjang" tidak menyebut cara membuktikan field terisi; spec lebih dulu memverifikasi isi field 120 karakter sebagai anchor.

