---
id: TC-AC-ACC-E2E-206-sort-tabel-tab-tag-dan-storage-client-custom
title: "Sort Tabel Tab TAG dan Purchase History Storage: Quota TAG, Purchase History TAG, dan Purchase History Storage"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-836
  - TC-AC-ACC-837
  - TC-AC-ACC-841
coverage:
  web: automated
---

# Sort Tabel Tab TAG dan Purchase History Storage: Quota TAG, Purchase History TAG, dan Purchase History Storage

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A3): C-DTL-1 "PT Uji Tabel Detail". Quota TAG (Total Quota/Used/Available): QR 650/320/330, RFID 200/50/150, NFC 100/100/0. Purchase History TAG: Qty 150 RFID CV Mitra Sejati Andi Wijayanto (20 Jun 2026), Qty 100 NFC CV Mitra Sejati Andi Wijaya (05 Jul 2026), Qty 50 RFID PT Distribusi Nusantara Budi Santoso (01 Jul 2026). Purchase History Storage: Qty (GB) 50 CV Mitra Sejati Andi Wijaya (01 Jan 2026), Qty (GB) 30 PT Distribusi Nusantara Budi Santoso (20 Mar 2026), Qty (GB) 20 CV Mitra Sejati Citra Dewi (15 Jun 2026). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya. Spec tidak mengubah C-DTL-1.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-836: Sort Quota TAG: default Type A-Z dan kolom Total Quota, Used, Available

1. Ketik Search `PT Uji Tabel Detail`, tekan Enter
2. Klik Company Name "PT Uji Tabel Detail" untuk membuka Detail
3. Klik Tab `TAG`
4. Verifikasi urutan awal tabel Quota: NFC, QR, RFID
5. Klik header Total Quota
6. Verifikasi Total Quota klik 1: NFC (100), RFID (200), QR (650)
7. Klik header Used
8. Verifikasi Used klik 1: RFID (50), NFC (100), QR (320)
9. Klik header Available
10. Verifikasi Available klik 1: NFC (0), RFID (150), QR (330)
11. Klik header Available lagi
12. Verifikasi Available klik 2: QR (330), RFID (150), NFC (0)
13. Klik header Available ketiga kali
14. Verifikasi Available klik 3: kembali ke urutan awal NFC, QR, RFID

### TC-AC-ACC-837: Sort Purchase History TAG kolom Qty, Action by, Type, dan Source

15. Verifikasi urutan awal tabel Purchase History TAG (Date terbaru): Qty 100, Qty 50, Qty 150
16. Klik header Qty
17. Verifikasi Qty klik 1: Qty 50, Qty 100, Qty 150
18. Klik header Action by
19. Verifikasi Action by klik 1: Qty 100 (Andi Wijaya), Qty 150 (Andi Wijayanto), Qty 50 (Budi Santoso)
20. Klik header Type
21. Verifikasi Type klik 1: Qty 100 (NFC) pada posisi 1, lalu Qty 150 dan Qty 50 (RFID) pada posisi 2 dan 3
22. Klik header Source
23. Verifikasi Source klik 1: Qty 100 dan Qty 150 (CV Mitra Sejati) pada posisi 1 dan 2, lalu Qty 50 (PT Distribusi Nusantara) pada posisi 3

### TC-AC-ACC-841: Sort Purchase History Storage kolom Qty (GB), Source, dan Action by

24. Klik Tab `Storage`
25. Verifikasi urutan awal tabel Purchase History Storage (Date terbaru): Qty (GB) 20, 30, 50
26. Klik header Qty (GB)
27. Verifikasi Qty (GB) klik 1: 20, 30, 50
28. Klik header Qty (GB) lagi
29. Verifikasi Qty (GB) klik 2: 50, 30, 20
30. Klik header Source
31. Verifikasi Source klik 1: Qty (GB) 50 dan 20 (CV Mitra Sejati) pada posisi 1 dan 2, lalu Qty (GB) 30 (PT Distribusi Nusantara) pada posisi 3
32. Klik header Action by
33. Verifikasi Action by klik 1: Qty (GB) 50 (Andi Wijaya), 30 (Budi Santoso), 20 (Citra Dewi)

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pengurutan tabel pada satu dataset, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: sort tabel Tab Hardware (TC-839, TC-840) ada di spec 211 dan sort tabel Tab Subscription (TC-828, TC-829, TC-830) ada di spec 214; id TC masing-masing tetap satu spec.
- Temuan untuk QA (S-15): Post Condition seluruh TC `-` sehingga tidak diasersi. Klik header kolom berbeda memulai sort baru pada kolom itu (satu kali per kolom) sesuai Langkah TC-837 dan TC-841.
