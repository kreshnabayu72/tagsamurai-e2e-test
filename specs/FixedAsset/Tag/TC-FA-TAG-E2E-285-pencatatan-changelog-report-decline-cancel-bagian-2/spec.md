---
id: TC-FA-TAG-E2E-285-pencatatan-changelog-report-decline-cancel-bagian-2
title: "Pencatatan Changelog Report TAG dua Tag dan Decline Report"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1126
  - TC-FA-TAG-1127
  - TC-FA-TAG-1128
coverage:
  web: automated
---

# Pencatatan Changelog Report TAG dua Tag dan Decline Report

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai pada blok TC-FA-TAG-1127 dan 1128 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0044 ('Excavator 20 Ton - 44', group Plant B) berstatus In Audit; Tag [RFID] `RF-00132` dan [QR] `QR-00232` keduanya Paired tanpa laporan terbuka (blok TC-FA-TAG-1126); aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal `RF-00130` dan laporan terbuka Damaged dari Staff Auditor (TC-FA-TAG-1127); AST-0044 dengan laporan terbuka Missing pada `RF-00132` dan Unreadable pada `QR-00232` (TC-FA-TAG-1128).
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6); entri Changelog `Decline Report` per Tag (langkah 18, 27). Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130, RF-00132, QR-00232. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1126: Report TAG dua Tag menulis satu entri Changelog per Tag

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Centang opsi "RFID" dan "QR"
4. Pilih Report Type "Damaged"
5. Isi Textarea "Note" dengan "Dua label rusak"
6. Klik tombol [Submit]
7. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)
8. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
9. Login dengan akun Total Control [TC] lalu buka Fixed Asset > TAG tab Paired
10. Klik tombol "Changelog"
11. Verifikasi dua entri baru dengan Action "Report TAG", Name "Excavator 20 Ton - 44", Field "Report Type", Old Value "—", New Value "Damaged"
12. Verifikasi jumlah entri Changelog bertambah tepat dua terhadap baseline

### TC-FA-TAG-1127: Decline Report mencatat Report Status Open menjadi Declined

13. Tutup Modal Changelog, lalu pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend
14. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
15. Buka menu aksi baris Excavator 20 Ton - 20
16. Klik "Decline Report"
17. Isi Textarea "Reason" dengan "Tag masih terbaca"
18. Klik tombol [Submit]
19. Tunggu aksi selesai (dialog "Decline Report" tertutup dan tombol aktif kembali)
20. Klik tombol "Changelog" pada halaman Tag
21. Verifikasi satu entri baru dengan Action "Decline Report", Name "Excavator 20 Ton - 20", Field "Report Status", Old Value "Open", New Value "Declined", dan Modified By pelaku Decline

### TC-FA-TAG-1128: Decline Report dua Tag menulis satu entri Changelog per Tag

22. Tutup Modal Changelog, lalu pulihkan laporan terbuka Missing pada Tag RF-00132 dan Unreadable pada Tag QR-00232 lewat fixture backend
23. Buka menu aksi baris Excavator 20 Ton - 44
24. Klik "Decline Report"
25. Centang opsi RFID dan QR
26. Isi Textarea "Reason" dengan "Keduanya masih terbaca"
27. Klik tombol [Submit]
28. Tunggu aksi selesai (dialog "Decline Report" tertutup dan tombol aktif kembali)
29. Klik tombol "Changelog" pada halaman Tag
30. Verifikasi dua entri baru "Decline Report" untuk Name "Excavator 20 Ton - 44", Field "Report Status", Old Value "Open", New Value "Declined"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 7, 8, 9, 13, 19, 22 dan 28 (ganti akun eksplisit, S-07; menutup modal dan menyiapkan laporan terbuka lewat fixture antar TC, S-09). Langkah 7, 19 dan 28 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi ganti akun atau pindah surface.
- Urutan: TC-FA-TAG-1126 (akun Staff Auditor) mendahului TC-FA-TAG-1127 dan 1128 (akun Total Control) agar ganti akun hanya sekali.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6); entri Changelog `Decline Report` per Tag (langkah 18, 27).
- Temuan untuk QA:
  - TC-FA-TAG-1126 tidak menyebut pelaku Staff Auditor mana yang melaporkan; asersi tidak memuat Modified By.
  - TC-FA-TAG-1127 dan 1128 menyebut tombol "Changelog" pada halaman Tag sesudah Popup Assets dibuka; spec mengikuti TC dan tidak menambah langkah menutup popup.
