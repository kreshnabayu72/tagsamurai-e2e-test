---
id: TC-FA-GRP-E2E-058-edit-function-none-ke-assignable-disposal-tanpa-dialog-histori-disposal-dan-bersamaan-name
title: "Edit Function None ke Assignable/Disposal Group Tanpa Dialog, Function dari Disposal Group dengan Histori Disposal, dan Function Bersamaan dengan Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-183
  - TC-FA-GRP-184
  - TC-FA-GRP-185
  - TC-FA-GRP-186
coverage:
  web: automated
---

# Edit Function None ke Assignable/Disposal Group Tanpa Dialog, Function dari Disposal Group dengan Histori Disposal, dan Function Bersamaan dengan Name

## Prerequisites

- Mode: FE+BE (backend nyata; Edit Function menulis data; TC-FA-GRP-185 membaca record disposal lewat fixture BE).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-058` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): `Disposal Edit Own {runId}-058` (Disposal Group dengan histori Disposal Complete, milik spec ini, bukan Disposal Yard Pre-setup bersama; seeding disediakan tim FE/BE; TC-FA-GRP-185), `FN None A {runId}-058` (Function None; TC-FA-GRP-183), `FN None B {runId}-058` (Function None; TC-FA-GRP-184), `FN Assign {runId}-058` (Function Assignable, punya aset; TC-FA-GRP-186) yang diubah menjadi Name `FN Renamed {runId}-058` dan Function None.
- Kemampuan teknis: pembacaan record disposal lama dan nama yang menunjuk Disposal Edit Own (snapshot nama) lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD).
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-058`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-183: Function None ke Assignable langsung tersimpan tanpa dialog

1. Ketik Search `FN None A {runId}-058`, tekan Enter
2. Buka elipsis (⋯) baris `FN None A {runId}-058`, klik Edit, pilih Assignable, lalu klik [Save]
3. Verifikasi tidak ada Dialog Change Function
4. Verifikasi toast sukses `Success, group has been updated.`
5. Verifikasi badge Assignable pada baris `FN None A {runId}-058`

### TC-FA-GRP-184: Function None ke Disposal Group langsung tersimpan tanpa dialog

6. Ganti isi kotak Search dengan `FN None B {runId}-058`, tekan Enter
7. Buka elipsis (⋯) baris `FN None B {runId}-058`, klik Edit, pilih Disposal Group, lalu klik [Save]
8. Verifikasi tidak ada Dialog Change Function
9. Verifikasi toast sukses `Success, group has been updated.`
10. Verifikasi badge Disposal pada baris `FN None B {runId}-058`

### TC-FA-GRP-186: Function bersamaan dengan Name, dialog muncul lalu kedua field tersimpan

11. Ganti isi kotak Search dengan `FN Assign {runId}-058`, tekan Enter
12. Buka elipsis (⋯) baris `FN Assign {runId}-058`, klik Edit, ubah Name menjadi `FN Renamed {runId}-058`, pilih Function None, lalu klik [Save]
13. Verifikasi Dialog Change Function varian Assignable ke None tampil
14. Klik [Save] pada dialog
15. Verifikasi toast sukses `Success, group has been updated.`
16. Ganti isi kotak Search dengan `FN Renamed {runId}-058`, tekan Enter
17. Verifikasi Name baru `FN Renamed {runId}-058` dan Function baru `—` tersimpan pada baris itu

### TC-FA-GRP-185: Function dari Disposal Group pada node dengan histori disposal diizinkan

18. Ganti isi kotak Search dengan `Disposal Edit Own {runId}-058`, tekan Enter
19. Buka elipsis (⋯) baris `Disposal Edit Own {runId}-058`, lalu klik Edit
20. Verifikasi field Function enabled (tidak ada guard histori disposal)
21. Pilih Function None, klik [Save] pada Popup Edit, lalu klik [Save] pada dialog
22. Verifikasi perubahan sukses dengan toast `Success, group has been updated.`
23. Verifikasi record disposal lama tetap menunjuk `Disposal Edit Own {runId}-058` (snapshot nama), dibaca lewat fixture BE
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-183, 184, 186, lalu TC-FA-GRP-185 di akhir karena mengubah Function node berhistori disposal; berbeda dari urutan nomor TC sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `FN None A {runId}-058`, tekan Enter); langkah 6 (Ganti isi kotak Search dengan `FN None B {runId}-058`, tekan Enter); langkah 11 (Ganti isi kotak Search dengan `FN Assign {runId}-058`, tekan Enter); langkah 16 (Ganti isi kotak Search dengan `FN Renamed {runId}-058`, tekan Enter; Search `FN Assign {runId}-058` tidak lagi cocok dengan baris yang sudah diganti namanya); langkah 18 (Ganti isi kotak Search dengan `Disposal Edit Own {runId}-058`, tekan Enter); langkah 24 (Klik `(←)` pada kotak Search).
- Temuan untuk QA:
  - TC-FA-GRP-185 Expected a menyebut "Field Function enabled" tanpa langkah observasi; spec mengasersi field Function enabled sebelum [Save] (Langkah Uji [Save] → [Save]).
  - TC-FA-GRP-185 Expected b "Record disposal lama tetap menunjuk Disposal Edit Own" tidak menyebut cara membaca; spec memakai fixture BE (disediakan tim FE/BE).
  - TC-FA-GRP-186 Post Condition "Changelog 2 baris (Group Name, Function)" tidak punya langkah observasi di TC; tidak diasersi di spec ini.

