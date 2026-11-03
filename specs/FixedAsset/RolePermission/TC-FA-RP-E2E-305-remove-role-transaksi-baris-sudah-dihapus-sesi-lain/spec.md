---
id: TC-FA-RP-E2E-305-remove-role-transaksi-baris-sudah-dihapus-sesi-lain
title: Remove Role Transaksi atas baris yang sudah dihapus sesi lain
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-461
coverage:
  web: automated
---

# Remove Role Transaksi atas baris yang sudah dihapus sesi lain

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`, sebagai Sesi 1 (UI). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi 2 adalah Total Control kedua (Pre-setup #3, Rina Wulandari), `Spectra.env.FA_TC2_PASSWORD`, lewat sesi API yang tidak mengusir sesi UI (pernyataan "Hook suite" di `suite.md`).
- Flag Guided Tooltip dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (pohon Group), #19 (Putri Wulandari sebagai Staff pada `IT Infrastructure` sub-tab `Disposal`). Penugasan Putri Wulandari dipulihkan lewat fixture backend (disediakan tim FE/BE) di hook `after`.
- Kemampuan teknis: sesi API Total Control kedua (disediakan tim FE/BE).
- Spec ini sebagai satu-satunya TC yang memakai dua sesi; Sesi 2 hanya memicu state dan hasilnya tidak diasersi di sesinya.

## Test Steps

1. Buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
2. Verifikasi baris Putri Wulandari (Staff) tampil di Sesi 1.
3. Sesi 2 meng-Remove baris Putri Wulandari (Staff) pada `IT Infrastructure` sub-tab `Disposal` hingga penghapusan tersimpan.
4. Di Sesi 1, klik `[⋯]` pada baris Putri Wulandari, lalu pilih `Remove`.
5. Klik `[Remove]`.
6. Verifikasi toast netral `This role assignment is no longer available.` tidak muncul.
7. Verifikasi dialog konfirmasi tertutup.

## Notes

- Langkah penghubung (S-03): 1, 4, 5. Langkah 6 mengikuti 8b butir 11: asersi absence toast diletakkan segera sesudah pemicu (langkah 5), dengan langkah 7 sebagai bukti respons diproses.
- Pembagian TC lintas spec: klausa "tanpa entri log tambahan" TC-FA-RP-461 butir a diasersi di spec absence 291 dengan aksi nyata, baseline, dan anchor positif sendiri; id TC-FA-RP-461 tetap di `sourceTc` spec ini dan spec 291 (S-05).
- Temuan untuk QA:
  - TC 461 bertanda `Manual Only (d) dua sesi paralel` di TC. Sesi 2 hanya memicu state lewat sesi API; tidak ada asersi di sesi 2.
  - TC 461 Expected a "selesai tanpa efek" tidak merinci wujud di UI; spec mengasersi dialog tertutup (langkah 7) dan tidak ada toast netral (langkah 6).
