---
id: TC-AC-SG-E2E-003-loading-state-dan-empty-state-node-tanpa-subgroup
title: "Loading State Tabel dan Empty State Node Tanpa Subgroup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-10
  - TC-AC-SG-13
coverage:
  web: automated
---

# Loading State Tabel dan Empty State Node Tanpa Subgroup

## Prerequisites

- Mode: FE+BE (respons pengambilan data Group ditahan lewat intercept di atas backend nyata untuk mengamati Loading state; tidak ada kegagalan yang dipaksakan).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); `Room 301` tanpa subgroup dengan Total User 2 (#17) dan Total Member 1 (#19).
- Kemampuan teknis: penundaan (penahanan) respons pengambilan data Group lewat `Spectra.intercept()` pada endpoint list Group (Pre-setup #38); intercept dilepas segera setelah Loading state teramati dan tidak dipasang pada blok TC-AC-SG-13.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-003`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-10: Loading state saat data tabel diambil

1. Tahan respons pengambilan data Group lewat intercept
2. Buka halaman `Settings > Group` lewat sidebar
3. Verifikasi area tabel menampilkan Loading component selama respons tertunda
4. Lepas tahanan respons
5. Verifikasi Loading component hilang dari area tabel
6. Verifikasi baris tabel tampil

### TC-AC-SG-13: Tabel pada node terpilih tanpa subgroup menampilkan empty state khusus

7. Klik node `Room 301` di Sidebar Group Tree
8. Verifikasi Group Context Header menampilkan "Room 301" | "Total User: 2" | "Total Member: 1"
9. Verifikasi tabel menampilkan empty state dengan Title "No subgroup yet" dan Description "This group does not have any subgroups."
10. Klik node `Room 301` sekali lagi untuk melepas pilihan

## Notes

- Langkah penghubung (S-03, S-09): langkah 2 membuka ulang halaman (hook `beforeEach` suite sudah membuka halaman sebelum intercept terpasang, sehingga Loading state hanya teramati pada pembukaan kedua), langkah 4 melepas intercept sebelum blok berikutnya, dan langkah 10 melepas pilihan node.
- Kelas: Loading state dengan respons ditahan bukan kelas b (bagian 3 prinsip 13b) dan boleh di spec fungsional; tidak ada respons gagal yang dipaksakan di spec ini.
- Temuan untuk QA:
  - TC-AC-SG-10 Expected tidak memberi batas waktu Loading maupun bentuk Loading component; spec hanya mengasersi tampil selama respons ditahan dan hilang sesudah dilepas.
  - TC-AC-SG-10 bertanda `Automatable` tetapi memuat kebutuhan intercept; mekanisme penundaan respons disebut Pre-setup #38 tanpa endpoint, sehingga spec tidak menulis endpoint karangan (S-13).
