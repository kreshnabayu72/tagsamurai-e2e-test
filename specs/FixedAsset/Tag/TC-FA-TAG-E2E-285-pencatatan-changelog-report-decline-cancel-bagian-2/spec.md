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
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0044 ('Excavator 20 Ton - 44', group Plant B) berstatus In Audit; Tag [RFID] `RF-00132` dan [QR] `QR-00232` keduanya Paired tanpa laporan terbuka (blok TC-FA-TAG-1126); aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal `RF-00130` dan laporan terbuka Damaged dari Staff Auditor (TC-FA-TAG-1127); AST-0044 dengan laporan terbuka Missing pada `RF-00132` dan Unreadable pada `QR-00232` (TC-FA-TAG-1128).
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
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
7. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
8. Login dengan akun Total Control [TC] lalu buka Fixed Asset > TAG tab Paired
9. Klik tombol "Changelog"
10. Verifikasi dua entri baru dengan Action "Report TAG", Name "Excavator 20 Ton - 44", Field "Report Type", Old Value "—", New Value "Damaged"
11. Verifikasi jumlah entri Changelog bertambah tepat dua terhadap baseline

### TC-FA-TAG-1127: Decline Report mencatat Report Status Open menjadi Declined

12. Tutup Modal Changelog, lalu pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend
13. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
14. Buka menu aksi baris Excavator 20 Ton - 20
15. Klik "Decline Report"
16. Isi Textarea "Reason" dengan "Tag masih terbaca"
17. Klik tombol [Submit]
18. Klik tombol "Changelog" pada halaman Tag
19. Verifikasi satu entri baru dengan Action "Decline Report", Name "Excavator 20 Ton - 20", Field "Report Status", Old Value "Open", New Value "Declined", dan Modified By pelaku Decline

### TC-FA-TAG-1128: Decline Report dua Tag menulis satu entri Changelog per Tag

20. Tutup Modal Changelog, lalu pulihkan laporan terbuka Missing pada Tag RF-00132 dan Unreadable pada Tag QR-00232 lewat fixture backend
21. Buka menu aksi baris Excavator 20 Ton - 44
22. Klik "Decline Report"
23. Centang opsi RFID dan QR
24. Isi Textarea "Reason" dengan "Keduanya masih terbaca"
25. Klik tombol [Submit]
26. Klik tombol "Changelog" pada halaman Tag
27. Verifikasi dua entri baru "Decline Report" untuk Name "Excavator 20 Ton - 44", Field "Report Status", Old Value "Open", New Value "Declined"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 7, 8, 12 dan 20 (ganti akun eksplisit, S-07; menutup modal dan menyiapkan laporan terbuka lewat fixture antar TC, S-09).
- Urutan: TC-FA-TAG-1126 (akun Staff Auditor) mendahului TC-FA-TAG-1127 dan 1128 (akun Total Control) agar ganti akun hanya sekali.
- Temuan untuk QA:
  - TC-FA-TAG-1126 tidak menyebut pelaku Staff Auditor mana yang melaporkan; asersi tidak memuat Modified By.
  - TC-FA-TAG-1127 dan 1128 menyebut tombol "Changelog" pada halaman Tag sesudah Popup Assets dibuka; spec mengikuti TC dan tidak menambah langkah menutup popup.
