---
id: TC-FA-TAG-E2E-356-waktu-kolom-since-tag-to-be-returned-hari-kalender-dan-tanpa-bagian-2
title: "Waktu: Kolom Since Melewati Batas Pengembalian pada Hari ke-15 dan ke-30, Hari Kalender, dan Tanpa Aksi Otomatis"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1357
  - TC-FA-TAG-1358
  - TC-FA-TAG-1359
  - TC-FA-TAG-1360
coverage:
  web: automated
---

# Waktu: Kolom Since Melewati Batas Pengembalian pada Hari ke-15 dan ke-30, Hari Kalender, dan Tanpa Aksi Otomatis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): fixture timestamp masuk To Be Returned (umur Tag dalam hari kalender menurut zona waktu client); pengaturan jam server dan jam browser bersama ke waktu absolut (bagian 6) dan pemulihannya; seed idempotent Tag To Be Returned.
- Jam yang diubah: jam server dan jam browser bersama, hanya pada langkah 15 sampai 18 (TC-FA-TAG-1359), diset absolut ke 21 Sep 2026 00:10 menurut zona waktu client Asia/Jakarta dan dipulihkan pada langkah 18. Hook `after` memulihkan jam walau spec gagal.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada kode persis): Tag [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.) berstatus To Be Returned. Umur masuk diatur per TC: 15 hari (TC-FA-TAG-1357), 30 hari (TC-FA-TAG-1358 dan TC-FA-TAG-1360), dan 20 Sep 2026 23:50 menurut zona waktu client Asia/Jakarta (TC-FA-TAG-1359).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan jam, Tag RF-00071 ke keadaan awal lewat fixture backend.
- State global: jam server dan jam browser (dipulihkan seperti di atas). Suite serial (`parallel: false`).
- Nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 2, 8, 14, 19) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-1357: hari ke-15

1. Buka Fixed Asset > TAG > To Be Returned
2. Atur fixture: Tag RF-00071 masuk To Be Returned 15 hari kalender yang lalu menurut zona waktu client
3. Muat ulang halaman To Be Returned
4. Verifikasi kolom Since baris RF-00071 menampilkan tanggal masuk diikuti "(15 days)"
5. Verifikasi "(15 days)" bertanda warning
6. Arahkan kursor ke tanda warning
7. Verifikasi tooltip "Past the return limit." tampil

### TC-FA-TAG-1358: hari ke-30

8. Atur fixture: Tag RF-00071 masuk To Be Returned 30 hari kalender yang lalu menurut zona waktu client
9. Muat ulang halaman To Be Returned
10. Verifikasi kolom Since baris RF-00071 menampilkan tanggal masuk diikuti "(30 days)"
11. Verifikasi "(30 days)" bertanda warning
12. Arahkan kursor ke tanda warning
13. Verifikasi tooltip "Past the return limit." tampil

### TC-FA-TAG-1359: hari kalender zona waktu client

14. Atur fixture: zona waktu client Asia/Jakarta dan Tag RF-00071 masuk To Be Returned pada 20 Sep 2026 23:50
15. Atur jam server dan jam browser absolut ke 21 Sep 2026 00:10 menurut zona waktu client
16. Muat ulang halaman To Be Returned
17. Verifikasi kolom Since baris RF-00071 menampilkan "(1 day)"
18. Pulihkan jam server dan jam browser

### TC-FA-TAG-1360: melewati batas tidak mengubah status

19. Atur fixture: Tag RF-00071 masuk To Be Returned 30 hari kalender yang lalu
20. Muat ulang halaman To Be Returned
21. Verifikasi baris RF-00071 tampil pada tab To Be Returned
22. Verifikasi tidak ada badge status tambahan seperti Overdue pada baris RF-00071
23. Buka menu aksi baris RF-00071
24. Verifikasi menu aksi tetap hanya "Receive Manually"
25. Buka Global Settings > TAG
26. Verifikasi Tag RF-00071 tetap berstatus To be Returned

## Notes

- Spec harness eksternal waktu (kelas d). Jam dipenuhi dengan mengatur jam, bukan menunggu (R-10); tidak ada langkah "Tunggu" lebih dari 30 detik.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1, 3, 9, 16, 20 (membuka dan memuat ulang halaman), 6 dan 12 (hover), 18 (memulihkan jam, S-09), 23 dan 25 (navigasi dan membuka menu).
- Asersi tooltip memakai hover (langkah 6 dan 12) karena TC menyebut "Hover atau fokus keyboard"; spec memilih hover.
- Anchor positif absence (bagian 8b butir 2): langkah 21 untuk langkah 22 dan 24 (baris RF-00071 tampil).
- A-15: nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 2, 8, 14, 19) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-1359 menyebut "waktu sekarang 21 Sep 2026 00:10" tanpa menyebut jam mana yang diatur; spec mengatur jam server dan jam browser bersama (bagian 6).
  - TC-FA-TAG-1360 tidak menyebut cara membuka Global Settings > TAG selain "Periksa Global Settings > TAG"; spec memakai navigasi menu pada langkah 25.
  - TC-FA-TAG-1357 dan TC-FA-TAG-1358 tidak punya Post Condition; tidak ada yang diasersi di luar Expected.
