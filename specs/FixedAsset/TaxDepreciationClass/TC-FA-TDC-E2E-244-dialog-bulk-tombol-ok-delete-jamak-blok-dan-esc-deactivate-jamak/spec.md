---
id: TC-FA-TDC-E2E-244-dialog-bulk-tombol-ok-delete-jamak-blok-dan-esc-deactivate-jamak
title: "Dialog Bulk Tombol OK Delete Jamak Blok dan Esc Deactivate Jamak"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-439
  - TC-FA-TDC-440
sourceRules: ["D-04", "F-FATDC-13.k10", "§3.6#p1", "FATDC-LOGIC-14j", "§4.1#r7", "§4.5#b1", "FATDC-LOGIC-14k", "FATDC-LOGIC-08h", "L-04"]
smoke: []
dependsOn: []
trace:
  "D-04": 5
  "F-FATDC-13.k10": [6, 7, 12]
  "§3.6#p1": [8, 23]
  "FATDC-LOGIC-14j": 9
  "§4.1#r7": 11
  "§4.5#b1": 19
  "FATDC-LOGIC-14k": [20, 22]
  "FATDC-LOGIC-08h": 21
  "L-04": 24
coverage:
  web: automated
---

# Dialog Bulk Tombol OK Delete Jamak Blok dan Esc Deactivate Jamak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset244`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-1 dan NB-KHS (keduanya Last Posted Tax Year 2026) serta NB-3 dan NB-4 (Active, Used By 0). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Dialog hanya dibuka lalu ditutup; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menekan `Esc`; Kemampuan baca jumlah entri Changelog (baseline sebelum aksi dan jumlah sesudahnya, S-12) disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-439: Tombol OK pada dialog blok Delete jamak mempertahankan seleksi

1. Catat baseline jumlah entri Changelog yang memuat class NB-1 dan NB-KHS lewat kemampuan baca log
2. Centang checkbox baris NB-1 dan NB-KHS
3. Klik `Delete` pada Bulk Action Bar
4. Klik `[OK]` pada dialog blok
5. Verifikasi dialog blok menutup
6. Verifikasi tidak ada toast tampil
7. Verifikasi baris NB-1 dan NB-KHS tetap ada di tabel
8. Verifikasi Bulk Action Bar tetap tampil
9. Verifikasi seleksi sebelumnya dipertahankan (counter `2 class selected`)
10. Klik ikon Changelog di toolbar
11. Verifikasi popup Changelog tampil
12. Verifikasi jumlah entri Changelog yang memuat class NB-1 dan NB-KHS sama dengan baseline (tidak ada entri baru)
13. Tutup popup Changelog
14. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-440: Tombol Esc menutup dialog Deactivate jamak

15. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-4 lewat kemampuan baca log
16. Centang checkbox baris NB-3 dan NB-4
17. Klik `Deactivate` pada Bulk Action Bar
18. Tekan tombol `Esc`
19. Verifikasi dialog menutup
20. Verifikasi tidak ada toast tampil
21. Verifikasi toggle `Active` baris NB-3 dan NB-4 tetap On
22. Verifikasi seleksi dipertahankan
23. Verifikasi Bulk Action Bar dipertahankan
24. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-4 sama dengan baseline (tidak ada entri log baru)
25. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-439, 440 (urutan nomor).
- Langkah penghubung (S-03, S-09): langkah 14 dan 25 (klik icon `×` agar seleksi TC berikutnya bersih) dan langkah `Tutup popup Changelog` pada TC-FA-TDC-439 (TC tidak menyebutnya).
- Klausa "tanpa perubahan data" pada Expected a diasersi lewat `Verifikasi` state toggle atau baris; klausa "Changelog tidak memuat entri baru untuk baris terpilih" (TC-FA-TDC-439) dan "tidak ada entri log baru" (TC-FA-TDC-440) diasersi sebagai selisih jumlah entri terhadap baseline per TC (S-12); TC-FA-TDC-439 memakai popup Changelog sebagai anchor (8b.2). Asersi jumlah, bukan absence kelas g (prinsip 13g). Toast diasersi tidak tampil tepat sesudah dialog menutup (8b.11).
- Temuan untuk QA:
  - Kalimat Expected "tidak ada entri log baru" tidak menyebut surface log dan sebagian TC tidak punya langkah observasinya; spec memakai Changelog (surface yang disebut TC-FA-TDC-433 sampai 439) dan membandingkan jumlah entri terhadap baseline (asersi jumlah, bukan absence kelas g; prinsip 13g).
  - TC-FA-TDC-440 tidak punya langkah observasi log; jumlah entri dibaca lewat kemampuan baca log tanpa membuka popup Changelog.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
