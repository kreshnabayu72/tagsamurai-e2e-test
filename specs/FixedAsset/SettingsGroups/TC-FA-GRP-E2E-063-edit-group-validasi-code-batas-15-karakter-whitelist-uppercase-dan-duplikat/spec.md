---
id: TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat
title: "Popup Edit Group: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-200
  - TC-FA-GRP-201
  - TC-FA-GRP-202
  - TC-FA-GRP-203
  - TC-FA-GRP-204
  - TC-FA-GRP-205
coverage:
  web: automated
---

# Popup Edit Group: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-204 dan TC-FA-GRP-205 butuh pengecekan Code ke backend, TC-FA-GRP-200 dan TC-FA-GRP-203 menyimpan perubahan).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Pre-setup (hanya dibaca): Warehouse A ber-Code `WH-A` (pembanding duplikat TC-FA-GRP-204).
- Data Dinamis bersuffix `{runId}-063` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script):
  - Node `Edit Target {runId}-063` (level 1, Code `ET`, Description `Edit me`, Function None) di-seed lewat API di hook `before` (Pre-setup tambahan "Edit Target").
  - Tabel Nilai Code TC-FA-GRP-202 (iterasi langkah 5 sampai 7): `AB#1`, `A B`, `A@B`.
  - TC-FA-GRP-201: Code `ABCDEFGHIJ-12345` (16 karakter). TC-FA-GRP-200: Code `ABCDEFGHIJ-1234` (15 karakter). TC-FA-GRP-203: Code `wh_a-1.b` (hasil `WH_A-1.B`). TC-FA-GRP-204: Code `wh-a`. TC-FA-GRP-205: Code `NEW1`.
  - Name valid untuk submit: `Edit Code A {runId}-063` (TC-FA-GRP-204 dan TC-FA-GRP-200), `Edit Code B {runId}-063` (TC-FA-GRP-205), `Edit Code C {runId}-063` (TC-FA-GRP-203).
  - TC-FA-GRP-205: group pihak lain `Pihak Lain {runId}-063` ber-Code `NEW1`, dibuat lewat sesi API aktor pada langkah 15 (pelaku kedua hanya memicu perubahan state).
- Kemampuan teknis: pembacaan Code node target lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); penantian debounce ±500 ms.
- Pemulihan (hook `before` dan `after`): hapus lewat API seluruh group dengan suffix `{runId}-063` dan group ber-Code literal `ET`, `ABCDEFGHIJ-1234`, `WH_A-1.B`, dan `NEW1` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target {runId}-063`, tekan Enter

### TC-FA-GRP-201: Code 16 karakter langsung error

2. Buka elipsis (⋯) baris `Edit Target {runId}-063`, lalu klik Edit
3. Ketik Code `ABCDEFGHIJ-12345` (16 karakter)
4. Verifikasi inline error `Max. 15 characters` langsung tampil

### TC-FA-GRP-202: Code berisi karakter di luar whitelist

5. Untuk setiap baris tabel "Nilai Code TC-FA-GRP-202" pada Prerequisites (langkah 5 sampai 7): ganti isi Code dengan nilai baris itu
6. Verifikasi inline error `Code contains invalid characters` langsung tampil
7. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tetap tampil

### TC-FA-GRP-204: Code duplikat per client case-insensitive (debounce)

8. Ganti isi Code dengan `wh-a` (milik Warehouse A)
9. Tunggu ±500 ms
10. Verifikasi inline error `Code already exists` muncul saat mengetik
11. Klik [Save] (memeriksa "Submit tidak menyimpan")
12. Verifikasi Submit tidak menyimpan: Code node target lewat fixture BE tetap `ET`

### TC-FA-GRP-205: Code dipakai saat submit oleh user lain (re-check atomik)

13. Ganti isi Code dengan `NEW1` (unik)
14. Tunggu ±500 ms (Code lolos debounce)
15. Lewat sesi API aktor, simpan group `Pihak Lain {runId}-063` ber-Code `NEW1` hingga tersimpan
16. Klik [Save]
17. Verifikasi inline error `Code already exists` dari server pada field Code
18. Verifikasi popup tetap terbuka dengan input dipertahankan (Code `NEW1`)

### TC-FA-GRP-200: Code 15 karakter diterima

19. Isi Group Name `Edit Code A {runId}-063`, ganti isi Code dengan `ABCDEFGHIJ-1234` (15 karakter), lalu klik [Save]
20. Verifikasi toast sukses `Success, group has been updated.`
21. Ketik Search `Edit Code A {runId}-063`, tekan Enter
22. Verifikasi Code `ABCDEFGHIJ-1234` tersimpan utuh 15 karakter pada baris hasil Search

### TC-FA-GRP-203: Code menerima huruf, angka, -, _, . dan auto-uppercase

23. Buka elipsis (⋯) baris hasil Search, klik Edit, isi Group Name `Edit Code C {runId}-063` dan Code `wh_a-1.b`, lalu klik [Save]
24. Verifikasi Code tampil dan tersimpan uppercase `WH_A-1.B`
25. Verifikasi toast sukses `Success, group has been updated.`
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-201, 202, 204, 205), lalu aksi sukses (TC-FA-GRP-200, 203) sesuai S-10; berbeda dari urutan nomor TC sumber. Dalam satu popup, nilai Code diganti sehingga error TC sebelumnya hilang sebelum TC berikutnya (R-12, S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Edit Target {runId}-063`, tekan Enter); langkah 9 (Tunggu ±500 ms); langkah 11 (Klik [Save] (memeriksa "Submit tidak menyimpan")); langkah 14 (Tunggu ±500 ms (Code lolos debounce)); langkah 21 (Ketik Search `Edit Code A {runId}-063`, tekan Enter); langkah 26 (Klik `(←)` pada kotak Search).
- Langkah 5 sampai 7 berulang untuk tiga nilai tabel Prerequisites; `Verifikasi` tetap satu per klausa dan ekspansinya 3 x 3 langkah (8b butir 7). Langkah Search mencari baris target (R-16).
- TC-FA-GRP-205: pelaku kedua memakai sesi API aktor (bukan konteks UI kedua), sehingga tidak butuh butir `P-2` (P-2 `[KEPUTUSAN 2026-10-30]`).
- Temuan untuk QA:
  - TC-FA-GRP-204 Expected b "Submit tidak menyimpan" tidak punya langkah klik [Save]; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-202 Data Uji menyebut tiga nilai (`AB#1`, `A B`, `A@B`) tetapi Langkah Uji hanya `AB#1`; spec mengiterasi ketiganya.
  - TC-FA-GRP-200 dan TC-FA-GRP-205 menyebut "Group Name valid" tanpa nilai; spec memakai nama bersuffix milik spec.

