---
id: TC-AC-ACTS-E2E-220-modal-event-log-tab-audit-tag-penulisan-found-not-found-dan-recovery
title: "Modal Event Log Tab Audit TAG: Penulisan Sesi dengan D-03 Dicentang dan Tidak serta Semua Verified dengan Recovery"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-927
  - TC-AC-ACTS-928
  - TC-AC-ACTS-929
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Penulisan Sesi dengan D-03 Dicentang dan Tidak serta Semua Verified dengan Recovery

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: SKU `Fixture.tagStock.skuRfid` memiliki 8 unit eligible Audit (Available) untuk TC-AC-ACTS-927; 8 unit eligible dengan sebagian berstatus Damaged/Missing untuk TC-AC-ACTS-928; 4 unit eligible dengan 1 unit Damaged/Missing untuk TC-AC-ACTS-929. Di-seed ulang fixture BE sebelum TC-AC-ACTS-928 dan 929 (langkah penghubung "Seed ulang", karena Submit sebelumnya mengubah status unit) dan dipulihkan di hook `after`.
- Spec berjalan serial karena memakai simulator pemindai bersama.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- Kemampuan teknis: Simulator pemindai RFID `Zebra RFD40 (SN-2201)` (scan satu per satu dan beruntun, kode tidak dikenali) disediakan tim FE; mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pembacaan status unit di BE (tidak terlihat di UI) lewat fixture BE, disediakan tim FE/BE; hanya dipakai untuk butir Expected TC.
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-927: Audit Submit dengan checkbox `D-03` dicentang menulis satu sesi Found, Not Found, dan Not Found Action `Marked as Damaged/Missing`

3. Catat jumlah total entri sesi Tab Audit TAG SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
4. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`
5. Pindai 5 unit eligible (8 unit Available) lewat reader RFID `Zebra RFD40 (SN-2201)`, klik `[Stop]`
6. Klik `[Submit]`, biarkan checkbox `D-03` dicentang, klik `[Confirm]`
7. Tunggu aksi selesai (tombol aksi aktif kembali)
8. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
9. Verifikasi baris sesi terbaru: Found `5`, Not Found `3`, Not Found Action `Marked as Damaged/Missing`, Hardware `Zebra RFD40 (SN-2201)`, Modified By pelaku
10. Verifikasi jumlah total entri Tab Audit TAG bertambah tepat satu dari baseline sehingga hanya satu baris untuk sesi ini

### TC-AC-ACTS-928: Audit Submit dengan checkbox `D-03` tidak dicentang menulis Not Found Action `Kept previous status`

11. Tutup modal Event Log dengan klik (X)
12. Seed ulang 8 unit eligible Audit SKU `Fixture.tagStock.skuRfid` (sebagian berstatus Damaged/Missing, termasuk 1 unit yang dipindai pada langkah 15) lewat fixture BE
13. Catat jumlah total entri sesi Tab Audit TAG SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
14. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`
15. Pindai 5 unit termasuk 1 unit Damaged/Missing lewat reader RFID `Zebra RFD40 (SN-2201)`, klik `[Stop]`
16. Klik `[Submit]`, hilangkan centang checkbox `D-03`, klik `[Confirm]`
17. Tunggu aksi selesai (tombol aksi aktif kembali)
18. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
19. Verifikasi baris sesi terbaru: Found `5`, Not Found `3`, Not Found Action `Kept previous status`
20. Verifikasi jumlah total entri Tab Audit TAG bertambah tepat satu dari baseline
21. Verifikasi 3 unit Not Scanned tidak berubah status (status unit dibaca lewat fixture BE)

### TC-AC-ACTS-929: Audit Submit dengan semua unit Verified dan ada recovery menulis Not Found 0 dan Not Found Action `—`

22. Tutup modal Event Log dengan klik (X)
23. Seed ulang 4 unit eligible Audit SKU `Fixture.tagStock.skuRfid` (1 unit Damaged/Missing) lewat fixture BE
24. Catat jumlah total entri sesi Tab Audit TAG SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
25. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`
26. Pindai semua 4 unit eligible (1 unit Damaged/Missing) lewat reader RFID `Zebra RFD40 (SN-2201)`, klik `[Stop]`
27. Klik `[Submit]`
28. Verifikasi dialog `D-03` tidak muncul
29. Tunggu aksi selesai (tombol aksi aktif kembali)
30. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
31. Verifikasi baris sesi terbaru: Found `4`, Not Found `0`, Not Found Action `—`
32. Verifikasi jumlah total entri Tab Audit TAG bertambah tepat satu dari baseline

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16) dan langkah 2 (row action `Detail`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; mencatat baseline; memulihkan state antar TC.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- TC-AC-ACTS-930 (Audit Submit tanpa perubahan status) bukan asersi di spec ini; TC-AC-ACTS-931 dan 932 ada di spec 261.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-927 menyebut "halaman Audit TAG", sedangkan TC-AC-ACTS-904 menyebut Popup Audit TAG; spec memakai `[Audit TAG]` di toolbar Tab Available.
  - TC-AC-ACTS-927 sampai 929 tidak menyebut cara membaca jumlah entri sebelum aksi (baseline); spec memakai kemampuan baca fixture BE dan teks footer pagination.
  - TC-AC-ACTS-928 Expected b (unit Not Scanned tidak berubah status) tidak memberi cara cek; spec memakai pembacaan status unit di BE (disediakan tim FE/BE).
  - TC-AC-ACTS-929 tidak menyebut anchor positif untuk "dialog `D-03` tidak muncul"; spec mengasersi segera setelah `[Submit]`.
  - Cara simulasi reader RFID tidak didefinisikan di TC, PRD, atau LLD; ditulis "disediakan tim FE".
