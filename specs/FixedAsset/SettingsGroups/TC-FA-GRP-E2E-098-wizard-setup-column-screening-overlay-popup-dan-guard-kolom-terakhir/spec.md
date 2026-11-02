---
id: TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir
title: "Wizard Setup Column: Column Visibility, Screening Popup 3 Zona + Live Preview, dan Guard Kolom Terakhir yang Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-960
  - TC-FA-GRP-1096
  - TC-FA-GRP-1097
  - TC-FA-GRP-1101
coverage:
  web: automated
---

# Wizard Setup Column: Column Visibility, Screening Popup 3 Zona + Live Preview, dan Guard Kolom Terakhir yang Visible

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Pemulihan konfigurasi kolom: preferensi kolom tabel Step Group Consolidation yang disimpan spec dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan [Reset to Default]); kemampuan disediakan tim FE (bagian 4).

## Test Steps

### TC-FA-GRP-1096 dan TC-FA-GRP-960: Overlay Column Visibility

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Hover icon `⋯` di header kolom terakhir
3. Verifikasi tooltip Column Visibility tampil
4. Klik icon `⋯`
5. Verifikasi overlay terbuka dengan item `Setup Column...` di bagian bawah panel
6. Verifikasi daftar kolom berurutan Group, Total Asset, Total User, masing-masing Hideable checked dan enabled dengan drag handle, dan kolom Checkbox Keep usable tidak termasuk daftar

### TC-FA-GRP-960: Uncheck satu kolom pada Column Visibility

7. Uncheck Total User
8. Verifikasi kolom Total User hilang dari tabel
9. Check Total User kembali, lalu tutup overlay

### TC-FA-GRP-1097: Screening Popup Setup Column

10. Klik icon `⋯`, lalu klik [Setup Column]
11. Verifikasi Header: title Setup Column, teks panduan drag, check, dan pin, serta icon close (X)
12. Verifikasi Body: daftar kolom Group, Total Asset, Total User (Hideable checked dan enabled) dengan drag handle dan icon Pin
13. Verifikasi Live Preview menampilkan header kolom dan sel data sesuai tabel asli
14. Verifikasi Footer: [Reset to Default] (text, primary) dan [Save] (filled, success)
15. Verifikasi footer tidak memiliki [Cancel]

### TC-FA-GRP-1101: Guard kolom terakhir yang visible

16. Uncheck Total Asset dan Total User
17. Hover checkbox kolom tersisa (Group)
18. Verifikasi checkbox Group disabled (tetap tampil)
19. Verifikasi tooltip "At least one column must remain visible."
20. Tutup popup lewat icon close (X) tanpa menyimpan

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 9, 20: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah 5 dan 6 mencakup Expected TC-960 a (ketiga kolom tercantum hideable checked) dan TC-1096 b; Expected TC-960 b (kolom Checkbox Keep usable tidak termasuk daftar) dicakup langkah 6. Pemulihan Total User pada TC-960 dilakukan lewat langkah penghubung (S-09).
- Temuan untuk QA:
  - TC-960 menyebut "Column Visibility" untuk Uncheck Total User tanpa menyebut apakah perubahan langsung tersimpan; spec mengasersi kolom hilang dari tabel dan memulihkannya.
