---
id: TC-FA-TAG-E2E-284-pencatatan-changelog-report-decline-cancel-bagian-1
title: "Pencatatan Changelog Report TAG: Report Type Damaged, Missing, dan Unreadable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1123
  - TC-FA-TAG-1124
  - TC-FA-TAG-1125
coverage:
  web: automated
---

# Pencatatan Changelog Report TAG: Report Type Damaged, Missing, dan Unreadable

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai untuk membaca Changelog (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0020 ('Excavator 20 Ton - 20', group Plant B) berstatus In Audit; Tag tunggal [RFID] `RF-00130` tanpa laporan terbuka (laporan terbuka Damaged dari Staff Auditor dibuat fixture sesuai kebutuhan TC).
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 5, 11, 17). Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag RF-00130 dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1123: aksi Report TAG dengan Report Type Damaged

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Klik tombol [Submit]
6. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)

### TC-FA-TAG-1124: aksi Report TAG dengan Report Type Missing

7. Pulihkan Tag RF-00130 tanpa laporan terbuka lewat fixture backend
8. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
9. Pilih Report Type "Missing"
10. Isi Textarea "Note" dengan "Label retak"
11. Klik tombol [Submit]
12. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)

### TC-FA-TAG-1125: aksi Report TAG dengan Report Type Unreadable

13. Pulihkan Tag RF-00130 tanpa laporan terbuka lewat fixture backend
14. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
15. Pilih Report Type "Unreadable"
16. Isi Textarea "Note" dengan "Label retak"
17. Klik tombol [Submit]
18. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)

### TC-FA-TAG-1123 sampai 1125: pembacaan Changelog oleh Total Control

19. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
20. Login dengan akun Total Control [TC] lalu buka Fixed Asset > TAG tab Paired
21. Klik tombol "Changelog"
22. Verifikasi modal berjudul "Changelog: Paired TAG" tampil
23. Verifikasi satu entri baru dengan Action "Report TAG", Name "Excavator 20 Ton - 20", Field "Report Type", Old Value "—", New Value "Damaged"
24. Verifikasi kolom Modified By entri Damaged berisi nama pelaku Report TAG dan Date terisi
25. Verifikasi Old Value dan New Value entri Damaged berupa teks polos tanpa badge
26. Verifikasi satu entri baru dengan Action "Report TAG", Name "Excavator 20 Ton - 20", Field "Report Type", Old Value "—", New Value "Missing"
27. Verifikasi kolom Modified By entri Missing berisi nama pelaku Report TAG dan Date terisi
28. Verifikasi Old Value dan New Value entri Missing berupa teks polos tanpa badge
29. Verifikasi satu entri baru dengan Action "Report TAG", Name "Excavator 20 Ton - 20", Field "Report Type", Old Value "—", New Value "Unreadable"
30. Verifikasi kolom Modified By entri Unreadable berisi nama pelaku Report TAG dan Date terisi
31. Verifikasi Old Value dan New Value entri Unreadable berupa teks polos tanpa badge

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6, 7, 12, 13, 18, 19 dan 20 (menutup laporan terbuka lewat fixture antar TC, S-09; ganti akun eksplisit, S-07). Langkah 6, 12 dan 18 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi permintaan langsung (fixture atau sesi API) atau ganti akun.
- Urutan (S-10): ketiga Report TAG dijalankan berturut-turut oleh Staff Auditor sebelum ganti akun, lalu Changelog dibaca sekali oleh Total Control; entri tiap Report Type dicari lewat New Value (Damaged, Missing, Unreadable) karena entri Changelog tidak dapat diubah. Penggabungan ini menghindari dua kali ganti akun.
- Judul modal diasersi satu kali karena Expected tiga TC memuat judul yang sama pada modal yang sama.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 5, 11, 17).
- Temuan untuk QA:
  - TC-FA-TAG-1123 sampai 1125 tidak menyebut nama tampil pelaku Report TAG; asersi Modified By memakai nama tampil akun Staff Auditor dari fixture.
  - TC-FA-TAG-1123 sampai 1125 Expected c ('teks polos tanpa badge') diasersi per entri.
