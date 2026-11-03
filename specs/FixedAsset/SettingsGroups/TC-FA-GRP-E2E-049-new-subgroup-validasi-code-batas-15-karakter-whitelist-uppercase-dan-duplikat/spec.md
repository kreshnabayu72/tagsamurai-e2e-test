---
id: TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat
title: "Popup New Subgroup: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-142
  - TC-FA-GRP-143
  - TC-FA-GRP-144
  - TC-FA-GRP-145
  - TC-FA-GRP-146
  - TC-FA-GRP-147
coverage:
  web: automated
---

# Popup New Subgroup: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-146 dan TC-FA-GRP-147 butuh pengecekan Code ke backend, TC-FA-GRP-142 dan TC-FA-GRP-145 menyimpan subgroup).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Pre-setup tambahan (hanya dibaca): Warehouse A ber-Code `WH-A` (pembanding duplikat TC-FA-GRP-146).
- Data Dinamis bersuffix `{runId}-049` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script):
  - Tabel Nilai Code TC-FA-GRP-144 (iterasi langkah 4 sampai 6): `AB#1`, `A B`, `A@B`.
  - TC-FA-GRP-143: Code `ABCDEFGHIJ-12345` (16 karakter). TC-FA-GRP-142: Code `ABCDEFGHIJ-1234` (15 karakter). TC-FA-GRP-145: Code `wh_a-1.b` (hasil `WH_A-1.B`). TC-FA-GRP-146: Code `wh-a`. TC-FA-GRP-147: Code `NEW1`.
  - Name valid untuk submit: `Sub Code {runId}-049-A` (TC-FA-GRP-146 dan TC-FA-GRP-142), `Sub Code {runId}-049-B` (TC-FA-GRP-147), `Sub Code {runId}-049-C` (TC-FA-GRP-145).
  - TC-FA-GRP-147: group pihak lain `Pihak Lain {runId}-049` ber-Code `NEW1`, dibuat lewat sesi API aktor pada langkah 14 (pelaku kedua hanya memicu perubahan state).
- Kemampuan teknis: pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); penantian debounce ±500 ms.
- Pemulihan (hook `before` dan `after`): hapus lewat API seluruh group dengan suffix `{runId}-049` dan group ber-Code literal `ABCDEFGHIJ-1234`, `WH_A-1.B`, dan `NEW1` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-143: Code 16 karakter langsung error

1. Ketik Search `Head Office`, tekan Enter
2. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
3. Ketik Code `ABCDEFGHIJ-12345` (16 karakter)
4. Verifikasi inline error `Max. 15 characters` langsung tampil

### TC-FA-GRP-144: Code berisi karakter di luar whitelist

5. Untuk setiap baris tabel "Nilai Code TC-FA-GRP-144" pada Prerequisites (langkah 5 sampai 7): ganti isi Code dengan nilai baris itu
6. Verifikasi inline error `Code contains invalid characters` langsung tampil
7. Verifikasi helper text `Letters, numbers, hyphens, underscores, and dots only` tetap tampil

### TC-FA-GRP-146: Code duplikat per client case-insensitive (debounce)

8. Ganti isi Code dengan `wh-a` (milik Warehouse A)
9. Tunggu ±500 ms
10. Verifikasi inline error `Code already exists` muncul saat mengetik
11. Isi Group Name `Sub Code {runId}-049-A`, lalu klik [Submit] (memeriksa "Submit tidak menyimpan")
12. Verifikasi Submit tidak menyimpan: jumlah group lewat fixture BE sama dengan baseline

### TC-FA-GRP-147: Code dipakai saat submit oleh user lain (re-check atomik)

13. Ganti isi Code dengan `NEW1` (unik), isi Group Name `Sub Code {runId}-049-B`
14. Tunggu ±500 ms (Code lolos debounce)
15. Lewat sesi API aktor, simpan group `Pihak Lain {runId}-049` ber-Code `NEW1` hingga tersimpan
16. Klik [Submit]
17. Verifikasi inline error `Code already exists` dari server pada field Code
18. Verifikasi popup tetap terbuka dengan input dipertahankan (Group Name dan Code `NEW1`)

### TC-FA-GRP-142: Code 15 karakter diterima

19. Isi Group Name `Sub Code {runId}-049-A`, ganti isi Code dengan `ABCDEFGHIJ-1234` (15 karakter), lalu klik [Submit]
20. Verifikasi toast sukses `Success, group has been created.`
21. Klik Head Office di sidebar, lalu ganti isi kotak Search dengan `Sub Code {runId}-049-A`, tekan Enter
22. Verifikasi Code `ABCDEFGHIJ-1234` tersimpan utuh 15 karakter pada baris hasil Search
23. Klik `(←)` pada kotak Search

### TC-FA-GRP-145: Code menerima huruf, angka, -, _, . dan auto-uppercase

24. Klik All Groups di sidebar
25. Ketik Search `Head Office`, tekan Enter
26. Buka elipsis (⋯) baris Head Office, lalu klik Add Subgroup
27. Isi Group Name `Sub Code {runId}-049-C`, isi Code `wh_a-1.b`, lalu klik [Submit]
28. Verifikasi Code tampil dan tersimpan uppercase `WH_A-1.B`
29. Verifikasi toast sukses `Success, group has been created.`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-GRP-143, 144, 146, 147), lalu aksi sukses (TC-FA-GRP-142, 145) sesuai S-10; berbeda dari urutan nomor TC sumber. Dalam satu popup, nilai Code diganti sehingga error TC sebelumnya hilang sebelum TC berikutnya (R-12, S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 9 (Tunggu ±500 ms); langkah 11 (Isi Group Name `Sub Code {runId}-049-A`, lalu klik [Submit] (memeriksa "Submit tidak menyimpan")); langkah 14 (Tunggu ±500 ms (Code lolos debounce)); langkah 21 (Klik Head Office di sidebar, lalu ganti isi kotak Search dengan `Sub Code {runId}-049-A`, tekan Enter); langkah 23 (Klik `(←)` pada kotak Search).
- Pencarian baris target (S-03, R-16): langkah 1 (Ketik Search `Head Office`, tekan Enter) menemukan baris Head Office; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris Head Office tidak dijamin berada di halaman 1 All Groups. Langkah 24 (Klik All Groups di sidebar) dan langkah 25 (Ketik Search `Head Office`, tekan Enter) memulihkan tabel yang sesudah langkah 21 berisi child Head Office, supaya baris Head Office tampil kembali.
- Langkah 5 sampai 7 berulang untuk tiga nilai tabel Prerequisites; `Verifikasi` tetap satu per klausa dan ekspansinya 3 x 3 langkah (8b butir 7).
- TC-FA-GRP-147: pelaku kedua memakai sesi API aktor (bukan konteks UI kedua), sehingga tidak butuh butir `P-2` (P-2 `[KEPUTUSAN 2026-10-30]`).
- Temuan untuk QA:
  - TC-FA-GRP-146 Expected b dan TC-FA-GRP-147 tidak menyebut Group Name valid yang diisi saat [Submit]; spec memakai nama bersuffix milik spec.
  - TC-FA-GRP-146 Expected b "Submit tidak menyimpan" tidak punya langkah klik [Submit]; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-144 Data Uji menyebut tiga nilai (`AB#1`, `A B`, `A@B`) tetapi Langkah Uji hanya `AB#1`; spec mengiterasi ketiganya.

