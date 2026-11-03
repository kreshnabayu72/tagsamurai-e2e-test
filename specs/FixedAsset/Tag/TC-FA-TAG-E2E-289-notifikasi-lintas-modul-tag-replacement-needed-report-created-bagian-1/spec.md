---
id: TC-FA-TAG-E2E-289-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-1
title: "Notifikasi Lintas Modul: tag_replacement_needed dan tag_report_created, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1135
  - TC-FA-TAG-1136
  - TC-FA-TAG-1223
  - TC-FA-TAG-1248
  - TC-FA-TAG-1249
coverage:
  web: automated
---

# Notifikasi Lintas Modul: tag_replacement_needed dan tag_report_created, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Budi S. (pengamat notifikasi; pemegang Update, lihat butir akun di bawah).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Akun Budi S., Maya R., dan Dedi K. tidak tertulis di Tabel Pre-setup TC; disediakan tim FE (email dan password lewat env yang didaftarkan tim FE). Capability tiap akun diatur lewat fixture backend sesuai precondition TC pada langkah penghubung sebelum pemicu.
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (pemicu perubahan TAG Type).
- Akun aktor: Asset Admin [AA] `assetAdmin_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_AA_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (Check-in dengan identifikasi manual).
- Akun aktor: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (Report TAG).
- Data (Pre-setup TC, tanpa suffix): grup Excavator 20 Ton / Plant A (18 aset ber-Tag RFID dan 2 Not Paired Yet; TAG Type Asset Name RFID); aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal [RFID] `RF-00130`, berstatus Borrowed pada blok TC-FA-TAG-1223 dan In Audit pada task Existence Audit pada blok TC-FA-TAG-1248.
- Kemampuan teknis (disediakan tim FE/BE): membaca dropdown notifikasi tiap akun dan menjalankan Check-in dengan identifikasi manual lewat sesi API.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: TAG Type Asset Name 'Excavator 20 Ton' (dan Asset Name lain yang disebut pada langkah). Suite serial (`parallel: false`).

## Test Steps

### Pemicu (sesi API)

1. Atur lewat fixture backend: Budi S. memegang Update di group Plant A; Maya R. memegang Read Only; Dedi K. memegang Update hanya di group Plant B
2. Pelaku kedua (Total Control) lewat sesi API mengubah TAG Type 'Excavator 20 Ton' dari RFID menjadi NFC hingga perubahan tersimpan
3. Atur lewat fixture backend: Budi S. memegang Update di group Plant B; Maya R. memegang Update hanya di group Plant A; aset AST-0020 berstatus Borrowed dengan Tag RF-00130 tidak terbaca dan tanpa laporan terbuka
4. Pelaku kedua (Asset Admin) lewat sesi API menjalankan Check-in dengan identifikasi manual untuk aset AST-0020 hingga selesai
5. Tutup laporan terbuka Unreadable pada Tag RF-00130 lewat fixture backend
6. Pelaku kedua (Staff Auditor) lewat sesi API melaporkan Tag RF-00130 pada AST-0020 di task Existence Audit dengan Report Type "Damaged" dan Note "Label retak" hingga laporan tersimpan

### TC-FA-TAG-1135, 1223, 1248: notifikasi diterima Budi S.

7. Muat ulang halaman
8. Buka dropdown notifikasi
9. Verifikasi notifikasi event `tag_replacement_needed` diterima oleh Budi S.
10. Verifikasi notifikasi berjudul "TAG reported" dengan isi "RF-00130 (AST-0020) was reported as Unreadable." tampil
11. Verifikasi notifikasi Unreadable itu memuat tombol [Mark as Read] dan tombol aksi
12. Verifikasi notifikasi berjudul "TAG reported" dengan isi "RF-00130 (AST-0020) was reported as Damaged." tampil
13. Verifikasi notifikasi Damaged itu memuat tombol aksi bersama [Mark as Read] (actionable)
14. Klik notifikasi "TAG reported" dengan isi "RF-00130 (AST-0020) was reported as Damaged."
15. Verifikasi halaman tujuan notifikasi adalah Fixed Asset > TAG tab Paired

### TC-FA-TAG-1136, 1249: Maya R. dan Dedi K. tidak menerima notifikasi

16. Ganti akun: logout dari akun Budi S.
17. Login dengan akun Maya R.
18. Buka dropdown notifikasi
19. Verifikasi dropdown notifikasi Maya R. terbuka
20. Verifikasi Maya R. tidak menerima notifikasi `tag_replacement_needed` (bukan pemegang Update)
21. Verifikasi tidak ada notifikasi "TAG reported" untuk RF-00130 pada dropdown Maya R.
22. Ganti akun: logout dari akun Maya R.
23. Login dengan akun Dedi K. (Update hanya Plant B)
24. Buka dropdown notifikasi
25. Verifikasi dropdown notifikasi Dedi K. terbuka
26. Verifikasi Dedi K. tidak menerima notifikasi `tag_replacement_needed` untuk aset Plant A

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 3, 5, 7, 16, 17, 22 dan 23 (mengatur capability dan data lewat fixture, menutup laporan, memuat ulang halaman, ganti akun eksplisit, S-07).
- Pemicu TC-FA-TAG-1135, 1223, dan 1248 memakai pelaku kedua lewat sesi API karena hanya memicu notifikasi dan tidak diasersi di sesinya (R-20); semua pemicu dijalankan sebelum notifikasi dibaca, dan absence notifikasi (TC-FA-TAG-1136, 1249) diasersi sesudah anchor positif notifikasi Budi S. yang membuktikan pemicu sudah diproses (bagian 8b butir 2 dan 11).
- TC-FA-TAG-1249 memakai Report TAG yang sama dengan TC-FA-TAG-1248 (pelapor, Tag, dan aset sama); penerima yang diamati berbeda.
- Temuan untuk QA:
  - Budi S. memegang Update di Plant A (TC-FA-TAG-1135) dan Update di Plant B (TC-FA-TAG-1223, 1248); Maya R. Read Only (TC-FA-TAG-1136) dan Update hanya di Plant A (TC-FA-TAG-1249). Spec mengatur capability tiap akun lewat fixture sebelum pemicunya.
  - TC-FA-TAG-1135 Expected tidak menyebut judul dan isi notifikasi `tag_replacement_needed`; spec mengasersi hanya event yang disebut TC.
  - TC-FA-TAG-1223 mensyaratkan Role 'Asset Admin' tanpa menyebut modul Borrow/Check-in yang dipakai; spec memakai akun [AA] sesuai TC.
  - TC-FA-TAG-1136 langkah TC ke-2 dan 3 menyebut 'Buka notifikasi lonceng'; spec memakai dropdown notifikasi.
  - TC-FA-TAG-1135 sampai 1249 Post Condition ('Notifikasi in-app tercatat untuk pemegang Update dalam scope') tidak punya langkah observasi tambahan; sama dengan Expected yang diasersi.
