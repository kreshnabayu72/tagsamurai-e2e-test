---
id: TC-FA-FAAC-E2E-091-unassign-berhasil-dan-ditolak-state-berubah
title: "Unassign: Berhasil Single dan Massal, serta Ditolak atau Dilewati Saat State Berubah"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-231
  - TC-FA-FAAC-232
  - TC-FA-FAAC-236
  - TC-FA-FAAC-237
sourceRules: ["F-FAAC-10.k2", "D-17", "T-09a", "§4.1.3#p6", "F-FAAC-10.k4", "D-15", "§4.1.3#r11", "D-16", "§7.3#b2"]
smoke: []
dependsOn: []
trace:
  "F-FAAC-10.k2": [7, 10]
  "D-17": 8
  "T-09a": [15, 22, 27]
  "§4.1.3#p6": [16, 28]
  "F-FAAC-10.k4": [17, 18]
  "D-15": 21
  "§4.1.3#r11": 23
  "D-16": 25
  "§7.3#b2": 29
coverage:
  web: automated
---

# Unassign: Berhasil Single dan Massal, serta Ditolak atau Dilewati Saat State Berubah

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Machinery` (`MACHINERY`) dengan Asset Name ter-assign `Spare Parts Cart`, `Pallet Jack Manual`, `Hand Pallet`, `Shelving Rack`, `Tool Cabinet`, dan `Work Bench`, masing-masing 0 aset aktif.
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): mendaftarkan satu aset berlifecycle Active pada `Spare Parts Cart` dan melepas `Tool Cabinet` dari `MACHINERY` lewat fixture BE, bukan sesi UI kedua.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: `Pallet Jack Manual`, `Hand Pallet`, `Shelving Rack`, `Tool Cabinet`, dan `Work Bench` kembali ter-assign ke `MACHINERY`, serta aset aktif pada `Spare Parts Cart` dihapus.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama dan jumlah aset aktif itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `MACHINERY`, tekan Enter
2. Klik link Class Code `MACHINERY` di tabel
3. Klik tab `Asset Names`

### TC-FA-FAAC-236: Unassign single ditolak saat Asset Name menjadi memiliki aset aktif setelah dialog dibuka

4. Klik ikon `⋯` pada baris `Spare Parts Cart`, lalu pilih `Unassign`
5. Lewat sesi API aktor, daftarkan satu aset berlifecycle Active pada Asset Name `Spare Parts Cart` hingga aset tersimpan
6. Klik `[Unassign]` pada dialog
7. Verifikasi tidak ada toast yang tampil
8. Verifikasi Dialog Blok dengan Title `Cannot Unassign Asset Name`, Body `• Spare Parts Cart` dan `This asset name still has active assets. Move it to another asset class instead.`, dan tombol `[OK]`
9. Klik `[OK]`
10. Verifikasi `Spare Parts Cart` tetap ter-assign (masih tampil di tab Asset Names)

### TC-FA-FAAC-237: Unassign melewati Asset Name yang sudah tidak ter-assign tanpa log

11. Centang baris `Tool Cabinet` dan `Work Bench`, lalu klik `Bulk Action` dan pilih `Unassign`
12. Lewat sesi API aktor, lepas `Tool Cabinet` dari `MACHINERY` hingga pelepasan tersimpan
13. Catat jumlah entri Changelog Asset Class yang memuat "Tool Cabinet" (Nt) sebagai baseline lewat kemampuan baca log
14. Klik `[Unassign]` pada dialog
15. Verifikasi toast sukses `Success, asset name has been unassigned.`
16. Verifikasi `Work Bench` dilepas (hilang dari tab Asset Names)
17. Verifikasi `Tool Cabinet` dilewati dan tidak dihitung pada toast (toast tidak memuat `Some items were skipped`)
18. Verifikasi jumlah entri Changelog Asset Class yang memuat "Tool Cabinet" sama dengan Nt (dilewati tanpa log)

### TC-FA-FAAC-231: Unassign satu Asset Name tanpa aset aktif

19. Klik ikon `⋯` pada baris `Pallet Jack Manual`, lalu pilih `Unassign`
20. Klik `[Unassign]` pada dialog
21. Verifikasi dialog menutup
22. Verifikasi toast sukses `Success, asset name has been unassigned.`
23. Verifikasi `Pallet Jack Manual` hilang dari tab Asset Names

### TC-FA-FAAC-232: Unassign massal dua Asset Name tanpa aset aktif

24. Centang baris `Hand Pallet` dan `Shelving Rack`, lalu klik `Bulk Action` dan pilih `Unassign`
25. Verifikasi Dialog `Unassign Asset Names` berisi `• Hand Pallet`, `• Shelving Rack`, dan `They will have no asset class and their assets will not be depreciated. Are you sure you want to unassign them?` dengan footer `[Cancel]` dan `[Unassign]` (danger)
26. Klik `[Unassign]`
27. Verifikasi toast sukses `Success, asset name has been unassigned.`
28. Verifikasi `Hand Pallet` dan `Shelving Rack` hilang dari tab Asset Names
29. Verifikasi seleksi direset
30. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: kasus ditolak (TC-236) lebih dulu, lalu TC-237 yang melewati satu item, lalu Unassign berhasil (TC-231 dan TC-232) yang melepas Asset Name di akhir. Semua pada Detail `MACHINERY` yang sama, dibuka sekali di langkah 2 dan 3.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 9 (menutup dialog), langkah 13 (baseline Changelog, S-12), dan langkah 30 (mengosongkan Search). Langkah 5 dan 12 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2).
3. Pengecualian kode seed literal: TC mewajibkan Asset Class dan Asset Name seed bernama literal dengan jumlah aset aktif tertentu; dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini). Target Unassign adalah Asset Name seed milik spec ini yang dipulihkan fixture BE.
4. S-05 dan P-1: Expected "tanpa log" pada TC-237 diasersi di spec ini (langkah 18) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class. Entri Unassign untuk "Work Bench" memang bertambah, sehingga baseline dan asersi dibatasi pada entri yang memuat Asset Name yang dilewati ("Tool Cabinet").
5. Pembagian TC: TC-233 (Unassign massal campuran) ada di spec 110.
6. Temuan untuk QA: Post Condition TC-231 dan TC-232 (Asset Name menjadi tanpa Asset Class, masuk hitungan banner, dan modul terdampak) tidak punya langkah observasi di TC sehingga tidak diasersi. Precondition TC-237 menyebut `Tool Cabinet` dan `Work Bench` sebagai Asset Name `MACHINERY` tetapi tidak menyebut cara sesi kedua melepasnya; ditulis sebagai kemampuan sesi API tanpa endpoint (S-13).
